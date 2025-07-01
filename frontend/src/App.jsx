import React, { useState } from 'react';
import axios from 'axios';
import RadarChart from './RadarChart';

const App = () => {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) return;

    const formData = new FormData();
    formData.append('file', file);

    const res = await axios.post('/predict', formData);
    setResult(res.data);
  };

  return (
    <div className="p-6 space-y-4 text-center">
      <form onSubmit={handleSubmit} className="space-y-2">
        <input
          type="file"
          onChange={(e) => setFile(e.target.files[0])}
          className="block mx-auto"
        />
        <button
          type="submit"
          className="px-4 py-2 bg-green-600 text-white rounded-lg"
        >
          Analyser
        </button>
      </form>
      {result && <RadarChart predictions={result.predictions_by_class} />}
    </div>
  );
};

export default App;
