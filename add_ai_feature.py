import os
import glob
import re

ai_widget_html = """
<!-- Elite AI Concierge -->
<div id="ai-widget-container" class="fixed bottom-6 right-6 z-[200] font-['Manrope']">
    <!-- Chat Button -->
    <button id="ai-toggle-btn" class="bg-[#366549] text-white p-4 rounded-full shadow-2xl hover:scale-110 hover:bg-[#2a593e] transition-all flex items-center justify-center border-2 border-[#b5e9c5]/30 group">
        <span class="material-symbols-outlined text-3xl group-hover:rotate-12 transition-transform">smart_toy</span>
    </button>

    <!-- Chat Box -->
    <div id="ai-chat-box" class="absolute bottom-20 right-0 w-80 md:w-96 bg-white rounded-2xl shadow-[0_30px_60px_rgba(0,0,0,0.15)] border border-[#acadac]/20 hidden flex-col overflow-hidden transform origin-bottom-right transition-all duration-300 opacity-0 scale-95">
        <!-- Header -->
        <div class="bg-[#366549] text-white p-5 flex justify-between items-center">
            <div class="flex items-center gap-3">
                <span class="material-symbols-outlined">psychology</span>
                <div>
                    <h4 class="font-['Epilogue'] font-black text-sm uppercase tracking-widest">Elite AI Concierge</h4>
                    <p class="text-[10px] text-[#c3f7d3] uppercase tracking-widest">Online • Navigational Assistant</p>
                </div>
            </div>
            <button id="ai-close-btn" class="text-white hover:text-[#c3f7d3] transition-colors p-1">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <line x1="18" y1="6" x2="6" y2="18"></line>
                    <line x1="6" y1="6" x2="18" y2="18"></line>
                </svg>
            </button>
        </div>
        
        <!-- Chat Area -->
        <div id="ai-messages" class="p-5 h-72 overflow-y-auto bg-[#f6f6f5] flex flex-col gap-4">
            <div class="bg-white p-4 rounded-xl rounded-tl-sm shadow-sm border border-[#acadac]/10 self-start max-w-[85%]">
                <p class="text-sm text-[#575d5a] leading-relaxed">Greetings. I am the Elite AI Concierge. Do you require assistance navigating our digital estate?</p>
            </div>
            
            <!-- Quick Options -->
            <div id="ai-quick-options" class="flex flex-col gap-2 mt-2 w-full">
                <button class="ai-quick-btn text-left text-xs font-bold text-[#366549] bg-[#c3f7d3]/30 hover:bg-[#c3f7d3] p-3 rounded-lg border border-[#c3f7d3] transition-colors" data-reply="Where can I view your past work?" data-action="window.location.href='portfolio.html'">Show me the Portfolio</button>
                <button class="ai-quick-btn text-left text-xs font-bold text-[#366549] bg-[#c3f7d3]/30 hover:bg-[#c3f7d3] p-3 rounded-lg border border-[#c3f7d3] transition-colors" data-reply="How does the 48-Hour Strike work?" data-action="window.location.href='process.html'">Explain the Process</button>
                <button class="ai-quick-btn text-left text-xs font-bold text-[#366549] bg-[#c3f7d3]/30 hover:bg-[#c3f7d3] p-3 rounded-lg border border-[#c3f7d3] transition-colors" data-reply="I need to speak with an architect." data-action="window.location.href='contact.html'">Request Consultation</button>
            </div>
        </div>
    </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const aiToggleBtn = document.getElementById('ai-toggle-btn');
    const aiChatBox = document.getElementById('ai-chat-box');
    const aiCloseBtn = document.getElementById('ai-close-btn');
    const aiMessages = document.getElementById('ai-messages');
    const quickBtns = document.querySelectorAll('.ai-quick-btn');
    const aiQuickOptions = document.getElementById('ai-quick-options');

    function toggleChat() {
        if (aiChatBox.classList.contains('hidden')) {
            aiChatBox.classList.remove('hidden');
            setTimeout(() => {
                aiChatBox.classList.remove('opacity-0', 'scale-95');
                aiChatBox.classList.add('opacity-100', 'scale-100');
            }, 10);
        } else {
            aiChatBox.classList.remove('opacity-100', 'scale-100');
            aiChatBox.classList.add('opacity-0', 'scale-95');
            setTimeout(() => {
                aiChatBox.classList.add('hidden');
            }, 300);
        }
    }

    if(aiToggleBtn && aiChatBox && aiCloseBtn) {
        aiToggleBtn.addEventListener('click', toggleChat);
        aiCloseBtn.addEventListener('click', toggleChat);
    }

    quickBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            // Remove options
            aiQuickOptions.style.display = 'none';
            
            // Add user message
            const userMsg = document.createElement('div');
            userMsg.className = 'bg-[#366549] text-white p-3 rounded-xl rounded-tr-sm shadow-sm self-end max-w-[85%] text-sm';
            userMsg.textContent = this.getAttribute('data-reply');
            aiMessages.appendChild(userMsg);
            
            // Scroll down
            aiMessages.scrollTop = aiMessages.scrollHeight;
            
            // Simulate AI typing
            setTimeout(() => {
                const aiMsg = document.createElement('div');
                aiMsg.className = 'bg-white p-4 rounded-xl rounded-tl-sm shadow-sm border border-[#acadac]/10 self-start max-w-[85%] text-sm text-[#575d5a] leading-relaxed';
                aiMsg.innerHTML = 'Executing request... Redirecting you immediately.';
                aiMessages.appendChild(aiMsg);
                aiMessages.scrollTop = aiMessages.scrollHeight;
                
                // Execute action
                setTimeout(() => {
                    eval(this.getAttribute('data-action'));
                }, 1000);
            }, 800);
        });
    });
});
</script>
"""

def add_ai_and_interactivity():
    files = glob.glob('/Users/user/Documents/Elite 4/*.html')
    
    for f in files:
        with open(f, 'r') as file:
            content = file.read()
            
        # 1. Remove "custom design" / "they design it" implications
        content = content.replace(
            "custom outdoor living spaces.",
            "exclusive outdoor living estates."
        )
        content = content.replace(
            "We design and construct premium natural stone patios",
            "Our master architects design and engineer premium natural stone patios"
        )
        content = content.replace(
            "We draft fully symmetrical, 3D luxury landscape designs ensuring exact aesthetic alignment.",
            "You leave the design entirely to us. Our architects dictate the aesthetic and engineer a masterplan that guarantees absolute perfection."
        )
        
        # 2. Add AI Widget right before </body>
        if "id=\"ai-widget-container\"" not in content:
            content = content.replace("</body>", ai_widget_html + "\n</body>")
            
        with open(f, 'w') as file:
            file.write(content)

    print("AI Feature added and design verbiage updated.")

if __name__ == "__main__":
    add_ai_and_interactivity()
