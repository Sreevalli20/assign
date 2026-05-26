import React from 'react'
import ReactDOM from 'react-dom/client'
import axios from 'axios'

function App() {

  const upload = async () => {
    await axios.post('http://localhost:8000/api/upload/')
    alert('Sample data uploaded')
  }

  return (
    <div style={{padding: 40, fontFamily: 'Arial'}}>
      <h1>Breathe ESG Prototype</h1>

      <button onClick={upload}>
        Upload SAP Sample Data
      </button>

      <p style={{marginTop: 20}}>
        ESG ingestion and review prototype
      </p>
    </div>
  )
}

ReactDOM.createRoot(document.getElementById('root')).render(<App />)