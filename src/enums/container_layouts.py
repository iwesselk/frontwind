"""
WARNING: THIS FILE IS AUTOMATICALLY GENERATED FROM _gen_everything.py
"""
from enum import Enum

class FlexDirection(Enum):
    """Utilities for controlling the direction of flex items.
    Tailwind documentation URL: https://tailwindcss.com/docs/flex-direction"""
    FLEX_ROW = "flex-row"
    FLEX_ROW_REVERSE = "flex-row-reverse"
    FLEX_COL = "flex-col"
    FLEX_COL_REVERSE = "flex-col-reverse"


class FlexWrap(Enum):
    """Utilities for controlling how flex items wrap.
    Tailwind documentation URL: https://tailwindcss.com/docs/flex-wrap"""
    FLEX_WRAP = "flex-wrap"
    FLEX_WRAP_REVERSE = "flex-wrap-reverse"
    FLEX_NOWRAP = "flex-nowrap"


class Flex(Enum):
    """Utilities for controlling how flex items both grow and shrink.
    Tailwind documentation URL: https://tailwindcss.com/docs/flex"""
    FLEX_1 = "flex-1"
    FLEX_AUTO = "flex-auto"
    FLEX_INITIAL = "flex-initial"
    FLEX_NONE = "flex-none"


class FlexGrow(Enum):
    """Utilities for controlling how flex items grow.
    Tailwind documentation URL: https://tailwindcss.com/docs/flex-grow"""
    FLEX_GROW_0 = "flex-grow-0"
    FLEX_GROW = "flex-grow"


class FlexShrink(Enum):
    """Utilities for controlling how flex items shrink.
    Tailwind documentation URL: https://tailwindcss.com/docs/flex-shrink"""
    FLEX_SHRINK_0 = "flex-shrink-0"
    FLEX_SHRINK = "flex-shrink"


class Order(Enum):
    """Utilities for controlling the order of flex and grid items.
    Tailwind documentation URL: https://tailwindcss.com/docs/order"""
    ORDER_1 = "order-1"
    ORDER_2 = "order-2"
    ORDER_3 = "order-3"
    ORDER_4 = "order-4"
    ORDER_5 = "order-5"
    ORDER_6 = "order-6"
    ORDER_7 = "order-7"
    ORDER_8 = "order-8"
    ORDER_9 = "order-9"
    ORDER_10 = "order-10"
    ORDER_11 = "order-11"
    ORDER_12 = "order-12"
    ORDER_FIRST = "order-first"
    ORDER_LAST = "order-last"
    ORDER_NONE = "order-none"


class GridTemplateColumns(Enum):
    """Utilities for specifying the columns in a grid layout.
    Tailwind documentation URL: https://tailwindcss.com/docs/grid-template-columns"""
    GRID_COLS_1 = "grid-cols-1"
    GRID_COLS_2 = "grid-cols-2"
    GRID_COLS_3 = "grid-cols-3"
    GRID_COLS_4 = "grid-cols-4"
    GRID_COLS_5 = "grid-cols-5"
    GRID_COLS_6 = "grid-cols-6"
    GRID_COLS_7 = "grid-cols-7"
    GRID_COLS_8 = "grid-cols-8"
    GRID_COLS_9 = "grid-cols-9"
    GRID_COLS_10 = "grid-cols-10"
    GRID_COLS_11 = "grid-cols-11"
    GRID_COLS_12 = "grid-cols-12"
    GRID_COLS_NONE = "grid-cols-none"


class GridColumn(Enum):
    """Utilities for controlling how elements are sized and placed across grid columns.
    Tailwind documentation URL: https://tailwindcss.com/docs/grid-column"""
    COL_AUTO = "col-auto"
    COL_SPAN_1 = "col-span-1"
    COL_SPAN_2 = "col-span-2"
    COL_SPAN_3 = "col-span-3"
    COL_SPAN_4 = "col-span-4"
    COL_SPAN_5 = "col-span-5"
    COL_SPAN_6 = "col-span-6"
    COL_SPAN_7 = "col-span-7"
    COL_SPAN_8 = "col-span-8"
    COL_SPAN_9 = "col-span-9"
    COL_SPAN_10 = "col-span-10"
    COL_SPAN_11 = "col-span-11"
    COL_SPAN_12 = "col-span-12"
    COL_SPAN_FULL = "col-span-full"
    COL_START_1 = "col-start-1"
    COL_START_2 = "col-start-2"
    COL_START_3 = "col-start-3"
    COL_START_4 = "col-start-4"
    COL_START_5 = "col-start-5"
    COL_START_6 = "col-start-6"
    COL_START_7 = "col-start-7"
    COL_START_8 = "col-start-8"
    COL_START_9 = "col-start-9"
    COL_START_10 = "col-start-10"
    COL_START_11 = "col-start-11"
    COL_START_12 = "col-start-12"
    COL_START_13 = "col-start-13"
    COL_START_AUTO = "col-start-auto"
    COL_END_1 = "col-end-1"
    COL_END_2 = "col-end-2"
    COL_END_3 = "col-end-3"
    COL_END_4 = "col-end-4"
    COL_END_5 = "col-end-5"
    COL_END_6 = "col-end-6"
    COL_END_7 = "col-end-7"
    COL_END_8 = "col-end-8"
    COL_END_9 = "col-end-9"
    COL_END_10 = "col-end-10"
    COL_END_11 = "col-end-11"
    COL_END_12 = "col-end-12"
    COL_END_13 = "col-end-13"
    COL_END_AUTO = "col-end-auto"


class GridTemplateRows(Enum):
    """Utilities for specifying the rows in a grid layout.
    Tailwind documentation URL: https://tailwindcss.com/docs/grid-template-rows"""
    GRID_ROWS_1 = "grid-rows-1"
    GRID_ROWS_2 = "grid-rows-2"
    GRID_ROWS_3 = "grid-rows-3"
    GRID_ROWS_4 = "grid-rows-4"
    GRID_ROWS_5 = "grid-rows-5"
    GRID_ROWS_6 = "grid-rows-6"
    GRID_ROWS_NONE = "grid-rows-none"


class GridRow(Enum):
    """Utilities for controlling how elements are sized and placed across grid rows.
    Tailwind documentation URL: https://tailwindcss.com/docs/grid-row"""
    ROW_AUTO = "row-auto"
    ROW_SPAN_1 = "row-span-1"
    ROW_SPAN_2 = "row-span-2"
    ROW_SPAN_3 = "row-span-3"
    ROW_SPAN_4 = "row-span-4"
    ROW_SPAN_5 = "row-span-5"
    ROW_SPAN_6 = "row-span-6"
    ROW_SPAN_FULL = "row-span-full"
    ROW_START_1 = "row-start-1"
    ROW_START_2 = "row-start-2"
    ROW_START_3 = "row-start-3"
    ROW_START_4 = "row-start-4"
    ROW_START_5 = "row-start-5"
    ROW_START_6 = "row-start-6"
    ROW_START_7 = "row-start-7"
    ROW_START_AUTO = "row-start-auto"
    ROW_END_1 = "row-end-1"
    ROW_END_2 = "row-end-2"
    ROW_END_3 = "row-end-3"
    ROW_END_4 = "row-end-4"
    ROW_END_5 = "row-end-5"
    ROW_END_6 = "row-end-6"
    ROW_END_7 = "row-end-7"
    ROW_END_AUTO = "row-end-auto"


class GridAutoFlow(Enum):
    """Utilities for controlling how elements in a grid are auto-placed.
    Tailwind documentation URL: https://tailwindcss.com/docs/grid-auto-flow"""
    GRID_FLOW_ROW = "grid-flow-row"
    GRID_FLOW_COL = "grid-flow-col"
    GRID_FLOW_ROW_DENSE = "grid-flow-row-dense"
    GRID_FLOW_COL_DENSE = "grid-flow-col-dense"


class GridAutoColumns(Enum):
    """Utilities for controlling the size of implicitly-created grid columns.
    Tailwind documentation URL: https://tailwindcss.com/docs/grid-auto-columns"""
    AUTO_COLS_AUTO = "auto-cols-auto"
    AUTO_COLS_MIN = "auto-cols-min"
    AUTO_COLS_MAX = "auto-cols-max"
    AUTO_COLS_FR = "auto-cols-fr"


class GridAutoRows(Enum):
    """Utilities for controlling the size of implicitly-created grid rows.
    Tailwind documentation URL: https://tailwindcss.com/docs/grid-auto-rows"""
    AUTO_ROWS_AUTO = "auto-rows-auto"
    AUTO_ROWS_MIN = "auto-rows-min"
    AUTO_ROWS_MAX = "auto-rows-max"
    AUTO_ROWS_FR = "auto-rows-fr"


class Gap(Enum):
    """Utilities for controlling gutters between grid and flexbox items.
    Tailwind documentation URL: https://tailwindcss.com/docs/gap"""
    GAP_0 = "gap-0"
    GAP_X_0 = "gap-x-0"
    GAP_Y_0 = "gap-y-0"
    GAP_PX = "gap-px"
    GAP_X_PX = "gap-x-px"
    GAP_Y_PX = "gap-y-px"
    GAP_0_5 = "gap-0.5"
    GAP_X_0_5 = "gap-x-0.5"
    GAP_Y_0_5 = "gap-y-0.5"
    GAP_1 = "gap-1"
    GAP_X_1 = "gap-x-1"
    GAP_Y_1 = "gap-y-1"
    GAP_1_5 = "gap-1.5"
    GAP_X_1_5 = "gap-x-1.5"
    GAP_Y_1_5 = "gap-y-1.5"
    GAP_2 = "gap-2"
    GAP_X_2 = "gap-x-2"
    GAP_Y_2 = "gap-y-2"
    GAP_2_5 = "gap-2.5"
    GAP_X_2_5 = "gap-x-2.5"
    GAP_Y_2_5 = "gap-y-2.5"
    GAP_3 = "gap-3"
    GAP_X_3 = "gap-x-3"
    GAP_Y_3 = "gap-y-3"
    GAP_3_5 = "gap-3.5"
    GAP_X_3_5 = "gap-x-3.5"
    GAP_Y_3_5 = "gap-y-3.5"
    GAP_4 = "gap-4"
    GAP_X_4 = "gap-x-4"
    GAP_Y_4 = "gap-y-4"
    GAP_5 = "gap-5"
    GAP_X_5 = "gap-x-5"
    GAP_Y_5 = "gap-y-5"
    GAP_6 = "gap-6"
    GAP_X_6 = "gap-x-6"
    GAP_Y_6 = "gap-y-6"
    GAP_7 = "gap-7"
    GAP_X_7 = "gap-x-7"
    GAP_Y_7 = "gap-y-7"
    GAP_8 = "gap-8"
    GAP_X_8 = "gap-x-8"
    GAP_Y_8 = "gap-y-8"
    GAP_9 = "gap-9"
    GAP_X_9 = "gap-x-9"
    GAP_Y_9 = "gap-y-9"
    GAP_10 = "gap-10"
    GAP_X_10 = "gap-x-10"
    GAP_Y_10 = "gap-y-10"
    GAP_11 = "gap-11"
    GAP_X_11 = "gap-x-11"
    GAP_Y_11 = "gap-y-11"
    GAP_12 = "gap-12"
    GAP_X_12 = "gap-x-12"
    GAP_Y_12 = "gap-y-12"
    GAP_14 = "gap-14"
    GAP_X_14 = "gap-x-14"
    GAP_Y_14 = "gap-y-14"
    GAP_16 = "gap-16"
    GAP_X_16 = "gap-x-16"
    GAP_Y_16 = "gap-y-16"
    GAP_20 = "gap-20"
    GAP_X_20 = "gap-x-20"
    GAP_Y_20 = "gap-y-20"
    GAP_24 = "gap-24"
    GAP_X_24 = "gap-x-24"
    GAP_Y_24 = "gap-y-24"
    GAP_28 = "gap-28"
    GAP_X_28 = "gap-x-28"
    GAP_Y_28 = "gap-y-28"
    GAP_32 = "gap-32"
    GAP_X_32 = "gap-x-32"
    GAP_Y_32 = "gap-y-32"
    GAP_36 = "gap-36"
    GAP_X_36 = "gap-x-36"
    GAP_Y_36 = "gap-y-36"
    GAP_40 = "gap-40"
    GAP_X_40 = "gap-x-40"
    GAP_Y_40 = "gap-y-40"
    GAP_44 = "gap-44"
    GAP_X_44 = "gap-x-44"
    GAP_Y_44 = "gap-y-44"
    GAP_48 = "gap-48"
    GAP_X_48 = "gap-x-48"
    GAP_Y_48 = "gap-y-48"
    GAP_52 = "gap-52"
    GAP_X_52 = "gap-x-52"
    GAP_Y_52 = "gap-y-52"
    GAP_56 = "gap-56"
    GAP_X_56 = "gap-x-56"
    GAP_Y_56 = "gap-y-56"
    GAP_60 = "gap-60"
    GAP_X_60 = "gap-x-60"
    GAP_Y_60 = "gap-y-60"
    GAP_64 = "gap-64"
    GAP_X_64 = "gap-x-64"
    GAP_Y_64 = "gap-y-64"
    GAP_72 = "gap-72"
    GAP_X_72 = "gap-x-72"
    GAP_Y_72 = "gap-y-72"
    GAP_80 = "gap-80"
    GAP_X_80 = "gap-x-80"
    GAP_Y_80 = "gap-y-80"
    GAP_96 = "gap-96"
    GAP_X_96 = "gap-x-96"
    GAP_Y_96 = "gap-y-96"


class JustifyContent(Enum):
    """Utilities for controlling how flex and grid items are positioned along a container's main axis.
    Tailwind documentation URL: https://tailwindcss.com/docs/justify-content"""
    JUSTIFY_START = "justify-start"
    JUSTIFY_END = "justify-end"
    JUSTIFY_CENTER = "justify-center"
    JUSTIFY_BETWEEN = "justify-between"
    JUSTIFY_AROUND = "justify-around"
    JUSTIFY_EVENLY = "justify-evenly"


class JustifyItems(Enum):
    """Utilities for controlling how grid items are aligned along their inline axis.
    Tailwind documentation URL: https://tailwindcss.com/docs/justify-items"""
    JUSTIFY_ITEMS_START = "justify-items-start"
    JUSTIFY_ITEMS_END = "justify-items-end"
    JUSTIFY_ITEMS_CENTER = "justify-items-center"
    JUSTIFY_ITEMS_STRETCH = "justify-items-stretch"


class JustifySelf(Enum):
    """Utilities for controlling how an individual grid item is aligned along its inline axis.
    Tailwind documentation URL: https://tailwindcss.com/docs/justify-self"""
    JUSTIFY_SELF_AUTO = "justify-self-auto"
    JUSTIFY_SELF_START = "justify-self-start"
    JUSTIFY_SELF_END = "justify-self-end"
    JUSTIFY_SELF_CENTER = "justify-self-center"
    JUSTIFY_SELF_STRETCH = "justify-self-stretch"


class AlignContent(Enum):
    """Utilities for controlling how rows are positioned in multi-row flex and grid containers.
    Tailwind documentation URL: https://tailwindcss.com/docs/align-content"""
    CONTENT_CENTER = "content-center"
    CONTENT_START = "content-start"
    CONTENT_END = "content-end"
    CONTENT_BETWEEN = "content-between"
    CONTENT_AROUND = "content-around"
    CONTENT_EVENLY = "content-evenly"


class AlignItems(Enum):
    """Utilities for controlling how flex and grid items are positioned along a container's cross axis.
    Tailwind documentation URL: https://tailwindcss.com/docs/align-items"""
    ITEMS_START = "items-start"
    ITEMS_END = "items-end"
    ITEMS_CENTER = "items-center"
    ITEMS_BASELINE = "items-baseline"
    ITEMS_STRETCH = "items-stretch"


class AlignSelf(Enum):
    """Utilities for controlling how an individual flex or grid item is positioned along its container's cross axis.
    Tailwind documentation URL: https://tailwindcss.com/docs/align-self"""
    SELF_AUTO = "self-auto"
    SELF_START = "self-start"
    SELF_END = "self-end"
    SELF_CENTER = "self-center"
    SELF_STRETCH = "self-stretch"
    SELF_BASELINE = "self-baseline"


class PlaceContent(Enum):
    """Utilities for controlling how content is justified and aligned at the same time.
    Tailwind documentation URL: https://tailwindcss.com/docs/place-content"""
    PLACE_CONTENT_CENTER = "place-content-center"
    PLACE_CONTENT_START = "place-content-start"
    PLACE_CONTENT_END = "place-content-end"
    PLACE_CONTENT_BETWEEN = "place-content-between"
    PLACE_CONTENT_AROUND = "place-content-around"
    PLACE_CONTENT_EVENLY = "place-content-evenly"
    PLACE_CONTENT_STRETCH = "place-content-stretch"


class PlaceItems(Enum):
    """Utilities for controlling how items are justified and aligned at the same time.
    Tailwind documentation URL: https://tailwindcss.com/docs/place-items"""
    PLACE_ITEMS_START = "place-items-start"
    PLACE_ITEMS_END = "place-items-end"
    PLACE_ITEMS_CENTER = "place-items-center"
    PLACE_ITEMS_STRETCH = "place-items-stretch"


class PlaceSelf(Enum):
    """Utilities for controlling how an individual item is justified and aligned at the same time.
    Tailwind documentation URL: https://tailwindcss.com/docs/place-self"""
    PLACE_SELF_AUTO = "place-self-auto"
    PLACE_SELF_START = "place-self-start"
    PLACE_SELF_END = "place-self-end"
    PLACE_SELF_CENTER = "place-self-center"
    PLACE_SELF_STRETCH = "place-self-stretch"

