(function () {
  "use strict";

  const panel = document.getElementById("strength");
  if (!panel) return;

  const status = panel.querySelector(".panel-head span");
  const tbody = panel.querySelector(".daytrade-table tbody");
  if (!status || !tbody) return;

  const directionClasses = {
    "上昇": "trend-up",
    "下降": "trend-down"
  };
  const verdictClasses = {
    "最適": "rank-best",
    "適": "rank-good",
    "候補": "rank-watch",
    "見送り": "rank-skip",
    "対象外": "rank-out"
  };

  function jstDateParts(date) {
    const parts = new Intl.DateTimeFormat("en-CA", {
      timeZone: "Asia/Tokyo",
      year: "numeric",
      month: "2-digit",
      day: "2-digit"
    }).formatToParts(date);
    return Object.fromEntries(parts.map((part) => [part.type, part.value]));
  }

  function formatJst(date) {
    const parts = new Intl.DateTimeFormat("en-CA", {
      timeZone: "Asia/Tokyo",
      year: "numeric",
      month: "2-digit",
      day: "2-digit",
      hour: "2-digit",
      minute: "2-digit",
      hourCycle: "h23"
    }).formatToParts(date);
    const values = Object.fromEntries(parts.map((part) => [part.type, part.value]));
    return `${values.year}-${values.month}-${values.day} ${values.hour}:${values.minute}`;
  }

  function jstDayNumber(date) {
    const parts = jstDateParts(date);
    return Date.UTC(Number(parts.year), Number(parts.month) - 1, Number(parts.day)) / 86400000;
  }

  function setStatus(payload, generatedAt) {
    const staleDays = Math.max(jstDayNumber(new Date()) - jstDayNumber(generatedAt), 0);
    const updated = formatJst(generatedAt);
    status.className = "";

    if (staleDays > 0) {
      const prefix = staleDays >= 2 ? `要確認: ${staleDays}日未更新` : "データ未更新";
      status.textContent = `${prefix} / 最終成功 ${updated} JST`;
      status.className = "daytrade-update-stale";
    } else if (Array.isArray(payload.errors) && payload.errors.length > 0) {
      status.textContent = `一部取得失敗 / ${updated} JST 更新`;
      status.className = "daytrade-update-partial";
    } else {
      status.textContent = `${updated} JST 更新`;
    }
  }

  function numberText(value, digits, suffix) {
    const number = Number(value);
    return Number.isFinite(number) ? `${number.toFixed(digits)}${suffix || ""}` : "—";
  }

  function renderRows(rankings) {
    const fragment = document.createDocumentFragment();
    rankings.forEach((item) => {
      const row = document.createElement("tr");
      const cells = [
        item.rank || "—",
        item.pair || "—",
        numberText(item.adr_5_pips, 1),
        numberText(item.adr_ratio_pct, 0, "%"),
        numberText(item.atr_h4_pips, 1),
        numberText(item.adx_h4, 1),
        item.direction || "レンジ",
        `${item.verdict || "見送り"} ${Number.isFinite(Number(item.score)) ? Number(item.score) : "—"}`
      ];

      cells.forEach((value, index) => {
        const cell = document.createElement("td");
        if (index === 0) cell.className = "daytrade-rank";
        if (index === 1) {
          const strong = document.createElement("strong");
          strong.textContent = value;
          cell.appendChild(strong);
        } else if (index === 6) {
          cell.className = directionClasses[value] || "trend-range";
          cell.textContent = value;
        } else if (index === 7) {
          const badge = document.createElement("span");
          badge.className = `daytrade-verdict ${verdictClasses[item.verdict] || "rank-skip"}`;
          badge.textContent = value;
          cell.appendChild(badge);
        } else {
          cell.textContent = value;
        }
        row.appendChild(cell);
      });
      fragment.appendChild(row);
    });
    tbody.replaceChildren(fragment);
  }

  async function refreshRanking() {
    try {
      const response = await fetch(`data/daytrade-ranking.json?v=${Date.now()}`, { cache: "no-store" });
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      const payload = await response.json();
      const generatedAt = new Date(payload.generated_at_jst);
      if (!Array.isArray(payload.rankings) || !payload.rankings.length || Number.isNaN(generatedAt.getTime())) {
        throw new Error("Invalid ranking data");
      }
      renderRows(payload.rankings);
      setStatus(payload, generatedAt);
    } catch (error) {
      console.warn("Latest daytrade ranking could not be loaded; keeping embedded data.", error);
    }
  }

  refreshRanking();
})();
