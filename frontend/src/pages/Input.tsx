import { useState } from "react";

function App() {
  const [date, setDate] = useState(null);

  const handleClick = () => {};

  const handleChange = () => {};

  return (
    <div>
      <h1 className="text-xl"> Wildfire Tracker x Predictor</h1>
      <input type="Date" onChange={handleChange} />
      <button onClick={handleClick}>Submit</button>
    </div>
  );
}

export default App;
