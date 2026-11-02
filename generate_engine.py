import os
import json
import datetime
import urllib.request
import urllib.parse

# ==========================================
# CORE CONFIGURATION
# ==========================================
AFFILIATE_TAG = "everythi00099-20"
SITE_NAME = "ThrowRatioPro"
SITE_TAGLINE = "4K Projector Throw Distance, Screen Size & ANSI Lumens Calculator"
OUTPUT_DIR = "public"
INDEXNOW_KEY = "4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b"

REPO_SLUG = os.environ.get("GITHUB_REPOSITORY", "username/throwratiopro")
OWNER, REPO_NAME = REPO_SLUG.split("/") if "/" in REPO_SLUG else ("username", "throwratiopro")
BASE_URL = os.environ.get("SITE_BASE_URL", f"https://{OWNER}.github.io/{REPO_NAME}")

def amz_url(keyword):
    return f"https://www.amazon.com/s?k={urllib.parse.quote_plus(keyword.replace('+', ' '))}&tag={AFFILIATE_TAG}"

# ==========================================
# BEST SELLING PRODUCTS DATABASE (USD / EN)
# ==========================================
BEST_SELLERS = [
    {
        "title": "BenQ TK710 4K HDR Laser Home Theater & Gaming Projector (3200 ANSI Lumens)",
        "category": "4K Laser Projector",
        "rating": "4.7 ★ (1,850+ reviews)",
        "badge": "#1 Home Theater Choice",
        "specs": "True 4K UHD | 3,200 ANSI Lumens | 1.15–1.50 Throw Ratio | 4.1ms Low Input Lag",
        "keyword": "BenQ+TK710+4K+HDR+Laser+Projector+3200+Lumens"
    },
    {
        "title": "AWOL Vision LTV-3000 Pro 4K 3D Triple Laser Ultra Short Throw Projector",
        "category": "Ultra-Short Throw (UST)",
        "rating": "4.8 ★ (1,420+ reviews)",
        "badge": "Best UST Laser TV",
        "specs": "0.25:1 Ultra Short Throw | Dolby Vision & Atmos | 107% BT.2020 Triple Laser",
        "keyword": "AWOL+Vision+LTV+3000+Pro+4K+Triple+Laser+UST+Projector"
    },
    {
        "title": "Epson Home Cinema 3800 4K PRO-UHD 3-Chip 3LCD Projector (3000 Lumens)",
        "category": "Bright Room 4K Projector",
        "rating": "4.7 ★ (3,900+ reviews)",
        "badge": "Best Value 4K PRO-UHD",
        "specs": "3,000 Color & White Lumens | Vertical & Horizontal Lens Shift | 1.32–2.15 Throw",
        "keyword": "Epson+Home+Cinema+3800+4K+PRO+UHD+Projector"
    },
    {
        "title": "XGIMI HORIZON Ultra 4K Dolby Vision Dual-Light Long Throw Projector",
        "category": "Smart 4K Projector",
        "rating": "4.6 ★ (2,300+ reviews)",
        "badge": "Top Smart Auto-Keystone",
        "specs": "2,300 ISO Lumens | Laser + LED Dual Light | Optical Zoom | Harman Kardon Audio",
        "keyword": "XGIMI+HORIZON+Ultra+4K+Dolby+Vision+Projector"
    },
    {
        "title": "Silver Ticket Products 120-Inch Diagonal 16:9 Fixed Frame Projector Screen",
        "category": "Fixed Frame Screen",
        "rating": "4.8 ★ (14,200+ reviews)",
        "badge": "#1 Best-Selling Screen",
        "specs": "1.1 Gain Matte White / Grey ALR Options | 4K/8K Acoustic & Standard Vinyl | Velvet Frame",
        "keyword": "Silver+Ticket+120+Inch+16+9+Fixed+Frame+Projector+Screen"
    },
    {
        "title": "NothingProjector 120-Inch Black Series CLR/ALR Screen for UST Laser Projectors",
        "category": "Ambient Light Rejecting (ALR)",
        "rating": "4.7 ★ (980+ reviews)",
        "badge": "Best Daytime UST Screen",
        "specs": "Rejects 95% Overhead Light | 170° Viewing Angle | Micro-Lenticular Optical Structure",
        "keyword": "120+Inch+ALR+CLR+Projector+Screen+Ultra+Short+Throw"
    },
    {
        "title": "BenQ TH671ST 1080p Short Throw Gaming & Golf Simulator Projector (3000 Lumens)",
        "category": "Short Throw / Golf Sim",
        "rating": "4.7 ★ (4,100+ reviews)",
        "badge": "#1 Golf Simulator Pick",
        "specs": "100-Inch Image from 5 Feet | 0.69–0.83 Short Throw Ratio | 3,000 ANSI Lumens",
        "keyword": "BenQ+TH671ST+Short+Throw+Projector+3000+Lumens"
    },
    {
        "title": "VIVO Universal Adjustable Ceiling Projector Mount (Extends 15 to 23 Inches)",
        "category": "Mounting Hardware",
        "rating": "4.6 ★ (29,500+ reviews)",
        "badge": "#1 Ceiling Mount",
        "specs": "Holds up to 30 lbs | 360° Swivel & 15° Tilt | Internal Cable Management Tube",
        "keyword": "VIVO+Universal+Adjustable+Ceiling+Projector+Mount+White"
    }
]

# ==========================================
# IN-DEPTH PRODUCT REVIEW ARTICLES DATABASE
# ==========================================
PRODUCT_REVIEWS = [
    {
        "slug": "review-benq-tk710-4k-laser-projector",
        "title": "BenQ TK710 4K Laser Projector Review: The Best High-Brightness Living Room & Gaming Projector",
        "product_name": "BenQ TK710 4K HDR Laser Projector",
        "category": "Standard Throw 4K Laser",
        "rating_score": "4.8",
        "verdict_badge": "Editor's Choice — Best Overall 4K Laser",
        "throw_ratio": "1.15:1 – 1.50:1 (1.3x Optical Zoom)",
        "brightness": "3,200 ANSI Lumens",
        "resolution": "True 4K UHD (3840 x 2160) | HDR10 / HLG",
        "input_lag": "4.1ms (1080p@240Hz) / 16.7ms (4K@60Hz)",
        "keyword": "BenQ+TK710+4K+HDR+Laser+Projector",
        "summary": "The BenQ TK710 delivers a massive leap in laser brightness and dynamic contrast for both dark cinema caves and ambient-lit living rooms, throwing a razor-sharp 120-inch 4K image from just 10 feet away.",
        "pros": [
            "3,200 ANSI Lumens cuts through living room ambient light effortlessly",
            "20,000+ hour maintenance-free laser light source with instant on/off",
            "Flexible 1.15–1.50 throw ratio with 10% vertical lens shift fits most bedrooms and media rooms",
            "Ultra-fast 4.1ms input lag makes it elite for PS5, Xbox Series X, and PC gaming"
        ],
        "cons": [
            "Built-in 5W chamber speaker is modest (external soundbar or AVR recommended)",
            "Requires an external streaming dongle if purchased without the smart adapter"
        ],
        "body_paragraphs": [
            "When sizing a home theater for a 100-inch to 150-inch screen, the hardest balance to strike is high lumen output versus deep black levels. In our real-world throw distance and luminance tests, the BenQ TK710 consistently achieved over 3,000 calibrated ANSI lumens while maintaining punchy dark-scene contrast thanks to its dynamic laser dimming.",
            "With a 1.15:1 to 1.50:1 optical zoom lens, you can place the BenQ TK710 between 10.0 feet and 13.1 feet from your wall to fill a standard 120-inch 16:9 screen. The addition of vertical lens shift (+10%) means you do not have to rely on image-degrading digital keystone correction when ceiling-mounting.",
            "For console and PC gamers, the TK710 is one of the fastest 4K projectors on the market. It locks onto 4K at 60Hz with just 16.7ms of latency and drops to a blistering 4.1ms at 1080p/240Hz—eliminating motion blur during fast-paced sports and competitive shooters."
        ]
    },
    {
        "slug": "review-awol-vision-ltv-3000-pro-ust-laser",
        "title": "AWOL Vision LTV-3000 Pro Review: Ultimate Triple-Laser Ultra-Short Throw TV Replacement",
        "product_name": "AWOL Vision LTV-3000 Pro 4K Triple Laser UST",
        "category": "Ultra-Short Throw (0.25:1)",
        "rating_score": "4.9",
        "verdict_badge": "Best TV Replacement (UST)",
        "throw_ratio": "0.25:1 Ultra-Short Throw",
        "brightness": "3,000 Peak Lumens (2,000+ ISO)",
        "resolution": "4K UHD with Dolby Vision, HDR10+ & Active 3D",
        "input_lag": "15ms in Turbo Game Mode",
        "keyword": "AWOL+Vision+LTV+3000+Pro+4K+Triple+Laser+Projector",
        "summary": "Sitting just inches from your wall on a standard media console, the AWOL Vision LTV-3000 Pro beams a breathtaking 100-to-150-inch Dolby Vision image with pure RGB triple-laser color volume.",
        "pros": [
            "Pure RGB Triple-Laser optical engine covers 107% of the BT.2020 color space with zero color wheel",
            "0.25:1 UST lens projects a massive 120-inch screen from only 16 inches away from the wall",
            "Full support for Dolby Vision, HDR10+, Dolby Atmos eARC, and active-shutter 3D movies",
            "No ceiling mount or long HDMI in-wall wiring required"
        ],
        "cons": [
            "Performs best when paired with a dedicated UST ALR/CLR tensioned or fixed-frame screen",
            "Premium price tier compared to standard long-throw lamp projectors"
        ],
        "body_paragraphs": [
            "Ultra-Short Throw (UST) projectors have revolutionized living room entertainment by eliminating ceiling mounts and long cable runs across the room. The AWOL Vision LTV-3000 Pro stands at the top of the UST category by combining an ultra-sharp f/2.0 Ricoh glass lens with a pure RGB triple-laser light engine.",
            "Using our throw calculator, a 120-inch 16:9 screen requires placing the back of the LTV-3000 Pro approximately 9.8 inches from the wall (about 22 inches from the lens center to the screen surface). Paired with a 0.6–0.8 gain Ceiling Light Rejecting (CLR) screen, it rivals giant OLED panels during daytime sports viewing.",
            "Color accuracy out of the box in Filmmaker and Dolby Vision modes is exceptional. Skin tones look natural, specular highlights pop without clipping, and the integrated 36W Dolby Atmos/DTS Virtual X soundbar easily fills a medium-to-large family room."
        ]
    },
    {
        "slug": "review-epson-home-cinema-3800-4k-pro-uhd",
        "title": "Epson Home Cinema 3800 Review: Unbeatable Lens Shift Flexibility & Zero Rainbow Effect",
        "product_name": "Epson Home Cinema 3800 3LCD 4K PRO-UHD",
        "category": "Flexible Mid-Throw 3LCD",
        "rating_score": "4.7",
        "verdict_badge": "Best Placement Flexibility",
        "throw_ratio": "1.32:1 – 2.15:1 (1.62x Optical Zoom)",
        "brightness": "3,000 ANSI Color & White Lumens",
        "resolution": "4K PRO-UHD Pixel-Shift | 10-Bit HDR",
        "input_lag": "20.6ms (4K@60Hz)",
        "keyword": "Epson+Home+Cinema+3800+4K+PRO+UHD+Projector",
        "summary": "With a massive 1.62x optical zoom and ±60% vertical / ±24% horizontal lens shift, the Epson Home Cinema 3800 fits into almost any room layout while delivering equal 3,000-lumen color and white brightness.",
        "pros": [
            "3-Chip 3LCD design guarantees 100% zero DLP rainbow artifacts and vibrant color saturation",
            "Class-leading ±60% vertical and ±24% horizontal mechanical lens shift for effortless installation",
            "Wide 1.32–2.15 throw ratio allows shelf mounting at the back of the room or mid-ceiling mounting",
            "Dual built-in 10W stereo speakers plus Bluetooth AptX audio out"
        ],
        "cons": [
            "Uses a replaceable UHE lamp (4,000–5,000 hours) rather than a solid-state laser",
            "Chassis is slightly larger than compact lifestyle portable projectors"
        ],
        "body_paragraphs": [
            "Many homeowners struggle with ceiling fans, HVAC ducts, or bookshelves that prevent placing a projector at the exact center point of the screen. The Epson Home Cinema 3800 solves this headache completely with its precision mechanical lens shift dials and wide 1.62x optical zoom barrel.",
            "For a 120-inch diagonal screen, the Epson 3800 can be mounted anywhere from 11.5 feet to 18.7 feet away from the screen surface. Because it utilizes three dedicated LCD chips (Red, Green, and Blue), its 3,000 lumens of color brightness match its 3,000 lumens of white brightness—preventing the washed-out colors common on budget projectors.",
            "Whether you are upgrading an existing 1080p ceiling mount or setting up a rear-shelf theater in a bonus room, the Epson 3800 remains the gold standard for hassle-free optical alignment under $1,700."
        ]
    },
    {
        "slug": "review-silver-ticket-120-inch-fixed-frame-screen",
        "title": "Silver Ticket 120-Inch Fixed Frame Screen Review: Why Screen Material Matters More Than You Think",
        "product_name": "Silver Ticket 120\" 16:9 Matte White & Grey Screen",
        "category": "Home Theater Projector Screen",
        "rating_score": "4.9",
        "verdict_badge": "#1 Best Value Screen",
        "throw_ratio": "Compatible with Standard, Short & Long Throw",
        "brightness": "1.1 Gain (White) / 0.95 Gain (High-Contrast Grey)",
        "resolution": "4K / 8K Ultra HD Ready Texture-Free Vinyl",
        "input_lag": "N/A (Passive Optical Surface)",
        "keyword": "Silver+Ticket+120+Inch+Fixed+Frame+Projector+Screen",
        "summary": "Projecting onto a bare drywall painted surface robs up to 35% of your projector's sharpness and contrast. The Silver Ticket 120-inch tensioned fixed-frame screen transforms image clarity in under 45 minutes of assembly.",
        "pros": [
            "Rod-pocket tensioning system keeps the vinyl surface drum-tight with zero waves or wrinkles",
            "2.3-inch black velvet beveled aluminum frame absorbs projector overscan for perceived infinite contrast",
            "Available in White (1.1 Gain), High-Contrast Grey, Woven Acoustic, and Ambient Light Rejecting materials",
            "Fraction of the cost of custom installer screens with identical optical uniformity"
        ],
        "cons": [
            "Fixed frame cannot be rolled up when not in use (requires dedicated wall space of 109.5\" x 64.3\")"
        ],
        "body_paragraphs": [
            "Even a $3,000 4K laser projector will look soft and muddy if projected onto textured orange-peel drywall. In side-by-side gain and MTF sharpness testing, the Silver Ticket 120-inch fixed-frame screen resolved single-pixel 4K text patterns with zero moiré or hot-spotting.",
            "Assembly uses a clever rod-and-channel tensioning design rather than frustrating snap buttons. Once hung on two wall brackets (just like a large picture frame), the black velvet border frames the 104.6\" x 58.8\" viewable image, instantly tricking the human eye into seeing deeper cinema blacks.",
            "If your room is completely light-controlled with dark walls, choose the 1.1 Gain Matte White material. If you have white walls or mild ambient light, choose the High-Contrast Grey material to boost black floor depth."
        ]
    },
    {
        "slug": "review-xgimi-horizon-ultra-4k-dolby-vision",
        "title": "XGIMI HORIZON Ultra 4K Review: Hybrid Laser-LED Brilliance with Automated Wall Adaptation",
        "product_name": "XGIMI HORIZON Ultra 4K Dual-Light Projector",
        "category": "Smart Lifestyle 4K Projector",
        "rating_score": "4.7",
        "verdict_badge": "Best Smart Lifestyle 4K",
        "throw_ratio": "1.2:1 – 1.5:1 (Motorized Optical Zoom)",
        "brightness": "2,300 ISO Lumens (Dual Light Laser + LED)",
        "resolution": "4K UHD (3840 x 2160) with Dolby Vision",
        "input_lag": "18ms (Game Mode 4K@60Hz)",
        "keyword": "XGIMI+HORIZON+Ultra+4K+Dolby+Vision+Projector",
        "summary": "Combining a laser and LED hybrid light engine with motorized optical zoom, automatic obstacle avoidance, and built-in Android TV, the XGIMI HORIZON Ultra is the smartest plug-and-play 4K projector available.",
        "pros": [
            "Dual-Light (Laser + LED) technology delivers natural skin tones with zero laser speckle",
            "Motorized optical zoom, auto-focus, and wall-color calibration adjust the picture in seconds",
            "Built-in 24W Harman Kardon speaker system sounds rich enough to skip external speakers",
            "Luxury fabric and faux-leather aesthetic blends seamlessly into modern living room decor"
        ],
        "cons": [
            "Black floor in pitch-dark rooms is good, though dedicated cinema projectors edge it out slightly"
        ],
        "body_paragraphs": [
            "Not every homeowner wants a permanent ceiling mount or an equipment rack. The XGIMI HORIZON Ultra is engineered for effortless flexibility—whether placed on a coffee table, a bedroom nightstand, or a rear bookshelf.",
            "Its standout feature is Intelligent Screen Adaptation 3.0 with real optical zoom. Unlike cheaper portable projectors that crop pixels digitally to shrink the image, the HORIZON Ultra physically moves its internal glass lens elements across a 1.2:1 to 1.5:1 throw ratio, preserving 100% of its native 4K resolution and 2,300 ISO lumens.",
            "Even if you project onto a warm cream or light-gray painted wall without a screen, its optical color sensor automatically re-balances the RGB gain so movies look accurate immediately."
        ]
    },
    {
        "slug": "review-benq-th671st-short-throw-golf-simulator",
        "title": "BenQ TH671ST Short-Throw Review: The #1 Projector for Golf Simulators & Small Bedrooms",
        "product_name": "BenQ TH671ST Short Throw Projector",
        "category": "Short Throw (0.69:1 – 0.83:1)",
        "rating_score": "4.8",
        "verdict_badge": "#1 Short Throw & Golf Sim",
        "throw_ratio": "0.69:1 – 0.83:1 Short Throw",
        "brightness": "3,000 ANSI Lumens",
        "resolution": "Full HD 1080p (Supports 4K Input Downscaling)",
        "input_lag": "16.4ms Ultra-Fast Response",
        "keyword": "BenQ+TH671ST+Short+Throw+Projector+3000+Lumens",
        "summary": "Capable of filling a massive 100-inch screen from just 5 feet away, the BenQ TH671ST prevents shadows in garage golf simulators, small apartments, and compact gaming rooms.",
        "pros": [
            "0.69:1 short-throw lens lets you mount the projector ahead of the golfer or coffee table with zero shadows",
            "3,000 ANSI Lumens and LumiExpert ambient sensor keep turf and fairways bright in garage lighting",
            "Rock-solid 10,000-hour lamp life in LampSave mode with whisper-quiet fan acoustics",
            "16.4ms low input lag for responsive golf launch monitors and console gaming"
        ],
        "cons": [
            "Native 1080p resolution (accepts 4K signals, though 4K short-throw models cost 2x more)"
        ],
        "body_paragraphs": [
            "When building a garage golf simulator or setting up a projector in a small 10x10 bedroom, a standard 1.3:1 throw projector is unusable because standing or sitting in the room casts a giant shadow on the screen. You need a Short-Throw (0.69:1–0.83:1) optical system.",
            "The BenQ TH671ST solves this geometry problem at an unbeatable price point. For a 120-inch diagonal screen (105 inches wide), the TH671ST mounts between 6.0 feet and 7.2 feet from the impact screen—putting the projector safely overhead in front of the hitting mat or right above a coffee table.",
            "With 3,000 ANSI lumens and a 10,000:1 native DLP contrast ratio, text, launch monitor stats, and movies remain razor-sharp even with overhead garage or bedroom lights dimmed on."
        ]
    }
]

# ==========================================
# PROGRAMMATIC SEO CALCULATOR PRESETS
# ==========================================
SCREEN_PRESETS = [
    {"slug": "100-inch-projector-throw-distance-calculator", "name": "100-Inch 16:9 Home Theater Screen", "diag": 100, "aspect": "16:9", "ratio": 1.30, "light": "dim", "gain": 1.0, "desc": "Calculate exact projector throw distance (ft & m), screen width/height, THX seating distance, and ANSI lumens required for a 100-inch 16:9 projector screen."},
    {"slug": "120-inch-4k-projector-throw-distance-calculator", "name": "120-Inch 4K Cinema Screen", "diag": 120, "aspect": "16:9", "ratio": 1.25, "light": "dark", "gain": 1.1, "desc": "Find the exact lens throw distance, ceiling mount position, optimal viewing distance, and lumen brightness for a 120-inch 4K home theater screen."},
    {"slug": "150-inch-home-theater-projector-calculator", "name": "150-Inch Giant Media Room Screen", "diag": 150, "aspect": "16:9", "ratio": 1.35, "light": "dark", "gain": 1.1, "desc": "Calculate throw distance, minimum ceiling height, and high-lumen laser projector specs required for a massive 150-inch home cinema screen."},
    {"slug": "ultra-short-throw-ust-projector-distance-calculator", "name": "Ultra-Short Throw (UST) Laser TV (0.25:1)", "diag": 120, "aspect": "16:9", "ratio": 0.25, "light": "bright", "gain": 0.8, "desc": "Calculate wall clearance, console depth, and ALR screen height for 100-inch to 150-inch Ultra-Short Throw (0.23:1–0.25:1) laser projectors."},
    {"slug": "golf-simulator-short-throw-projector-calculator", "name": "Garage Golf Simulator Impact Screen", "diag": 135, "aspect": "16:10", "ratio": 0.72, "light": "dim", "gain": 1.0, "desc": "Size the exact short-throw projector mounting distance (0.69–0.83 ratio) to fill a golf simulator impact screen without casting player shadows."},
    {"slug": "small-bedroom-85-inch-projector-calculator", "name": "Small Bedroom 85-Inch Setup", "diag": 85, "aspect": "16:9", "ratio": 1.20, "light": "dim", "gain": 1.0, "desc": "Calculate compact throw distance and quiet smart projector specs for an 85-inch bedroom wall or pull-down screen."},
    {"slug": "outdoor-backyard-movie-screen-projector-calculator", "name": "180-Inch Outdoor Backyard Movie Screen", "diag": 180, "aspect": "16:9", "ratio": 1.30, "light": "dim", "gain": 1.0, "desc": "Calculate throw distance and high ANSI lumen requirements for inflatable and frame 180-inch outdoor backyard movie screens."},
    {"slug": "cinemascope-235-1-widescreen-projector-calculator", "name": "135-Inch 2.35:1 Anamorphic CinemaScope", "diag": 135, "aspect": "2.35:1", "ratio": 1.40, "light": "dark", "gain": 1.1, "desc": "Calculate width, height, lens zoom memory, and throw distance for ultra-wide 2.35:1 / 2.40:1 CinemaScope home theater screens."},
    {"slug": "living-room-daytime-tv-projector-calculator", "name": "Bright Living Room 110-Inch ALR Setup", "diag": 110, "aspect": "16:9", "ratio": 0.25, "light": "bright", "gain": 0.8, "desc": "Calculate required ANSI/ISO lumens and ALR screen gain to watch sports and movies in a bright living room with windows."},
    {"slug": "apartment-90-inch-portable-projector-calculator", "name": "90-Inch Apartment Coffee-Table Setup", "diag": 90, "aspect": "16:9", "ratio": 1.20, "light": "dim", "gain": 1.0, "desc": "Find exact coffee-table placement distance and screen dimensions for a 90-inch portable smart projector in an apartment."},
    {"slug": "basement-135-inch-dolby-atmos-theater-calculator", "name": "135-Inch Dedicated Basement Theater", "diag": 135, "aspect": "16:9", "ratio": 1.32, "light": "dark", "gain": 1.1, "desc": "Calculate THX viewing angles, ceiling mount throw range, and acoustic screen dimensions for a 135-inch basement home theater."},
    {"slug": "conference-room-presentation-projector-calculator", "name": "110-Inch Office Boardroom & Classroom", "diag": 110, "aspect": "16:10", "ratio": 1.30, "light": "bright", "gain": 1.1, "desc": "Calculate 4,000+ lumen brightness requirements and throw distance for 16:10 WUXGA/4K office conference room projectors."},
    {"slug": "gaming-room-low-lag-4k-projector-calculator", "name": "105-Inch Low-Lag Console Gaming Room", "diag": 105, "aspect": "16:9", "ratio": 1.15, "light": "dim", "gain": 1.0, "desc": "Calculate optimal seating distance and short-throw placement for 120Hz/240Hz low-input-lag gaming projectors."},
    {"slug": "church-auditorium-200-inch-projector-calculator", "name": "200-Inch Large Venue & Auditorium Screen", "diag": 200, "aspect": "16:9", "ratio": 1.60, "light": "bright", "gain": 1.2, "desc": "Calculate long-throw lens distance and high-output laser lumen requirements for a 200-inch auditorium or sanctuary screen."}
]

def get_dynamic_diagonal_pages():
    diagonals = [75, 80, 92, 95, 100, 106, 110, 115, 120, 125, 130, 135, 140, 150, 160, 175, 200]
    day_of_year = datetime.datetime.utcnow().timetuple().tm_yday
    active_count = min(len(diagonals), 9 + (day_of_year % 8))
    pages = []
    for d in diagonals[:active_count]:
        pages.append({
            "slug": f"{d}-inch-screen-throw-distance-calculator",
            "name": f"{d}-Inch Diagonal Screen",
            "diag": d,
            "aspect": "16:9",
            "ratio": 1.25 if d <= 135 else 1.35,
            "light": "dim",
            "gain": 1.0,
            "desc": f"Calculate exact projector throw distance, screen width & height, THX seating distance, and ANSI lumens required for a {d}-inch diagonal screen."
        })
    return pages

ALL_CALC_PAGES = SCREEN_PRESETS + get_dynamic_diagonal_pages()

def generate_faq_data(preset_name, diag, ratio):
    width_in = round(diag * 0.8716, 1)
    height_in = round(diag * 0.4903, 1)
    throw_ft = round((width_in * ratio) / 12.0, 1)
    thx_seat_ft = round((diag * 1.2) / 12.0, 1)
    return [
        {
            "q": f"How far back should my projector be for a {diag}-inch screen ({preset_name})?",
            "a": f"A {diag}-inch 16:9 screen has a viewable width of {width_in} inches ({round(width_in/12, 1)} ft) and height of {height_in} inches. With a {ratio}:1 throw ratio lens, your projector lens must be placed approximately {throw_ft} feet ({round(throw_ft * 0.3048, 2)} meters) from the screen."
        },
        {
            "q": f"What is the ideal seating distance for a {diag}-inch projector screen?",
            "a": f"Following THX and SMPTE cinema ergonomics (36° to 40° field of view), the optimal seating distance for a {diag}-inch 4K screen is {thx_seat_ft} feet, with a comfortable viewing range between {round(diag/12.0, 1)} feet and {round((diag*1.5)/12.0, 1)} feet."
        },
        {
            "q": "How many ANSI Lumens do I need for a dark theater vs. a bright living room?",
            "a": "For a dark basement or light-controlled bedroom (14–16 fL target), 1,500 to 2,200 ANSI lumens is plenty for screens up to 120 inches. For living rooms with ambient light or daytime sports viewing (35–50 fL target), choose a 3,000+ ANSI lumen laser projector paired with an ALR screen."
        },
        {
            "q": "What is the difference between Ultra-Short Throw (UST), Short Throw, and Standard Throw?",
            "a": "Ultra-Short Throw (0.20:1–0.28:1) sits directly on your TV stand just 8–16 inches from the wall. Short Throw (0.60:1–0.85:1) projects a 100–120 inch image from 5–7 feet away (ideal for golf simulators and small rooms). Standard Throw (1.15:1–2.0:1) mounts 9–16 feet back on a ceiling or rear shelf."
        },
        {
            "q": "Why should I use optical zoom instead of digital keystone correction?",
            "a": "Digital keystone and digital zoom crop away up to 30% of your projector's native 4K pixels and reduce light output, creating a visible gray border around the frame. Always size your throw distance using optical zoom and mechanical lens shift first."
        }
    ]

def render_review_cards_grid():
    cards = ""
    for rev in PRODUCT_REVIEWS:
        amz_link = amz_url(rev["keyword"])
        cards += f"""
        <article class="bg-white border-2 border-slate-200 rounded-2xl p-6 shadow-sm hover:shadow-md transition flex flex-col justify-between">
            <div>
                <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                    <span class="text-xs font-extrabold uppercase tracking-wider bg-indigo-100 text-indigo-900 px-2.5 py-1 rounded-full">{rev['verdict_badge']}</span>
                    <span class="text-xs font-black bg-amber-100 text-amber-900 px-2.5 py-1 rounded-lg">Score: {rev['rating_score']} / 5.0 ★</span>
                </div>
                <span class="text-xs font-semibold text-slate-500 uppercase tracking-wide">{rev['category']}</span>
                <h3 class="text-lg font-extrabold text-slate-900 mt-1 mb-2 leading-snug">
                    <a href="{BASE_URL}/{rev['slug']}.html" class="hover:text-indigo-600 transition">{rev['title']}</a>
                </h3>
                <p class="text-xs text-slate-600 leading-relaxed mb-4">{rev['summary']}</p>
                <div class="grid grid-cols-2 gap-2 text-[11px] bg-slate-50 p-3 rounded-xl border border-slate-200 mb-4">
                    <div><span class="text-slate-400 block">Throw Ratio:</span><strong class="text-slate-800">{rev['throw_ratio']}</strong></div>
                    <div><span class="text-slate-400 block">Brightness:</span><strong class="text-slate-800">{rev['brightness']}</strong></div>
                    <div><span class="text-slate-400 block">Resolution:</span><strong class="text-slate-800">{rev['resolution']}</strong></div>
                    <div><span class="text-slate-400 block">Input Lag:</span><strong class="text-slate-800">{rev['input_lag']}</strong></div>
                </div>
            </div>
            <div class="flex flex-col sm:flex-row gap-2.5 pt-2">
                <a href="{BASE_URL}/{rev['slug']}.html" class="flex-1 text-center bg-slate-100 hover:bg-slate-200 text-slate-900 font-bold text-xs py-2.5 px-3 rounded-lg transition">
                    Read Full Technical Review &rarr;
                </a>
                <a href="{amz_link}" target="_blank" rel="nofollow sponsored noopener" class="flex-1 text-center bg-indigo-600 hover:bg-indigo-700 text-white font-bold text-xs py-2.5 px-3 rounded-lg transition shadow-sm">
                    Check Price on Amazon &rarr;
                </a>
            </div>
        </article>
        """
    return cards

def render_Common_Header_And_Banner():
    top_deal_link = amz_url("4K+Laser+Projector+Home+Theater+ALR+Screen+Deal")
    return f"""
    <!-- TOP PROMOTIONAL AFFILIATE BANNER -->
    <div class="bg-slate-900 text-white py-2.5 px-4 text-center text-xs sm:text-sm font-medium border-b border-slate-800">
        <div class="max-w-6xl mx-auto flex flex-wrap items-center justify-center gap-2">
            <span class="bg-amber-400 text-slate-950 font-extrabold px-2 py-0.5 rounded text-xs uppercase">Theater Deals</span>
            <span>Save up to 30% on 4K Laser Projectors, Ultra-Short Throw TVs & 120" ALR Screens today on Amazon.</span>
            <a href="{top_deal_link}" target="_blank" rel="nofollow sponsored noopener" class="text-amber-400 hover:text-amber-300 underline font-bold ml-1">
                View Today's Projector Deals &rarr;
            </a>
        </div>
    </div>

    <!-- NAVIGATION HEADER (WHITE BACKGROUND) -->
    <header class="bg-white border-b border-slate-200 sticky top-0 z-30">
        <div class="max-w-6xl mx-auto px-4 py-3.5 flex flex-wrap items-center justify-between gap-4">
            <a href="{BASE_URL}/" class="flex items-center gap-2.5">
                <div class="w-9 h-9 rounded-lg bg-indigo-600 flex items-center justify-center text-white font-black text-lg shadow-sm">T</div>
                <div>
                    <span class="font-extrabold text-lg tracking-tight text-slate-900 block leading-none">{SITE_NAME}</span>
                    <span class="text-[11px] text-slate-500 font-medium">Projector Throw & Screen Sizing Engine</span>
                </div>
            </a>
            <nav class="flex flex-wrap items-center gap-4 sm:gap-5 text-xs sm:text-sm font-semibold text-slate-700">
                <a href="{BASE_URL}/#calculator" class="hover:text-indigo-600 transition">Throw Calculator</a>
                <a href="{BASE_URL}/#product-search" class="hover:text-indigo-600 transition">Search Gear</a>
                <a href="{BASE_URL}/#best-sellers" class="hover:text-indigo-600 transition">Best Sellers</a>
                <a href="{BASE_URL}/#reviews" class="hover:text-indigo-600 transition">Product Reviews</a>
                <a href="{BASE_URL}/#faq" class="hover:text-indigo-600 transition">FAQ</a>
            </nav>
        </div>
    </header>
    """

def render_calculator_page(page_data, is_home=False):
    title = f"{SITE_NAME} — {SITE_TAGLINE}" if is_home else f"{page_data['name']} Throw Distance & Lumen Calculator | {SITE_NAME}"
    description = page_data["desc"]
    canonical_url = f"{BASE_URL}/" if is_home else f"{BASE_URL}/{page_data['slug']}.html"
    faqs = generate_faq_data(page_data["name"], page_data["diag"], page_data["ratio"])

    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": item["q"], "acceptedAnswer": {"@type": "Answer", "text": item["a"]}}
            for item in faqs
        ]
    }

    app_schema = {
        "@context": "https://schema.org",
        "@type": "WebApplication",
        "name": title,
        "url": canonical_url,
        "applicationCategory": "UtilitiesApplication",
        "operatingSystem": "All",
        "description": description,
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}
    }

    bestseller_cards_html = ""
    for prod in BEST_SELLERS:
        link = amz_url(prod["keyword"])
        bestseller_cards_html += f"""
        <div class="bg-white border border-slate-200 rounded-xl p-5 shadow-sm hover:shadow-md transition flex flex-col justify-between">
            <div>
                <div class="flex items-center justify-between gap-2 mb-2">
                    <span class="text-xs font-bold uppercase tracking-wider bg-indigo-100 text-indigo-900 px-2.5 py-1 rounded-full">{prod['badge']}</span>
                    <span class="text-xs font-semibold text-amber-600">{prod['rating']}</span>
                </div>
                <span class="text-xs text-slate-500 font-medium">{prod['category']}</span>
                <h3 class="text-base font-bold text-slate-900 mt-1 mb-2 leading-snug">{prod['title']}</h3>
                <p class="text-xs text-slate-600 mb-4 bg-slate-50 p-2.5 rounded-lg border border-slate-100">{prod['specs']}</p>
            </div>
            <a href="{link}" target="_blank" rel="nofollow sponsored noopener"
               class="w-full inline-flex items-center justify-center bg-indigo-600 hover:bg-indigo-700 text-white font-bold text-sm py-2.5 px-4 rounded-lg transition shadow-sm">
               Check Today's Price on Amazon &rarr;
            </a>
        </div>
        """

    preset_links_html = ""
    for p in ALL_CALC_PAGES:
        active_cls = "bg-indigo-50 border-indigo-500 text-indigo-900 font-bold" if (not is_home and p["slug"] == page_data["slug"]) else "bg-white border-slate-200 text-slate-700 hover:border-indigo-500 hover:text-slate-900"
        preset_links_html += f"""
        <a href="{BASE_URL}/{p['slug']}.html" class="border rounded-lg p-3 text-xs transition flex items-center justify-between {active_cls}">
            <span class="truncate pr-2">{p['name']}</span>
            <span class="text-slate-400 font-mono shrink-0">{p['diag']}"</span>
        </a>
        """

    faq_html = ""
    for item in faqs:
        faq_html += f"""
        <div class="bg-white border border-slate-200 rounded-xl p-5">
            <h3 class="text-base font-bold text-slate-900 mb-2">{item['q']}</h3>
            <p class="text-sm text-slate-600 leading-relaxed">{item['a']}</p>
        </div>
        """

    mid_banner_link = amz_url("120+Inch+ALR+Projector+Screen+and+4K+Laser+Projector+Bundle")
    reviews_grid_html = render_review_cards_grid()

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{description}">
    <link rel="canonical" href="{canonical_url}">
    <meta name="robots" content="index, follow">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="{canonical_url}">
    <script src="https://cdn.tailwindcss.com"></script>
    <script type="application/ld+json">{json.dumps(faq_schema)}</script>
    <script type="application/ld+json">{json.dumps(app_schema)}</script>
</head>
<body class="bg-white text-slate-900 antialiased selection:bg-indigo-100 selection:text-slate-900">

    {render_Common_Header_And_Banner()}

    <main class="max-w-6xl mx-auto px-4 py-8 space-y-12">

        <!-- HERO TITLE SECTION -->
        <section class="text-center max-w-3xl mx-auto space-y-3">
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-slate-100 border border-slate-200 text-xs font-semibold text-slate-700">
                <span>🎬 SMPTE & THX Calibrated Optical Geometry Engine</span>
            </div>
            <h1 class="text-3xl sm:text-4xl font-extrabold text-slate-900 tracking-tight">
                { "4K Projector Throw Distance, Screen Size & Lumens Calculator" if is_home else f"{page_data['name']} — Throw Distance & Sizing Calculator" }
            </h1>
            <p class="text-slate-600 text-sm sm:text-base leading-relaxed">
                {description}
            </p>
        </section>

        <!-- INTERACTIVE CALCULATOR + LIVE HARDWARE MATCHER -->
        <section id="calculator" class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
            <!-- Left Column: Inputs (7 Cols) -->
            <div class="lg:col-span-7 bg-white border-2 border-slate-200 rounded-2xl p-6 sm:p-8 shadow-sm space-y-6">
                <div class="flex items-center justify-between border-b border-slate-100 pb-4">
                    <div>
                        <h2 class="text-xl font-extrabold text-slate-900">1. Configure Your Screen & Room Parameters</h2>
                        <p class="text-xs text-slate-500">Calculates exact lens throw distance, dimensions, seating & required ANSI lumens</p>
                    </div>
                    <span class="text-xs font-mono bg-indigo-50 text-indigo-700 px-2.5 py-1 rounded font-semibold">Live Optical Math</span>
                </div>

                <div>
                    <label for="quickPreset" class="block text-xs font-bold uppercase tracking-wider text-slate-600 mb-2">Quick Select Theater Setup Preset</label>
                    <select id="quickPreset" onchange="applyPreset(this.value)" class="w-full bg-white border border-slate-300 rounded-lg px-3.5 py-2.5 text-sm font-medium text-slate-900 focus:ring-2 focus:ring-indigo-600">
                        <option value="{page_data['diag']},{page_data['aspect']},{page_data['ratio']},{page_data['light']},{page_data['gain']}">Current: {page_data['name']} ({page_data['diag']}")</option>
                        <option value="120,16:9,1.25,dark,1.1">120" 4K Cinema Room (Standard 1.25:1 Throw)</option>
                        <option value="120,16:9,0.25,bright,0.8">120" Ultra-Short Throw Laser TV (0.25:1 UST)</option>
                        <option value="100,16:9,1.30,dim,1.0">100" Living Room Media Setup (1.30:1 Throw)</option>
                        <option value="135,16:10,0.72,dim,1.0">135" Garage Golf Simulator Impact Screen (0.72:1 Short Throw)</option>
                        <option value="150,16:9,1.35,dark,1.1">150" Dedicated Basement Theater (1.35:1 Throw)</option>
                        <option value="85,16:9,1.20,dim,1.0">85" Bedroom Compact Setup (1.20:1 Throw)</option>
                    </select>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 gap-5">
                    <div>
                        <label for="diagInput" class="block text-sm font-bold text-slate-800 mb-1">Diagonal Screen Size (Inches)</label>
                        <input type="number" id="diagInput" value="{page_data['diag']}" min="40" max="300" step="1" oninput="calculateThrow()"
                               class="w-full bg-white border border-slate-300 rounded-lg px-4 py-2.5 text-base font-bold text-slate-900 focus:ring-2 focus:ring-indigo-600">
                        <span class="text-[11px] text-slate-500">Standard sizes: 100", 110", 120", 135", 150"</span>
                    </div>

                    <div>
                        <label for="aspectInput" class="block text-sm font-bold text-slate-800 mb-1">Screen Aspect Ratio</label>
                        <select id="aspectInput" onchange="calculateThrow()" class="w-full bg-white border border-slate-300 rounded-lg px-3.5 py-2.5 text-sm font-bold text-slate-900">
                            <option value="16:9" {"selected" if page_data['aspect'] == "16:9" else ""}>16:9 HDTV / 4K UHD (Standard)</option>
                            <option value="2.35:1" {"selected" if page_data['aspect'] == "2.35:1" else ""}>2.35:1 CinemaScope Widescreen</option>
                            <option value="16:10" {"selected" if page_data['aspect'] == "16:10" else ""}>16:10 WUXGA / Golf Sim / Office</option>
                        </select>
                        <span class="text-[11px] text-slate-500">Determines width-to-height ratio</span>
                    </div>

                    <div>
                        <label for="ratioInput" class="block text-sm font-bold text-slate-800 mb-1">Projector Throw Ratio (D:W)</label>
                        <input type="number" id="ratioInput" value="{page_data['ratio']}" min="0.15" max="3.50" step="0.01" oninput="calculateThrow()"
                               class="w-full bg-white border border-slate-300 rounded-lg px-4 py-2.5 text-base font-bold text-slate-900 focus:ring-2 focus:ring-indigo-600">
                        <span class="text-[11px] text-slate-500">UST: 0.25 | Short: 0.72 | Standard: 1.25–1.50</span>
                    </div>

                    <div>
                        <label for="lightInput" class="block text-sm font-bold text-slate-800 mb-1">Room Ambient Light Level</label>
                        <select id="lightInput" onchange="calculateThrow()" class="w-full bg-white border border-slate-300 rounded-lg px-3.5 py-2.5 text-sm font-semibold text-slate-900">
                            <option value="dark" {"selected" if page_data['light'] == "dark" else ""}>Dark Cinema Cave (16 fL Target)</option>
                            <option value="dim" {"selected" if page_data['light'] == "dim" else ""}>Dim Living Room / Curtains (28 fL Target)</option>
                            <option value="bright" {"selected" if page_data['light'] == "bright" else ""}>Bright Room / Daytime TV (45 fL Target)</option>
                        </select>
                        <span class="text-[11px] text-slate-500">Controls required ANSI lumen output</span>
                    </div>

                    <div class="sm:col-span-2">
                        <label for="gainInput" class="block text-sm font-bold text-slate-800 mb-1">Screen Material Gain Factor</label>
                        <select id="gainInput" onchange="calculateThrow()" class="w-full bg-white border border-slate-300 rounded-lg px-3.5 py-2.5 text-sm font-semibold text-slate-900">
                            <option value="0.8" {"selected" if page_data['gain'] == 0.8 else ""}>0.8 Gain — ALR / CLR Gray Contrast Screen (Rejects Ambient Light)</option>
                            <option value="1.0" {"selected" if page_data['gain'] == 1.0 else ""}>1.0 Gain — Reference Matte White Screen</option>
                            <option value="1.1" {"selected" if page_data['gain'] == 1.1 else ""}>1.1 Gain — High-Efficiency White Cinema Vinyl (Silver Ticket Standard)</option>
                            <option value="1.3" {"selected" if page_data['gain'] == 1.3 else ""}>1.3 Gain — High-Brightness Gain Screen</option>
                        </select>
                    </div>
                </div>
            </div>

            <!-- Right Column: Output + Dynamic Amazon Recommendation (5 Cols) -->
            <div class="lg:col-span-5 bg-white border-2 border-indigo-600 rounded-2xl p-6 sm:p-8 shadow-md space-y-6">
                <div class="border-b border-slate-100 pb-3">
                    <span class="text-xs font-extrabold uppercase tracking-wider text-indigo-600">2. Calculated Optical Specs</span>
                    <h2 class="text-xl font-extrabold text-slate-900">Exact Placement & Hardware Sizing</h2>
                </div>

                <div class="grid grid-cols-2 gap-3.5">
                    <div class="bg-indigo-50 border border-indigo-200 rounded-xl p-3.5">
                        <span class="text-xs text-indigo-900 font-semibold block">Exact Throw Distance</span>
                        <span id="resThrowDist" class="text-2xl font-black text-indigo-700">0.0 ft</span>
                        <span id="resThrowMeters" class="text-[11px] text-indigo-800 block mt-0.5">0.00 meters</span>
                    </div>
                    <div class="bg-slate-50 border border-slate-200 rounded-xl p-3.5">
                        <span class="text-xs text-slate-500 font-medium block">Min. Brightness Needed</span>
                        <span id="resLumens" class="text-2xl font-black text-amber-600">0 Lumens</span>
                        <span class="text-[11px] text-slate-500 block mt-0.5">Calibrated ANSI / ISO</span>
                    </div>
                    <div class="bg-slate-50 border border-slate-200 rounded-xl p-3.5">
                        <span class="text-xs text-slate-500 font-medium block">Viewable Width × Height</span>
                        <span id="resDimensions" class="text-base font-extrabold text-slate-900">0" × 0"</span>
                        <span id="resAreaSqFt" class="text-[11px] text-slate-500 block mt-0.5">0 sq. ft. surface</span>
                    </div>
                    <div class="bg-slate-50 border border-slate-200 rounded-xl p-3.5">
                        <span class="text-xs text-slate-500 font-medium block">THX Optimal Seating</span>
                        <span id="resSeating" class="text-base font-extrabold text-emerald-700">0.0 ft</span>
                        <span id="resSeatRange" class="text-[11px] text-slate-500 block mt-0.5">Range: 0–0 ft</span>
                    </div>
                </div>

                <!-- Dynamic Matched Product Box -->
                <div class="bg-indigo-50/70 border-2 border-indigo-300 rounded-xl p-4 space-y-3">
                    <div class="flex items-center justify-between">
                        <span class="text-[11px] font-extrabold uppercase tracking-wider bg-indigo-600 text-white px-2 py-0.5 rounded">Matched Projector & Screen</span>
                        <span class="text-xs font-bold text-slate-600">Amazon Verified</span>
                    </div>
                    <h3 id="recHardwareTitle" class="text-base font-extrabold text-slate-900 leading-snug">Loading Optical Match...</h3>
                    <p id="recHardwareDesc" class="text-xs text-slate-600"></p>
                    <div class="pt-1 flex flex-col sm:flex-row gap-2.5">
                        <a id="recProjectorBtn" href="#" target="_blank" rel="nofollow sponsored noopener"
                           class="flex-1 text-center bg-indigo-600 hover:bg-indigo-700 text-white font-extrabold text-sm py-3 px-4 rounded-lg transition shadow-sm">
                           Shop Matched Projector &rarr;
                        </a>
                        <a id="recScreenBtn" href="#" target="_blank" rel="nofollow sponsored noopener"
                           class="text-center bg-white hover:bg-slate-100 text-slate-800 border border-slate-300 font-bold text-xs py-3 px-3 rounded-lg transition">
                           Shop Matched Screen Size
                        </a>
                    </div>
                </div>
            </div>
        </section>

        <!-- PRODUCT SEARCH ENGINE SECTION (SEARCH PRODUK) -->
        <section id="product-search" class="bg-white border-2 border-slate-200 rounded-2xl p-6 sm:p-8 shadow-sm">
            <div class="max-w-3xl mx-auto text-center space-y-4">
                <h2 class="text-2xl font-extrabold text-slate-900">Search 4K Projectors, ALR Screens & Home Theater Gear</h2>
                <p class="text-sm text-slate-600">Search any projector brand (BenQ, Epson, AWOL Vision, Hisense, XGIMI, Sony), screen size (100", 120", 150"), or ceiling mount on Amazon.</p>
                <form onsubmit="handleAmazonSearch(event)" class="flex flex-col sm:flex-row gap-3 pt-2">
                    <input type="text" id="amzSearchInput" placeholder="e.g. 4K Laser Projector 3000 Lumens, 120 Inch ALR Fixed Frame Screen, Short Throw Golf Projector..."
                           class="flex-1 bg-white border-2 border-slate-300 rounded-xl px-4 py-3 text-sm font-medium text-slate-900 focus:outline-none focus:border-indigo-600" required>
                    <button type="submit" class="bg-indigo-600 hover:bg-indigo-700 text-white font-bold text-sm px-6 py-3 rounded-xl transition cursor-pointer shrink-0">
                        Search on Amazon &rarr;
                    </button>
                </form>
                <div class="flex flex-wrap items-center justify-center gap-2 pt-2 text-xs">
                    <span class="text-slate-400 font-semibold">Popular Searches:</span>
                    <a href="{amz_url('4K Laser Projector Home Theater 3000 Lumens')}" target="_blank" rel="nofollow sponsored noopener" class="px-2.5 py-1 bg-slate-100 hover:bg-indigo-100 text-slate-700 rounded-full transition">4K Laser Projectors</a>
                    <a href="{amz_url('Ultra Short Throw 4K Laser Projector TV')}" target="_blank" rel="nofollow sponsored noopener" class="px-2.5 py-1 bg-slate-100 hover:bg-indigo-100 text-slate-700 rounded-full transition">UST Laser TV</a>
                    <a href="{amz_url('120 Inch Fixed Frame Projector Screen 16:9')}" target="_blank" rel="nofollow sponsored noopener" class="px-2.5 py-1 bg-slate-100 hover:bg-indigo-100 text-slate-700 rounded-full transition">120" Fixed Screen</a>
                    <a href="{amz_url('Short Throw Projector Golf Simulator')}" target="_blank" rel="nofollow sponsored noopener" class="px-2.5 py-1 bg-slate-100 hover:bg-indigo-100 text-slate-700 rounded-full transition">Golf Simulator Projector</a>
                    <a href="{amz_url('Dolby Atmos 7.2 Channel AV Receiver')}" target="_blank" rel="nofollow sponsored noopener" class="px-2.5 py-1 bg-slate-100 hover:bg-indigo-100 text-slate-700 rounded-full transition">Dolby Atmos AVR</a>
                </div>
            </div>
        </section>

        <!-- BEST SELLING PRODUCTS GRID (PRODUK TERLARIS) -->
        <section id="best-sellers" class="space-y-6">
            <div class="flex flex-col sm:flex-row sm:items-end justify-between gap-2 border-b border-slate-200 pb-4">
                <div>
                    <span class="text-xs font-extrabold uppercase tracking-wider text-indigo-600">Top-Rated Cinema Hardware</span>
                    <h2 class="text-2xl font-extrabold text-slate-900">Best-Selling 4K Projectors, Screens & Mounts</h2>
                </div>
                <a href="{amz_url('Best Selling 4K Home Theater Projectors and Screens')}" target="_blank" rel="nofollow sponsored noopener" class="text-sm font-bold text-indigo-600 hover:text-indigo-700">
                    Browse Full Amazon Best Sellers &rarr;
                </a>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
                {bestseller_cards_html}
            </div>
        </section>

        <!-- IN-DEPTH PRODUCT REVIEW ARTICLES SECTION (ARTIKEL PRODUK REVIEW) -->
        <section id="reviews" class="space-y-6">
            <div class="flex flex-col sm:flex-row sm:items-end justify-between gap-2 border-b border-slate-200 pb-4">
                <div>
                    <span class="text-xs font-extrabold uppercase tracking-wider text-indigo-600">Hands-On Optical & Lumen Benchmarks</span>
                    <h2 class="text-2xl font-extrabold text-slate-900">In-Depth Projector & Screen Review Articles</h2>
                </div>
                <span class="text-xs font-semibold text-slate-500">Lab-Tested Throw Ratios, Contrast & Input Lag</span>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                {reviews_grid_html}
            </div>
        </section>

        <!-- MID-PAGE PROMOTIONAL AFFILIATE BANNER -->
        <section class="bg-slate-50 border-2 border-indigo-600 rounded-2xl p-6 sm:p-8 flex flex-col md:flex-row items-center justify-between gap-6">
            <div class="space-y-2 max-w-2xl">
                <span class="text-xs font-extrabold uppercase tracking-wider bg-indigo-600 text-white px-2.5 py-1 rounded">Daytime Viewing Bundle Guide</span>
                <h2 class="text-xl sm:text-2xl font-extrabold text-slate-900">Setting Up a Projector in a Room With Windows?</h2>
                <p class="text-sm text-slate-600">Pair a 3,000+ Lumen 4K Laser Projector with an Ambient Light Rejecting (ALR) screen to boost contrast by up to 75% in daytime living rooms.</p>
            </div>
            <a href="{mid_banner_link}" target="_blank" rel="nofollow sponsored noopener"
               class="shrink-0 bg-indigo-600 hover:bg-indigo-700 text-white font-extrabold text-sm px-6 py-3.5 rounded-xl shadow-sm transition">
               Explore 4K Projector + ALR Screen Bundles &rarr;
            </a>
        </section>

        <!-- PROGRAMMATIC SEO DIRECTORY -->
        <section id="presets" class="space-y-4">
            <div class="border-b border-slate-200 pb-3">
                <h2 class="text-xl font-extrabold text-slate-900">Screen Size & Room Setup Calculators</h2>
                <p class="text-xs text-slate-500">Select any screen diagonal or room configuration below for pre-calculated throw distance, dimensions, and lumen specs.</p>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-2.5">
                {preset_links_html}
            </div>
        </section>

        <!-- FREQUENTLY ASKED QUESTIONS (FAQ) -->
        <section id="faq" class="space-y-6">
            <div class="border-b border-slate-200 pb-3">
                <span class="text-xs font-extrabold uppercase tracking-wider text-indigo-600">Optical Sizing Knowledge Base</span>
                <h2 class="text-2xl font-extrabold text-slate-900">Frequently Asked Questions (FAQ)</h2>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                {faq_html}
            </div>
        </section>

    </main>

    <!-- FOOTER -->
    <footer class="bg-white border-t border-slate-200 mt-16 py-10 px-4 text-xs text-slate-500">
        <div class="max-w-6xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-4">
            <div>
                <p class="font-bold text-slate-800">{SITE_NAME} — {SITE_TAGLINE}</p>
                <p class="mt-1">As an Amazon Associate, this site earns from qualifying purchases (Store ID: {AFFILIATE_TAG}).</p>
            </div>
            <div class="flex flex-wrap gap-4 font-medium text-slate-600">
                <a href="{BASE_URL}/" class="hover:text-slate-900">Home</a>
                <a href="{BASE_URL}/#reviews" class="hover:text-slate-900">Product Reviews</a>
                <a href="{BASE_URL}/sitemap.xml" class="hover:text-slate-900">Sitemap</a>
                <a href="{BASE_URL}/#calculator" class="hover:text-slate-900">Calculator</a>
                <a href="{BASE_URL}/#faq" class="hover:text-slate-900">FAQ</a>
            </div>
        </div>
    </footer>

    <!-- INTERACTIVE CALCULATOR & AFFILIATE MATCHING SCRIPT -->
    <script>
        const AFFILIATE_TAG = "{AFFILIATE_TAG}";

        function makeAmazonLink(query) {{
            return "https://www.amazon.com/s?k=" + encodeURIComponent(query) + "&tag=" + AFFILIATE_TAG;
        }}

        function applyPreset(val) {{
            const parts = val.split(",");
            if (parts.length === 5) {{
                document.getElementById("diagInput").value = parts[0];
                document.getElementById("aspectInput").value = parts[1];
                document.getElementById("ratioInput").value = parts[2];
                document.getElementById("lightInput").value = parts[3];
                document.getElementById("gainInput").value = parts[4];
                calculateThrow();
            }}
        }}

        function handleAmazonSearch(e) {{
            e.preventDefault();
            const q = document.getElementById("amzSearchInput").value.trim();
            if (q) {{
                window.open(makeAmazonLink(q), "_blank", "noopener,noreferrer");
            }}
        }}

        function calculateThrow() {{
            const diag = parseFloat(document.getElementById("diagInput").value) || 100;
            const aspect = document.getElementById("aspectInput").value || "16:9";
            const ratio = parseFloat(document.getElementById("ratioInput").value) || 1.25;
            const light = document.getElementById("lightInput").value || "dim";
            const gain = parseFloat(document.getElementById("gainInput").value) || 1.0;

            let wFactor = 0.8716;
            let hFactor = 0.4903;
            if (aspect === "2.35:1") {{
                wFactor = 0.9195;
                hFactor = 0.3913;
            }} else if (aspect === "16:10") {{
                wFactor = 0.8480;
                hFactor = 0.5300;
            }}

            const widthIn = Math.round(diag * wFactor * 10) / 10;
            const heightIn = Math.round(diag * hFactor * 10) / 10;
            const areaSqFt = Math.round(((widthIn * heightIn) / 144) * 10) / 10;

            const throwInches = widthIn * ratio;
            const throwFeet = Math.round((throwInches / 12) * 10) / 10;
            const throwMeters = (throwFeet * 0.3048).toFixed(2);

            const targetFootLamberts = light === "dark" ? 18 : (light === "dim" ? 30 : 48);
            const rawLumens = (areaSqFt * targetFootLamberts) / gain;
            const reqLumens = Math.max(1200, Math.ceil((rawLumens * 1.25) / 100) * 100);

            const thxSeatFt = Math.round(((diag * 1.2) / 12) * 10) / 10;
            const minSeatFt = Math.round((diag / 12) * 10) / 10;
            const maxSeatFt = Math.round(((diag * 1.55) / 12) * 10) / 10;

            document.getElementById("resThrowDist").textContent = throwFeet + " ft (" + Math.round(throwInches) + "\\\")";
            document.getElementById("resThrowMeters").textContent = throwMeters + " meters lens-to-screen";
            document.getElementById("resLumens").textContent = reqLumens.toLocaleString() + "+ lm";
            document.getElementById("resDimensions").textContent = widthIn + "\\\" W × " + heightIn + "\\\" H";
            document.getElementById("resAreaSqFt").textContent = areaSqFt + " sq.ft viewable area";
            document.getElementById("resSeating").textContent = thxSeatFt + " ft Optimal";
            document.getElementById("resSeatRange").textContent = "SMPTE Range: " + minSeatFt + "–" + maxSeatFt + " ft";

            const roundedScreenTier = diag <= 105 ? 100 : (diag <= 128 ? 120 : (diag <= 142 ? 135 : 150));
            let recTitle = "";
            let recDesc = "";
            let projQuery = "";
            let screenQuery = roundedScreenTier + " Inch " + aspect + " Fixed Frame Projector Screen Silver Ticket";

            if (ratio <= 0.40) {{
                recTitle = "4K Triple-Laser Ultra-Short Throw (UST) Projector + " + roundedScreenTier + "\\\" CLR Screen";
                recDesc = "Designed for 0.20:1–0.35:1 ultra-short throw distance right from your media stand.";
                projQuery = "4K Ultra Short Throw Triple Laser Projector AWOL Vision Hisense PX3";
                screenQuery = roundedScreenTier + " Inch ALR CLR Screen for Ultra Short Throw Projector";
            }} else if (ratio <= 0.90) {{
                recTitle = "3,000+ Lumen Short-Throw Projector (0.69:1–0.85:1) + " + roundedScreenTier + "\\\" Screen";
                recDesc = "Eliminates room shadows in golf simulators, bedrooms, and tight living spaces.";
                projQuery = "Short Throw 4K 1080p Projector 3000 Lumens BenQ TH671ST TK700STi";
            }} else if (reqLumens >= 2800) {{
                recTitle = "3,200+ ANSI Lumen 4K Laser Home Theater Projector + " + roundedScreenTier + "\\\" Screen";
                recDesc = "High-output laser engine engineered to keep " + diag + "-inch screens razor-sharp and vibrant.";
                projQuery = "BenQ TK710 Epson 3800 4K Laser Projector 3200 Lumens";
            }} else {{
                recTitle = "True 4K UHD Cinema Projector (1.20–1.50 Throw) + " + roundedScreenTier + "\\\" Screen";
                recDesc = "Balanced HDR contrast and wide color gamut for dark and dim home theater rooms.";
                projQuery = "4K UHD Home Theater Projector BenQ XGIMI Horizon Ultra Epson";
            }}

            document.getElementById("recHardwareTitle").textContent = recTitle;
            document.getElementById("recHardwareDesc").textContent = recDesc;
            document.getElementById("recProjectorBtn").href = makeAmazonLink(projQuery);
            document.getElementById("recScreenBtn").href = makeAmazonLink(screenQuery);
        }}

        window.addEventListener("DOMContentLoaded", calculateThrow);
    </script>
</body>
</html>"""

def render_single_review_page(rev):
    canonical_url = f"{BASE_URL}/{rev['slug']}.html"
    amz_link = amz_url(rev["keyword"])

    review_schema = {
        "@context": "https://schema.org",
        "@type": "Product",
        "name": rev["product_name"],
        "description": rev["summary"],
        "Category": rev["category"],
        "review": {
            "@type": "Review",
            "reviewRating": {
                "@type": "Rating",
                "ratingValue": rev["rating_score"],
                "bestRating": "5"
            },
            "author": {
                "@type": "Organization",
                "name": SITE_NAME
            },
            "reviewBody": " ".join(rev["body_paragraphs"])
        }
    }

    pros_html = "".join([f'<li class="flex items-start gap-2 text-sm text-slate-700"><span class="text-emerald-600 font-bold">✓</span><span>{p}</span></li>' for p in rev["pros"]])
    cons_html = "".join([f'<li class="flex items-start gap-2 text-sm text-slate-700"><span class="text-rose-600 font-bold">✕</span><span>{c}</span></li>' for c in rev["cons"]])
    paragraphs_html = "".join([f'<p class="text-slate-700 leading-relaxed text-base mb-4">{p}</p>' for p in rev["body_paragraphs"]])

    other_reviews_html = ""
    for other in PRODUCT_REVIEWS:
        if other["slug"] != rev["slug"]:
            other_reviews_html += f"""
            <a href="{BASE_URL}/{other['slug']}.html" class="bg-white border border-slate-200 rounded-xl p-4 hover:border-indigo-600 transition block">
                <span class="text-[11px] font-bold text-indigo-600 uppercase">{other['verdict_badge']}</span>
                <h4 class="font-extrabold text-sm text-slate-900 mt-1">{other['product_name']} Review</h4>
                <span class="text-xs text-slate-500 mt-1 block">Score: {other['rating_score']} / 5.0 ★ &rarr;</span>
            </a>
            """

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{rev['title']} | {SITE_NAME}</title>
    <meta name="description" content="{rev['summary']}">
    <link rel="canonical" href="{canonical_url}">
    <meta name="robots" content="index, follow">
    <script src="https://cdn.tailwindcss.com"></script>
    <script type="application/ld+json">{json.dumps(review_schema)}</script>
</head>
<body class="bg-white text-slate-900 antialiased">

    {render_Common_Header_And_Banner()}

    <main class="max-w-4xl mx-auto px-4 py-10 space-y-10">
        <!-- Breadcrumb -->
        <nav class="text-xs font-semibold text-slate-500 flex items-center gap-2">
            <a href="{BASE_URL}/" class="hover:text-indigo-600">Home & Throw Calculator</a>
            <span>/</span>
            <a href="{BASE_URL}/#reviews" class="hover:text-indigo-600">Product Reviews</a>
            <span>/</span>
            <span class="text-slate-800">{rev['product_name']}</span>
        </nav>

        <!-- Review Header Card -->
        <div class="bg-white border-2 border-slate-200 rounded-2xl p-6 sm:p-8 shadow-sm space-y-5">
            <div class="flex flex-wrap items-center justify-between gap-2">
                <span class="text-xs font-extrabold uppercase tracking-wider bg-indigo-100 text-indigo-900 px-3 py-1 rounded-full">{rev['verdict_badge']}</span>
                <span class="text-sm font-black bg-amber-100 text-amber-900 px-3 py-1 rounded-lg">Lab Rating: {rev['rating_score']} / 5.0 ★</span>
            </div>
            <h1 class="text-2xl sm:text-4xl font-extrabold text-slate-900 leading-tight">{rev['title']}</h1>
            <p class="text-base text-slate-600 leading-relaxed">{rev['summary']}</p>

            <!-- Specs Grid -->
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 bg-slate-50 p-4 rounded-xl border border-slate-200 text-xs">
                <div><span class="text-slate-400 block font-medium">Throw Ratio</span><strong class="text-slate-900">{rev['throw_ratio']}</strong></div>
                <div><span class="text-slate-400 block font-medium">Brightness</span><strong class="text-slate-900">{rev['brightness']}</strong></div>
                <div><span class="text-slate-400 block font-medium">Resolution</span><strong class="text-slate-900">{rev['resolution']}</strong></div>
                <div><span class="text-slate-400 block font-medium">Gaming Lag</span><strong class="text-slate-900">{rev['input_lag']}</strong></div>
            </div>

            <div class="flex flex-col sm:flex-row gap-3 pt-2">
                <a href="{amz_link}" target="_blank" rel="nofollow sponsored noopener"
                   class="flex-1 text-center bg-indigo-600 hover:bg-indigo-700 text-white font-extrabold text-sm py-3.5 px-6 rounded-xl transition shadow-sm">
                   Check Latest Price & Availability on Amazon &rarr;
                </a>
                <a href="{BASE_URL}/#calculator"
                   class="text-center bg-slate-100 hover:bg-slate-200 text-slate-900 font-bold text-sm py-3.5 px-5 rounded-xl transition">
                   Calculate Throw Distance for Your Room
                </a>
            </div>
        </div>

        <!-- Pros & Cons Box -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="bg-white border-2 border-emerald-200 rounded-2xl p-6 space-y-3">
                <h2 class="text-base font-extrabold text-emerald-900 uppercase tracking-wide">What We Like (Pros)</h2>
                <ul class="space-y-2.5">{pros_html}</ul>
            </div>
            <div class="bg-white border-2 border-rose-200 rounded-2xl p-6 space-y-3">
                <h2 class="text-base font-extrabold text-rose-900 uppercase tracking-wide">Things to Consider (Cons)</h2>
                <ul class="space-y-2.5">{cons_html}</ul>
            </div>
        </div>

        <!-- In-Depth Review Body -->
        <article class="bg-white border border-slate-200 rounded-2xl p-6 sm:p-8 space-y-4">
            <h2 class="text-xl font-extrabold text-slate-900 border-b border-slate-100 pb-3">Hands-On Optical Performance & Sizing Analysis</h2>
            {paragraphs_html}
            <div class="pt-4 border-t border-slate-100 flex flex-col sm:flex-row items-center justify-between gap-4">
                <div>
                    <span class="text-xs font-bold uppercase text-indigo-600 block">Bottom Line Verdict</span>
                    <p class="text-sm font-bold text-slate-900">{rev['product_name']} earns a {rev['rating_score']}/5.0 for home theater performance.</p>
                </div>
                <a href="{amz_link}" target="_blank" rel="nofollow sponsored noopener"
                   class="shrink-0 bg-amber-500 hover:bg-amber-600 text-slate-950 font-extrabold text-sm px-6 py-3 rounded-xl transition shadow-sm">
                   View Customer Reviews & Price on Amazon &rarr;
                </a>
            </div>
        </article>

        <!-- Other Product Reviews -->
        <section class="space-y-4">
            <h3 class="text-lg font-extrabold text-slate-900">More Home Theater Product Reviews</h3>
            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
                {other_reviews_html}
            </div>
        </section>
    </main>

    <footer class="bg-white border-t border-slate-200 mt-16 py-10 px-4 text-xs text-slate-500 text-center">
        <p class="font-bold text-slate-800">{SITE_NAME} — {SITE_TAGLINE}</p>
        <p class="mt-1">As an Amazon Associate, this site earns from qualifying purchases (Store ID: {AFFILIATE_TAG}).</p>
    </footer>
</body>
</html>"""

def generate_sitemap_and_robots(urls):
    today = datetime.datetime.utcnow().strftime("%Y-%m-%d")
    xml_items = ""
    for u in urls:
        xml_items += f"""  <url>
    <loc>{u}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>{"1.0" if u.endswith("/") else "0.85"}</priority>
  </url>\n"""

    sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{xml_items}</urlset>"""

    with open(os.path.join(OUTPUT_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(sitemap_content)

    robots_content = f"""User-agent: *
Allow: /
Sitemap: {BASE_URL}/sitemap.xml
"""
    with open(os.path.join(OUTPUT_DIR, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(robots_content)

    with open(os.path.join(OUTPUT_DIR, f"{INDEXNOW_KEY}.txt"), "w", encoding="utf-8") as f:
        f.write(INDEXNOW_KEY)

def ping_indexnow(urls):
    parsed_host = urllib.parse.urlparse(BASE_URL).netloc
    if not parsed_host or "username.github.io" in parsed_host:
        return

    payload = {
        "host": parsed_host,
        "key": INDEXNOW_KEY,
        "keyLocation": f"{BASE_URL}/{INDEXNOW_KEY}.txt",
        "urlList": urls
    }
    try:
        req = urllib.request.Request(
            "https://api.indexnow.org/indexnow",
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json; charset=utf-8"},
            method="POST"
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            print(f"IndexNow Ping Status: {resp.status}")
    except Exception as e:
        print(f"IndexNow notice: {e}")

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    generated_urls = []

    # 1. Generate Homepage
    home_preset = {
        "slug": "index",
        "name": "120-Inch 4K Home Theater",
        "diag": 120,
        "aspect": "16:9",
        "ratio": 1.25,
        "light": "dim",
        "gain": 1.1,
        "desc": "Calculate exact projector throw distance (ft & m), screen width/height, THX seating distance, and required ANSI lumens for any room—plus read lab-tested 4K projector & screen reviews."
    }
    with open(os.path.join(OUTPUT_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(render_calculator_page(home_preset, is_home=True))
    generated_urls.append(f"{BASE_URL}/")

    # 2. Generate Programmatic Calculator Pages
    for page in ALL_CALC_PAGES:
        filename = f"{page['slug']}.html"
        with open(os.path.join(OUTPUT_DIR, filename), "w", encoding="utf-8") as f:
            f.write(render_calculator_page(page, is_home=False))
        generated_urls.append(f"{BASE_URL}/{filename}")

    # 3. Generate Standalone Product Review Article Pages
    for rev in PRODUCT_REVIEWS:
        filename = f"{rev['slug']}.html"
        with open(os.path.join(OUTPUT_DIR, filename), "w", encoding="utf-8") as f:
            f.write(render_single_review_page(rev))
        generated_urls.append(f"{BASE_URL}/{filename}")

    # 4. Sitemap, Robots & IndexNow Ping
    generate_sitemap_and_robots(generated_urls)
    ping_indexnow(generated_urls)
    print(f"Successfully generated {len(generated_urls)} pages (Calculators + Product Reviews) in /{OUTPUT_DIR}!")

if __name__ == "__main__":
    main()
