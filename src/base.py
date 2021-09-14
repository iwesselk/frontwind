
#import uuid
from dataclasses import dataclass, field
# Base page input passed to a template.
base_page_template = """<!DOCTYPE html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1" />

{metadata_inject}
{stylesheet_data}
{head_javascript}
</head>
<body>
{body_content}
{body_javascript}
</body>"""


@dataclass(repr=False)
class BaseFrontwind:
    #id: uuid.UUID = field(default_factory=uuid.uuid4)
    def render(self):
        return self.__repr__()
    def __str__(self):
        return self.__repr__()
    def __repr__(self):
        return "NoPageElement"


@dataclass(repr=False)
class JavascriptSnippet(BaseFrontwind):
    src:str = ""
    def __repr__(self):
        return "<script src=\"{src}\">".format(src=self.src)


@dataclass(repr=False)
class Metadata(BaseFrontwind):
    name:str = ""
    content:str = ""
    def __repr__(self):
        return "<meta name={name} content={content}>".format(name=self.name, content=self.content)


@dataclass(repr=False)
class Stylesheet(BaseFrontwind):
    href:str = ""
    def __repr__(self):
        return "<link rel=\"stylesheet\" href=\"{href}\">".format(href=self.href)


@dataclass(repr=False)
class Tag(BaseFrontwind):
    pass


@dataclass(repr=False)
class Width(Tag):
    width_type: str = "0"
    def __repr__(self):
        return "w-{width_type}".format(width_type=self.width_type)


"""
Future method of doing this:
BodyElement(element_type="p", inner_content="blah blah blah", width: Width.w_min)
instead of
BodyElement("h1", "Hello webpage", extra_fanciez=[Width("min")])

also:
Form([Form_Button("Press me", "id_1", width: Width.w_min)], action="target_url", method=Form.POST])
"""
@dataclass(repr=False)
class BodyElement(BaseFrontwind):
    tag: str = ""
    content: str = ""
    is_full_tag: bool = True
    # TODO: Don't be dumb with naming
    extra_fanciez: list[Tag] = field(default_factory=list)
    classes: list[str] = field(default_factory=list)
    def preprocess_classes(self):
        self.classes
        for tag in self.extra_fanciez:
            self.classes.append(tag.render())
    def __repr__(self):
        # Side effect function
        self.preprocess_classes()
        return "<{tag}{class_info} {id}>{content}{tail_add}".format(
                tag=self.tag, 
                content=self.content, 
                class_info = " class=\"{}\"".format(" ".join([tag.render() for tag in self.extra_fanciez])) if len(self.extra_fanciez) > 0 else "",
                tail_add = "</{tag}>".format(tag=self.tag) if self.is_full_tag else "",
                id = "id=\""+str(self.id)+"\"")


@dataclass(repr=False)
class FrontwindPage(BaseFrontwind):
    metadata: list[Metadata] = field(default_factory=list)
    stylesheets: list[Stylesheet] = field(default_factory=list)
    javascript: list[JavascriptSnippet] = field(default_factory=list)
    content: list[BodyElement] = field(default_factory=list)
    body_javascript: list[JavascriptSnippet] = field(default_factory=list)
    tailwind_location: str = "tailwind.css"
    def __repr__(self):
        return base_page_template.format(
            metadata_inject = self.self_to_str(self.metadata),
            stylesheet_data = self.self_to_str(self.stylesheets + [Stylesheet(self.tailwind_location)]),
            head_javascript = self.self_to_str(self.javascript),
            body_content = self.self_to_str(self.content),
            body_javascript = self.self_to_str(self.body_javascript)
            )
    def self_to_str(self, lst):
        return "\n".join([str(thing) for thing in lst])
    # def force_render(self, lst):
    #     all_content = []
    #     for i in lst:
    #         if not isinstance(i, str):
    #             all_content.append(i.render())
    #         else:
    #             all_content.append(i)            

