import { useState } from "react";
import axios from "axios";
import { Link } from "react-router-dom";
import "../pages/NotesPage.scss";

//Import Components
import Notes from "../components/Notes/Notes";
import ViewOutput from "../components/ViewOutput/ViewOutput";
import VerticalNavBar from "../components/VerticalNavBar/VerticalNavBar";

function NotesPage() {
  const [notesText, setNotesText] = useState("");
  const [title, setTitle] = useState("");

  const handleSave = (e) => {
    const note = {
      title: title,
      content: notesText,
    };

    console.log("successfully saved");
    axios
      .post(`http://127.0.0.1:8000/api/notes/save/`, note)
      .then((response) => {
        console.log(response.data);
      })
      .catch((error) => {
        console.log("error saving post", error);
      });
  };

  return (
    <>
      <section className="page">
        <div className="container">
          <VerticalNavBar onSave={handleSave} />
          <Notes
            title={title}
            setTitle={setTitle}
            notesText={notesText}
            setNotesText={setNotesText}
            onSave={handleSave}
          />
          <ViewOutput notesText={notesText} />
        </div>
      </section>
    </>
  );
}

export default NotesPage;
