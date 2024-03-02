# pip install inference
# for bash: export ROBOFLOW_API_KEY=<api key>
# for windows: set ROBOFLOW_API_KEY=<api key>
# Import the InferencePipeline object
from inference import InferencePipeline

# Import the built in render_boxes sink for visualizing results
from inference.core.interfaces.stream.sinks import render_boxes

# initialize a pipeline object
pipeline = InferencePipeline.init(
    model_id="asl-alphabet-recognition/7",  # Roboflow model to use
    video_reference=0,  # Path to video, device id (int, usually 0 for built in webcams), or RTSP stream url
    on_prediction=render_boxes,  # Function to run after each prediction
)
pipeline.start()
pipeline.join()
