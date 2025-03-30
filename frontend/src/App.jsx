import "./App.scss";
import {BrowserRouter, Routes, Route} from 'react-router-dom';

import NotesPage from './pages/NotesPage';
import HomePage from "./pages/HomePage";
import PastNotesPage from "./pages/PastNotesPage";

function App() {
  return (
    <div className="App">
        <BrowserRouter>
    <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/notes" element={<NotesPage />} />
        <Route path="/pastNotes" element={<PastNotesPage />} />
    </Routes>
      
      </BrowserRouter>
    </div>
  );
}

export default App;
