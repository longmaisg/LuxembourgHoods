# LuxembourgHoods - Blogger Setup Instructions

## Overview

This project contains a Blogger theme and pre-written posts for a Luxembourg neighborhood guide website.

---

## Step 1: Create Your Blogger Blog

1. Go to [blogger.com](https://www.blogger.com)
2. Sign in with your Google account
3. Click **"Create New Blog"**
4. Choose a name: e.g., "LuxembourgHoods" or "Luxembourg Neighborhood Guide"
5. Pick a URL: e.g., `luxembourghoods.blogspot.com`
6. Click **Create blog**

---

## Step 2: Install the Theme

1. In Blogger dashboard, go to **Theme** (left sidebar)
2. Click the **dropdown arrow** next to "Customize"
3. Select **"Edit HTML"**
4. **Select all** existing code (Ctrl+A / Cmd+A)
5. **Delete** it
6. Open `neighborhood-theme.xml` from this project
7. **Copy all** the content
8. **Paste** into Blogger's HTML editor
9. Click **Save** (disk icon, top right)

**Note:** You may see a warning about widgets. Click "Keep widgets" if prompted.

---

## Step 3: Create Posts

For each commune (HTML file in `/posts/` folder):

### 3.1 Create New Post
1. In Blogger, click **"+ New post"** (orange button)
2. Enter the **title**: e.g., "Belvaux" or "Luxembourg City"

### 3.2 Switch to HTML Mode
1. In the post editor, click the **pencil icon** (top left of editor)
2. Select **"HTML view"** (not "Compose view")

### 3.3 Paste Content
1. Open the corresponding `.html` file from `/posts/`
2. **Copy everything** (skip the comment at the top if you want)
3. **Paste** into Blogger's HTML editor

### 3.4 Add Labels
1. On the right sidebar, find **"Labels"**
2. Add labels based on the comment at the top of each HTML file
3. Example for Belvaux: `South`, `Family`, `Affordable`

**Standard Labels to Use:**

| Region Labels | Type Labels |
|---------------|-------------|
| Luxembourg-City | Family |
| South | Expat |
| North | Affordable |
| East | Urban |
| West | Rural |

### 3.5 Add Featured Image
1. On the right sidebar, find **"Featured image"**
2. Upload or link an image of the commune
3. Recommended: 1200x630px for social sharing

**Free image sources:**
- [Unsplash](https://unsplash.com) - search "Luxembourg"
- [Wikimedia Commons](https://commons.wikimedia.org) - search commune names
- Google Maps screenshots (for personal/editorial use)

### 3.6 Publish
1. Click **"Publish"** (top right)
2. Or click **"Schedule"** to publish later

---

## Step 4: Create Static Pages

Create these pages (not posts) for site structure:

1. **About** (`/p/about.html`)
   - Who you are, why you created the site

2. **Methodology** (`/p/methodology.html`)
   - How you research and rate communes

3. **Privacy Policy** (`/p/privacy.html`)
   - Required if using ads/analytics

4. **Contact** (`/p/contact.html`)
   - How readers can reach you

### To Create a Page:
1. Go to **Pages** (left sidebar)
2. Click **"+ New page"**
3. Write content and publish

---

## Step 5: Configure Widgets

### Labels Widget (Browse by Region)
1. Go to **Layout** (left sidebar)
2. Find the sidebar section
3. The theme already includes a Labels widget
4. Click **Edit** to configure display options

### Popular Posts Widget
1. Already included in theme
2. Will auto-populate as you get traffic

### Newsletter Widget
1. The theme has a placeholder form
2. To make it functional:
   - Use [Mailchimp](https://mailchimp.com) (free tier)
   - Or [Buttondown](https://buttondown.email) (simple)
   - Replace the form HTML in Layout > HTML widget

---

## Step 6: Add Google AdSense (Optional)

1. Apply at [adsense.google.com](https://www.adsense.com)
2. Need some content first (10-20 posts recommended)
3. Once approved:
   - Go to **Layout**
   - Find the "Ad Space" HTML widget
   - Replace placeholder with your AdSense code

---

## File Reference

```
LuxembourgHoods/
├── neighborhood-theme.xml    # Upload to Blogger Theme
├── posts/
│   ├── belvaux.html         # Labels: South, Family, Affordable
│   ├── bertrange.html       # Labels: West, Family, Expat
│   ├── differdange.html     # Labels: South, Affordable, Urban
│   ├── dudelange.html       # Labels: South, Affordable, Family
│   ├── esch-sur-alzette.html # Labels: South, Urban, Affordable, Expat
│   ├── luxembourg-city.html  # Labels: Luxembourg-City, Urban, Expat
│   └── strassen.html        # Labels: West, Family, Expat, Urban
└── INSTRUCTIONS.md          # This file
```

---

## Backlinks Explained

Each post contains internal links to related communes. The URL format used is:

```
/2025/01/commune-name.html
```

**Important:** Blogger generates URLs based on:
- Year/month of publishing
- Post title (slugified)

If you publish in January 2025 with title "Belvaux", the URL will be:
```
/2025/01/belvaux.html
```

**To ensure backlinks work:**
1. Publish all posts in the same month, OR
2. After publishing, update the links in each post to match actual URLs

**To find a post's URL:**
1. Publish the post
2. Click "View" to see it
3. Copy the URL from browser

### IMPORTANT: Publish All Posts in the Same Month

Blogger URLs include the publish date: `/2026/01/belvaux.html`

All backlinks in the posts assume **January 2026**. To ensure links work:

1. **Option A (Recommended):** Publish all posts in January 2026
2. **Option B:** When creating a new post, set "Published on" date to January 2026 (backdate it)
3. **Option C:** If you publish in a different month, update all backlinks in other posts

To backdate a post:
1. In post editor, click "Post settings" (right sidebar)
2. Click "Published on"
3. Change the date to January 2026
4. Save and publish

---

## Customization Tips

### Change Colors
In Theme > Edit HTML, find the `:root` section and modify:
```css
--primary: #1e40af;      /* Main blue */
--primary-dark: #1e3a8a; /* Darker blue */
--accent: #dc2626;       /* Red accent */
```

### Change Logo Text
In the HTML, find:
```html
<div class='logo-text'>Luxembourg<span>Hoods</span></div>
```
Change to your preferred name.

### Change Navigation
Find the `nav-menu` section and update region links.

---

## Content Guidelines

### Updating Prices
- Update price ranges quarterly or when market changes significantly
- Always include "Last researched: [Month Year]" at bottom

### Adding New Communes
1. Copy any existing post as template
2. Update all sections with new commune data
3. Add backlinks to/from related communes
4. Use consistent rating scale (A, A-, B+, B, B-, C+, etc.)

### Rating Scale
| Rating | Meaning |
|--------|---------|
| A | Excellent - premium choice |
| A- | Very good - minor trade-offs |
| B+ | Good - solid value |
| B | Average - acceptable |
| B- | Below average - notable drawbacks |
| C+ | Fair - significant compromises |

---

## SEO Tips

1. **Title format:** "[Commune Name] - Living Guide & Housing Prices 2025"
2. **Meta description:** First paragraph should summarize the commune
3. **Internal links:** Each post should link to 3-5 other posts
4. **Labels:** Use consistently for category pages
5. **Images:** Add alt text describing the commune

---

## Maintenance Checklist

### Monthly
- [ ] Check for price updates in news
- [ ] Respond to any comments
- [ ] Share new posts on social media

### Quarterly
- [ ] Update price ranges if needed
- [ ] Add new commune posts
- [ ] Review and fix any broken links

### Yearly
- [ ] Major price/market update
- [ ] Review all ratings
- [ ] Update "Last researched" dates

---

## Questions?

If you need help:
1. Blogger Help: [support.google.com/blogger](https://support.google.com/blogger)
2. Theme issues: Check the CSS in Edit HTML
3. Content questions: Research on immotop.lu, athome.lu, STATEC

Good luck with LuxembourgHoods! 🏠
