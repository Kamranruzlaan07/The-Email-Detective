function GeoCard({ geo }) {
  return (
    <div className="card">
      <h2>🌍 Geolocation</h2>

      {geo.map((location, index) => (
        <div key={index}>
          <p><strong>IP:</strong> {location.ip}</p>
          <p><strong>Country:</strong> {location.country}</p>
          <p><strong>City:</strong> {location.city}</p>
          <p><strong>ISP:</strong> {location.isp}</p>

          {index !== geo.length - 1 && <hr />}
        </div>
      ))}
    </div>
  );
}

export default GeoCard;