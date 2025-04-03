import { useState, useEffect, useRef, useCallback } from "react";
import axios from "axios";
import debounce from "lodash/debounce";

import "../ViewOutput/ViewOutput.scss";
const DEBOUNCE_DELAY = 10000; //  seconds

function ViewOutput({ notesText, title }) {
  const [response, setResponse] = useState(null);
  const [lastSentText, setLastSentText] = useState("");
  const prevWordCountRef = useRef(0);

  const currentText = (text) => {
    return text.trim().split(/\s+/).filter(Boolean).length;
  };

  const tryParseJSON = (text) => {
    try {
      const parsed = JSON.parse(text);
      if (Array.isArray(parsed)) return parsed;
    } catch (err) {
      console.warn("Could not parse structured synthesis JSON:", err);
    }
    return text;
  };
  // Debounced API call
  const debouncedAPICall = useCallback(
    debounce((content, title) => {
      if (content.trim() === lastSentText.trim()) return;
      const payload = {
        title: title?.trim() || "Untitled",
        content: content,
      };

      console.log("Sending to /analyzedraft/:", payload);

      axios
        .post("http://127.0.0.1:8000/api/notes/analyzedraft/", payload)
        .then((res) => {
          setResponse(res.data);
          setLastSentText(content);
          console.log("API Response", res.data);
        })
        .catch((error) => console.log(error));
    }, DEBOUNCE_DELAY),
    [lastSentText]
  );

  useEffect(() => {
    const currentWordCount = currentText(notesText);

    if (currentWordCount >= 10 && notesText.trim().length > 0) {
      debouncedAPICall(notesText, title);
    }

    prevWordCountRef.current = currentWordCount;

    return () => {
      debouncedAPICall.cancel();
    };
  }, [notesText, title, debouncedAPICall]);

  return (
    <div className="viewOutputWrapper">
      <div className="viewOutput">
        {response ? (
          <span className="apiResponse">
            <h3>Similar Notes:</h3>
            <ul>
              {response.similar_notes.map((note, index) => (
                <li key={index}>
                  <strong>{note.title}</strong>
                  <p>{note.preview}</p>
                </li>
              ))}
            </ul>
            <h3>Synthesis:</h3>
            <p>{tryParseJSON(response.synthesis)}</p>
          </span>
        ) : (
          <p>Start typing and will load shortly...</p>
        )}
      </div>
    </div>
  );
}

export default ViewOutput;
