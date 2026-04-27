document.addEventListener('DOMContentLoaded', function() {
    const navbar = document.querySelector('.navbar');
    let lastScrollY = window.scrollY;
    let isHidden = false;

    window.addEventListener('scroll', function() {
        const currentScrollY = window.scrollY;
        
        // 下滑时隐藏导航栏
        if (currentScrollY > lastScrollY && currentScrollY > 100 && !isHidden) {
            navbar.classList.add('hidden');
            isHidden = true;
        }
        // 上滑时显示导航栏
        else if (currentScrollY < lastScrollY && isHidden) {
            navbar.classList.remove('hidden');
            isHidden = false;
        }
        
        // 滚动超过100px时添加阴影
        if (currentScrollY > 100) {
            navbar.style.boxShadow = '0 8px 32px rgba(12, 74, 110, 0.15)';
        } else {
            navbar.style.boxShadow = '0 4px 24px rgba(12, 74, 110, 0.1)';
        }
        
        lastScrollY = currentScrollY;
    });

    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            // 只有当链接是当前页面的锚点链接时，才阻止默认行为
            if (href.startsWith('#')) {
                e.preventDefault();
                const targetId = href;
                const targetSection = document.querySelector(targetId);
                if (targetSection) {
                    targetSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
            }
            // 对于跨页面的链接，允许默认行为
        });
    });

    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    const animatedElements = document.querySelectorAll('.service-card, .advantage-item');
    animatedElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });

    const serviceCards = document.querySelectorAll('.service-card');
    serviceCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transition = 'all 0.3s ease';
        });
    });

    const buttons = document.querySelectorAll('.btn-primary, .btn-secondary, .nav-cta');
    buttons.forEach(button => {
        button.addEventListener('click', function(e) {
            const ripple = document.createElement('span');
            const rect = this.getBoundingClientRect();
            const size = Math.max(rect.width, rect.height);
            const x = e.clientX - rect.left - size / 2;
            const y = e.clientY - rect.top - size / 2;
            
            ripple.style.width = ripple.style.height = size + 'px';
            ripple.style.left = x + 'px';
            ripple.style.top = y + 'px';
            ripple.style.position = 'absolute';
            ripple.style.borderRadius = '50%';
            ripple.style.background = 'rgba(255, 255, 255, 0.5)';
            ripple.style.transform = 'scale(0)';
            ripple.style.animation = 'ripple 0.6s ease-out';
            ripple.style.pointerEvents = 'none';
            
            this.style.position = 'relative';
            this.style.overflow = 'hidden';
            this.appendChild(ripple);
            
            setTimeout(() => ripple.remove(), 600);
        });
    });

    const style = document.createElement('style');
    style.textContent = `
        @keyframes ripple {
            to {
                transform: scale(4);
                opacity: 0;
            }
        }
    `;
    document.head.appendChild(style);

    // 百度搜索引擎推送功能
    function pushToBaidu(url) {
        const apiUrl = '/api/baidu-push';
        
        fetch(apiUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ url: url })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                console.log('百度推送成功:', data.data);
            } else {
                console.error('百度推送失败:', data.error);
            }
        })
        .catch(error => {
            console.error('百度推送请求失败:', error);
        });
    }

    // 页面加载时推送当前页面
    const currentUrl = window.location.href;
    pushToBaidu(currentUrl);

    console.log('Walanka AI Website Loaded Successfully!');
});