function RiskCard({ risk }) {
  return (
    <div className="card">
      <h2>⚠️ Risk Assessment</h2>

      <p>
        <strong>Risk Level:</strong>{" "}
        <span className={`badge ${risk.level.toLowerCase()}`}>
          {risk.level}
        </span>
      </p>

      <p>
        <strong>Risk Score:</strong> {risk.score}
      </p>

      <strong>Reasons</strong>

      <ul>
        {risk.reasons.length > 0 ? (
          risk.reasons.map((reason, index) => (
            <li key={index}>{reason}</li>
          ))
        ) : (
          <li>No issues detected</li>
        )}
      </ul>
    </div>
  );
}

export default RiskCard;