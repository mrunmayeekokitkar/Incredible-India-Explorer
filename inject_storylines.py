import os

filepath = 'd:/INDIA/travel.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Hero to use rotating text
target_hero = '<h1 class="hero-title animate-slide-up">Travel <span class="highlight">Explorer</span></h1>'
replace_hero = '<h1 class="hero-title animate-slide-up">Travel <span class="highlight rotating-text-container rotating-text-wrapper" data-words="Explorer, Destinations, Journeys, Adventures"></span></h1>'
content = content.replace(target_hero, replace_hero)

# 2. Insert Narrative Storyline
storyline_html = """
        <!-- The Great Indian Journey Storyline -->
        <section class="fade-in-section" style="padding: 20px 0;">
            <div class="section-container">
                <div class="section-header">
                    <span class="section-badge">Narrative</span>
                    <h2>A Journey Down the Subcontinent</h2>
                </div>
                
                <div class="narrative-storyline">
                    <div class="story-step scroll-section">
                        <span class="story-time">01 • The Northern Peaks</span>
                        <div class="story-content">
                            <h3>The Roof of the World</h3>
                            <p>Our journey begins in the high-altitude deserts of Ladakh and the snow-capped peaks of Kashmir. Here, ancient Buddhist monasteries cling to sheer cliff faces, and the air is thin but pure. Trekking through the Himalayas offers an unmatched sense of spiritual and physical elevation.</p>
                        </div>
                    </div>
                    
                    <div class="story-step scroll-section">
                        <span class="story-time">02 • The Golden Heart</span>
                        <div class="story-content">
                            <h3>Sands of Time</h3>
                            <p>Moving southwest, the landscape flattens into the golden expanse of the Thar Desert. Magnificent sandstone forts rise from the dunes like mirages in Rajasthan. The rich Rajput heritage is alive in the vibrant colors worn by locals, contrasting sharply with the arid surroundings.</p>
                        </div>
                    </div>
                    
                    <div class="story-step scroll-section">
                        <span class="story-time">03 • The Emerald Coast</span>
                        <div class="story-content">
                            <h3>Monsoon Canopies</h3>
                            <p>Continuing south, we enter the dense, tropical rainforests of the Western Ghats. A UNESCO World Heritage site, these mountains catch the monsoon rains, feeding countless waterfalls and rivers. The air here is thick with the scent of wild cardamom, coffee, and pepper.</p>
                        </div>
                    </div>
                    
                    <div class="story-step scroll-section">
                        <span class="story-time">04 • The Ocean's Embrace</span>
                        <div class="story-content">
                            <h3>Where Three Seas Meet</h3>
                            <p>Our journey concludes at Kanyakumari, the southernmost tip of mainland India. Here, the Arabian Sea, the Bay of Bengal, and the Indian Ocean converge. Watching the sunset and moonrise simultaneously over the vast ocean is a humbling end to the great Indian journey.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
"""

content = content.replace('<!-- Destinations Section -->', storyline_html + '\n        <!-- Destinations Section -->')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

# Do the same for wildlife.html
filepath_wildlife = 'd:/INDIA/wildlife.html'
with open(filepath_wildlife, 'r', encoding='utf-8') as f:
    content_w = f.read()

target_hero_w = '<h1 class="hero-title animate-slide-up">Nature & <span class="highlight">Wildlife</span></h1>'
replace_hero_w = '<h1 class="hero-title animate-slide-up">Nature & <span class="highlight rotating-text-container rotating-text-wrapper" data-words="Wildlife, Conservation, Ecosystems, Habitats"></span></h1>'
content_w = content_w.replace(target_hero_w, replace_hero_w)

storyline_w = """
        <!-- A Day in the Jungle Storyline -->
        <section class="fade-in-section" style="padding: 20px 0;">
            <div class="section-container">
                <div class="section-header">
                    <span class="section-badge">Narrative</span>
                    <h2>A Day in the Indian Jungle</h2>
                </div>
                
                <div class="narrative-storyline">
                    <div class="story-step scroll-section">
                        <span class="story-time">Dawn • 06:00 AM</span>
                        <div class="story-content">
                            <h3>The Forest Awakens</h3>
                            <p>As the first rays of sunlight pierce through the thick canopy of Jim Corbett National Park, the forest floor is painted in golden hues. The air is crisp, and the silence is suddenly broken by the alarm call of a spotted deer, warning the jungle that a predator is on the move.</p>
                        </div>
                    </div>
                    
                    <div class="story-step scroll-section">
                        <span class="story-time">Morning • 09:00 AM</span>
                        <div class="story-content">
                            <h3>The Royal Walk</h3>
                            <p>Emerging from the tall elephant grass in Kaziranga, the magnificent one-horned rhinoceros grazes peacefully. Meanwhile, in the mangroves of the Sundarbans, a Royal Bengal Tiger glides silently across a muddy creek, its majestic orange and black stripes shimmering in the morning sun.</p>
                        </div>
                    </div>
                    
                    <div class="story-step scroll-section">
                        <span class="story-time">Afternoon • 02:00 PM</span>
                        <div class="story-content">
                            <h3>Heat of the Day</h3>
                            <p>The scorching midday heat settles over the dry deciduous forests of Gir. Here, a pride of rare Asiatic lions rests in the shade of a large acacia tree. Above them, in the branches, Langur monkeys lazily groom each other, keeping a watchful eye on the sleeping kings below.</p>
                        </div>
                    </div>
                    
                    <div class="story-step scroll-section">
                        <span class="story-time">Dusk • 06:30 PM</span>
                        <div class="story-content">
                            <h3>The Nocturnal Shift</h3>
                            <p>As the sun sets over the Western Ghats, the jungle completely transforms. The diurnal animals retreat to safety, and the nocturnal creatures emerge. The elusive Indian Leopard begins its stealthy hunt, and the forest comes alive with the symphony of millions of crickets and frogs.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
"""

content_w = content_w.replace('<!-- National Parks Section -->', storyline_w + '\n        <!-- National Parks Section -->')

with open(filepath_wildlife, 'w', encoding='utf-8') as f:
    f.write(content_w)

# Spiritual.html
filepath_s = 'd:/INDIA/spiritual.html'
with open(filepath_s, 'r', encoding='utf-8') as f:
    content_s = f.read()

target_hero_s = '<h1 class="hero-title animate-slide-up">Spiritual <span class="highlight">India</span></h1>'
replace_hero_s = '<h1 class="hero-title animate-slide-up">Spiritual <span class="highlight rotating-text-container rotating-text-wrapper" data-words="India, Awakening, Heritage, Peace"></span></h1>'
content_s = content_s.replace(target_hero_s, replace_hero_s)

storyline_s = """
        <!-- Timeline of Faith Storyline -->
        <section class="fade-in-section" style="padding: 20px 0;">
            <div class="section-container">
                <div class="section-header">
                    <span class="section-badge">Narrative</span>
                    <h2>The Evolution of Faith</h2>
                </div>
                
                <div class="narrative-storyline">
                    <div class="story-step scroll-section">
                        <span class="story-time">Ancient Era • The Vedic Period</span>
                        <div class="story-content">
                            <h3>The Dawn of Philosophy</h3>
                            <p>Thousands of years ago, along the banks of the sacred Saraswati and Indus rivers, ancient sages composed the Vedas and Upanishads. These profound texts laid the foundation for Hinduism, introducing concepts of Dharma (duty), Karma (action), and Moksha (liberation).</p>
                        </div>
                    </div>
                    
                    <div class="story-step scroll-section">
                        <span class="story-time">500 BCE • The Great Awakening</span>
                        <div class="story-content">
                            <h3>Buddhism and Jainism</h3>
                            <p>In the quiet groves of Bodh Gaya, Siddhartha Gautama attained enlightenment to become the Buddha, teaching the middle path. Around the same time, Mahavira formalized Jainism, emphasizing absolute non-violence (Ahimsa) towards all living beings.</p>
                        </div>
                    </div>
                    
                    <div class="story-step scroll-section">
                        <span class="story-time">15th Century • The Path of Equality</span>
                        <div class="story-content">
                            <h3>The Birth of Sikhism</h3>
                            <p>In the vibrant lands of Punjab, Guru Nanak founded Sikhism, a beautiful faith rejecting caste divisions and emphasizing equality, community service (Langar), and devotion to one formless creator.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
"""

content_s = content_s.replace('<!-- Spiritual Hubs Section -->', storyline_s + '\n        <!-- Spiritual Hubs Section -->')

with open(filepath_s, 'w', encoding='utf-8') as f:
    f.write(content_s)

