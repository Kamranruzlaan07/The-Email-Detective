function VerdictCard({ risk, authentication, geo }) {
  const score = risk.score || 0;

  let verdict = "🟢 Safe Email";
  let barColor = "low";

  if (risk.level === "Medium") {
    verdict = "🟡 Suspicious Email";
    barColor = "medium";
  }

  if (risk.level === "High") {
    verdict = "🔴 High Risk Email";
    barColor = "high";
  }

  return (
    <div className="card verdict-card">
      <h2>🛡 Email Verdict</h2>

      <h3>{verdict}</h3>

      <div className="progress">
        <div
          className={`progress-fill ${barColor}`}
          style={{ width: `${score}%` }}
        />
      </div>

      <p>
        <strong>{score}</strong> / 100
      </p>

      <hr />

      <h3>Authentication</h3>

      <p>
        ✅ SPF: <strong>{authentication.spf.toUpperCase()}</strong>
      </p>

      <p>
        ✅ DKIM: <strong>{authentication.dkim.toUpperCase()}</strong>
      </p>

      <p>
        ✅ DMARC: <strong>{authentication.dmarc.toUpperCase()}</strong>
      </p>

      <hr />

      <h3>Origin</h3>

      <p>
        🌍 {geo.length ? geo[0].country : "Unknown"}
      </p>
    </div>
  );
}

export default VerdictCard;