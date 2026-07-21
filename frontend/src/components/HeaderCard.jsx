function HeaderCard({ headers }) {
  return (
    <div className="card">
      <h2>📧 Header Information</h2>

      <p><strong>From:</strong> {headers.from}</p>
      <p><strong>To:</strong> {headers.to || "N/A"}</p>
      <p><strong>Subject:</strong> {headers.subject}</p>
      <p><strong>Date:</strong> {headers.date || "N/A"}</p>
    </div>
  );
}

export default HeaderCard;