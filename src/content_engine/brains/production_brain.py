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


class ProductionBrain:


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



    def format(

        self,

        content,

        platform

    ):

        return self.formatter.format(
            content,
            platform
        )



    def image_prompt(

        self,

        content

    ):

        return self.image.generate_prompt(
            content
        )



    def video_script(

        self,

        content

    ):

        return self.video.generate(
            content
        )



    def carousel_content(

        self,

        topic

    ):

        return self.carousel.generate(
            topic
        )



    def newsletter_content(

        self,

        content

    ):

        return self.newsletter.generate(
            content
        )



    def thumbnail_content(

        self,

        content

    ):

        return self.thumbnail.generate(
            content
        )



    def repurpose_content(

        self,

        content

    ):

        return self.repurpose.generate(
            content
        )



    def podcast_content(

        self,

        content

    ):

        return self.podcast.generate(
            content
        )



    def youtube_title_content(

        self,

        content

    ):

        return self.youtube_title.generate(
            content
        )



    def youtube_description_content(

        self,

        content

    ):

        return self.youtube_description.generate(
            content
        )



    def generate_assets(

        self,

        content,

        platform,

        topic

    ):

        return {

            "formatted":

                self.format(
                    content,
                    platform
                ),


            "image_prompt":

                self.image_prompt(
                    content
                ),


            "video_script":

                self.video_script(
                    content
                ),


            "newsletter":

                self.newsletter_content(
                    content
                ),


            "carousel":

                self.carousel_content(
                    topic
                ),


            "thumbnail":

                self.thumbnail_content(
                    content
                ),


            "repurposed":

                self.repurpose_content(
                    content
                ),


            "podcast":

                self.podcast_content(
                    content
                ),


            "youtube_title":

                self.youtube_title_content(
                    content
                ),


            "youtube_description":

                self.youtube_description_content(
                    content
                )

        }