import { useState } from "react";
import axios from "axios";
import "./App.css";

import VerdictCard from "./components/VerdictCard";
import HeaderCard from "./components/HeaderCard";
import AuthenticationCard from "./components/AuthenticationCard";
import RiskCard from "./components/RiskCard";
import GeoCard from "./components/GeoCard";
import ProviderCard from "./components/ProviderCard";
import TrustCard from "./components/TrustCard";

const API_URL =
  import.meta.env.VITE_API_URL || "http://127.0.0.1:8000";

function App() {
  const [header, setHeader] = useState("");
  const [selectedFile, setSelectedFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleAnalyze = async () => {
    if (!header.trim()) return;

    setLoading(true);
    setResult(null);

    try {
      const response = await axios.post(
        `${API_URL}/analyze`,
        {
          header: header.trim(),
        }
      );

      setResult(response.data);
    } catch (error) {
      console.error(error);
      alert("Failed to analyze email headers.");
    } finally {
      setLoading(false);
    }
  };

  const handleFileChange = (e) => {
    const file = e.target.files[0];

    if (!file) {
      setSelectedFile(null);
      return;
    }

    if (!file.name.toLowerCase().endsWith(".eml")) {
      alert("Please select a valid .eml file.");
      e.target.value = "";
      return;
    }

    setSelectedFile(file);
  };

  const handleFileUpload = async () => {
    if (!selectedFile) return;

    setLoading(true);
    setResult(null);

    const formData = new FormData();
    formData.append("file", selectedFile);

    try {
      const response = await axios.post(
        `${API_URL}/analyze-file`,
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      setResult(response.data);
    } catch (error) {
      console.error(error);
      alert("Failed to analyze .eml file.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>The Email Detective</h1>

      <h2>Paste Email Headers</h2>

      <textarea
        placeholder="Paste the email header here..."
        value={header}
        onChange={(e) => setHeader(e.target.value)}
      />

      <button
        onClick={handleAnalyze}
        disabled={!header.trim() || loading}
      >
        {loading ? "Analyzing..." : "Analyze Headers"}
      </button>

      <div className="divider">
        <span>OR</span>
      </div>

      <h2>Upload .eml File</h2>

      <input
        type="file"
        accept=".eml"
        onChange={handleFileChange}
      />

      {selectedFile && (
        <p className="selected-file">
          📄 {selectedFile.name}
        </p>
      )}

      <button
        onClick={handleFileUpload}
        disabled={!selectedFile || loading}
      >
        {loading ? "Uploading..." : "Analyze .eml File"}
      </button>

      {result && (
        <>
          <VerdictCard
            risk={result.risk}
            authentication={result.authentication}
            geo={result.geo}
            trust={result.trust}
          />

          <div className="dashboard">
            <HeaderCard headers={result.headers} />

            <AuthenticationCard
              authentication={result.authentication}
            />

            <RiskCard risk={result.risk} />

            <GeoCard geo={result.geo} />

            <ProviderCard provider={result.provider} />

            <TrustCard trust={result.trust} />
          </div>
        </>
      )}
    </div>
  );
}

export default App;