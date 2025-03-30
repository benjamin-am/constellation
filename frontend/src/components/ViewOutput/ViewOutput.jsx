import { useState, useEffect, useRef } from "react";
import axios from "axios";

import "../ViewOutput/ViewOutput.scss";

function ViewOutput({ notesText }) {
  const [response, setResponse] = useState(null);
  const prevWordCountRef = useRef(0);

  const currentText = (text) => {
    return text.trim().split(/\s+/).filter(Boolean).length;
  };

  //API call
  useEffect(() => {
    const currentWordCount = currentText(notesText);
    const prevWordCount = prevWordCountRef.current;

    if (currentWordCount >= 10 && prevWordCount < 10) {
      axios
        .get(`http://127.0.0.1:8000/api/synthesize/`)
        .then((res) => {
          setResponse(res.data);
          console.log("API Response", res.data);
        })
        .catch((error) => console.log(error));
    }

    prevWordCountRef.current = currentWordCount;
  }, [notesText]);

  return (
    <div className="viewOutputWrapper">
      <div className="viewOutput">
        {response ? (
          <span className="apiResponse">
            {JSON.stringify(response, null, 1)}
          </span>
        ) : (
          <p>Start typing and will load shortly...</p>
        )}
      </div>
    </div>
  );
}
export default ViewOutput;
