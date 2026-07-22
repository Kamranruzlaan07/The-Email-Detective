function ProviderCard({ provider }) {
  return (
    <div className="card">
      <h2>📧 Email Provider</h2>

      <p>
        <strong>Provider:</strong>{" "}
        {provider?.name || "Unknown"}
      </p>

      <p>
        <strong>Confidence:</strong>{" "}
        <span
          className={`badge ${
            provider?.confidence?.toLowerCase() || "unknown"
          }`}
        >
          {provider?.confidence || "Unknown"}
        </span>
      </p>

      <p>
        <strong>Matched Domain:</strong>{" "}
        {provider?.matched_domain || "N/A"}
      </p>
    </div>
  );
}

export default ProviderCard;