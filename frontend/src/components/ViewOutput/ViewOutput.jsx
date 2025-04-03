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

  const parseAndRenderSynthesis = (text) => {
    if (!text || typeof text !== "string")
      return <p>No synthesis available.</p>;

    const lines = text.split("\n").filter(Boolean);
    const elements = [];
    let currentSection = {};

    lines.forEach((line) => {
      const [keyword, ...rest] = line.split(":");
      const value = rest.join(":").trim();

      switch (keyword.trim()) {
        case "Intro":
          elements.push(
            <p key="intro">
              <strong>Intro:</strong> {value}
            </p>
          );
          break;

        case "Connection Title":
          if (currentSection.title) {
            // Push previous connection section
            elements.push(
              <div key={currentSection.title}>
                <h4>Connection Title: {currentSection.title}</h4>
                <p>{currentSection.insight}</p>
                <em>Q: {currentSection.question}</em>
              </div>
            );
          }
          currentSection = { title: value };
          break;

        case "Insight":
          currentSection.insight = value;
          break;

        case "Question":
          currentSection.question = value;
          break;

        default:
          break;
      }
    });

    // Push the final connection section if it exists
    if (currentSection.title) {
      elements.push(
        <div key={currentSection.title}>
          <h4>Connection Title: {currentSection.title}</h4>
          <p>{currentSection.insight}</p>
          <em>Q: {currentSection.question}</em>
        </div>
      );
    }

    return <div>{elements}</div>;
  };

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
            <p>{parseAndRenderSynthesis(response.synthesis)}</p>
          </span>
        ) : (
          <p>Start typing and will load shortly...</p>
        )}
      </div>
    </div>
  );
}

export default ViewOutput;
