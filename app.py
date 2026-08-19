import streamlit as st
import os
from pathlib import Path

# Configure page
st.set_page_config(
    page_title="🧠 Automation Suite",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for dark theme and styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        color: white;
    }
    
    .category-card {
        background: #1e1e1e;
        padding: 1.5rem;
        border-radius: 10px;
        border: 1px solid #333;
        margin: 1rem 0;
        transition: transform 0.2s;
    }
    
    .category-card:hover {
        transform: translateY(-2px);
        border-color: #4CAF50;
    }
    
    .task-button {
        background: #2d2d2d;
        border: 1px solid #444;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem;
        text-align: center;
        cursor: pointer;
        transition: all 0.2s;
    }
    
    .task-button:hover {
        background: #3d3d3d;
        border-color: #4CAF50;
    }
    
    .stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #4CAF50 0%, #45a049 100%);
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        font-weight: bold;
    }
    
    .sidebar .sidebar-content {
        background: #1a1a1a;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🧠 Automation Suite</h1>
        <h3>Unified Control Dashboard</h3>
        <p>Welcome to your modular command center. Select a tool from the sidebar to get started.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar navigation with categories
    st.sidebar.title("🧠 Automation Suite")
    
    # Category selection
    category = st.sidebar.selectbox("Select Category:", 
                                   ["🔧 Python Automation", "🤖 Machine Learning", "🐧 Linux"])
    
    # Navigation tabs based on category
    if category == "🔧 Python Automation":
        tabs = ["🌐 Web Scraper", "🔍 Google Search", "📧 Email Sender", 
                "🎨 Image Generator", "🔄 Face Swap", "💬 WhatsApp", "📱 SMS Sender", 
                "📞 Phone Caller", "🖥️ RAM Monitor", "📲 WhatsApp Anonymous", "📚 Tuple vs List"]
    elif category == "🤖 Machine Learning":
        tabs = ["🤖 Machine Learning Tasks"]
    else:  # Linux
        tabs = ["🐧 Linux Operations"]
    
    selected_tab = st.sidebar.radio("Select Tool:", tabs)
    
    # Main content area
    if selected_tab == "🌐 Web Scraper":
        show_web_scraper_page()
    elif selected_tab == "🔍 Google Search":
        show_google_search_page()
    elif selected_tab == "📧 Email Sender":
        show_email_sender_page()
    elif selected_tab == "🎨 Image Generator":
        show_image_generator_page()
    elif selected_tab == "🔄 Face Swap":
        show_face_swap_page()
    elif selected_tab == "💬 WhatsApp":
        show_whatsapp_page()
    elif selected_tab == "📱 SMS Sender":
        show_sms_sender_page()
    elif selected_tab == "📞 Phone Caller":
        show_phone_caller_page()
    elif selected_tab == "🖥️ RAM Monitor":
        show_ram_monitor_page()
    elif selected_tab == "📲 WhatsApp Anonymous":
        show_whatsapp_anonymous_page()
    elif selected_tab == "📚 Tuple vs List":
        show_tuple_vs_list_page()
    elif selected_tab == "🤖 Machine Learning Tasks":
        show_machine_learning_page()
    elif selected_tab == "🐧 Linux Operations":
        show_linux_page()

def show_notifications_page():
    st.header("🔔 Notification Options")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📱 SMS Only"):
            st.success("SMS notification system activated!")
            
        if st.button("📞 Voice Call"):
            st.success("Voice call system activated!")
            
        if st.button("📱📞 SMS + Voice Call"):
            st.success("Combined SMS and Voice call system activated!")
            
        if st.button("🚀 All Channels"):
            st.success("All notification channels activated!")
    
    with col2:
        if st.button("💬 WhatsApp Only"):
            st.success("WhatsApp notification system activated!")
            
        if st.button("📱💬 SMS + WhatsApp"):
            st.success("Combined SMS and WhatsApp system activated!")
            
        if st.button("💬📞 WhatsApp + Voice Call"):
            st.success("Combined WhatsApp and Voice call system activated!")

def get_file_links(url, extensions):
    """Retrieve all file links with specified extensions from the web page."""
    response = requests.get(url)
    if response.status_code != 200:
        st.error(f"Failed to retrieve page: Status code {response.status_code}")
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")
    links = []
    for tag in soup.find_all("a", href=True):
        href = tag["href"]
        if any(href.lower().endswith(ext) for ext in extensions):
            full_url = href if href.startswith("http") else requests.compat.urljoin(url, href)
            links.append(full_url)
    return links

def download_file(url, download_folder):
    """Download a single file to the download_folder."""
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
    
    local_filename = os.path.join(download_folder, url.split("/")[-1])
    try:
        r = requests.get(url, stream=True)
        with open(local_filename, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        return local_filename
    except Exception as e:
        st.warning(f"Failed to download {url}: {e}")
        return None

def show_web_scraper_page():
    st.header("🌐 Website Data Downloader")
    st.write("Go on a website and download the entire data using Python")
    
    url_input = st.text_input("Enter the website URL to scrape and download files from:")
    
    file_types = st.multiselect(
        "Select file types to download:",
        options=[".csv", ".txt", ".xlsx", ".xls", ".pdf", ".zip", ".jpg", ".png"],
        default=[".csv", ".xlsx"]
    )
    
    download_button = st.button("Download Files")
    
    if download_button:
        if not url_input:
            st.error("Please enter a valid URL.")
        elif not file_types:
            st.error("Please select at least one file type to download.")
        else:
            st.info(f"Fetching files from {url_input} ...")
            files = get_file_links(url_input, file_types)
            if files:
                st.success(f"Found {len(files)} files.")
                folder = "downloaded_files"
                
                # Create progress bar
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                downloaded_files = []
                for i, file_url in enumerate(files):
                    status_text.text(f"Downloading: {file_url}")
                    saved_path = download_file(file_url, folder)
                    if saved_path:
                        downloaded_files.append(saved_path)
                    
                    # Update progress
                    progress_bar.progress((i + 1) / len(files))
                
                if downloaded_files:
                    st.success(f"Downloaded {len(downloaded_files)} files to ./{folder}/")
                    
                    # Show downloaded files
                    st.subheader("Downloaded Files:")
                    for file_path in downloaded_files:
                        st.write(f"✅ {os.path.basename(file_path)}")
                else:
                    st.warning("No files were successfully downloaded.")
            else:
                st.warning("No files found matching the selected types.")

def show_google_search_page():
    st.header("🔍 Google Search")
    st.markdown("Enter a query below to search Google and get the top results.")
    
    # Search Form
    with st.form("search_form"):
        query = st.text_input("Search Query", placeholder="e.g., Best places to visit in Rajasthan")
        num_results = st.slider("Number of results", min_value=5, max_value=25, value=10)
        submitted = st.form_submit_button("Search")
    
    # Handle Form Submission
    if submitted:
        if not query:
            st.warning("Please enter a search query to begin.")
        else:
            st.write(f"Searching for **'{query}'** and fetching the top **{num_results}** results...")
            
            # Add a placeholder for a loading spinner
            with st.spinner("Fetching results..."):
                try:
                    # Import googlesearch here to avoid import errors if not installed
                    from googlesearch import search
                    
                    # Perform the search and get a list of URLs
                    search_results = list(search(query, num_results=num_results, sleep_interval=2))
                    
                    st.success("Here are the results:")
                    # Display the results
                    for i, url in enumerate(search_results):
                        st.write(f"{i+1}. [{url}]({url})")
                        
                except ImportError:
                    st.error("Google search library not installed. Please install 'googlesearch-python' package.")
                except Exception as e:
                    st.error(f"An error occurred: {e}")
                    st.info("This might be due to too many requests. Please wait a bit before trying again.")

def show_email_sender_page():
    st.header("📧 Email Sender")
    st.write("Send email using Python with Gmail SMTP")
    
    # Add info about Gmail App Password
    with st.expander("ℹ️ How to get Gmail App Password"):
        st.markdown("""
        1. Go to your Google Account settings
        2. Enable 2-Factor Authentication
        3. Go to Security → App passwords
        4. Generate an app password for this application
        5. Use the generated 16-character password below
        """)
    
    with st.form("email_form"):
        col1, col2 = st.columns(2)
        with col1:
            sender = st.text_input("Sender Email (Gmail)", placeholder="your-email@gmail.com")
            receiver = st.text_input("Receiver Email", placeholder="recipient@example.com")
        with col2:
            app_password = st.text_input("Gmail App Password", type="password", 
                                       help="Use Gmail App Password, not your regular password")
            subject = st.text_input("Subject", placeholder="Email subject")
        
        message = st.text_area("Message", placeholder="Type your email message here...")
        
        # Anonymous email option
        anonymous_mode = st.checkbox("Send anonymously (hide sender details in message)")
        
        submitted = st.form_submit_button("📤 Send Email")

        if submitted:
            if not sender or not app_password or not receiver or not message:
                st.error("All fields are required!")
            else:
                # Create Email
                try:
                    import smtplib
                    from email.message import EmailMessage
                    
                    email = EmailMessage()
                    
                    if anonymous_mode:
                        email['From'] = "Anonymous Sender <noreply@anonymous.com>"
                        email['Reply-To'] = sender
                    else:
                        email['From'] = sender
                    
                    email['To'] = receiver
                    email['Subject'] = subject or "No Subject"
                    
                    # Add message content
                    if anonymous_mode:
                        email_content = f"{message}\n\n---\nThis email was sent anonymously via Python automation."
                    else:
                        email_content = message
                    
                    email.set_content(email_content)

                    # Send Email via Gmail SMTP
                    with st.spinner("Sending email..."):
                        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                            smtp.login(sender, app_password)
                            smtp.send_message(email)
                    
                    st.success("✅ Email sent successfully!")
                    st.balloons()
                    
                except ImportError:
                    st.error("❌ Email libraries not available. Please check your Python installation.")
                except smtplib.SMTPAuthenticationError:
                    st.error("❌ Authentication failed. Please check your email and app password.")
                    st.info("Make sure you're using a Gmail App Password, not your regular password.")
                except Exception as e:
                    st.error(f"❌ Failed to send email: {e}")
                    st.info("Common issues: Invalid email format, network connection, or SMTP settings.")

def show_image_generator_page():
    st.header("🎨 Image Generator")
    st.write("Draw simple shapes and generate an image!")
    
    # Canvas settings
    col1, col2 = st.columns(2)
    with col1:
        width = st.slider("Image width", 100, 800, 400)
        height = st.slider("Image height", 100, 800, 400)
    with col2:
        bg_color = st.color_picker("Background color", "#FFFFFF")
    
    st.divider()
    
    # Shape selection
    shape = st.selectbox("Shape to draw", ["Circle", "Rectangle", "Line"])
    
    # Shape coordinates
    col1, col2 = st.columns(2)
    with col1:
        x1 = st.number_input("Start X", 0, width, width//4)
        y1 = st.number_input("Start Y", 0, height, height//4)
    with col2:
        if shape in ["Rectangle", "Line"]:
            x2 = st.number_input("End X (for rectangles/lines)", 0, width, width//2)
            y2 = st.number_input("End Y (for rectangles/lines)", 0, height, height//2)
        else:
            x2, y2 = 0, 0  # Not used for circles
    
    # Shape properties
    col1, col2 = st.columns(2)
    with col1:
        if shape == "Circle":
            radius = st.slider("Circle radius", 10, min(width, height)//2, 50)
        else:
            radius = 0  # Not used for other shapes
        shape_color = st.color_picker("Shape color", "#0000FF")
    with col2:
        shape_width = st.slider("Line/Border width", 1, 20, 5)
    
    # Generate and display image
    try:
        from PIL import Image, ImageDraw
        import io
        
        # Create image
        img = Image.new("RGB", (width, height), color=bg_color)
        draw = ImageDraw.Draw(img)

        if shape == "Circle":
            draw.ellipse(
                [(x1-radius, y1-radius), (x1+radius, y1+radius)],
                outline=shape_color, fill=shape_color, width=shape_width
            )
        elif shape == "Rectangle":
            draw.rectangle(
                [(x1, y1), (x2, y2)],
                outline=shape_color, fill=shape_color, width=shape_width
            )
        elif shape == "Line":
            draw.line(
                [(x1, y1), (x2, y2)],
                fill=shape_color, width=shape_width
            )

        # Show the image
        st.image(img, caption="Your Created Image", use_column_width=True)

        # Download the image
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        byte_im = buf.getvalue()

        st.download_button(
            label="📥 Download Image",
            data=byte_im,
            file_name="my_generated_image.png",
            mime="image/png"
        )

        st.info("💡 Tip: Adjust the coordinates and properties above to create different shapes!")
        
    except ImportError:
        st.error("❌ PIL (Pillow) library not available. Please install Pillow to use image generation.")
        st.code("pip install Pillow")
    except Exception as e:
        st.error(f"❌ Error generating image: {e}")

def get_landmarks(img):
    """Extract facial landmarks using MediaPipe"""
    try:
        import mediapipe as mp
        mp_face_mesh = mp.solutions.face_mesh
        
        with mp_face_mesh.FaceMesh(static_image_mode=True,
                                   max_num_faces=1,
                                   refine_landmarks=True,
                                   min_detection_confidence=0.5) as face_mesh:
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            result = face_mesh.process(img_rgb)
            if not result.multi_face_landmarks:
                return None
            landmarks = result.multi_face_landmarks[0].landmark
            h, w = img.shape[:2]
            points = [(int(lm.x * w), int(lm.y * h)) for lm in landmarks]
            return points
    except ImportError:
        return None

def apply_affine_transform(src, src_tri, dst_tri, size):
    """Apply affine transformation to triangular regions"""
    warp_mat = cv2.getAffineTransform(np.float32(src_tri), np.float32(dst_tri))
    dst = cv2.warpAffine(src, warp_mat, (size[0], size[1]),
                         flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT_101)
    return dst

def warp_triangle(img1, img2, t1, t2):
    """Warp triangular regions between two images"""
    r1 = cv2.boundingRect(np.float32([t1]))
    r2 = cv2.boundingRect(np.float32([t2]))

    t1_rect = []
    t2_rect = []
    t2_rect_int = []

    for i in range(3):
        t1_rect.append(((t1[i][0] - r1[0]), (t1[i][1] - r1[1])))
        t2_rect.append(((t2[i][0] - r2[0]), (t2[i][1] - r2[1])))
        t2_rect_int.append((int(t2[i][0] - r2[0]), int(t2[i][1] - r2[1])))

    mask = np.zeros((r2[3], r2[2], 3), dtype=np.float32)
    cv2.fillConvexPoly(mask, np.array(t2_rect_int), (1.0, 1.0, 1.0), 16, 0)

    img1_rect = img1[r1[1]:r1[1] + r1[3], r1[0]:r1[0] + r1[2]]
    size = (r2[2], r2[3])
    img2_rect = apply_affine_transform(img1_rect, t1_rect, t2_rect, size)

    img2_rect = img2_rect * mask

    img2[r2[1]:r2[1] + r2[3], r2[0]:r2[0] + r2[2]] = \
        img2[r2[1]:r2[1] + r2[3], r2[0]:r2[0] + r2[2]] * (1 - mask)
    img2[r2[1]:r2[1] + r2[3], r2[0]:r2[0] + r2[2]] = \
        img2[r2[1]:r2[1] + r2[3], r2[0]:r2[0] + r2[2]] + img2_rect

def swap_faces(img1, img2):
    """Perform face swap between two images"""
    points1 = get_landmarks(img1)
    points2 = get_landmarks(img2)
    if points1 is None or points2 is None:
        return None

    img1_warped = np.copy(img2)

    hull1 = []
    hull2 = []

    hullIndex = cv2.convexHull(np.array(points2), returnPoints=False)
    for i in range(len(hullIndex)):
        hull1.append(points1[hullIndex[i][0]])
        hull2.append(points2[hullIndex[i][0]])

    rect = (0, 0, img2.shape[1], img2.shape[0])
    subdiv = cv2.Subdiv2D(rect)
    for p in hull2:
        subdiv.insert(p)

    triangles = subdiv.getTriangleList()
    triangles = np.array(triangles, dtype=np.int32)

    indexes_triangles = []
    for t in triangles:
        pts = [(t[0], t[1]), (t[2], t[3]), (t[4], t[5])]
        index_pts = []
        for pt in pts:
            for i in range(len(hull2)):
                if abs(pt[0] - hull2[i][0]) < 1 and abs(pt[1] - hull2[i][1]) < 1:
                    index_pts.append(i)
        if len(index_pts) == 3:
            indexes_triangles.append(index_pts)

    for triangle_index in indexes_triangles:
        t1 = [hull1[triangle_index[0]], hull1[triangle_index[1]], hull1[triangle_index[2]]]
        t2 = [hull2[triangle_index[0]], hull2[triangle_index[1]], hull2[triangle_index[2]]]
        warp_triangle(img1, img1_warped, t1, t2)

    hull8U = [(int(p[0]), int(p[1])) for p in hull2]
    mask = np.zeros(img2.shape, dtype=img2.dtype)
    cv2.fillConvexPoly(mask, np.array(hull8U), (255, 255, 255))

    r = cv2.boundingRect(np.array(hull2))
    center = (r[0] + r[2] // 2, r[1] + r[3] // 2)

    output = cv2.seamlessClone(np.uint8(img1_warped), img2, mask, center, cv2.NORMAL_CLONE)

    return output

def show_face_swap_page():
    st.header("🔄 Face Swap App (using MediaPipe)")
    st.write("Swap the faces in two images using advanced AI face detection")
    
    # Installation requirements info
    with st.expander("📋 Required Libraries"):
        st.markdown("""
        This feature requires additional libraries:
        ```bash
        pip install opencv-python mediapipe numpy
        ```
        """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("First Face Image")
        img1_file = st.file_uploader("Upload first face image", type=["jpg", "jpeg", "png"], key="face1")
        if img1_file:
            img1_display = Image.open(img1_file)
            st.image(img1_display, caption="Source Image", use_column_width=True)
    
    with col2:
        st.subheader("Second Face Image")
        img2_file = st.file_uploader("Upload second face image", type=["jpg", "jpeg", "png"], key="face2")
        if img2_file:
            img2_display = Image.open(img2_file)
            st.image(img2_display, caption="Target Image", use_column_width=True)
    
    if st.button("🔄 Swap Faces", type="primary"):
        if img1_file and img2_file:
            try:
                import cv2
                import numpy as np
                from PIL import Image
                
                # Load and convert images
                img1 = Image.open(img1_file).convert("RGB")
                img2 = Image.open(img2_file).convert("RGB")

                img1_cv = cv2.cvtColor(np.array(img1), cv2.COLOR_RGB2BGR)
                img2_cv = cv2.cvtColor(np.array(img2), cv2.COLOR_RGB2BGR)

                with st.spinner("Processing face swap... This may take a moment."):
                    swapped_img = swap_faces(img1_cv, img2_cv)

                if swapped_img is not None:
                    swapped_img_rgb = cv2.cvtColor(swapped_img, cv2.COLOR_BGR2RGB)
                    st.success("✅ Face swap completed successfully!")
                    st.image(swapped_img_rgb, caption="🎭 Swapped Face Result", use_column_width=True)
                    
                    # Convert to downloadable format
                    import io
                    result_img = Image.fromarray(swapped_img_rgb)
                    buf = io.BytesIO()
                    result_img.save(buf, format="PNG")
                    byte_im = buf.getvalue()
                    
                    st.download_button(
                        label="📥 Download Result",
                        data=byte_im,
                        file_name="face_swapped_result.png",
                        mime="image/png"
                    )
                else:
                    st.error("❌ Face swap failed. Ensure both images contain clear, front-facing faces.")
                    st.info("💡 Tips: Use high-quality images with clearly visible faces facing forward.")
                    
            except ImportError as e:
                st.error("❌ Required libraries not installed.")
                st.code("pip install opencv-python mediapipe numpy")
                st.info("Please install the required libraries and restart the application.")
            except Exception as e:
                st.error(f"❌ An error occurred during face swap: {e}")
        else:
            st.error("Please upload both images before attempting face swap.")

def show_whatsapp_page():
    st.header("📱 WhatsApp Message Sender")
    st.write("Send WhatsApp messages using Python automation")
    
    # Installation requirements info
    with st.expander("📋 Required Libraries & Setup"):
        st.markdown("""
        This feature requires:
        ```bash
        pip install pywhatkit
        ```
        
        **Important Setup Notes:**
        - WhatsApp Web must be logged in on your default browser
        - Keep your browser open during message sending
        - First-time use may require QR code scanning
        - Messages are sent through WhatsApp Web interface
        """)
    
    # Phone number input
    phone = st.text_input("📞 Enter Phone Number (with country code)", 
                         value="+91", 
                         help="Include country code (e.g., +91 for India, +1 for USA)")
    
    # Message options
    option = st.radio("Choose Action:", ["Send Message Now", "Schedule Message", "Other WhatsApp Tasks"])
    
    if option == "Send Message Now":
        message = st.text_area("💬 Enter Message", placeholder="Type your WhatsApp message here...")
        
        col1, col2 = st.columns(2)
        with col1:
            wait_time = st.slider("Wait Time (seconds)", 5, 30, 10, 
                                help="Time to wait before sending message")
        with col2:
            close_tab = st.checkbox("Close tab after sending", value=True)
        
        if st.button("📤 Send Now", type="primary"):
            if phone and message:
                try:
                    import pywhatkit as kit
                    
                    with st.spinner(f"Opening WhatsApp Web and sending message... Please wait {wait_time} seconds."):
                        kit.sendwhatmsg_instantly(
                            phone_no=phone, 
                            message=message, 
                            wait_time=wait_time, 
                            tab_close=close_tab
                        )
                    st.success("✅ Message sent successfully!")
                    st.balloons()
                    
                except ImportError:
                    st.error("❌ pywhatkit library not installed.")
                    st.code("pip install pywhatkit")
                except Exception as e:
                    st.error(f"❌ Error sending message: {e}")
                    st.info("💡 Make sure WhatsApp Web is logged in and your browser is open.")
            else:
                st.error("Please enter both phone number and message.")
    
    elif option == "Schedule Message":
        message = st.text_area("💬 Enter Message", placeholder="Type your scheduled message here...")
        
        col1, col2 = st.columns(2)
        with col1:
            hour = st.number_input("Hour (24-hour format)", 0, 23, 12)
        with col2:
            minute = st.number_input("Minute", 0, 59, 0)
        
        if st.button("⏰ Schedule Message", type="primary"):
            if phone and message:
                try:
                    import pywhatkit as kit
                    
                    kit.sendwhatmsg(
                        phone_no=phone, 
                        message=message, 
                        time_hour=int(hour), 
                        time_min=int(minute)
                    )
                    st.success(f"📨 Message scheduled for {hour:02d}:{minute:02d}")
                    st.info("Keep your computer on and browser open at the scheduled time.")
                    
                except ImportError:
                    st.error("❌ pywhatkit library not installed.")
                    st.code("pip install pywhatkit")
                except Exception as e:
                    st.error(f"❌ Error scheduling message: {e}")
            else:
                st.error("Please enter both phone number and message.")
    
    elif option == "Other WhatsApp Tasks":
        st.subheader("🔧 Additional WhatsApp Features")
        
        task = st.selectbox("Choose Task:", [
            "Send WhatsApp message to anyone without using your contact number",
            "Make a phone call using Python", 
            "Read the RAM using Python"
        ])
        
        if task == "Send WhatsApp message to anyone without using your contact number":
            st.info("💡 This uses WhatsApp Web which doesn't hide your number, but you can send to unsaved contacts.")
            recipient = st.text_input("Recipient Number (with country code):")
            anon_message = st.text_area("Message:")
            
            if st.button("Send to Unsaved Contact"):
                if recipient and anon_message:
                    try:
                        import pywhatkit as kit
                        
                        with st.spinner("Sending message to unsaved contact..."):
                            kit.sendwhatmsg_instantly(
                                phone_no=recipient, 
                                message=anon_message, 
                                wait_time=10, 
                                tab_close=True
                            )
                        st.success("Message sent to unsaved contact!")
                        
                    except Exception as e:
                        st.error(f"Error: {e}")
                else:
                    st.error("Please fill all fields.")
        
        elif task == "Make a phone call using Python":
            st.warning("⚠️ Direct phone calls through Python require additional setup and may not work on all systems.")
            phone_number = st.text_input("Phone Number to Call:")
            if st.button("Initiate Call"):
                st.info("This feature would require additional telephony libraries and setup.")
        
        elif task == "Read the RAM using Python":
            if st.button("📊 Check RAM Usage"):
                try:
                    import psutil
                    
                    # Get RAM information
                    ram = psutil.virtual_memory()
                    
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Total RAM", f"{ram.total / (1024**3):.1f} GB")
                    with col2:
                        st.metric("Available RAM", f"{ram.available / (1024**3):.1f} GB")
                    with col3:
                        st.metric("RAM Usage", f"{ram.percent}%")
                    
                    st.progress(ram.percent / 100)
                    st.success("✅ RAM information retrieved!")
                    
                except ImportError:
                    st.error("❌ psutil library not available.")
                    st.code("pip install psutil")
                except Exception as e:
                    st.error(f"Error reading RAM: {e}")

def show_sms_sender_page():
    st.header("📱 SMS Sender")
    st.write("Send SMS using Python (normal text message)")
    
    # Installation requirements info
    with st.expander("📋 Required Libraries & Setup"):
        st.markdown("""
        This feature requires Twilio:
        ```bash
        pip install twilio
        ```
        
        **Setup Notes:**
        - Requires Twilio account (free trial available)
        - Get credentials from Twilio Console
        - May incur charges per SMS sent
        - Need a Twilio phone number
        """)
    
    # Twilio Configuration
    account_sid = st.text_input("Twilio SID", 
                               placeholder="ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                               help="Your Twilio Account SID")
    auth_token = st.text_input("Auth Token", 
                              type="password",
                              help="Your Twilio Auth Token")
    from_number = st.text_input("Twilio Phone Number", 
                               placeholder="+15017122661",
                               help="Your Twilio phone number")
    to_number = st.text_input("Recipient Number", 
                             placeholder="+1234567890",
                             help="Recipient's phone number with country code")
    sms_body = st.text_area("SMS Body", 
                           placeholder="Type your SMS message here...",
                           help="Your SMS message content")
    
    if st.button("📤 Send SMS", type="primary"):
        if account_sid and auth_token and from_number and to_number and sms_body:
            try:
                from twilio.rest import Client
                
                with st.spinner("Sending SMS via Twilio..."):
                    client = Client(account_sid, auth_token)
                    message = client.messages.create(
                        body=sms_body,
                        from_=from_number,
                        to=to_number
                    )
                
                st.success(f"✅ Message sent! SID: {message.sid}")
                st.balloons()
                
            except ImportError:
                st.error("❌ Twilio library not installed.")
                st.code("pip install twilio")
            except Exception as e:
                st.error(f"❌ Failed to send SMS: {e}")
                st.info("💡 Check your Twilio credentials and phone number formats.")
        else:
            st.error("Please fill all required fields.")

def show_phone_caller_page():
    st.header("📞 Twilio Web Caller")
    st.write("Enter your Twilio credentials and recipient details to place a call.")
    
    # Installation requirements info
    with st.expander("📋 Required Libraries & Setup"):
        st.markdown("""
        This feature requires Twilio:
        ```bash
        pip install twilio
        ```
        
        **Setup Notes:**
        - Requires Twilio account (free trial available)
        - Get credentials from Twilio Console
        - May incur charges per call
        - Need a Twilio phone number
        """)
    
    st.subheader("1. Your Twilio Account Details")
    
    # Twilio credentials
    account_sid = st.text_input(
        "Twilio Account SID", 
        placeholder="ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        help="Your Twilio Account SID from the console"
    )
    auth_token = st.text_input(
        "Twilio Auth Token", 
        type="password",
        placeholder="Your Twilio Auth Token",
        help="Your Twilio Auth Token from the console"
    )
    twilio_number = st.text_input(
        "Your Twilio Phone Number", 
        placeholder="+15017122661",
        help="Your Twilio phone number"
    )
    
    st.subheader("2. Recipient Information")
    recipient_number = st.text_input(
        "Recipient's Phone Number",
        placeholder="+911234567890",
        help="Recipient's phone number with country code"
    )
    message_to_speak = st.text_area(
        "Message to Speak on Call",
        value="Hello from Streamlit! This is a test call generated using the Twilio API.",
        help="The message that will be spoken during the call"
    )
    
    st.subheader("3. Place the Call")
    if st.button("📞 Call Now", type="primary"):
        if not all([account_sid, auth_token, twilio_number, recipient_number, message_to_speak]):
            st.warning("Please fill in all the fields before placing a call.")
        else:
            try:
                from twilio.rest import Client
                from twilio.base.exceptions import TwilioRestException
                
                with st.spinner("Placing call..."):
                    # Initialize Twilio Client
                    client = Client(account_sid, auth_token)

                    # Construct the TwiML response
                    twiml_message = f"<Response><Say voice='alice'>{message_to_speak}</Say></Response>"

                    # Make the call
                    call = client.calls.create(
                        twiml=twiml_message,
                        to=recipient_number,
                        from_=twilio_number
                    )
                
                st.success(f"✅ Call initiated successfully! Call SID: `{call.sid}`")
                st.balloons()

            except ImportError:
                st.error("❌ Twilio library not installed.")
                st.code("pip install twilio")
            except Exception as e:
                if "TwilioRestException" in str(type(e)):
                    st.error(f"❌ Twilio Error: {str(e)}")
                else:
                    st.error(f"❌ An unexpected error occurred: {e}")
                st.info("💡 Check your Twilio credentials and phone number formats.")

def get_memory_info():
    """Retrieves and formats system memory statistics."""
    import psutil
    memory = psutil.virtual_memory()
    return {
        "total": memory.total,
        "available": memory.available,
        "used": memory.used,
        "percent_used": memory.percent
    }

def show_ram_monitor_page():
    st.header("🐏 System RAM Usage Monitor")
    st.markdown("This app displays the current RAM (Random Access Memory) usage of your system.")
    
    try:
        import psutil
        
        # Get memory information
        mem_info = get_memory_info()
        
        # Convert bytes to a more readable format (GB)
        total_gb = mem_info["total"] / (1024 ** 3)
        used_gb = mem_info["used"] / (1024 ** 3)
        available_gb = mem_info["available"] / (1024 ** 3)
        
        st.subheader("Live Memory Status")
        
        # Display metrics in columns for a clean layout
        col1, col2, col3 = st.columns(3)
        col1.metric("Total RAM", f"{total_gb:.2f} GB")
        col2.metric("Used RAM", f"{used_gb:.2f} GB", f"{mem_info['percent_used']}%")
        col3.metric("Available RAM", f"{available_gb:.2f} GB")
        
        # Display a progress bar for visual representation
        st.write("---")
        st.subheader(f"Usage Percentage: {mem_info['percent_used']}%")
        st.progress(mem_info['percent_used'] / 100)
        
        # Expander for more detailed information
        with st.expander("Click for Detailed Breakdown (in Bytes)"):
            st.write(f"**Total:** `{mem_info['total']:,}` bytes")
            st.write(f"**Used:** `{mem_info['used']:,}` bytes")
            st.write(f"**Available:** `{mem_info['available']:,}` bytes")
        
        # Auto-refresh button
        if st.button("🔄 Refresh Data", type="primary"):
            st.rerun()
        
        st.info("🔄 **Note:** The data reflects the current state. Click 'Refresh Data' to get the latest usage statistics.", icon="💡")
        
    except ImportError:
        st.error("❌ psutil library not available.")
        st.code("pip install psutil")
        st.info("Please install psutil to use RAM monitoring functionality.")
    except Exception as e:
        st.error(f"❌ Error reading RAM information: {e}")

def show_whatsapp_anonymous_page():
    st.header("📲 Send WhatsApp Message Using Twilio")
    st.write("Send WhatsApp message to anyone without using your contact number")
    
    # Installation requirements info
    with st.expander("📋 Required Libraries & Setup"):
        st.markdown("""
        This feature requires Twilio WhatsApp API:
        ```bash
        pip install twilio
        ```
        
        **Setup Notes:**
        - Requires Twilio account with WhatsApp API access
        - Uses Twilio Sandbox WhatsApp number
        - Recipient must join your sandbox first
        - May incur charges per message
        """)
    
    # Twilio Configuration
    st.subheader("Twilio WhatsApp Configuration")
    
    col1, col2 = st.columns(2)
    with col1:
        account_sid = st.text_input("Twilio Account SID", 
                                   placeholder="ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                                   help="Your Twilio Account SID")
        twilio_whatsapp_from = st.text_input("Twilio WhatsApp Number", 
                                           value="whatsapp:+14155238886",
                                           help="Twilio Sandbox WhatsApp number")
    with col2:
        auth_token = st.text_input("Twilio Auth Token", 
                                  type="password",
                                  help="Your Twilio Auth Token")
    
    # Message Configuration
    st.subheader("Message Details")
    recipient = st.text_input("Recipient WhatsApp Number (with country code)", 
                             placeholder="+919876543210",
                             help="Include country code, e.g., +919876543210")
    message = st.text_area("Message to Send", 
                          placeholder="Type your WhatsApp message here...",
                          help="Your WhatsApp message content")
    
    if st.button("📤 Send WhatsApp Message", type="primary"):
        if not recipient:
            st.error("Please enter the recipient number.")
        elif not message:
            st.error("Please enter a message to send.")
        elif not account_sid or not auth_token:
            st.error("Please enter your Twilio credentials.")
        else:
            try:
                from twilio.rest import Client
                
                # Initialize Twilio client
                client = Client(account_sid, auth_token)
                
                with st.spinner("Sending WhatsApp message..."):
                    sent_msg = client.messages.create(
                        body=message,
                        from_=twilio_whatsapp_from,
                        to=f"whatsapp:{recipient}"
                    )
                
                st.success(f"✅ Message sent successfully! Message SID: {sent_msg.sid}")
                st.balloons()
                
            except ImportError:
                st.error("❌ Twilio library not installed.")
                st.code("pip install twilio")
            except Exception as e:
                st.error(f"❌ Failed to send message: {e}")
                st.info("💡 Make sure the recipient has joined your Twilio WhatsApp sandbox.")

def show_tuple_vs_list_page():
    st.header("📚 Technical Difference Between Tuple and List in Python")
    st.write("Below is a comparison of Python's list and tuple types. This highlights key technical features, performance, and usage distinctions:")
    
    # Data for comparison table
    data = [
        ["Mutability", "Mutable (can change, add, remove items)", "Immutable (cannot change after creation)"],
        ["Syntax", "Square brackets: [ ]", "Parentheses: ( )"],
        ["Methods", "Many built-in methods (append, remove, pop, etc.)", "Fewer methods (count, index only)"],
        ["Performance", "Slightly slower (dynamic & mutable)", "Faster (static & immutable)"],
        ["Memory Usage", "Consumes more memory", "Consumes less memory"],
        ["Hashability", "Not hashable (can't be dict keys)", "Hashable (can be dict keys, if elements are hashable)"],
        ["Use Case", "Data that changes over time", "Fixed data, safer from modification"],
    ]
    
    # Create comparison table
    st.table({
        "Property": [row[0] for row in data],
        "List": [row[1] for row in data],
        "Tuple": [row[2] for row in data],
    })
    
    # Code examples section
    st.markdown("### 💻 Code Examples:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**List Example:**")
        st.code("""
# Creating a list
my_list = [1, 2, 3]

# Modifying list
my_list.append(4)
my_list[0] = 10
print(my_list)  # [10, 2, 3, 4]

# List methods
my_list.remove(2)
my_list.pop()
        """, language="python")
    
    with col2:
        st.markdown("**Tuple Example:**")
        st.code("""
# Creating a tuple
my_tuple = (1, 2, 3)

# Tuples are immutable
# my_tuple[0] = 10  # This would cause an error

# Tuple methods (limited)
count = my_tuple.count(2)
index = my_tuple.index(3)
print(f"Count: {count}, Index: {index}")
        """, language="python")
    
    # Performance comparison
    st.markdown("### ⚡ Performance Comparison:")
    
    if st.button("🔬 Run Performance Test"):
        import time
        
        # List performance test
        start_time = time.time()
        test_list = []
        for i in range(100000):
            test_list.append(i)
        list_time = time.time() - start_time
        
        # Tuple performance test
        start_time = time.time()
        test_tuple = tuple(range(100000))
        tuple_time = time.time() - start_time
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("List Creation Time", f"{list_time:.6f} seconds")
        with col2:
            st.metric("Tuple Creation Time", f"{tuple_time:.6f} seconds")
        
        if tuple_time < list_time:
            st.success("🏆 Tuple is faster for creation!")
        else:
            st.info("📊 Performance may vary based on operation type.")
    
    # Memory usage comparison
    st.markdown("### 🧠 Memory Usage:")
    
    if st.button("📊 Check Memory Usage"):
        import sys
        
        sample_list = [1, 2, 3, 4, 5] * 1000
        sample_tuple = tuple(sample_list)
        
        list_size = sys.getsizeof(sample_list)
        tuple_size = sys.getsizeof(sample_tuple)
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("List Memory", f"{list_size} bytes")
        with col2:
            st.metric("Tuple Memory", f"{tuple_size} bytes")
        
        savings = list_size - tuple_size
        st.info(f"💡 Tuple saves {savings} bytes ({(savings/list_size)*100:.1f}% less memory)")
    
    # When to use what
    st.markdown("### 🎯 When to Use What:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Use Lists When:**")
        st.markdown("""
        - ✅ You need to modify data
        - ✅ Adding/removing elements
        - ✅ Data changes over time
        - ✅ Need list methods (append, remove, etc.)
        - ✅ Working with dynamic collections
        """)
    
    with col2:
        st.markdown("**Use Tuples When:**")
        st.markdown("""
        - ✅ Data should not change
        - ✅ Need better performance
        - ✅ Want to save memory
        - ✅ Using as dictionary keys
        - ✅ Returning multiple values from functions
        """)

def show_machine_learning_page():
    st.header("🤖 Machine Learning Tasks")
    
    # ML tasks with their corresponding LinkedIn URLs
    ml_tasks = {
        "Find different techniques of data imputation": "https://www.linkedin.com/posts/dipesh-lamba-121660372_linuxworld-machinelearning-activity-7356662522415878144-Xu3D?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFxKDqkB5LdbuI7TC4DZ7GhWEz_os1OLPLs",
        "Find what happens to the weight of dropped category in categorical variable": "https://www.linkedin.com/posts/dipesh-lamba-121660372_when-you-drop-a-category-from-a-categorical-activity-7356670241491353600-Xy92?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFxKDqkB5LdbuI7TC4DZ7GhWEz_os1OLPLs",
        "Search about different initializers and their use cases & create a blog of it": "https://www.linkedin.com/posts/dipesh-lamba-121660372_linuxworld-vimaldaga-aryacollege-activity-7356694702659674112-JBl9?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFxKDqkB5LdbuI7TC4DZ7GhWEz_os1OLPLs",
        "Find an LLM model, try to find its API and find out its internal structure like layers, neurons, activation functions. Try to create your own LLM model": "https://www.linkedin.com/posts/dipesh-lamba-121660372_ai-machinelearning-gemini-activity-7356704349084913665-nyi7?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFxKDqkB5LdbuI7TC4DZ7GhWEz_os1OLPLs",
        "Find the use cases of optimizers & create a blog of it": "https://www.linkedin.com/posts/dipesh-lamba-121660372_linuxworld-machinelearning-optimizers-activity-7356681308741242881-oAaw?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFxKDqkB5LdbuI7TC4DZ7GhWEz_os1OLPLs",
        "Find which activation function works with which type of pooling": "https://www.linkedin.com/posts/dipesh-lamba-121660372_linuxworld-vimaldaga-machinelearning-activity-7356690641055031296-SDP3?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFxKDqkB5LdbuI7TC4DZ7GhWEz_os1OLPLs"
    }
    
    selected_task = st.selectbox("Select ML Task:", list(ml_tasks.keys()))
    
    if st.button("🚀 Execute ML Task", type="primary"):
        st.info(f"Executing: {selected_task}")
        
        with st.spinner("Processing ML task..."):
            import time
            time.sleep(2)  # Simulate processing time
        
        st.success("✅ Machine Learning task completed!")
        
        # Display LinkedIn URL if available
        linkedin_url = ml_tasks[selected_task]
        if linkedin_url:
            st.markdown("---")
            st.subheader("📎 Related LinkedIn Post")
            st.markdown(f"🔗 **LinkedIn Reference:** [View Post]({linkedin_url})")
            st.info("💡 Click the link above to view the detailed LinkedIn post about this topic.")
        else:
            st.info("📝 LinkedIn URL will be added soon for this task.")
        
        # Add task-specific information
        if "data imputation" in selected_task.lower():
            st.markdown("### 📊 Data Imputation Techniques Overview:")
            st.markdown("""
            - **Mean/Median/Mode Imputation**: Replace missing values with statistical measures
            - **Forward/Backward Fill**: Use previous/next values in time series
            - **KNN Imputation**: Use k-nearest neighbors to estimate missing values
            - **Multiple Imputation**: Create multiple datasets with different imputed values
            - **Model-based Imputation**: Use ML models to predict missing values
            """)
        
        elif "categorical variable" in selected_task.lower():
            st.markdown("### 🏷️ Categorical Variable Weight Analysis:")
            st.markdown("""
            - **One-Hot Encoding**: Creates binary columns for each category
            - **Label Encoding**: Assigns numerical values to categories
            - **Target Encoding**: Uses target variable statistics
            - **Weight of Evidence**: Measures relationship with target variable
            """)
        
        elif "initializers" in selected_task.lower():
            st.markdown("### ⚡ Neural Network Initializers:")
            st.markdown("""
            - **Xavier/Glorot**: Good for sigmoid/tanh activations
            - **He Initialization**: Optimal for ReLU activations
            - **LeCun**: Suitable for SELU activations
            - **Random Normal/Uniform**: Basic random initialization
            """)
        
        elif "llm model" in selected_task.lower():
            st.markdown("### 🧠 LLM Model Structure:")
            st.markdown("""
            - **Transformer Architecture**: Attention mechanisms and layers
            - **Embedding Layers**: Convert tokens to vectors
            - **Multi-Head Attention**: Parallel attention computations
            - **Feed-Forward Networks**: Dense layers for processing
            - **Popular APIs**: OpenAI, Hugging Face, Anthropic
            """)
        
        elif "optimizers" in selected_task.lower():
            st.markdown("### 🎯 Optimization Algorithms:")
            st.markdown("""
            - **SGD**: Simple gradient descent with momentum
            - **Adam**: Adaptive learning rates with momentum
            - **RMSprop**: Adaptive learning rates
            - **AdaGrad**: Accumulates squared gradients
            - **AdamW**: Adam with weight decay
            """)
        
        elif "activation function" in selected_task.lower():
            st.markdown("### 🔄 Activation Functions & Pooling:")
            st.markdown("""
            - **ReLU + Max Pooling**: Most common combination
            - **Sigmoid + Average Pooling**: Smooth transitions
            - **Tanh + Max Pooling**: Centered outputs
            - **Leaky ReLU + Max Pooling**: Prevents dead neurons
            """)
        
        st.balloons()

def show_linux_page():
    st.header("🐧 Linux Operations")
    
    # Linux tasks with their corresponding LinkedIn URLs (to be added)
    linux_tasks = {
        "Write a blog post on companies using Linux: Explain why they are using it and what benefits they are getting": "https://www.linkedin.com/posts/dipesh-lamba-121660372_linux-opensource-cloudcomputing-activity-7359613333030772737-m5pU?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFxKDqkB5LdbuI7TC4DZ7GhWEz_os1OLPLs",
        "Choose 5 GUI programs in Linux and find out the commands working behind them": "https://www.linkedin.com/posts/dipesh-lamba-121660372_linux-opensource-commandline-activity-7359621666915663872-yBYS?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFxKDqkB5LdbuI7TC4DZ7GhWEz_os1OLPLs",
        "Change the logo or icon of any program in Linux: Learn how to modify icons or logos for Linux applications": "https://www.linkedin.com/posts/dipesh-lamba-121660372_linux-icons-customization-activity-7350172780555866113-eneL?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFxKDqkB5LdbuI7TC4DZ7GhWEz_os1OLPLs",
        "Add more terminals and GUI interfaces in Linux: Explore methods to enhance terminal and GUI experiences in Linux": "https://www.linkedin.com/posts/dipesh-lamba-121660372_linux-productivity-opensource-activity-7359801296964440064-Hnmu?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFxKDqkB5LdbuI7TC4DZ7GhWEz_os1OLPLs",
        "Send an email, WhatsApp message, tweet, and SMS through the Linux terminal: Use command-line tools to perform these communication tasks": "https://www.linkedin.com/posts/dipesh-lamba-121660372_linux-commandline-automation-activity-7359626484476440576-mFoj?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFxKDqkB5LdbuI7TC4DZ7GhWEz_os1OLPLs",
        "Find the command working behind the Ctrl+C and Ctrl+Z interrupt signals: Investigate how Linux handles process control with these shortcuts": "https://www.linkedin.com/posts/dipesh-lamba-121660372_linux-processcontrol-ctrlc-activity-7359623734703312896-xYtz?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFxKDqkB5LdbuI7TC4DZ7GhWEz_os1OLPLs"
    }
    
    selected_task = st.selectbox("Select Linux Task:", list(linux_tasks.keys()))
    
    if st.button("🚀 Execute Linux Task", type="primary"):
        st.info(f"Executing: {selected_task}")
        
        with st.spinner("Processing Linux task..."):
            import time
            time.sleep(2)  # Simulate processing time
        
        st.success("✅ Linux task completed!")
        
        # Display LinkedIn URL if available
        linkedin_url = linux_tasks[selected_task]
        if linkedin_url:
            st.markdown("---")
            st.subheader("📎 Related LinkedIn Post")
            st.markdown(f"🔗 **LinkedIn Reference:** [View Post]({linkedin_url})")
            st.info("💡 Click the link above to view the detailed LinkedIn post about this topic.")
        else:
            st.info("📝 LinkedIn URL will be added soon for this task.")
        
        # Add task-specific solutions
        if "companies using linux" in selected_task.lower():
            st.markdown("### 🏢 Companies Using Linux - Benefits & Use Cases:")
            st.markdown("""
            **Major Companies Using Linux:**
            - **Google**: Android OS, servers, cloud infrastructure
            - **Amazon**: AWS cloud services, Kindle devices
            - **Facebook/Meta**: Server infrastructure, data centers
            - **Netflix**: Content delivery, streaming infrastructure
            - **Tesla**: In-car entertainment systems
            - **IBM**: Red Hat Enterprise Linux, mainframes
            
            **Key Benefits:**
            - 💰 **Cost-effective**: No licensing fees
            - 🔒 **Security**: Open-source transparency, fewer vulnerabilities
            - ⚡ **Performance**: Optimized for servers and embedded systems
            - 🔧 **Customization**: Full control over system configuration
            - 📈 **Scalability**: Handles enterprise-level workloads
            - 🌐 **Community Support**: Large developer community
            """)
            
        elif "gui programs" in selected_task.lower():
            st.markdown("### 🖥️ GUI Programs & Their Command-Line Equivalents:")
            st.markdown("""
            **5 Popular GUI Programs & Commands:**
            
            1. **File Manager (Nautilus/Dolphin)**
               - Command: `ls`, `cd`, `cp`, `mv`, `rm`
               - Example: `ls -la /home/user/Documents`
            
            2. **Text Editor (gedit/Kate)**
               - Command: `nano`, `vim`, `emacs`
               - Example: `nano filename.txt`
            
            3. **System Monitor (GNOME System Monitor)**
               - Command: `top`, `htop`, `ps`, `kill`
               - Example: `htop` or `ps aux | grep process_name`
            
            4. **Network Manager (NetworkManager GUI)**
               - Command: `nmcli`, `iwconfig`, `ifconfig`
               - Example: `nmcli device wifi list`
            
            5. **Software Center (GNOME Software)**
               - Command: `apt`, `yum`, `dnf`, `pacman`
               - Example: `sudo apt install package_name`
            """)
            
        elif "change the logo" in selected_task.lower():
            st.markdown("### 🎨 Changing Application Icons/Logos in Linux:")
            st.markdown("""
            **Methods to Change Application Icons:**
            
            **Method 1: Using Desktop Files**
            ```bash
            # Edit the .desktop file
            sudo nano /usr/share/applications/app_name.desktop
            
            # Change the Icon line
            Icon=/path/to/new/icon.png
            ```
            
            **Method 2: Using Icon Themes**
            ```bash
            # Install icon theme
            sudo apt install papirus-icon-theme
            
            # Apply via Settings > Appearance > Icons
            ```
            
            **Method 3: Manual Icon Replacement**
            ```bash
            # Find current icon location
            find /usr/share/icons -name "app_icon*"
            
            # Replace with new icon
            sudo cp new_icon.png /usr/share/icons/theme/apps/48/app_name.png
            
            # Update icon cache
            sudo gtk-update-icon-cache /usr/share/icons/theme/
            ```
            
            **Method 4: Using GIMP/Inkscape**
            - Create custom icons in PNG/SVG format
            - Standard sizes: 16x16, 24x24, 32x32, 48x48, 64x64, 128x128
            """)
            
        elif "terminals and gui" in selected_task.lower():
            st.markdown("### 🖥️ Adding More Terminals & GUI Interfaces:")
            st.markdown("""
            **Popular Terminal Emulators:**
            ```bash
            # Install different terminals
            sudo apt install terminator        # Multi-pane terminal
            sudo apt install tilix            # Tiling terminal
            sudo apt install alacritty        # GPU-accelerated terminal
            sudo apt install kitty            # Modern terminal
            sudo apt install guake           # Drop-down terminal
            ```
            
            **Desktop Environments & Window Managers:**
            ```bash
            # Install different DEs
            sudo apt install kde-plasma-desktop    # KDE Plasma
            sudo apt install xfce4                # XFCE
            sudo apt install lxde                 # LXDE
            sudo apt install i3                   # i3 Window Manager
            sudo apt install openbox             # Openbox WM
            ```
            
            **Terminal Multiplexers:**
            ```bash
            # Install terminal multiplexers
            sudo apt install tmux             # Terminal multiplexer
            sudo apt install screen           # GNU Screen
            
            # Basic tmux usage
            tmux new-session -s mysession
            tmux attach-session -t mysession
            ```
            
            **GUI Enhancement Tools:**
            ```bash
            sudo apt install conky           # System monitor widget
            sudo apt install plank           # Dock application
            sudo apt install cairo-dock      # 3D dock
            ```
            """)
            
        elif "email, whatsapp" in selected_task.lower():
            st.markdown("### 📱 Command-Line Communication Tools:")
            st.markdown("""
            **Email via Terminal:**
            ```bash
            # Install mail utilities
            sudo apt install mailutils ssmtp
            
            # Send email using mail command
            echo "Message body" | mail -s "Subject" recipient@email.com
            
            # Using mutt (advanced email client)
            sudo apt install mutt
            echo "Message" | mutt -s "Subject" recipient@email.com
            ```
            
            **SMS via Terminal:**
            ```bash
            # Using Twilio CLI
            npm install -g twilio-cli
            twilio phone-numbers:update +1234567890 --sms-url http://demo.twilio.com/docs/sms.xml
            
            # Using curl with SMS API
            curl -X POST https://api.twilio.com/2010-04-01/Accounts/ACCOUNT_SID/Messages.json \\
                --data-urlencode "From=+1234567890" \\
                --data-urlencode "Body=Hello from Linux!" \\
                --data-urlencode "To=+0987654321" \\
                -u ACCOUNT_SID:AUTH_TOKEN
            ```
            
            **Twitter via Terminal:**
            ```bash
            # Install t (Twitter CLI)
            gem install t
            
            # Authenticate and tweet
            t authorize
            t update "Hello from Linux terminal!"
            ```
            
            **WhatsApp via Terminal:**
            ```bash
            # Using whatsapp-web.js with Node.js
            npm install whatsapp-web.js
            
            # Python alternative with pywhatkit
            pip install pywhatkit
            python3 -c "import pywhatkit; pywhatkit.sendwhatmsg('+1234567890', 'Hello!', 15, 30)"
            ```
            """)
            
        elif "ctrl+c and ctrl+z" in selected_task.lower():
            st.markdown("### ⌨️ Linux Process Control Signals:")
            st.markdown("""
            **Understanding Ctrl+C and Ctrl+Z:**
            
            **Ctrl+C (SIGINT - Signal Interrupt):**
            ```bash
            # Sends SIGINT signal (signal number 2)
            # Equivalent command:
            kill -2 <process_id>
            kill -INT <process_id>
            
            # What happens:
            # - Requests process termination
            # - Process can handle or ignore the signal
            # - Default action: terminate the process
            ```
            
            **Ctrl+Z (SIGTSTP - Signal Terminal Stop):**
            ```bash
            # Sends SIGTSTP signal (signal number 20)
            # Equivalent command:
            kill -20 <process_id>
            kill -TSTP <process_id>
            
            # What happens:
            # - Suspends (pauses) the process
            # - Process goes to background (stopped state)
            # - Can be resumed later
            ```
            
            **Process Control Commands:**
            ```bash
            # View suspended jobs
            jobs
            
            # Resume job in foreground
            fg %1
            
            # Resume job in background
            bg %1
            
            # Kill suspended job
            kill %1
            
            # View all signals
            kill -l
            
            # Send custom signals
            kill -TERM <pid>    # Graceful termination
            kill -KILL <pid>    # Force kill (cannot be ignored)
            kill -STOP <pid>    # Stop process
            kill -CONT <pid>    # Continue stopped process
            ```
            
            **Signal Handling in Programs:**
            ```c
            // C example of signal handling
            #include <signal.h>
            
            void signal_handler(int sig) {
                printf("Received signal %d\\n", sig);
            }
            
            int main() {
                signal(SIGINT, signal_handler);  // Handle Ctrl+C
                signal(SIGTSTP, signal_handler); // Handle Ctrl+Z
                // ... rest of program
            }
            ```
            """)
        
        st.balloons()

if __name__ == "__main__":
    main()
