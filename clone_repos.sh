#!/bin/bash

# List of repository URLs
repos=(
    "https://github.com/Justin10612/robot_controller_cpp.git"
    "https://github.com/Justin10612/robot_daq.git"
    "https://github.com/Justin10612/human_follower_cpp.git"
    "https://github.com/Justin10612/diffdrive_stm32f446re.git"
    "https://github.com/Justin10612/uwb_localization.git"
    # Add more repositories as needed
)

# Function to clone repository
clone_repo() {
    url=$1
    repo_name=$(basename "$url" .git)
    git clone "$url" "$repo_name"
}

# Loop through each repository and clone in parallel
for repo in "${repos[@]}"; do
    clone_repo "$repo" &
done

# Wait for all background jobs to finish
wait

echo "All repositories cloned successfully!"
