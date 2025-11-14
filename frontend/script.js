const API_BASE = "http://127.0.0.1:8000/resume";

// Handle tab switching
function showTab(tabId) {
  document.querySelectorAll('.tab-content').forEach(tab => tab.classList.remove('active'));
  document.querySelectorAll('.tab-button').forEach(btn => btn.classList.remove('active'));
  document.getElementById(tabId).classList.add('active');
  event.target.classList.add('active');

  if (tabId === 'history') {
    loadResumes();
  }
}

// Handle resume upload
document.getElementById('uploadForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  
  const fileInput = document.getElementById('resumeFile');
  if (!fileInput.files[0]) {
    alert("⚠️ Please select a resume file first!");
    return;
  }

  const formData = new FormData();
  formData.append('file', fileInput.files[0]);

  const resultDiv = document.getElementById('result');
  resultDiv.innerHTML = "<p>⏳ Uploading & analyzing resume... please wait.</p>";

  try {
    const response = await fetch(`${API_BASE}/upload`, {
      method: 'POST',
      body: formData
    });

    const data = await response.json();
    console.log("📩 Server Response:", data);

    if (data && data.data) {
      resultDiv.innerHTML = `
        <div class="result-card">
          <h3>🧾 Resume Analysis Result</h3>
          <p><strong>👤 Name:</strong> ${data.data.name || 'N/A'}</p>
          <p><strong>📧 Email:</strong> ${data.data.email || 'N/A'}</p>
          <p><strong>📞 Phone:</strong> ${data.data.phone || 'N/A'}</p>
          <p><strong>🧠 Skills:</strong> ${data.data.core_skills || 'N/A'}</p>
          <p><strong>⭐ Rating:</strong> ${data.data.resume_rating || 'N/A'}</p>
          <p><strong>🧩 Improvement Areas:</strong><br>${data.data.improvement_areas || 'N/A'}</p>
          <p><strong>🚀 Upskill Suggestions:</strong><br>${Array.isArray(data.data.upskill_suggestions) ? data.data.upskill_suggestions.join(', ') : data.data.upskill_suggestions}</p>
          <p class="success">✔ Resume analyzed & saved successfully!</p>
        </div>
      `;
    } else {
      resultDiv.innerHTML = "<p class='error'>❌ Server returned no data. Please try again.</p>";
    }
  } catch (error) {
    console.error("❌ Error:", error);
    resultDiv.innerHTML = "<p class='error'>❌ Failed to upload or analyze resume.</p>";
  }
});

// Load all stored resumes
async function loadResumes() {
  try {
    const response = await fetch(`${API_BASE}/all`);
    const data = await response.json();

    const tbody = document.querySelector('#resumeTable tbody');
    tbody.innerHTML = '';

    data.forEach(r => {
      const row = `
        <tr>
          <td>${r.id}</td>
          <td>${r.name || '-'}</td>
          <td>${r.email || '-'}</td>
          <td>${r.phone || '-'}</td>
          <td>${r.core_skills || '-'}</td>
        </tr>
      `;
      tbody.innerHTML += row;
    });
  } catch (err) {
    console.error("Error loading resumes:", err);
  }
}
