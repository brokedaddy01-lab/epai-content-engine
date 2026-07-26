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


class ProductionBrain:


    def __init__(self):

        self.formatter = FormatterAgent()

        self.image = ImageAgent()

        self.video = VideoScriptAgent()

        self.carousel = CarouselAgent()

        self.newsletter = NewsletterAgent()

        self.thumbnail = ThumbnailAgent()

        self.repurpose = RepurposeAgent()



    ##################################################
    # FORMAT CONTENT
    ##################################################

    def format(

        self,

        content,

        platform

    ):

        return (

            self.formatter
            .format(

                content,

                platform

            )

        )



    ##################################################
    # IMAGE PROMPT
    ##################################################

    def image_prompt(

        self,

        content

    ):

        return (

            self.image
            .generate_prompt(

                content

            )

        )



    ##################################################
    # VIDEO SCRIPT
    ##################################################

    def video_script(

        self,

        content

    ):

        return (

            self.video
            .generate(

                content

            )

        )



    ##################################################
    # CAROUSEL
    ##################################################

    def carousel_content(

        self,

        topic

    ):

        return (

            self.carousel
            .generate(

                topic

            )

        )



    ##################################################
    # NEWSLETTER
    ##################################################

    def newsletter_content(

        self,

        content

    ):

        return (

            self.newsletter
            .generate(

                content

            )

        )



    ##################################################
    # THUMBNAIL
    ##################################################

    def thumbnail_content(

        self,

        content

    ):

        return (

            self.thumbnail
            .generate(

                content

            )

        )



    ##################################################
    # REPURPOSE
    ##################################################

    def repurpose_content(

        self,

        content

    ):

        return (

            self.repurpose
            .generate(

                content

            )

        )



    ##################################################
    # COMPLETE ASSET PACKAGE
    ##################################################

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

                )

        }