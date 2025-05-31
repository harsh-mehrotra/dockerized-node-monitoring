import os
import random
import datetime
import git
import schedule
import time
from datetime import timedelta

# Configuration
REPO_PATH = "."  # Path to your GitHub repository (current directory)
FILES_TO_UPDATE = ["README.md", "CHANGELOG.md"]  # Files to make small changes to
COMMIT_MESSAGES = [
    "Update README with minor clarifications",
    "Add entry to changelog",
    "Tweak documentation formatting",
    "Update project notes",
    "Refine README instructions",
]
GITHUB_REMOTE = "origin"
BRANCH = "main"

def initialize_changelog():
    """Create CHANGELOG.md if it doesn't exist."""
    changelog_path = "CHANGELOG.md"
    if not os.path.exists(changelog_path):
        with open(changelog_path, "w") as f:
            f.write("# Changelog\n\n## [Unreleased]\n- Initial setup for streak automation\n")
        print("Initialized CHANGELOG.md")

def update_file():
    """Make a small, realistic change to a random file."""
    try:
        # Initialize changelog if needed
        initialize_changelog()

        # Pick a random file to update
        file_to_update = random.choice(FILES_TO_UPDATE)
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if file_to_update == "README.md":
            # Append a small note to README (e.g., a timestamped update log)
            with open(file_to_update, "a") as f:
                f.write(f"\n\n<!-- Streak update: {current_time} -->")
        elif file_to_update == "CHANGELOG.md":
            # Add a new entry to changelog
            with open(file_to_update, "r") as f:
                content = f.read()
            with open(file_to_update, "w") as f:
                f.write(content.replace("## [Unreleased]", f"## [Unreleased]\n- Updated project docs on {current_time}"))

        # Randomly select a commit message
        commit_message = random.choice(COMMIT_MESSAGES)

        # Git operations
        repo = git.Repo(REPO_PATH)
        repo.git.add(file_to_update)
        repo.git.commit(m=commit_message)
        repo.git.push(GITHUB_REMOTE, BRANCH)
        print(f"[{current_time}] Committed: {commit_message} to {file_to_update}")

    except Exception as e:
        print(f"Error during streak update: {e}")

def schedule_commit():
    """Schedule the next commit at a random time tomorrow."""
    tomorrow = datetime.datetime.now() + timedelta(days=1)
    random_hour = random.randint(9, 18)  # Random hour between 9 AM and 6 PM
    random_minute = random.randint(0, 59)
    run_time = tomorrow.replace(hour=random_hour, minute=random_minute, second=0, microsecond=0)

    schedule.clear()  # Clear previous schedules
    schedule.every().day.at(run_time.strftime("%H:%M")).do(update_file)
    print(f"Scheduled next commit for {run_time}")

def main():
    """Main function to run the streak script."""
    update_file()  # Run immediately for the first commit
    schedule_commit()  # Schedule the next commit

    # Keep the script running to check the schedule
    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    main()