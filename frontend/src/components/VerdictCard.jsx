function VerdictCard({ authentication, geo, trust }) {
  const score = trust?.score ?? 0;
  const rating = trust?.rating ?? "Unknown";

  let verdict = "🟢 Safe Email";
  let barColor = "low";

  if (score < 90) {
    verdict = "🟡 Suspicious Email";
    barColor = "medium";
  }

  if (score < 60) {
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
          style={{
            width: `${score}%`,
          }}
        />
      </div>

      <h1
        style={{
          fontSize: "3rem",
          margin: "15px 0 5px",
          color: "#58a6ff",
        }}
      >
        {score}/100
      </h1>

      <h3
        style={{
          color: "#58a6ff",
          marginTop: 0,
        }}
      >
        {rating}
      </h3>

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