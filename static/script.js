document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('analyze-form');
    const uploadSection = document.getElementById('upload-section');
    const resultsSection = document.getElementById('results-section');
    const resetBtn = document.getElementById('reset-btn');
    const submitBtn = document.getElementById('submit-btn');
    const btnText = submitBtn.querySelector('.btn-text');
    const loader = document.getElementById('loader');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        // Validate
        const resumeFile = document.getElementById('resume').files[0];
        const jdFile = document.getElementById('job_description').files[0];
        const jdText = document.getElementById('job_description_text').value.trim();

        if (!resumeFile) {
            alert('Please select a resume file.');
            return;
        }

        if (!jdFile && !jdText) {
            alert('Please provide either a job description file or paste the text.');
            return;
        }

        // Prepare FormData
        const formData = new FormData();
        formData.append('resume', resumeFile);
        
        if (jdFile) formData.append('job_description', jdFile);
        if (jdText) formData.append('job_description_text', jdText);

        // UI State: Loading
        btnText.classList.add('hidden');
        loader.classList.remove('hidden');
        submitBtn.disabled = true;

        try {
            const response = await fetch('/api/analyze/', {
                method: 'POST',
                body: formData
            });

            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.detail || 'An error occurred during analysis.');
            }

            // Display Results
            document.getElementById('candidate-filename').textContent = data.resume_filename;
            
            // Render markdown using the marked.js library
            document.getElementById('evaluation-content').innerHTML = marked.parse(data.evaluation);
            
            // Switch views
            uploadSection.classList.add('hidden');
            resultsSection.classList.remove('hidden');

            // Scroll to top gently
            window.scrollTo({ top: 0, behavior: 'smooth' });

        } catch (error) {
            alert('Error: ' + error.message);
        } finally {
            // Restore UI State
            btnText.classList.remove('hidden');
            loader.classList.add('hidden');
            submitBtn.disabled = false;
        }
    });

    resetBtn.addEventListener('click', () => {
        form.reset();
        resultsSection.classList.add('hidden');
        uploadSection.classList.remove('hidden');
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
});
