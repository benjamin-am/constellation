import { useState, useEffect, useRef } from "react";
import axios from "axios";

import "../ViewOutput/ViewOutput.scss";

function ViewOutput({ notesText, title }) {
  const [response, setResponse] = useState(null);
  const prevWordCountRef = useRef(0);

  const currentText = (text) => {
    return text.trim().split(/\s+/).filter(Boolean).length;
  };

  //API call
  useEffect(() => {
    const currentWordCount = currentText(notesText);
    const prevWordCount = prevWordCountRef.current;

    if (
      currentWordCount >= 30 &&
      prevWordCount < 30 &&
      notesText.trim().length > 0
    ) {
      const payload = {
        title: title,
        content: notesText,
      };

      console.log("Sending to /analyzedraft/:", payload);

      axios
        .post("http://127.0.0.1:8000/api/notes/analyzedraft/", payload)
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
            <h2>Synthesis:</h2>
            <p>{response.synthesis}</p>

            <h3>Similar Notes:</h3>
            <ul>
              {response.similar_notes.map((note, index) => (
                <li key={index}>
                  <strong>{note.title}</strong>
                  <p>{note.preview}</p>{" "}
                  {/* Show preview instead of full content */}
                </li>
              ))}
            </ul>
          </span>
        ) : (
          <p>Start typing and will load shortly...</p>
        )}
      </div>
    </div>
  );
}
export default ViewOutput;
