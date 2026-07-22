export default function TrustCard({ trust }) {
  if (!trust) return null;

  const getBadgeColor = () => {
    switch (trust.rating) {
      case "Excellent":
        return "#16a34a";
      case "Good":
        return "#2563eb";
      case "Fair":
        return "#d97706";
      case "Poor":
        return "#dc2626";
      default:
        return "#6b7280";
    }
  };

  return (
    <div className="card">
      <h2>⭐ Trust Score</h2>

      <div
        style={{
          fontSize: "3rem",
          fontWeight: "700",
          color: "#ffffff",
          textAlign: "center",
          marginTop: "10px",
        }}
      >
        {trust.score}
        <span
          style={{
            fontSize: "1.3rem",
            color: "#9ca3af",
          }}
        >
          /100
        </span>
      </div>

      <div
        style={{
          textAlign: "center",
          color: "#facc15",
          fontSize: "1.4rem",
          letterSpacing: "2px",
          marginTop: "8px",
        }}
      >
        {"★".repeat(trust.stars)}
        {"☆".repeat(5 - trust.stars)}
      </div>

      <div
        style={{
          display: "inline-block",
          alignSelf: "center",
          margin: "15px auto",
          padding: "6px 14px",
          borderRadius: "20px",
          backgroundColor: getBadgeColor(),
          color: "white",
          fontWeight: "bold",
          fontSize: "0.9rem",
        }}
      >
        {trust.rating}
      </div>

      <hr
        style={{
          margin: "18px 0",
          opacity: 0.2,
        }}
      />

      <div
        style={{
          display: "flex",
          flexDirection: "column",
          gap: "8px",
        }}
      >
        {trust.reasons.map((reason, index) => (
          <div
            key={index}
            style={{
              display: "flex",
              alignItems: "center",
              gap: "10px",
              fontSize: "0.95rem",
            }}
          >
            <span
              style={{
                color: "#22c55e",
                fontWeight: "bold",
                fontSize: "1rem",
              }}
            >
              ✓
            </span>

            <span>{reason}</span>
          </div>
        ))}
      </div>
    </div>
  );
}