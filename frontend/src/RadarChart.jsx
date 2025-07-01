import React from 'react';
import { Radar } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  RadialLinearScale,
  PointElement,
  LineElement,
  Filler,
  Tooltip,
  Legend
} from 'chart.js';

ChartJS.register(
  RadialLinearScale,
  PointElement,
  LineElement,
  Filler,
  Tooltip,
  Legend
);

const labels = {
  akiec: "Kératose actinique",
  bcc: "Carcinome basocellulaire",
  bkl: "Kératose bénigne",
  df: "Dermatofibrome",
  mel: "Mélanome",
  nv: "Nævus",
  vasc: "Lésion vasculaire"
};

const RadarChart = ({ predictions }) => {
  const data = {
    labels: Object.keys(predictions).map(key => labels[key]),
    datasets: [
      {
        label: 'Probabilité',
        data: Object.values(predictions),
        backgroundColor: 'rgba(34, 197, 94, 0.2)',
        borderColor: 'rgba(34, 197, 94, 1)',
        borderWidth: 2
      }
    ]
  };

  return <Radar data={data} />;
};

export default RadarChart;
