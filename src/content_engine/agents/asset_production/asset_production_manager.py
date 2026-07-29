from content_engine.agents.asset_production.formatter_agent import (
    FormatterAgent
)

from content_engine.agents.asset_production.image_agent import (
    ImageAgent
)

from content_engine.agents.asset_production.video_script_agent import (
    VideoScriptAgent
)

from content_engine.agents.asset_production.carousel_agent import (
    CarouselAgent
)

from content_engine.agents.asset_production.newsletter_agent import (
    NewsletterAgent
)

from content_engine.agents.asset_production.thumbnail_agent import (
    ThumbnailAgent
)

from content_engine.agents.asset_production.repurpose_agent import (
    RepurposeAgent
)

from content_engine.agents.asset_production.podcast_agent import (
    PodcastAgent
)

from content_engine.agents.asset_production.youtube_title_agent import (
    YouTubeTitleAgent
)

from content_engine.agents.asset_production.youtube_description_agent import (
    YouTubeDescriptionAgent
)

from content_engine.agents.base_manager import BaseManager

class AssetProductionManager(BaseManager):


    def __init__(self):

        self.formatter = FormatterAgent()

        self.image = ImageAgent()

        self.video = VideoScriptAgent()

        self.carousel = CarouselAgent()

        self.newsletter = NewsletterAgent()

        self.thumbnail = ThumbnailAgent()

        self.repurpose = RepurposeAgent()

        self.podcast = PodcastAgent()

        self.youtube_title = YouTubeTitleAgent()

        self.youtube_description = YouTubeDescriptionAgent()


    def generate_assets(
        self,
        content,
        platform,
        topic
    ):

        return {

            "formatted":
                self.formatter.format(
                    content,
                    platform
                ),

            "image_prompt":
                self.image.generate_prompt(
                    content
                ),

            "video_script":
                self.video.generate(
                    content
                ),

            "newsletter":
                self.newsletter.generate(
                    content
                ),

            "carousel":
                self.carousel.generate(
                    topic
                ),

            "thumbnail":
                self.thumbnail.generate(
                    content
                ),

            "repurposed":
                self.repurpose.generate(
                    content
                ),

            "podcast":
                self.podcast.generate(
                    content
                ),

            "youtube_title":
                self.youtube_title.generate(
                    content
                ),

            "youtube_description":
                self.youtube_description.generate(
                    content
                )

        }