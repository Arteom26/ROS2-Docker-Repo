# ~/workspaces/isaac_ros_dev/ros_ws/isaac_ros_common/docker/backend/

import uvicorn

if __name__ == '__main__':
    uvicorn.run("app.api:app", host="0.0.0.0", port=3000, reload=True)

