import streamlit as st

def main():
    st.title("Lane Monitoring System")

    st.header("Video Demonstration")

    st.write("The videos below demonstrate the results of the YOLO NAS model in action.")
    st.write("The first video shows the original input video, while the second video displays the predicted results.")

    # Define paths to videos
    video1_path = "original_video.mp4"
    video2_path = "prediction_video.mp4"

    # Display videos side by side
    col1, col2 = st.columns(2)
    with col1:
        st.header("Original Video")
        video_file = open('original_video.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)
        # st.video(open(video1_path, 'rb').read(), format='video/mp4', start_time=0)

    with col2:
        st.header("Predicted Video")
        # video_file = open('prediction_video.mp4', 'rb')
        video_file = open('alt_prediction_video.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)
        # st.video(open(video2_path, 'rb').read(), format='video/mp4', start_time=0)

    # Display links as clickable URLs
    st.write("\n\n**Links:**")
    st.markdown("- [Dataset](https://www.kaggle.com/datasets/pranayobla/lane-monitoring)")
    st.markdown("- [Notebook](https://www.kaggle.com/code/pranayobla/lane-monitoring-yolonas/notebook)")

if __name__ == "__main__":
    main()
