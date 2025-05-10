// Data visualization to show mood trends over time
import React from 'react';
import { Line } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement,
  Tooltip,
  Legend,
} from 'chart.js';

ChartJS.register(LineElement, CategoryScale, LinearScale, PointElement, Tooltip, Legend);

export default function Chart({ moodLogs }) {
  // Filter mood logs to include only those with a sentiment score
  const filteredLogs = moodLogs.filter((log) => log.sentiment_score !== null);

  // Prepare data for the chart
  const data = {
    labels: filteredLogs.map((log) =>
      new Date(log.created_at).toLocaleDateString('en-US', {
        month: 'short',
        day: 'numeric',
      })
    ),
    datasets: [
      {
        label: 'Sentiment Score',
        data: filteredLogs.map((log) => log.sentiment_score),
        borderColor: 'rgba(75, 192, 192, 1)',
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        borderWidth: 2,
        tension: 0.4, // Smooth curve
        pointRadius: 4,
        pointBackgroundColor: 'rgba(75, 192, 192, 1)',
      },
    ],
  };

  const options = {
    responsive: true,
    plugins: {
      legend: {
        display: true,
        position: 'top',
      },
      tooltip: {
        enabled: true,
      },
    },
    scales: {
      y: {
        beginAtZero: true,
        min: -1,
        max: 1,
        title: {
          display: true,
          text: 'Sentiment Score',
        },
      },
      x: {
        title: {
          display: true,
          text: 'Date',
        },
      },
    },
  };

  return (
    <div className="card bg-base-100 w-full shadow-sm p-4">
      <h2 className="card-title text-center mb-4">Mood Trends</h2>
      <div style={{ width: '80%', height: '300px', margin: '0 auto' }}>
        <Line data={data} options={options} />
      </div>
    </div>
  );
}
