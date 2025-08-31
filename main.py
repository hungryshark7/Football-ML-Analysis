
from utils import read_video, save_video
from trackers.tracker import Tracker 

def main():
    input_video_path = "Input_videos/08fd33_4.mp4"
    output_video_path = "output_videos/output.avi"

    print("Starting football analysis...")
    
    # Read the video
    print("Reading video...")
    output_video_frames = read_video(input_video_path)
    print(f"Loaded {len(output_video_frames)} frames")

    # Initializing the tracker
    print("Initializing tracker...")
    tracker = Tracker('models/best.pt')
    print("Tracker ready")

    tracks = tracker.get_object_tracker(output_video_frames, read_from_stub=True, stub_path='stubs/track_stubs.pkl')

    # Get tracking results
    print("Running object tracking...")
    #tracks = tracker.get_object_tracker(output_video_frames)
    
    # Debug: Check if tracking returned data
    if tracks is None:
        print("Warning: Tracker returned None - check tracker implementation")
        print("Tracking complete - no tracking data returned")
    else:
        print(f"Tracking complete - processed {len(tracks)} frames")

    # Process the frames (this is where processing logic is)
    print("Processing frames...")
    print("Frame processing complete")

    # Save the processed video
    print("Saving video...")
    save_video(output_video_frames, output_video_path)
    print(f"Video saved to {output_video_path}")
    
    print("Analysis complete!")

if __name__ == '__main__':
    main()