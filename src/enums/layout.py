"""
WARNING: THIS FILE IS AUTOMATICALLY GENERATED FROM _gen_everything.py
"""
from enum import Enum

class Container(Enum):
    """A component for fixing an element's width to the current breakpoint.
    Tailwind documentation URL: https://tailwindcss.com/docs/container"""
    CONTAINER = "container"


class BoxDecorationBreak(Enum):
    """Utilities for controlling how element fragments should be rendered across multiple lines, columns, or pages.
    Tailwind documentation URL: https://tailwindcss.com/docs/box-decoration-break"""
    DECORATION_SLICE = "decoration-slice"
    DECORATION_CLONE = "decoration-clone"


class BoxSizing(Enum):
    """Utilities for controlling how the browser should calculate an element's total size.
    Tailwind documentation URL: https://tailwindcss.com/docs/box-sizing"""
    BOX_BORDER = "box-border"
    BOX_CONTENT = "box-content"


class Display(Enum):
    """Utilities for controlling the display box type of an element.
    Tailwind documentation URL: https://tailwindcss.com/docs/display"""
    BLOCK = "block"
    INLINE_BLOCK = "inline-block"
    INLINE = "inline"
    FLEX = "flex"
    INLINE_FLEX = "inline-flex"
    TABLE = "table"
    INLINE_TABLE = "inline-table"
    TABLE_CAPTION = "table-caption"
    TABLE_CELL = "table-cell"
    TABLE_COLUMN = "table-column"
    TABLE_COLUMN_GROUP = "table-column-group"
    TABLE_FOOTER_GROUP = "table-footer-group"
    TABLE_HEADER_GROUP = "table-header-group"
    TABLE_ROW_GROUP = "table-row-group"
    TABLE_ROW = "table-row"
    FLOW_ROOT = "flow-root"
    GRID = "grid"
    INLINE_GRID = "inline-grid"
    CONTENTS = "contents"
    LIST_ITEM = "list-item"
    HIDDEN = "hidden"


class Float(Enum):
    """Utilities for controlling the wrapping of content around an element.
    Tailwind documentation URL: https://tailwindcss.com/docs/float"""
    FLOAT_RIGHT = "float-right"
    FLOAT_LEFT = "float-left"
    FLOAT_NONE = "float-none"


class Clear(Enum):
    """Utilities for controlling the wrapping of content around an element.
    Tailwind documentation URL: https://tailwindcss.com/docs/clear"""
    CLEAR_LEFT = "clear-left"
    CLEAR_RIGHT = "clear-right"
    CLEAR_BOTH = "clear-both"
    CLEAR_NONE = "clear-none"


class Isolation(Enum):
    """Utilities for controlling whether an element should explicitly create a new stacking context.
    Tailwind documentation URL: https://tailwindcss.com/docs/isolation"""
    ISOLATE = "isolate"
    ISOLATION_AUTO = "isolation-auto"


class ObjectFit(Enum):
    """Utilities for controlling how a replaced element's content should be resized.
    Tailwind documentation URL: https://tailwindcss.com/docs/object-fit"""
    OBJECT_CONTAIN = "object-contain"
    OBJECT_COVER = "object-cover"
    OBJECT_FILL = "object-fill"
    OBJECT_NONE = "object-none"
    OBJECT_SCALE_DOWN = "object-scale-down"


class ObjectPosition(Enum):
    """Utilities for controlling how a replaced element's content should be positioned within its container.
    Tailwind documentation URL: https://tailwindcss.com/docs/object-position"""
    OBJECT_BOTTOM = "object-bottom"
    OBJECT_CENTER = "object-center"
    OBJECT_LEFT = "object-left"
    OBJECT_LEFT_BOTTOM = "object-left-bottom"
    OBJECT_LEFT_TOP = "object-left-top"
    OBJECT_RIGHT = "object-right"
    OBJECT_RIGHT_BOTTOM = "object-right-bottom"
    OBJECT_RIGHT_TOP = "object-right-top"
    OBJECT_TOP = "object-top"


class Overflow(Enum):
    """Utilities for controlling how an element handles content that is too large for the container.
    Tailwind documentation URL: https://tailwindcss.com/docs/overflow"""
    OVERFLOW_AUTO = "overflow-auto"
    OVERFLOW_HIDDEN = "overflow-hidden"
    OVERFLOW_VISIBLE = "overflow-visible"
    OVERFLOW_SCROLL = "overflow-scroll"
    OVERFLOW_X_AUTO = "overflow-x-auto"
    OVERFLOW_Y_AUTO = "overflow-y-auto"
    OVERFLOW_X_HIDDEN = "overflow-x-hidden"
    OVERFLOW_Y_HIDDEN = "overflow-y-hidden"
    OVERFLOW_X_VISIBLE = "overflow-x-visible"
    OVERFLOW_Y_VISIBLE = "overflow-y-visible"
    OVERFLOW_X_SCROLL = "overflow-x-scroll"
    OVERFLOW_Y_SCROLL = "overflow-y-scroll"


class OverscrollBehavior(Enum):
    """Utilities for controlling how the browser behaves when reaching the boundary of a scrolling area.
    Tailwind documentation URL: https://tailwindcss.com/docs/overscroll-behavior"""
    OVERSCROLL_AUTO = "overscroll-auto"
    OVERSCROLL_CONTAIN = "overscroll-contain"
    OVERSCROLL_NONE = "overscroll-none"
    OVERSCROLL_Y_AUTO = "overscroll-y-auto"
    OVERSCROLL_Y_CONTAIN = "overscroll-y-contain"
    OVERSCROLL_Y_NONE = "overscroll-y-none"
    OVERSCROLL_X_AUTO = "overscroll-x-auto"
    OVERSCROLL_X_CONTAIN = "overscroll-x-contain"
    OVERSCROLL_X_NONE = "overscroll-x-none"


class Position(Enum):
    """Utilities for controlling how an element is positioned in the DOM.
    Tailwind documentation URL: https://tailwindcss.com/docs/position"""
    STATIC = "static"
    FIXED = "fixed"
    ABSOLUTE = "absolute"
    RELATIVE = "relative"
    STICKY = "sticky"


class TopRightBottomLeft(Enum):
    """Utilities for controlling the placement of positioned elements.
    Tailwind documentation URL: https://tailwindcss.com/docs/top-right-bottom-left"""
    INSET_0 = "inset-0"
    _INSET_0 = "-inset-0"
    INSET_X_0 = "inset-x-0"
    _INSET_X_0 = "-inset-x-0"
    INSET_Y_0 = "inset-y-0"
    _INSET_Y_0 = "-inset-y-0"
    TOP_0 = "top-0"
    _TOP_0 = "-top-0"
    RIGHT_0 = "right-0"
    _RIGHT_0 = "-right-0"
    BOTTOM_0 = "bottom-0"
    _BOTTOM_0 = "-bottom-0"
    LEFT_0 = "left-0"
    _LEFT_0 = "-left-0"
    INSET_PX = "inset-px"
    _INSET_PX = "-inset-px"
    INSET_X_PX = "inset-x-px"
    _INSET_X_PX = "-inset-x-px"
    INSET_Y_PX = "inset-y-px"
    _INSET_Y_PX = "-inset-y-px"
    TOP_PX = "top-px"
    _TOP_PX = "-top-px"
    RIGHT_PX = "right-px"
    _RIGHT_PX = "-right-px"
    BOTTOM_PX = "bottom-px"
    _BOTTOM_PX = "-bottom-px"
    LEFT_PX = "left-px"
    _LEFT_PX = "-left-px"
    INSET_0_5 = "inset-0.5"
    _INSET_0_5 = "-inset-0.5"
    INSET_X_0_5 = "inset-x-0.5"
    _INSET_X_0_5 = "-inset-x-0.5"
    INSET_Y_0_5 = "inset-y-0.5"
    _INSET_Y_0_5 = "-inset-y-0.5"
    TOP_0_5 = "top-0.5"
    _TOP_0_5 = "-top-0.5"
    RIGHT_0_5 = "right-0.5"
    _RIGHT_0_5 = "-right-0.5"
    BOTTOM_0_5 = "bottom-0.5"
    _BOTTOM_0_5 = "-bottom-0.5"
    LEFT_0_5 = "left-0.5"
    _LEFT_0_5 = "-left-0.5"
    INSET_1 = "inset-1"
    _INSET_1 = "-inset-1"
    INSET_X_1 = "inset-x-1"
    _INSET_X_1 = "-inset-x-1"
    INSET_Y_1 = "inset-y-1"
    _INSET_Y_1 = "-inset-y-1"
    TOP_1 = "top-1"
    _TOP_1 = "-top-1"
    RIGHT_1 = "right-1"
    _RIGHT_1 = "-right-1"
    BOTTOM_1 = "bottom-1"
    _BOTTOM_1 = "-bottom-1"
    LEFT_1 = "left-1"
    _LEFT_1 = "-left-1"
    INSET_1_5 = "inset-1.5"
    _INSET_1_5 = "-inset-1.5"
    INSET_X_1_5 = "inset-x-1.5"
    _INSET_X_1_5 = "-inset-x-1.5"
    INSET_Y_1_5 = "inset-y-1.5"
    _INSET_Y_1_5 = "-inset-y-1.5"
    TOP_1_5 = "top-1.5"
    _TOP_1_5 = "-top-1.5"
    RIGHT_1_5 = "right-1.5"
    _RIGHT_1_5 = "-right-1.5"
    BOTTOM_1_5 = "bottom-1.5"
    _BOTTOM_1_5 = "-bottom-1.5"
    LEFT_1_5 = "left-1.5"
    _LEFT_1_5 = "-left-1.5"
    INSET_2 = "inset-2"
    _INSET_2 = "-inset-2"
    INSET_X_2 = "inset-x-2"
    _INSET_X_2 = "-inset-x-2"
    INSET_Y_2 = "inset-y-2"
    _INSET_Y_2 = "-inset-y-2"
    TOP_2 = "top-2"
    _TOP_2 = "-top-2"
    RIGHT_2 = "right-2"
    _RIGHT_2 = "-right-2"
    BOTTOM_2 = "bottom-2"
    _BOTTOM_2 = "-bottom-2"
    LEFT_2 = "left-2"
    _LEFT_2 = "-left-2"
    INSET_2_5 = "inset-2.5"
    _INSET_2_5 = "-inset-2.5"
    INSET_X_2_5 = "inset-x-2.5"
    _INSET_X_2_5 = "-inset-x-2.5"
    INSET_Y_2_5 = "inset-y-2.5"
    _INSET_Y_2_5 = "-inset-y-2.5"
    TOP_2_5 = "top-2.5"
    _TOP_2_5 = "-top-2.5"
    RIGHT_2_5 = "right-2.5"
    _RIGHT_2_5 = "-right-2.5"
    BOTTOM_2_5 = "bottom-2.5"
    _BOTTOM_2_5 = "-bottom-2.5"
    LEFT_2_5 = "left-2.5"
    _LEFT_2_5 = "-left-2.5"
    INSET_3 = "inset-3"
    _INSET_3 = "-inset-3"
    INSET_X_3 = "inset-x-3"
    _INSET_X_3 = "-inset-x-3"
    INSET_Y_3 = "inset-y-3"
    _INSET_Y_3 = "-inset-y-3"
    TOP_3 = "top-3"
    _TOP_3 = "-top-3"
    RIGHT_3 = "right-3"
    _RIGHT_3 = "-right-3"
    BOTTOM_3 = "bottom-3"
    _BOTTOM_3 = "-bottom-3"
    LEFT_3 = "left-3"
    _LEFT_3 = "-left-3"
    INSET_3_5 = "inset-3.5"
    _INSET_3_5 = "-inset-3.5"
    INSET_X_3_5 = "inset-x-3.5"
    _INSET_X_3_5 = "-inset-x-3.5"
    INSET_Y_3_5 = "inset-y-3.5"
    _INSET_Y_3_5 = "-inset-y-3.5"
    TOP_3_5 = "top-3.5"
    _TOP_3_5 = "-top-3.5"
    RIGHT_3_5 = "right-3.5"
    _RIGHT_3_5 = "-right-3.5"
    BOTTOM_3_5 = "bottom-3.5"
    _BOTTOM_3_5 = "-bottom-3.5"
    LEFT_3_5 = "left-3.5"
    _LEFT_3_5 = "-left-3.5"
    INSET_4 = "inset-4"
    _INSET_4 = "-inset-4"
    INSET_X_4 = "inset-x-4"
    _INSET_X_4 = "-inset-x-4"
    INSET_Y_4 = "inset-y-4"
    _INSET_Y_4 = "-inset-y-4"
    TOP_4 = "top-4"
    _TOP_4 = "-top-4"
    RIGHT_4 = "right-4"
    _RIGHT_4 = "-right-4"
    BOTTOM_4 = "bottom-4"
    _BOTTOM_4 = "-bottom-4"
    LEFT_4 = "left-4"
    _LEFT_4 = "-left-4"
    INSET_5 = "inset-5"
    _INSET_5 = "-inset-5"
    INSET_X_5 = "inset-x-5"
    _INSET_X_5 = "-inset-x-5"
    INSET_Y_5 = "inset-y-5"
    _INSET_Y_5 = "-inset-y-5"
    TOP_5 = "top-5"
    _TOP_5 = "-top-5"
    RIGHT_5 = "right-5"
    _RIGHT_5 = "-right-5"
    BOTTOM_5 = "bottom-5"
    _BOTTOM_5 = "-bottom-5"
    LEFT_5 = "left-5"
    _LEFT_5 = "-left-5"
    INSET_6 = "inset-6"
    _INSET_6 = "-inset-6"
    INSET_X_6 = "inset-x-6"
    _INSET_X_6 = "-inset-x-6"
    INSET_Y_6 = "inset-y-6"
    _INSET_Y_6 = "-inset-y-6"
    TOP_6 = "top-6"
    _TOP_6 = "-top-6"
    RIGHT_6 = "right-6"
    _RIGHT_6 = "-right-6"
    BOTTOM_6 = "bottom-6"
    _BOTTOM_6 = "-bottom-6"
    LEFT_6 = "left-6"
    _LEFT_6 = "-left-6"
    INSET_7 = "inset-7"
    _INSET_7 = "-inset-7"
    INSET_X_7 = "inset-x-7"
    _INSET_X_7 = "-inset-x-7"
    INSET_Y_7 = "inset-y-7"
    _INSET_Y_7 = "-inset-y-7"
    TOP_7 = "top-7"
    _TOP_7 = "-top-7"
    RIGHT_7 = "right-7"
    _RIGHT_7 = "-right-7"
    BOTTOM_7 = "bottom-7"
    _BOTTOM_7 = "-bottom-7"
    LEFT_7 = "left-7"
    _LEFT_7 = "-left-7"
    INSET_8 = "inset-8"
    _INSET_8 = "-inset-8"
    INSET_X_8 = "inset-x-8"
    _INSET_X_8 = "-inset-x-8"
    INSET_Y_8 = "inset-y-8"
    _INSET_Y_8 = "-inset-y-8"
    TOP_8 = "top-8"
    _TOP_8 = "-top-8"
    RIGHT_8 = "right-8"
    _RIGHT_8 = "-right-8"
    BOTTOM_8 = "bottom-8"
    _BOTTOM_8 = "-bottom-8"
    LEFT_8 = "left-8"
    _LEFT_8 = "-left-8"
    INSET_9 = "inset-9"
    _INSET_9 = "-inset-9"
    INSET_X_9 = "inset-x-9"
    _INSET_X_9 = "-inset-x-9"
    INSET_Y_9 = "inset-y-9"
    _INSET_Y_9 = "-inset-y-9"
    TOP_9 = "top-9"
    _TOP_9 = "-top-9"
    RIGHT_9 = "right-9"
    _RIGHT_9 = "-right-9"
    BOTTOM_9 = "bottom-9"
    _BOTTOM_9 = "-bottom-9"
    LEFT_9 = "left-9"
    _LEFT_9 = "-left-9"
    INSET_10 = "inset-10"
    _INSET_10 = "-inset-10"
    INSET_X_10 = "inset-x-10"
    _INSET_X_10 = "-inset-x-10"
    INSET_Y_10 = "inset-y-10"
    _INSET_Y_10 = "-inset-y-10"
    TOP_10 = "top-10"
    _TOP_10 = "-top-10"
    RIGHT_10 = "right-10"
    _RIGHT_10 = "-right-10"
    BOTTOM_10 = "bottom-10"
    _BOTTOM_10 = "-bottom-10"
    LEFT_10 = "left-10"
    _LEFT_10 = "-left-10"
    INSET_11 = "inset-11"
    _INSET_11 = "-inset-11"
    INSET_X_11 = "inset-x-11"
    _INSET_X_11 = "-inset-x-11"
    INSET_Y_11 = "inset-y-11"
    _INSET_Y_11 = "-inset-y-11"
    TOP_11 = "top-11"
    _TOP_11 = "-top-11"
    RIGHT_11 = "right-11"
    _RIGHT_11 = "-right-11"
    BOTTOM_11 = "bottom-11"
    _BOTTOM_11 = "-bottom-11"
    LEFT_11 = "left-11"
    _LEFT_11 = "-left-11"
    INSET_12 = "inset-12"
    _INSET_12 = "-inset-12"
    INSET_X_12 = "inset-x-12"
    _INSET_X_12 = "-inset-x-12"
    INSET_Y_12 = "inset-y-12"
    _INSET_Y_12 = "-inset-y-12"
    TOP_12 = "top-12"
    _TOP_12 = "-top-12"
    RIGHT_12 = "right-12"
    _RIGHT_12 = "-right-12"
    BOTTOM_12 = "bottom-12"
    _BOTTOM_12 = "-bottom-12"
    LEFT_12 = "left-12"
    _LEFT_12 = "-left-12"
    INSET_14 = "inset-14"
    _INSET_14 = "-inset-14"
    INSET_X_14 = "inset-x-14"
    _INSET_X_14 = "-inset-x-14"
    INSET_Y_14 = "inset-y-14"
    _INSET_Y_14 = "-inset-y-14"
    TOP_14 = "top-14"
    _TOP_14 = "-top-14"
    RIGHT_14 = "right-14"
    _RIGHT_14 = "-right-14"
    BOTTOM_14 = "bottom-14"
    _BOTTOM_14 = "-bottom-14"
    LEFT_14 = "left-14"
    _LEFT_14 = "-left-14"
    INSET_16 = "inset-16"
    _INSET_16 = "-inset-16"
    INSET_X_16 = "inset-x-16"
    _INSET_X_16 = "-inset-x-16"
    INSET_Y_16 = "inset-y-16"
    _INSET_Y_16 = "-inset-y-16"
    TOP_16 = "top-16"
    _TOP_16 = "-top-16"
    RIGHT_16 = "right-16"
    _RIGHT_16 = "-right-16"
    BOTTOM_16 = "bottom-16"
    _BOTTOM_16 = "-bottom-16"
    LEFT_16 = "left-16"
    _LEFT_16 = "-left-16"
    INSET_20 = "inset-20"
    _INSET_20 = "-inset-20"
    INSET_X_20 = "inset-x-20"
    _INSET_X_20 = "-inset-x-20"
    INSET_Y_20 = "inset-y-20"
    _INSET_Y_20 = "-inset-y-20"
    TOP_20 = "top-20"
    _TOP_20 = "-top-20"
    RIGHT_20 = "right-20"
    _RIGHT_20 = "-right-20"
    BOTTOM_20 = "bottom-20"
    _BOTTOM_20 = "-bottom-20"
    LEFT_20 = "left-20"
    _LEFT_20 = "-left-20"
    INSET_24 = "inset-24"
    _INSET_24 = "-inset-24"
    INSET_X_24 = "inset-x-24"
    _INSET_X_24 = "-inset-x-24"
    INSET_Y_24 = "inset-y-24"
    _INSET_Y_24 = "-inset-y-24"
    TOP_24 = "top-24"
    _TOP_24 = "-top-24"
    RIGHT_24 = "right-24"
    _RIGHT_24 = "-right-24"
    BOTTOM_24 = "bottom-24"
    _BOTTOM_24 = "-bottom-24"
    LEFT_24 = "left-24"
    _LEFT_24 = "-left-24"
    INSET_28 = "inset-28"
    _INSET_28 = "-inset-28"
    INSET_X_28 = "inset-x-28"
    _INSET_X_28 = "-inset-x-28"
    INSET_Y_28 = "inset-y-28"
    _INSET_Y_28 = "-inset-y-28"
    TOP_28 = "top-28"
    _TOP_28 = "-top-28"
    RIGHT_28 = "right-28"
    _RIGHT_28 = "-right-28"
    BOTTOM_28 = "bottom-28"
    _BOTTOM_28 = "-bottom-28"
    LEFT_28 = "left-28"
    _LEFT_28 = "-left-28"
    INSET_32 = "inset-32"
    _INSET_32 = "-inset-32"
    INSET_X_32 = "inset-x-32"
    _INSET_X_32 = "-inset-x-32"
    INSET_Y_32 = "inset-y-32"
    _INSET_Y_32 = "-inset-y-32"
    TOP_32 = "top-32"
    _TOP_32 = "-top-32"
    RIGHT_32 = "right-32"
    _RIGHT_32 = "-right-32"
    BOTTOM_32 = "bottom-32"
    _BOTTOM_32 = "-bottom-32"
    LEFT_32 = "left-32"
    _LEFT_32 = "-left-32"
    INSET_36 = "inset-36"
    _INSET_36 = "-inset-36"
    INSET_X_36 = "inset-x-36"
    _INSET_X_36 = "-inset-x-36"
    INSET_Y_36 = "inset-y-36"
    _INSET_Y_36 = "-inset-y-36"
    TOP_36 = "top-36"
    _TOP_36 = "-top-36"
    RIGHT_36 = "right-36"
    _RIGHT_36 = "-right-36"
    BOTTOM_36 = "bottom-36"
    _BOTTOM_36 = "-bottom-36"
    LEFT_36 = "left-36"
    _LEFT_36 = "-left-36"
    INSET_40 = "inset-40"
    _INSET_40 = "-inset-40"
    INSET_X_40 = "inset-x-40"
    _INSET_X_40 = "-inset-x-40"
    INSET_Y_40 = "inset-y-40"
    _INSET_Y_40 = "-inset-y-40"
    TOP_40 = "top-40"
    _TOP_40 = "-top-40"
    RIGHT_40 = "right-40"
    _RIGHT_40 = "-right-40"
    BOTTOM_40 = "bottom-40"
    _BOTTOM_40 = "-bottom-40"
    LEFT_40 = "left-40"
    _LEFT_40 = "-left-40"
    INSET_44 = "inset-44"
    _INSET_44 = "-inset-44"
    INSET_X_44 = "inset-x-44"
    _INSET_X_44 = "-inset-x-44"
    INSET_Y_44 = "inset-y-44"
    _INSET_Y_44 = "-inset-y-44"
    TOP_44 = "top-44"
    _TOP_44 = "-top-44"
    RIGHT_44 = "right-44"
    _RIGHT_44 = "-right-44"
    BOTTOM_44 = "bottom-44"
    _BOTTOM_44 = "-bottom-44"
    LEFT_44 = "left-44"
    _LEFT_44 = "-left-44"
    INSET_48 = "inset-48"
    _INSET_48 = "-inset-48"
    INSET_X_48 = "inset-x-48"
    _INSET_X_48 = "-inset-x-48"
    INSET_Y_48 = "inset-y-48"
    _INSET_Y_48 = "-inset-y-48"
    TOP_48 = "top-48"
    _TOP_48 = "-top-48"
    RIGHT_48 = "right-48"
    _RIGHT_48 = "-right-48"
    BOTTOM_48 = "bottom-48"
    _BOTTOM_48 = "-bottom-48"
    LEFT_48 = "left-48"
    _LEFT_48 = "-left-48"
    INSET_52 = "inset-52"
    _INSET_52 = "-inset-52"
    INSET_X_52 = "inset-x-52"
    _INSET_X_52 = "-inset-x-52"
    INSET_Y_52 = "inset-y-52"
    _INSET_Y_52 = "-inset-y-52"
    TOP_52 = "top-52"
    _TOP_52 = "-top-52"
    RIGHT_52 = "right-52"
    _RIGHT_52 = "-right-52"
    BOTTOM_52 = "bottom-52"
    _BOTTOM_52 = "-bottom-52"
    LEFT_52 = "left-52"
    _LEFT_52 = "-left-52"
    INSET_56 = "inset-56"
    _INSET_56 = "-inset-56"
    INSET_X_56 = "inset-x-56"
    _INSET_X_56 = "-inset-x-56"
    INSET_Y_56 = "inset-y-56"
    _INSET_Y_56 = "-inset-y-56"
    TOP_56 = "top-56"
    _TOP_56 = "-top-56"
    RIGHT_56 = "right-56"
    _RIGHT_56 = "-right-56"
    BOTTOM_56 = "bottom-56"
    _BOTTOM_56 = "-bottom-56"
    LEFT_56 = "left-56"
    _LEFT_56 = "-left-56"
    INSET_60 = "inset-60"
    _INSET_60 = "-inset-60"
    INSET_X_60 = "inset-x-60"
    _INSET_X_60 = "-inset-x-60"
    INSET_Y_60 = "inset-y-60"
    _INSET_Y_60 = "-inset-y-60"
    TOP_60 = "top-60"
    _TOP_60 = "-top-60"
    RIGHT_60 = "right-60"
    _RIGHT_60 = "-right-60"
    BOTTOM_60 = "bottom-60"
    _BOTTOM_60 = "-bottom-60"
    LEFT_60 = "left-60"
    _LEFT_60 = "-left-60"
    INSET_64 = "inset-64"
    _INSET_64 = "-inset-64"
    INSET_X_64 = "inset-x-64"
    _INSET_X_64 = "-inset-x-64"
    INSET_Y_64 = "inset-y-64"
    _INSET_Y_64 = "-inset-y-64"
    TOP_64 = "top-64"
    _TOP_64 = "-top-64"
    RIGHT_64 = "right-64"
    _RIGHT_64 = "-right-64"
    BOTTOM_64 = "bottom-64"
    _BOTTOM_64 = "-bottom-64"
    LEFT_64 = "left-64"
    _LEFT_64 = "-left-64"
    INSET_72 = "inset-72"
    _INSET_72 = "-inset-72"
    INSET_X_72 = "inset-x-72"
    _INSET_X_72 = "-inset-x-72"
    INSET_Y_72 = "inset-y-72"
    _INSET_Y_72 = "-inset-y-72"
    TOP_72 = "top-72"
    _TOP_72 = "-top-72"
    RIGHT_72 = "right-72"
    _RIGHT_72 = "-right-72"
    BOTTOM_72 = "bottom-72"
    _BOTTOM_72 = "-bottom-72"
    LEFT_72 = "left-72"
    _LEFT_72 = "-left-72"
    INSET_80 = "inset-80"
    _INSET_80 = "-inset-80"
    INSET_X_80 = "inset-x-80"
    _INSET_X_80 = "-inset-x-80"
    INSET_Y_80 = "inset-y-80"
    _INSET_Y_80 = "-inset-y-80"
    TOP_80 = "top-80"
    _TOP_80 = "-top-80"
    RIGHT_80 = "right-80"
    _RIGHT_80 = "-right-80"
    BOTTOM_80 = "bottom-80"
    _BOTTOM_80 = "-bottom-80"
    LEFT_80 = "left-80"
    _LEFT_80 = "-left-80"
    INSET_96 = "inset-96"
    _INSET_96 = "-inset-96"
    INSET_X_96 = "inset-x-96"
    _INSET_X_96 = "-inset-x-96"
    INSET_Y_96 = "inset-y-96"
    _INSET_Y_96 = "-inset-y-96"
    TOP_96 = "top-96"
    _TOP_96 = "-top-96"
    RIGHT_96 = "right-96"
    _RIGHT_96 = "-right-96"
    BOTTOM_96 = "bottom-96"
    _BOTTOM_96 = "-bottom-96"
    LEFT_96 = "left-96"
    _LEFT_96 = "-left-96"
    INSET_AUTO = "inset-auto"
    INSET_1_2 = "inset-1/2"
    INSET_1_3 = "inset-1/3"
    INSET_2_3 = "inset-2/3"
    INSET_1_4 = "inset-1/4"
    INSET_2_4 = "inset-2/4"
    INSET_3_4 = "inset-3/4"
    INSET_FULL = "inset-full"
    _INSET_1_2 = "-inset-1/2"
    _INSET_1_3 = "-inset-1/3"
    _INSET_2_3 = "-inset-2/3"
    _INSET_1_4 = "-inset-1/4"
    _INSET_2_4 = "-inset-2/4"
    _INSET_3_4 = "-inset-3/4"
    _INSET_FULL = "-inset-full"
    INSET_X_AUTO = "inset-x-auto"
    INSET_X_1_2 = "inset-x-1/2"
    INSET_X_1_3 = "inset-x-1/3"
    INSET_X_2_3 = "inset-x-2/3"
    INSET_X_1_4 = "inset-x-1/4"
    INSET_X_2_4 = "inset-x-2/4"
    INSET_X_3_4 = "inset-x-3/4"
    INSET_X_FULL = "inset-x-full"
    _INSET_X_1_2 = "-inset-x-1/2"
    _INSET_X_1_3 = "-inset-x-1/3"
    _INSET_X_2_3 = "-inset-x-2/3"
    _INSET_X_1_4 = "-inset-x-1/4"
    _INSET_X_2_4 = "-inset-x-2/4"
    _INSET_X_3_4 = "-inset-x-3/4"
    _INSET_X_FULL = "-inset-x-full"
    INSET_Y_AUTO = "inset-y-auto"
    INSET_Y_1_2 = "inset-y-1/2"
    INSET_Y_1_3 = "inset-y-1/3"
    INSET_Y_2_3 = "inset-y-2/3"
    INSET_Y_1_4 = "inset-y-1/4"
    INSET_Y_2_4 = "inset-y-2/4"
    INSET_Y_3_4 = "inset-y-3/4"
    INSET_Y_FULL = "inset-y-full"
    _INSET_Y_1_2 = "-inset-y-1/2"
    _INSET_Y_1_3 = "-inset-y-1/3"
    _INSET_Y_2_3 = "-inset-y-2/3"
    _INSET_Y_1_4 = "-inset-y-1/4"
    _INSET_Y_2_4 = "-inset-y-2/4"
    _INSET_Y_3_4 = "-inset-y-3/4"
    _INSET_Y_FULL = "-inset-y-full"
    TOP_AUTO = "top-auto"
    TOP_1_2 = "top-1/2"
    TOP_1_3 = "top-1/3"
    TOP_2_3 = "top-2/3"
    TOP_1_4 = "top-1/4"
    TOP_2_4 = "top-2/4"
    TOP_3_4 = "top-3/4"
    TOP_FULL = "top-full"
    _TOP_1_2 = "-top-1/2"
    _TOP_1_3 = "-top-1/3"
    _TOP_2_3 = "-top-2/3"
    _TOP_1_4 = "-top-1/4"
    _TOP_2_4 = "-top-2/4"
    _TOP_3_4 = "-top-3/4"
    _TOP_FULL = "-top-full"
    RIGHT_AUTO = "right-auto"
    RIGHT_1_2 = "right-1/2"
    RIGHT_1_3 = "right-1/3"
    RIGHT_2_3 = "right-2/3"
    RIGHT_1_4 = "right-1/4"
    RIGHT_2_4 = "right-2/4"
    RIGHT_3_4 = "right-3/4"
    RIGHT_FULL = "right-full"
    _RIGHT_1_2 = "-right-1/2"
    _RIGHT_1_3 = "-right-1/3"
    _RIGHT_2_3 = "-right-2/3"
    _RIGHT_1_4 = "-right-1/4"
    _RIGHT_2_4 = "-right-2/4"
    _RIGHT_3_4 = "-right-3/4"
    _RIGHT_FULL = "-right-full"
    BOTTOM_AUTO = "bottom-auto"
    BOTTOM_1_2 = "bottom-1/2"
    BOTTOM_1_3 = "bottom-1/3"
    BOTTOM_2_3 = "bottom-2/3"
    BOTTOM_1_4 = "bottom-1/4"
    BOTTOM_2_4 = "bottom-2/4"
    BOTTOM_3_4 = "bottom-3/4"
    BOTTOM_FULL = "bottom-full"
    _BOTTOM_1_2 = "-bottom-1/2"
    _BOTTOM_1_3 = "-bottom-1/3"
    _BOTTOM_2_3 = "-bottom-2/3"
    _BOTTOM_1_4 = "-bottom-1/4"
    _BOTTOM_2_4 = "-bottom-2/4"
    _BOTTOM_3_4 = "-bottom-3/4"
    _BOTTOM_FULL = "-bottom-full"
    LEFT_AUTO = "left-auto"
    LEFT_1_2 = "left-1/2"
    LEFT_1_3 = "left-1/3"
    LEFT_2_3 = "left-2/3"
    LEFT_1_4 = "left-1/4"
    LEFT_2_4 = "left-2/4"
    LEFT_3_4 = "left-3/4"
    LEFT_FULL = "left-full"
    _LEFT_1_2 = "-left-1/2"
    _LEFT_1_3 = "-left-1/3"
    _LEFT_2_3 = "-left-2/3"
    _LEFT_1_4 = "-left-1/4"
    _LEFT_2_4 = "-left-2/4"
    _LEFT_3_4 = "-left-3/4"
    _LEFT_FULL = "-left-full"


class Visibility(Enum):
    """Utilities for controlling the visibility of an element.
    Tailwind documentation URL: https://tailwindcss.com/docs/visibility"""
    VISIBLE = "visible"
    INVISIBLE = "invisible"


class ZIndex(Enum):
    """Utilities for controlling the stack order of an element.
    Tailwind documentation URL: https://tailwindcss.com/docs/z-index"""
    Z_0 = "z-0"
    Z_10 = "z-10"
    Z_20 = "z-20"
    Z_30 = "z-30"
    Z_40 = "z-40"
    Z_50 = "z-50"
    Z_AUTO = "z-auto"
