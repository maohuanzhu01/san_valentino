import React from 'react';
import '../styles/DaysCounter.css';

const DaysCounter = () => {
  // Calcola i giorni direttamente
  const startDate = new Date('2021-02-07');
  const today = new Date();
  const diffTime = Math.abs(today - startDate);
  const daysCount = Math.ceil(diffTime / (1000 * 60 * 60 * 24));

  return (
    <div className="days-counter-container">
      <div className="heart-background">
        <div className="counter-content">
          <h1>{daysCount}</h1>
          <h2>days together!</h2>
        </div>
      </div>
    </div>
  );
};

export default DaysCounter; 