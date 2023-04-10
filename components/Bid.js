import React, { useEffect, useState } from 'react';

const Bid = () => {
  const [bid, setBid] = useState([]);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const response = await fetch('api-url');
      const data = await response.json();
      setBid(data);
    } catch (error) {
      console.error('Fetching Error:', error);
    }
  };

  return (
    <div>
      <h1>Bid Data</h1>
      {bid.map((bid) => (
        <div key={bid.id}>
          <p>Product: {bid.product}</p>
          <p>Bidder: {bid.bidder}</p>
          <p>Amount: {bid.amount}</p>
          <p>Time: {bid.time}</p>
        </div>
      ))}
    </div>
  );
};

export default Bid;
