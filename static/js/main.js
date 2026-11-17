/* ==========================================================================
   Gym Management System — Main JavaScript
   ========================================================================== */

(function () {
    'use strict';

    /* -----------------------------------------------------------------------
       1. Sidebar Toggle
       ----------------------------------------------------------------------- */
    const sidebar       = document.querySelector('.sidebar');
    const toggleBtn     = document.querySelector('.sidebar-toggle');
    const overlay       = document.querySelector('.sidebar-overlay');
    const mainContent   = document.querySelector('.main-content');

    function closeMobileSidebar() {
        if (sidebar)  sidebar.classList.remove('mobile-open');
        if (overlay)  overlay.classList.remove('active');
        document.body.style.overflow = '';
    }

    if (toggleBtn && sidebar) {
        toggleBtn.addEventListener('click', function () {
            if (window.innerWidth <= 768) {
                // Mobile: slide in / out
                sidebar.classList.toggle('mobile-open');
                if (overlay) overlay.classList.toggle('active');
                document.body.style.overflow = sidebar.classList.contains('mobile-open') ? 'hidden' : '';
            } else {
                // Desktop: collapse / expand
                sidebar.classList.toggle('collapsed');
            }
        });
    }

    if (overlay) {
        overlay.addEventListener('click', closeMobileSidebar);
    }

    /* -----------------------------------------------------------------------
       2. Responsive Sidebar — auto-close on resize
       ----------------------------------------------------------------------- */
    let resizeTimer;
    window.addEventListener('resize', function () {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(function () {
            if (window.innerWidth > 768) {
                closeMobileSidebar();
            }
        }, 150);
    });

    /* -----------------------------------------------------------------------
       3. User Profile Dropdown
       ----------------------------------------------------------------------- */
    const profileTrigger = document.querySelector('.user-profile');
    const dropdownMenu   = document.querySelector('.user-profile .dropdown-menu');

    if (profileTrigger && dropdownMenu) {
        profileTrigger.addEventListener('click', function (e) {
            e.stopPropagation();
            dropdownMenu.classList.toggle('show');
        });

        document.addEventListener('click', function () {
            dropdownMenu.classList.remove('show');
        });
    }

    /* -----------------------------------------------------------------------
       4. Delete Confirmation Dialogs
       ----------------------------------------------------------------------- */
    document.addEventListener('click', function (e) {
        const deleteBtn = e.target.closest('[data-confirm-delete]');
        if (!deleteBtn) return;

        e.preventDefault();
        const name = deleteBtn.getAttribute('data-name') || 'this item';
        const url  = deleteBtn.getAttribute('href') || deleteBtn.getAttribute('data-url');

        if (confirm('Are you sure you want to delete ' + name + '? This action cannot be undone.')) {
            if (deleteBtn.hasAttribute('data-ajax')) {
                ajaxRequest(url, { method: 'DELETE' })
                    .then(function () { location.reload(); })
                    .catch(function (err) { showFlash('Failed to delete: ' + err.message, 'error'); });
            } else if (url) {
                window.location.href = url;
            } else {
                // Submit the closest form
                var form = deleteBtn.closest('form');
                if (form) form.submit();
            }
        }
    });

    /* -----------------------------------------------------------------------
       5. DataTables Initialization
       ----------------------------------------------------------------------- */
    function initDataTables() {
        if (typeof $.fn === 'undefined' || typeof $.fn.DataTable === 'undefined') return;

        document.querySelectorAll('.data-table[data-datatable]').forEach(function (table) {
            if ($.fn.DataTable.isDataTable(table)) return; // already initialized
            $(table).DataTable({
                responsive: true,
                pageLength: 10,
                lengthMenu: [5, 10, 25, 50, 100],
                language: {
                    search: '',
                    searchPlaceholder: 'Search…',
                    lengthMenu: 'Show _MENU_ entries',
                    info: 'Showing _START_–_END_ of _TOTAL_',
                    emptyTable: 'No records found',
                    zeroRecords: 'No matching records'
                },
                dom: '<"d-flex justify-between align-center flex-wrap gap-2 mb-3"lf>rt<"d-flex justify-between align-center flex-wrap gap-2 mt-3"ip>',
                order: [[0, 'asc']]
            });
        });
    }

    /* -----------------------------------------------------------------------
       6. Form Validation Helpers
       ----------------------------------------------------------------------- */
    function validateForm(formEl) {
        let isValid = true;

        // Clear previous errors
        formEl.querySelectorAll('.is-invalid').forEach(function (el) {
            el.classList.remove('is-invalid');
        });
        formEl.querySelectorAll('.invalid-feedback').forEach(function (el) {
            el.remove();
        });

        // Required fields
        formEl.querySelectorAll('[required]').forEach(function (input) {
            if (!input.value.trim()) {
                markInvalid(input, 'This field is required.');
                isValid = false;
            }
        });

        // Email pattern
        formEl.querySelectorAll('input[type="email"]').forEach(function (input) {
            if (input.value && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(input.value)) {
                markInvalid(input, 'Please enter a valid email address.');
                isValid = false;
            }
        });

        // Phone pattern
        formEl.querySelectorAll('input[data-validate="phone"]').forEach(function (input) {
            if (input.value && !/^[\d\s\-+()]{7,15}$/.test(input.value)) {
                markInvalid(input, 'Please enter a valid phone number.');
                isValid = false;
            }
        });

        // Min length
        formEl.querySelectorAll('[minlength]').forEach(function (input) {
            var min = parseInt(input.getAttribute('minlength'), 10);
            if (input.value && input.value.length < min) {
                markInvalid(input, 'Must be at least ' + min + ' characters.');
                isValid = false;
            }
        });

        // Password match
        var pw  = formEl.querySelector('input[name="password"]');
        var cpw = formEl.querySelector('input[name="confirm_password"]');
        if (pw && cpw && cpw.value && pw.value !== cpw.value) {
            markInvalid(cpw, 'Passwords do not match.');
            isValid = false;
        }

        return isValid;
    }

    function markInvalid(input, message) {
        input.classList.add('is-invalid');
        var div = document.createElement('div');
        div.className = 'invalid-feedback';
        div.textContent = message;
        input.parentNode.appendChild(div);
    }

    // Attach to forms with data-validate
    document.querySelectorAll('form[data-validate]').forEach(function (form) {
        form.addEventListener('submit', function (e) {
            if (!validateForm(form)) {
                e.preventDefault();
                // Scroll to first error
                var first = form.querySelector('.is-invalid');
                if (first) first.focus();
            }
        });
    });

    // Live clear error on input
    document.addEventListener('input', function (e) {
        if (e.target.classList.contains('is-invalid')) {
            e.target.classList.remove('is-invalid');
            var fb = e.target.parentNode.querySelector('.invalid-feedback');
            if (fb) fb.remove();
        }
    });

    /* -----------------------------------------------------------------------
       7. Flash Message Auto-Dismiss (5 seconds)
       ----------------------------------------------------------------------- */
    function showFlash(message, type) {
        type = type || 'info';
        var container = document.querySelector('.flash-container');
        if (!container) {
            container = document.createElement('div');
            container.className = 'flash-container';
            document.body.appendChild(container);
        }

        var iconMap = {
            success: 'fa-check-circle',
            error:   'fa-exclamation-circle',
            danger:  'fa-exclamation-circle',
            warning: 'fa-exclamation-triangle',
            info:    'fa-info-circle'
        };

        var div = document.createElement('div');
        div.className = 'flash-message ' + type;
        div.innerHTML =
            '<i class="fas ' + (iconMap[type] || iconMap.info) + '"></i>' +
            '<span>' + message + '</span>' +
            '<button class="flash-close" aria-label="Close">&times;</button>';

        container.appendChild(div);

        // Close button
        div.querySelector('.flash-close').addEventListener('click', function () {
            dismissFlash(div);
        });

        // Auto-dismiss after 5 seconds
        setTimeout(function () { dismissFlash(div); }, 5000);
    }

    function dismissFlash(el) {
        if (!el || el._dismissed) return;
        el._dismissed = true;
        el.style.opacity = '0';
        el.style.transform = 'translateX(30px)';
        el.style.transition = 'all 0.3s ease';
        setTimeout(function () { if (el.parentNode) el.parentNode.removeChild(el); }, 300);
    }

    // Auto-dismiss server-rendered flash messages
    document.querySelectorAll('.flash-message').forEach(function (msg) {
        var closeBtn = msg.querySelector('.flash-close');
        if (closeBtn) {
            closeBtn.addEventListener('click', function () { dismissFlash(msg); });
        }
        setTimeout(function () { dismissFlash(msg); }, 5000);
    });

    // Expose globally for Jinja / other scripts
    window.showFlash = showFlash;

    /* -----------------------------------------------------------------------
       8. Dashboard Charts (Chart.js)
       ----------------------------------------------------------------------- */
    function initCharts() {
        if (typeof Chart === 'undefined') return;

        // Shared defaults
        Chart.defaults.font.family = "'Segoe UI', Roboto, 'Helvetica Neue', sans-serif";
        Chart.defaults.plugins.legend.labels.usePointStyle = true;

        // --- Membership Stats Bar Chart ---
        var memberCtx = document.getElementById('membershipChart');
        if (memberCtx) {
            new Chart(memberCtx.getContext('2d'), {
                type: 'bar',
                data: {
                    labels: window.chartData?.membershipLabels || ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
                    datasets: [{
                        label: 'New Members',
                        data: window.chartData?.membershipData || [12, 19, 8, 15, 22, 30, 25, 18, 28, 32, 24, 20],
                        backgroundColor: 'rgba(233, 69, 96, 0.75)',
                        borderColor: '#e94560',
                        borderWidth: 1,
                        borderRadius: 6,
                        maxBarThickness: 40
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        title: { display: true, text: 'Monthly Membership Registrations', font: { size: 14, weight: '600' } },
                        legend: { display: false }
                    },
                    scales: {
                        y: { beginAtZero: true, grid: { color: 'rgba(0,0,0,0.05)' } },
                        x: { grid: { display: false } }
                    }
                }
            });
        }

        // --- Revenue Line Chart ---
        var revenueCtx = document.getElementById('revenueChart');
        if (revenueCtx) {
            new Chart(revenueCtx.getContext('2d'), {
                type: 'line',
                data: {
                    labels: window.chartData?.revenueLabels || ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
                    datasets: [{
                        label: 'Revenue (₹)',
                        data: window.chartData?.revenueData || [45000, 52000, 38000, 61000, 55000, 72000, 68000, 59000, 78000, 82000, 71000, 90000],
                        borderColor: '#0f3460',
                        backgroundColor: 'rgba(15, 52, 96, 0.08)',
                        borderWidth: 2.5,
                        fill: true,
                        tension: 0.4,
                        pointBackgroundColor: '#0f3460',
                        pointBorderColor: '#fff',
                        pointBorderWidth: 2,
                        pointRadius: 4,
                        pointHoverRadius: 6
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        title: { display: true, text: 'Monthly Revenue', font: { size: 14, weight: '600' } },
                        legend: { display: false }
                    },
                    scales: {
                        y: { beginAtZero: true, grid: { color: 'rgba(0,0,0,0.05)' },
                             ticks: { callback: function (v) { return '₹' + v.toLocaleString(); } } },
                        x: { grid: { display: false } }
                    }
                }
            });
        }

        // --- Attendance Doughnut Chart ---
        var attendCtx = document.getElementById('attendanceChart');
        if (attendCtx) {
            new Chart(attendCtx.getContext('2d'), {
                type: 'doughnut',
                data: {
                    labels: window.chartData?.attendanceLabels || ['Morning', 'Afternoon', 'Evening'],
                    datasets: [{
                        data: window.chartData?.attendanceData || [35, 25, 40],
                        backgroundColor: ['#e94560', '#0f3460', '#27ae60'],
                        borderWidth: 0,
                        hoverOffset: 8
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        title: { display: true, text: 'Attendance Distribution', font: { size: 14, weight: '600' } },
                        legend: { position: 'bottom' }
                    },
                    cutout: '65%'
                }
            });
        }
    }

    /* -----------------------------------------------------------------------
       9. Table Search / Filter
       ----------------------------------------------------------------------- */
    function initTableSearch() {
        document.querySelectorAll('[data-table-search]').forEach(function (input) {
            var targetSelector = input.getAttribute('data-table-search');
            var table = document.querySelector(targetSelector);
            if (!table) return;

            input.addEventListener('input', function () {
                var query = this.value.toLowerCase().trim();
                var rows  = table.querySelectorAll('tbody tr');

                rows.forEach(function (row) {
                    var text = row.textContent.toLowerCase();
                    row.style.display = text.includes(query) ? '' : 'none';
                });
            });
        });
    }

    // Global search bar in navbar
    var globalSearch = document.querySelector('.search-bar input');
    if (globalSearch) {
        globalSearch.addEventListener('input', function () {
            var query = this.value.toLowerCase().trim();
            // Search visible data-table on the page
            document.querySelectorAll('.data-table tbody tr').forEach(function (row) {
                var text = row.textContent.toLowerCase();
                row.style.display = (!query || text.includes(query)) ? '' : 'none';
            });
        });
    }

    /* -----------------------------------------------------------------------
       10. Print Receipt
       ----------------------------------------------------------------------- */
    window.printReceipt = function (receiptId) {
        var receipt = document.getElementById(receiptId || 'receipt');
        if (!receipt) {
            showFlash('Receipt not found.', 'error');
            return;
        }

        var printWindow = window.open('', '_blank', 'width=450,height=600');
        printWindow.document.write(
            '<!DOCTYPE html><html><head><title>Receipt</title>' +
            '<style>' +
            'body { font-family: "Courier New", monospace; padding: 20px; color: #000; }' +
            '.receipt-header { text-align: center; border-bottom: 2px dashed #333; padding-bottom: 10px; margin-bottom: 10px; }' +
            '.receipt-row { display: flex; justify-content: space-between; padding: 4px 0; }' +
            '.receipt-total { border-top: 2px dashed #333; margin-top: 10px; padding-top: 10px; font-weight: bold; }' +
            'h2, h3, h4 { margin: 5px 0; }' +
            '</style></head><body>' +
            receipt.innerHTML +
            '<script>window.onload=function(){window.print();window.close();};<\/script>' +
            '</body></html>'
        );
        printWindow.document.close();
    };

    /* Print current page */
    window.printPage = function () {
        window.print();
    };

    /* -----------------------------------------------------------------------
       11. Date Picker Initialization
       ----------------------------------------------------------------------- */
    function initDatePickers() {
        // flatpickr (if loaded)
        if (typeof flatpickr !== 'undefined') {
            document.querySelectorAll('.date-picker').forEach(function (el) {
                flatpickr(el, {
                    dateFormat: 'Y-m-d',
                    allowInput: true
                });
            });

            document.querySelectorAll('.datetime-picker').forEach(function (el) {
                flatpickr(el, {
                    enableTime: true,
                    dateFormat: 'Y-m-d H:i',
                    allowInput: true
                });
            });
            return;
        }

        // Fallback: set type="date" on inputs that don't have it
        document.querySelectorAll('.date-picker').forEach(function (el) {
            if (el.type !== 'date') el.type = 'date';
        });
    }

    /* -----------------------------------------------------------------------
       12. AJAX Helper
       ----------------------------------------------------------------------- */
    function ajaxRequest(url, options) {
        options = options || {};
        var method  = (options.method || 'GET').toUpperCase();
        var headers = Object.assign({ 'X-Requested-With': 'XMLHttpRequest' }, options.headers || {});
        var body    = options.body || null;

        if (body && typeof body === 'object' && !(body instanceof FormData)) {
            headers['Content-Type'] = 'application/json';
            body = JSON.stringify(body);
        }

        return fetch(url, { method: method, headers: headers, body: body })
            .then(function (response) {
                if (!response.ok) throw new Error('HTTP ' + response.status);
                var ct = response.headers.get('content-type') || '';
                return ct.includes('application/json') ? response.json() : response.text();
            });
    }

    window.ajaxRequest = ajaxRequest;

    /* Convenience: buttons with data-ajax-url */
    document.addEventListener('click', function (e) {
        var btn = e.target.closest('[data-ajax-url]');
        if (!btn) return;
        e.preventDefault();

        var url    = btn.getAttribute('data-ajax-url');
        var method = btn.getAttribute('data-ajax-method') || 'POST';

        btn.disabled = true;
        btn.style.opacity = '0.6';

        ajaxRequest(url, { method: method })
            .then(function (data) {
                showFlash(typeof data === 'object' ? (data.message || 'Done!') : 'Done!', 'success');
                if (btn.hasAttribute('data-ajax-reload')) location.reload();
            })
            .catch(function (err) {
                showFlash('Error: ' + err.message, 'error');
            })
            .finally(function () {
                btn.disabled = false;
                btn.style.opacity = '';
            });
    });

    /* -----------------------------------------------------------------------
       13. Modal Helpers
       ----------------------------------------------------------------------- */
    // Open
    document.addEventListener('click', function (e) {
        var trigger = e.target.closest('[data-modal]');
        if (!trigger) return;
        e.preventDefault();
        var modal = document.querySelector(trigger.getAttribute('data-modal'));
        if (modal) {
            modal.classList.add('active');
            document.body.style.overflow = 'hidden';
        }
    });

    // Close
    document.addEventListener('click', function (e) {
        var closer = e.target.closest('.modal-close, [data-modal-close]');
        if (closer) {
            var overlay = closer.closest('.modal-overlay');
            if (overlay) {
                overlay.classList.remove('active');
                document.body.style.overflow = '';
            }
        }

        // Click outside
        if (e.target.classList.contains('modal-overlay')) {
            e.target.classList.remove('active');
            document.body.style.overflow = '';
        }
    });

    // Escape key
    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape') {
            document.querySelectorAll('.modal-overlay.active').forEach(function (m) {
                m.classList.remove('active');
            });
            document.body.style.overflow = '';
        }
    });

    /* -----------------------------------------------------------------------
       14. Tooltip Bootstrap (optional — simple title-based)
       ----------------------------------------------------------------------- */
    document.querySelectorAll('[data-tooltip]').forEach(function (el) {
        el.setAttribute('title', el.getAttribute('data-tooltip'));
    });

    /* -----------------------------------------------------------------------
       15. Active Nav Link Highlight
       ----------------------------------------------------------------------- */
    (function highlightActiveNav() {
        var path = window.location.pathname;
        document.querySelectorAll('.sidebar .nav-link').forEach(function (link) {
            var href = link.getAttribute('href');
            if (!href) return;
            if (href === path || (href !== '/' && path.startsWith(href))) {
                link.classList.add('active');
            }
        });
    })();

    /* -----------------------------------------------------------------------
       16. Number Counter Animation (stat cards)
       ----------------------------------------------------------------------- */
    function animateCounters() {
        document.querySelectorAll('[data-count]').forEach(function (el) {
            if (el._counted) return;
            el._counted = true;
            var target   = parseInt(el.getAttribute('data-count'), 10) || 0;
            var duration = 1200;
            var start    = 0;
            var startTime = null;

            function step(ts) {
                if (!startTime) startTime = ts;
                var progress = Math.min((ts - startTime) / duration, 1);
                var value    = Math.floor(progress * target);
                el.textContent = value.toLocaleString();
                if (progress < 1) requestAnimationFrame(step);
                else el.textContent = target.toLocaleString();
            }

            requestAnimationFrame(step);
        });
    }

    /* -----------------------------------------------------------------------
       Boot
       ----------------------------------------------------------------------- */
    document.addEventListener('DOMContentLoaded', function () {
        initDataTables();
        initTableSearch();
        initDatePickers();
        initCharts();
        animateCounters();

        // Page fade-in
        document.querySelectorAll('.fade-in-on-load').forEach(function (el) {
            el.classList.add('fade-in');
        });
    });

})();
