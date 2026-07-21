function AuthenticationCard({ authentication }) {
  return (
    <div className="card">
      <h2>🔐 Authentication</h2>

      <p>
        <strong>SPF:</strong>{" "}
        <span className={`badge ${authentication.spf}`}>
          {authentication.spf.toUpperCase()}
        </span>
      </p>

      <p>
        <strong>DKIM:</strong>{" "}
        <span className={`badge ${authentication.dkim}`}>
          {authentication.dkim.toUpperCase()}
        </span>
      </p>

      <p>
        <strong>DMARC:</strong>{" "}
        <span className={`badge ${authentication.dmarc}`}>
          {authentication.dmarc.toUpperCase()}
        </span>
      </p>
    </div>
  );
}

export default AuthenticationCard;