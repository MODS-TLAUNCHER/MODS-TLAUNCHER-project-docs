/**
 * Custom JavaScript for biUNestar
 */

document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Initialize popovers
    const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });

    // Auto-dismiss alerts after 5 seconds
    setTimeout(function() {
        const alerts = document.querySelectorAll('.alert:not(.alert-permanent)');
        alerts.forEach(function(alert) {
            bootstrap.Alert.getInstance(alert)?.close();
        });
    }, 5000);

    // Form validation enhancement
    const forms = document.querySelectorAll('.needs-validation');
    Array.from(forms).forEach(function(form) {
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });

    // Toggle password visibility
    const togglePasswordButtons = document.querySelectorAll('.toggle-password');
    togglePasswordButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            const targetId = this.getAttribute('data-target');
            const targetInput = document.getElementById(targetId);
            
            if (targetInput.type === 'password') {
                targetInput.type = 'text';
                this.innerHTML = '<i class="fas fa-eye-slash"></i>';
            } else {
                targetInput.type = 'password';
                this.innerHTML = '<i class="fas fa-eye"></i>';
            }
        });
    });

    // Habit completion toggle
    const completionCheckboxes = document.querySelectorAll('.completion-checkbox');
    completionCheckboxes.forEach(function(checkbox) {
        checkbox.addEventListener('change', function() {
            const habitId = this.getAttribute('data-habit-id');
            const isCompleted = this.checked;
            
            // Update server via AJAX
            fetch(`/habits/${habitId}/toggle/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify({completed: isCompleted})
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // Update UI
                    const badge = this.closest('.habit-item').querySelector('.completion-badge');
                    badge.textContent = isCompleted ? '✅ Completado' : '⏳ Pendiente';
                    badge.className = `badge ${isCompleted ? 'bg-success' : 'bg-secondary'} completion-badge`;
                }
            });
        });
    });

    // Theme toggle
    const themeToggle = document.getElementById('themeToggle');
    if (themeToggle) {
        themeToggle.addEventListener('click', function() {
            const currentTheme = document.documentElement.getAttribute('data-bs-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            
            document.documentElement.setAttribute('data-bs-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            
            this.innerHTML = newTheme === 'dark' 
                ? '<i class="fas fa-sun"></i>' 
                : '<i class="fas fa-moon"></i>';
        });
        
        // Load saved theme
        const savedTheme = localStorage.getItem('theme') || 'light';
        document.documentElement.setAttribute('data-bs-theme', savedTheme);
        themeToggle.innerHTML = savedTheme === 'dark' 
            ? '<i class="fas fa-sun"></i>' 
            : '<i class="fas fa-moon"></i>';
    }

    // Mobile sidebar toggle
    const sidebarToggle = document.getElementById('sidebarToggle');
    if (sidebarToggle) {
        sidebarToggle.addEventListener('click', function() {
            document.querySelector('.sidebar').classList.toggle('show');
        });
    }

    // Habit value field toggle
    const completionCheckboxes = document.querySelectorAll('input[name="completed"]');
    completionCheckboxes.forEach(function(checkbox) {
        checkbox.addEventListener('change', function() {
            const valueField = this.closest('form').querySelector('input[name="value"]');
            if (valueField) {
                valueField.disabled = !this.checked;
                if (!this.checked) {
                    valueField.value = 0;
                }
            }
        });
        
        // Initialize state
        if (checkbox.checked) {
            checkbox.dispatchEvent(new Event('change'));
        }
    });
});

// Utility function to get CSRF token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Habit statistics calculation
function calculateHabitStats(records, goal) {
    const total = records.length;
    const completed = records.filter(r => r.completed).length;
    const completionRate = total > 0 ? (completed / total * 100) : 0;
    const streak = calculateStreak(records);
    
    return {
        total,
        completed,
        completionRate: completionRate.toFixed(1),
        streak,
        goalAchievement: total > 0 ? Math.min((completed / (goal * total)) * 100, 100).toFixed(1) : 0
    };
}

function calculateStreak(records) {
    // Sort records by date descending
    const sortedRecords = [...records].sort((a, b) => new Date(b.date) - new Date(a.date));
    
    let streak = 0;
    let currentDate = new Date();
    
    for (const record of sortedRecords) {
        const recordDate = new Date(record.date);
        const diffDays = Math.floor((currentDate - recordDate) / (1000 * 60 * 60 * 24));
        
        if (diffDays <= 1 && record.completed) {
            streak++;
            currentDate = recordDate;
        } else {
            break;
        }
    }
    
    return streak;
}

// Export data function
function exportHabitData(format = 'csv') {
    // This would be implemented with actual data export logic
    alert(`Exporting data in ${format.toUpperCase()} format...`);
}