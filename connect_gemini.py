import os
import glob
import re

API_KEY = "AIzaSyDXSFuM69s66-XDLXiXtKG6ncBnKBWhRGY"

new_ai_widget_html = f"""
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
                    <p class="text-[10px] text-[#c3f7d3] uppercase tracking-widest">Online • Generative AI Assistant</p>
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
                <p class="text-sm text-[#575d5a] leading-relaxed">Greetings. I am the Elite AI Concierge, powered by Google Gemini. How can I assist you with your luxury landscape project today?</p>
            </div>
            
            <!-- Quick Options -->
            <div id="ai-quick-options" class="flex flex-col gap-2 mt-2 w-full">
                <button class="ai-quick-btn text-left text-xs font-bold text-[#366549] bg-[#c3f7d3]/30 hover:bg-[#c3f7d3] p-3 rounded-lg border border-[#c3f7d3] transition-colors" data-reply="Where can I view your past work?">Show me the Portfolio</button>
                <button class="ai-quick-btn text-left text-xs font-bold text-[#366549] bg-[#c3f7d3]/30 hover:bg-[#c3f7d3] p-3 rounded-lg border border-[#c3f7d3] transition-colors" data-reply="How does the 48-Hour Strike work?">Explain the Process</button>
                <button class="ai-quick-btn text-left text-xs font-bold text-[#366549] bg-[#c3f7d3]/30 hover:bg-[#c3f7d3] p-3 rounded-lg border border-[#c3f7d3] transition-colors" data-reply="I need to speak with an architect.">Request Consultation</button>
            </div>
        </div>

        <!-- Input Area -->
        <div class="p-3 border-t border-[#acadac]/20 bg-white flex items-center gap-2">
            <input type="text" id="ai-input" class="w-full text-sm outline-none placeholder-[#acadac] text-[#575d5a]" placeholder="Ask the concierge..." autocomplete="off">
            <button id="ai-send-btn" class="text-[#366549] hover:text-[#2a593e] transition-colors p-1">
                <span class="material-symbols-outlined">send</span>
            </button>
        </div>
    </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', () => {{
    const aiToggleBtn = document.getElementById('ai-toggle-btn');
    const aiChatBox = document.getElementById('ai-chat-box');
    const aiCloseBtn = document.getElementById('ai-close-btn');
    const aiMessages = document.getElementById('ai-messages');
    const aiInput = document.getElementById('ai-input');
    const aiSendBtn = document.getElementById('ai-send-btn');
    const quickBtns = document.querySelectorAll('.ai-quick-btn');
    const aiQuickOptions = document.getElementById('ai-quick-options');

    const GEMINI_API_KEY = "{API_KEY}";
    
    // Conversation history to send to the model for context
    let conversationHistory = [];

    function toggleChat() {{
        if (aiChatBox.classList.contains('hidden')) {{
            aiChatBox.classList.remove('hidden');
            setTimeout(() => {{
                aiChatBox.classList.remove('opacity-0', 'scale-95');
                aiChatBox.classList.add('opacity-100', 'scale-100');
            }}, 10);
            aiInput.focus();
        }} else {{
            aiChatBox.classList.remove('opacity-100', 'scale-100');
            aiChatBox.classList.add('opacity-0', 'scale-95');
            setTimeout(() => {{
                aiChatBox.classList.add('hidden');
            }}, 300);
        }}
    }}

    if(aiToggleBtn && aiChatBox && aiCloseBtn) {{
        aiToggleBtn.addEventListener('click', toggleChat);
        aiCloseBtn.addEventListener('click', toggleChat);
    }}

    async function sendToGemini(text) {{
        // Hide quick options if they are still there
        if(aiQuickOptions) aiQuickOptions.style.display = 'none';

        // Add user message to UI
        const userMsg = document.createElement('div');
        userMsg.className = 'bg-[#366549] text-white p-3 rounded-xl rounded-tr-sm shadow-sm self-end max-w-[85%] text-sm';
        userMsg.textContent = text;
        aiMessages.appendChild(userMsg);
        aiMessages.scrollTop = aiMessages.scrollHeight;

        // Add loading indicator
        const loadingMsg = document.createElement('div');
        loadingMsg.className = 'bg-white p-4 rounded-xl rounded-tl-sm shadow-sm border border-[#acadac]/10 self-start max-w-[85%] text-sm text-[#575d5a] leading-relaxed';
        loadingMsg.textContent = 'Thinking...';
        aiMessages.appendChild(loadingMsg);
        aiMessages.scrollTop = aiMessages.scrollHeight;
        
        // Add user message to history
        conversationHistory.push({{"role": "user", "parts": [{{"text": text}}]}});

        try {{
            // Build the system prompt
            const systemPrompt = "You are the Elite AI Concierge for Elite 4 Landscaping, a luxury architectural landscaping firm in Minnesota. Provide helpful, concise, and professional answers. You represent a highly exclusive 4-man strike force that operates mostly on weekends. Keep answers relatively short.";
            
            // Build the payload
            const payload = {{
                "systemInstruction": {{
                    "parts": [
                        {{ "text": systemPrompt }}
                    ]
                }},
                "contents": conversationHistory,
                "generationConfig": {{
                    "temperature": 0.7,
                    "maxOutputTokens": 200
                }}
            }};

            const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${{GEMINI_API_KEY}}`, {{
                method: 'POST',
                headers: {{'Content-Type': 'application/json'}},
                body: JSON.stringify(payload)
            }});
            
            const data = await response.json();
            
            if (data.candidates && data.candidates[0].content) {{
                const aiText = data.candidates[0].content.parts[0].text;
                
                // Add model response to history
                conversationHistory.push({{"role": "model", "parts": [{{"text": aiText}}]}});
                
                // Convert simple markdown or newlines to HTML
                let formattedText = aiText.replace(/\\n/g, '<br>');
                formattedText = formattedText.replace(/\\*\\*(.*?)\\*\\*/g, '<b>$1</b>');
                
                loadingMsg.innerHTML = formattedText;
            }} else {{
                loadingMsg.textContent = "I am currently unable to process requests. Please try again later.";
            }}
        }} catch (e) {{
            console.error(e);
            loadingMsg.textContent = "Connection error. Please try again later.";
        }}
        aiMessages.scrollTop = aiMessages.scrollHeight;
    }}

    quickBtns.forEach(btn => {{
        btn.addEventListener('click', function() {{
            sendToGemini(this.getAttribute('data-reply'));
        }});
    }});
    
    aiSendBtn.addEventListener('click', () => {{
        if(aiInput.value.trim()) {{
            sendToGemini(aiInput.value.trim());
            aiInput.value = '';
        }}
    }});
    
    aiInput.addEventListener('keypress', (e) => {{
        if(e.key === 'Enter' && aiInput.value.trim()) {{
            sendToGemini(aiInput.value.trim());
            aiInput.value = '';
        }}
    }});
}});
</script>
"""

def apply_gemini_api():
    files = glob.glob('/Users/user/Documents/Elite 4/*.html')
    for f in files:
        with open(f, 'r') as file:
            content = file.read()
            
        # Strip existing widget
        content = re.sub(r'<!-- Elite AI Concierge -->.*?(?=</body>)', '', content, flags=re.DOTALL)
        
        # Add new widget
        if "id=\"ai-widget-container\"" not in content:
            content = content.replace("</body>", new_ai_widget_html + "\n</body>")
            
        with open(f, 'w') as file:
            file.write(content)
            
    print("Gemini API connected successfully to all HTML files!")

if __name__ == "__main__":
    apply_gemini_api()
