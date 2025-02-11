import React, { useEffect, useState } from 'react';
import '../styles/DaysCounter.css';

const DaysCounter = () => {
  const [daysCount, setDaysCount] = useState(0);
  const startDate = '2021-02-07';

  useEffect(() => {
    const fetchDays = async () => {
      try {
        const response = await fetch('http://localhost:8000/calculate-days/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            date: startDate,
            description: 'Il nostro inizio'
          })
        });
        const data = await response.json();
        setDaysCount(data.days_passed);
      } catch (error) {
        console.error('Error fetching days:', error);
      }
    };

    fetchDays();
  }, []);

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