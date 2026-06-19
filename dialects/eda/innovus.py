"""Cadence EDA Tcl commands — Innovus.

Vendor-specific commands for the ``innovus-eda-tcl`` dialect.
SDC base commands are provided separately by ``eda_sdc_base``.
"""

from __future__ import annotations

from compiler.registry.models import CommandSpec, FormKind, FormSpec, HoverSnippet, ValidationSpec
from compiler.registry.signatures import Arity

_SOURCE = "Cadence Innovus"
_DIALECT = frozenset({"innovus-eda-tcl"})


def _syn(
    name: str,
    summary: str,
    synopsis: str = "",
    arity: Arity | None = None,
) -> CommandSpec:
    syn = synopsis or f"{name} ?options? ?args ...?"
    return CommandSpec(
        name=name,
        dialects=_DIALECT,
        hover=HoverSnippet(
            summary=summary,
            synopsis=(syn,),
            source=_SOURCE,
        ),
        forms=(FormSpec(kind=FormKind.DEFAULT, synopsis=syn),),
        validation=ValidationSpec(arity=arity or Arity()),
    )


def cadence_command_specs() -> tuple[CommandSpec, ...]:
    """Return Cadence-specific command specs."""
    return (
        # man1/add_cell_obs.1
        _syn(
            "add_cell_obs",
            "",
            "add_cell_obs ?-help? -cell <cell_name_or_pointer>?-exceptPGNet? -layer <layer_name_or_pointer> ?-mask <int_value>? {-rects {{<llx1 lly1 urx1 ury1>} {<llx2 lly2 urx2 ury2>}...} | -polygon {<x1 y1 x2 y2 x3 y3 ...>}} ?-spacing <value> | -design_rule_width <value>?",
        ),
        # man1/add_clock_tree_source_group_roots.1
        _syn(
            "add_clock_tree_source_group_roots",
            'This command updates the design and clock tree specification to create a multiple-tree "source group" below the specified driving root pin',
            "add_clock_tree_source_group_roots ?-help? -cell <driverCell> ?-locations {{x1 y1} {x2 y2}...}? -name <sourceGroupName> -pin <rootPin>?-grid {columns rows} ??-adjust_grid_for_aspect_ratio? ?-grid_rect {lx ly ux uy}? ?-grid_search_area {width height}? ?-grid_exclusion_rects {{lx1 ly1 ux1 uy1} {lx2 ly2 ux2 uy2}...}???",
        ),
        # man1/add_connection_to_neighbor_partition.1
        _syn(
            "add_connection_to_neighbor_partition",
            "Adds a partition pin on the abutted edge of unique abutting partitions to create a 2-partition pin scenario for target pins",
            "add_connection_to_neighbor_partition ?-help? ?-dictFile <file_name>?",
        ),
        # man1/add_decomp_filler.1
        _syn(
            "add_decomp_filler",
            "Inserts breaker cells to divide the chip into several small parts",
            "add_decomp_filler ?-help? -bottom_edge_endcap {<cell_name>} -core_column_cell {<cell_name>} -core_row_cell {<cell_name_list>} ?-offsetx <offset_in_microns>? ?-offsety <offset_in_microns>? ?-power_domain <power_domain_name>? ?-prefix <prefix_name>? -stepx <step_in_microns> -stepy <step_in_microns> -top_edge_endcap {<cell_name>} -vertical_edge_endcap {<cell_name>}",
        ),
        # man1/add_gate_array_filler.1
        _syn(
            "add_gate_array_filler",
            "Inserts GA filler cells with regular pattern during the pre-place stage",
            "add_gate_array_filler ?-help? ?-allow_shift_distance <x> <y>? ?-area <x1> <y1> <x2> <y2>? ?-cell_orientation {R0|MX|MY|R180}? ?-min_spacing_x <distance>? ?-min_spacing_y <distance>? ?-offsetx <offset_in_microns>? ?-offsety <offset_in_microns>? ?-powerDomain <powerDomainName>? ?-prefix <prefixName>? {-cell <cellName> -stepx <step_in_microns> -stepy <step_in_microns>}",
        ),
        # man1/add_gui_marker.1
        _syn(
            "add_gui_marker",
            "Places a marker to indicate location on the design layout",
            "add_gui_marker ?-help? -color <string> -name <string> -pt {x y} -type {X TICK STAR}",
        ),
        # man1/add_gui_shape.1
        _syn(
            "add_gui_shape",
            "",
            "add_gui_shape ?-help? ?-layer <layerName>? ?-name <guiShapeName>? ?-width <width>? {-rect {x1 y1 x2 y2} | -line {x1 y1 x2 y2 ...} | -polygon {x1 y1 x2 y2 ...}} ?-line {x1 y1 x2 y2 ...} ?-arrow??",
        ),
        # man1/add_gui_text.1
        _syn(
            "add_gui_text",
            "",
            "add_gui_text ?-help? ?-alignment {upperLeft centerLeft lowerLeft upperCenter centerCenter lowerCenter upperRight centerRight lowerRight}? -label <text> -layer <layerName> {-box {<x1 y1 x2 y2>} | {{-height <height> | -fixed_height <fixHeight>} -pt {<x y>} ?-orient <direction>?}} ?-box {<x1 y1 x2 y2>} ?-no_bbox??",
        ),
        # man1/add_interposer_route_block.1
        _syn(
            "add_interposer_route_block",
            "Adds the clone blocks",
            "add_interposer_route_block ?-help? -cell <cell_name> -inst <clone_name> -location {<x y>} -orient {R0 R90 R180 R270 MX MY MX90 MY90}",
        ),
        # man1/add_line_end_track.1
        _syn(
            "add_line_end_track",
            "Creates a line-end track",
            "add_line_end_track ?-help? ?-eol_width <float>? ?-except_eol_spacing <float >?-within <float>?? -layer <string>-offset <float>?-track_distance <float>? ?-track_pitch <float>?",
        ),
        # man1/add_metal_fill_signoff.1
        _syn(
            "add_metal_fill_signoff",
            "Runs the signoff metal fill flow as per specified primary and sub options",
            "add_metal_fill_signoff ?-help? ?-and_area_size <size_value>? ?-area {<x1 y1 x2 y2>}? ?-attach_instance_name <attr_num>? ?-attach_net_name <attr_num>? ?-attach_net_prop {{<prop_name attr_num>} ... }? ?-auto_load_fills? ?-bg? ?-clock? ?-common_blockage {<layer_num1 layer_datatype1> ...}? ?-control <file_name>? ?-delete_area {{<layer_list1>}{<x1 y1 x2 y2>}...}? ?-delete_point {{<layer_list1>}{<x1 y1>}...}? ?-die_area_as_boundary? ?-dp <n>? ?-dp_timeout <value>? ?-excl_area_size <size_value>? ?-fill | -incremental | -trim | -flatten | -delete_fill | -merge_fill_edits | -view_fills | -delete_flatten_fills? ?-fill_cell <cell_name>? ?-fill_layer {<layers_list>}? ?-fill_output_mode {gdsii | oasis}? ?-layer_map_file <streamOut_map_file>? ?-license_timeout? ?-license_dp_continue? ?-lib_name <library_name>? ?-lsf? ?-master_lsf? ?-merge <list_of_external_stream_files>? ?-min_density <percent1 layer_list1>? ?-net <net_names>? ?-no_structure_name? ?-no_via_fills? ?-offset {<x y>}? ?-output_macros? ?-report_file? ?-rule_file <rule_file_name>? ?-skip_map_check? ?-slack_threshold <float>? ?-spacing <float>? ?-spacing_above <float>? ?-spacing_below <float>? ?-stripes <number>? ?-structure_name <structureName>? ?-tech_lib <string>? ?-tech_set <string>? ?-technology <string>? ?-temp_working_dir <work_dir>? ?-trim_effort {high | med | low}? ?-trim_layer {<layers_list>}? ?-trim_mf <spacing_file>? ?-union_density <percent1 layer_list1>? ?-uniquify_cell_names? ?-units {100 | 200 | 400 | 800 | 1000 | 2000 | 4000 | 8000 | 10000 | 20000}? ?-window_size <float>? ?-window_step <float>?",
        ),
        # man1/add_ndr.1
        _syn(
            "add_ndr",
            "Adds a non-default rule for objects",
            "add_ndr ?-help? ?-add_via {<via_name1 via_name2 ...>}? ?-exclude_backside_via? ?-generate_via? ?-hard_spacing? ?-init <string>? ?-min_cut {layer1?:layer2? <min_cut ...>}? ?-spacing <string> | -spacing_multiplier <string>? ?-via {<via_name1 via_name2 ...>}? ?-width <string> | -width_multiplier <string>? {-name <ruleName>} ?-use_via_cut_class <string>?",
        ),
        # man1/add_oa_library_property.1
        _syn(
            "add_oa_library_property",
            "Adds a new property to the specified OpenAccess library",
            "add_oa_library_property ?-help? -lib <libName> -name <prop_name> -type {boolean integer float string} -value <propValue>",
        ),
        # man1/add_obj_on_bump.1
        _syn(
            "add_obj_on_bump",
            "Adds shapes on the TSV bumps",
            "add_obj_on_bump ?-help? {{-cell <bump_cell_name> | -selected | -feedthru } {-relative_pin_layer <pin_layer_name> | -rect {x1 y1 x2 y2} | -polygon {{x1 y1} {x2 y2}...}}} ?-check_only <bump_name> | -write_script <filename>? {?-shape <layer>+? ?-placement_blockage? ?-routing_blockage <layer>+? ?-physical_pin <layer>+?} ?-shape <layer>+ ?-check_only <bump_name>? ?-incremental??-shape_keep_net?? ?-feedthru ?-cdl_map_file <cdl_map_file_name>??",
        ),
        # man1/add_pg_fill.1
        _syn(
            "add_pg_fill",
            "Runs Pegasus PG Fill with default settings and any specified options",
            "add_pg_fill ?-help? ?-attach_instance_name <attr_num>? ?-attach_net_name <attr_num>? ?-attach_net_prop {{<prop_name attr_num>} ... }? ?-bsub <resource_string>? ?-core_license <license_combination>? ?-die_area_as_boundary? ?-dp <n>? ?-dp_timeout <seconds>? ?-extra_options <options>? ?-fix_post_process_drc? ?-format {stream oasis}? ?-incremental? ?-initial_working_dir <string>? ?-layer_map_file <streamOut_map_file>? ?-lib_name <library_name>? ?-license_dp_continue? ?-license_timeout <seconds>? ?-merge <list_of_external_stream_files>? ?-nc <resource_string>? ?-no_structure_name? ?-offset {<x y>}? ?-output_macros? ?-pg_fill_config_file <file_name>? ?-pg_hookup_flow {ALL | PG_ONLY | FLOAT_ONLY}? ?-qsub <resource_string>? ?-report_file? ?-stripes <number>? ?-structure_name <structureName>? ?-turbo <jobs_num>? ?-uniquify_cell_names? ?-units {100 | 200 | 400 | 800 | 1000 | 2000 | 4000 | 8000 | 10000 | 20000}? ?-working_dir <working_directory>? ?-xor_via_layers?",
        ),
        # man1/add_sai_boundary_flops.1
        _syn(
            "add_sai_boundary_flops",
            "",
            "add_sai_boundary_flops ?-help? ?-clock <string>? ?-delete_flops? -hinsts <string> -ports <string> ?-ref_flop <string> ?-clock_input_pin <string>? ?-data_input_pin <string>? ?-data_output_pin <string>??",
        ),
        # man1/add_shape.1
        _syn(
            "add_shape",
            "The command add_shape adds DEF SPECIALNETS wiring shapes to the database",
            "add_shape ?-help? -layer {<layerNameOrPointer>} ?-net {<netName>}? ?-shape {None RING STRIPE FOLLOWPIN IOWIRE COREWIRE BLOCKWIRE FILLWIRE BLOCKAGEWIRE PADRING BLOCKRING DRCFILL FILLWIRE‐ OPC}? ?-shield_net {<netNameOrPointer>}? ?-status {ROUTED FIXED COVER SHIELD NOSHIELD}? ?-user_class <className>? {-rect {<x1 y1 x2 y2>} | -patch {<x1 y1 x2 y2>} | -polygon {<x1 y1 x2 y2 ...xn yn>} | ?-pathSeg {<x1 y1 x2 y2>} -width <value> ?-beginExt <value> -endExt <value>??}",
        ),
        # man1/add_tap_walls.1
        _syn(
            "add_tap_walls",
            "Adds tap walls to the assigned left, right, top, and/or bottom side of a block",
            "add_tap_walls ?-help? ?-bottom? -cell <cellName> ?-layer <layer_name>? ?-left? ?-orientation {R0 MX MY R180}? ?-pitch <distance>? ?-prefix <prefix>? ?-range <lx ux>|<ly uy>? ?-right? ?-top? ?-y_flip_side {left right both}?",
        ),
        # man1/add_target_pg.1
        _syn(
            "add_target_pg",
            "",
            "add_target_pg ?-help? ?-area {<x1 y1 x2 y2>}{<x1 y1 x2 y2 x3 y3 x4 y4> ...}? ?-force? ?-instance {<list_of_instances>}? -nets {<list_of_nets>} -pin_layer <layer> ?-stack_layer_config {<stack_layer_pattern>}? ?-stack_layer_config_file <filename>? -target_layer {<layer1 layer2>} ?-uda <subclass_string>?",
        ),
        # man1/add_text.1
        _syn(
            "add_text",
            "Adds text to the specified custom layer",
            "add_text ?-help? ?-alignment {centerCenter centerLeft centerRight lowerCenter lowerLeft lowerRight upperCenter upperLeft upperRight}? ?-drafting {true | false}? ?-font {euroStyle gothic math roman script stick fixed swedish milSpec}? ?-height <value>? -label {<string>} ?-layer {<layerNameOrPointer>}? ?-oaPurpose {<string>}? ?-orient {MX MX90 MY90 R0 R180 R270 R90}? -pt {<x y>}",
        ),
        # man1/add_thru_substrate_insts.1
        _syn(
            "add_thru_substrate_insts",
            "Adds thru-substrate instances to a net to specify two-sided routing for a critical net (back‐ side routing has lower RC than frontside routing)",
            "add_thru_substrate_insts ?-help? ?-driver_thru_substrate_cell <cell1>?",
        ),
        # man1/add_to_collection.1
        _syn(
            "add_to_collection",
            "",
            "add_to_collection ?-help? <base_collection> <second_collection_or_list> ?-unique?",
        ),
        # man1/add_track_fill.1
        _syn(
            "add_track_fill",
            "Adds the Track-Based Fill (TBF) flow to the metal fill layers",
            "add_track_fill ?-help? ?-attach_instance_name <attr_num>? ?-attach_net_name <attr_num>? ?-attach_net_prop {{<prop_name attr_num>} ... }? ?-bsub <resource_string>? ?-core_license <license_combination>? ?-die_area_as_boundary? ?-dp <n>? ?-dp_timeout <seconds>? ?-extra_options <options>? ?-fix_post_process_drc? ?-format {stream oasis}? ?-incremental? ?-initial_working_dir <string>? ?-layer_map_file <streamOut_map_file>? ?-lib_name <library_name>? ?-license_dp_continue? ?-license_timeout <seconds>? ?-merge <list_of_external_stream_files>? ?-nc <resource_string>? ?-no_structure_name? ?-offset {<x y>}? ?-output_macros? ?-qsub <resource_string>? ?-report_file? ?-stripes <number>? ?-structure_name <structureName>? ?-track_fill_config_file <file_name>? ?-turbo <jobs_num>? ?-uniquify_cell_names? ?-units {100 | 200 | 400 | 800 | 1000 | 2000 | 4000 | 8000 | 10000 | 20000}? ?-working_dir <working_directory>?",
        ),
        # man1/add_tracks.1
        #   WARNING: bracket mismatch: '[' at position 156 closed by '}' at position 225
        #   WARNING: unmatched closing bracket ']' at position 226
        #   WARNING: bracket mismatch: '[' at position 228 closed by '}' at position 319
        #   WARNING: unmatched closing bracket ']' at position 320
        #   WARNING: bracket mismatch: '[' at position 322 closed by '}' at position 397
        #   WARNING: unmatched closing bracket ']' at position 398
        _syn(
            "add_tracks",
            "Deletes existing routing tracks and generates new routing tracks based on the technology data or user spe‐ cific values",
            "add_tracks ?-help? ?-backside? ?-honor_pitch? ?-keep_default_width? ?-mask_pattern {{<layer1> <mask> ?<mask …>?} ?<layer2 ...>? }? ?-mode {replace append}? ?-offsets {<layer1> horiz|vert ?die_box? <offset>} ?{<layer2 …>}? ...}? ?-pitch_pattern {<layer1> offset <offset> pitch <pitch> ?pitch<pitch> …?} ?{<layer2> …}?...}? ?-pitches {<layer1> horiz|vert <pitch>} ?{<layer2> horiz|vert <pitch>}? ...}? ?-rect_only_pattern {{layer1 ?<pattern> ...?} {layer2 ?<pattern> ...?} .. }? ?-route_rule <route_rule_name>? ?-snap_m1_track_to_cell_pins? ?-width_pitch_pattern {{<layer1> offset <offset> width <width>pitch <pitch> ?width <width>pitch <pitch>?...} ?{<layer2> …}?...}?",
        ),
        # man1/add_via.1
        _syn(
            "add_via",
            "Adds a new special-route via instance to the design",
            "add_via ?-help? ?-net <net>? -pt {<x y>} ?-shape {blockring | blockagewire | blockwire | corewire | drcfill | fillopc | fillwire | followpin | iowire | none | padring | ring | stripe}? ?-shield_net <net>? ?-status {routed | fixed | cover | shield}? ?-user_class <value>? -via <via_def>",
        ),
        # man1/add_via_definition.1
        #   WARNING: unclosed bracket '{' at position 94
        _syn(
            "add_via_definition",
            "Creates a via definition (master) from the specified parameters or list of shapes",
            "add_via_definition ?-help? ?-bottom_layer_masks <int+>? ?-cut_masks <int+>? ?-name <viaName>? {{?-via_rule <via_def_rule> | -cut_pattern <viaDef>? ??-cut_size {<x y>}??-cut_spacing {<x y>}??-top_enclosure {<x y>}? ?-bottom_enclosure {<x y>}??-top_offset {<x y>}??-bottom_offset {<x y>}??-row_col {<x y>}? ?-origin {<x y>}? ?-pattern <pattern>??} | {{-cut_layer <layer> -cut_rects {{<x1 y1 x2 y2>} {<x3 y3 x4 y4>} ...} {?-top_layer <layer>? {-top_rects {{<x1 y1 x2 y2>} {<x3 y3 x4 y4>} ...} | -top_polygon {{<x1 y1>}{<x2 y2>}...}}} {?-bottom_layer <layer>? {-bottom_rects {{<x1 y1 x2 y2>} {<x3 y3 x4 y4>} ...} | -bottom_polygon {{<x1 y1>} {<x2 y2>}...}}}}} ?-top_layer_masks <int+>?",
        ),
        # man1/addAIoFiller.1
        _syn(
            "addAIoFiller",
            "Adds area I/O filler cell instances",
            "addAIoFiller ?-help? {-cell <fillerCellName> | -cellList {<fillerCellName1><fillerCellName2><...>}} ?-prefix <prefix>? ?-aioRowCluster <aioRowClusterName> | -allAIORowCluster? ?-setPreplaced? ?-onlyESD? ?-onlyShoulder? ?-onlyGap? ?-powerDomain <powerDomainName>?",
        ),
        # man1/addAIORow.1
        _syn(
            "addAIORow",
            "Adds area I/O rows",
            "addAIORow ?-help? -site <site_name> {-bump <bumpId> | -loc <llx><lly>} ?-dx <x_dist>? ?-dy <y_dist>? ?-orient {R0|R90|R180|R270|MX|MX90|MY|MY90}? ?-H | -V? ?-esd <esites_no>...? ?-shoulder <site_no>...? ?-cluster_halo <space>? ?-num <num>? ?-abutRow? ?-rowName <name>? ?-noSnap? ?-soft? ?{-ptnArrX <elem1> | -ptnArrY <elem2>} {-pitchX <dist> | -pitchY <dist>}?",
        ),
        # man1/addBumpConnectTargetConstraint.1
        _syn(
            "addBumpConnectTargetConstraint",
            "Adds a string property in one or multiple bumps",
            "addBumpConnectTargetConstraint ?-help? {-bump <list_of_bumps> | -selected } { {-instName <instance_name> ?{-pinName <pin_name> | -netName <net_name>} ?-portNum <value>??} |-PGConnectType {ioring corering stripe iopin}}",
        ),
        # man1/addChannelDensityControl.1
        _syn(
            "addChannelDensityControl",
            "Controls the routing density for a specified area on a layer by setting a maximum density per‐ centage that early Global Route cannot exceed",
            "addChannelDensityControl ?-help? <llx><lly><urx><ury><layer> <ratio>",
        ),
        # man1/addDeCap.1
        _syn(
            "addDeCap",
            "Adds the specified total decoupling capacitance to the design",
            "addDeCap ?-help? -totCap <total_cap_in_fF>< > ?-cells <cellName>? ?-addFixAttr? ?-area <x1 y1 x2 y2><| >-exclude {{<x1 y1 x2 y2>} ...}? ?-effort ?low | high?? ?-prefix <prefixName>? ?-noFixDRC? ?-log <logName>? ?-maxNrIter <number>? ?-fromFile <fileName>? ?-pgNet <netName>?",
        ),
        # man1/addDeCapCellCandidates.1
        _syn(
            "addDeCapCellCandidates",
            "Defines the cells that can be used by the addDeCap command to insert decoupling capacitance into the design",
            "addDeCapCellCandidates ?-help? {<cellName><capacitance>| -fromFile <fileName>}",
        ),
        # man1/addDummyBoundaryWires.1
        _syn(
            "addDummyBoundaryWires",
            "Add wires on the first and last tracks in the direction parallel to preferred routing direction with specified layers",
            "addDummyBoundaryWires ?-help? -layers <layerName> | { <layerNameList ...> } ?-masks <maskNumber> | { <maskNumberList ...> }? ?-shape {blockring | blockagewire | blockwire | corewire | drcfill| fillwireopc | fillwire | followpin | iowire | none | padring | ring | stripe}? ?-shortWires <wireLength> | { <wireLengthList ...> }? ?-space <spaceValue> | { <spaceValueList ...> }?",
        ),
        # man1/addEndCap.1
        _syn(
            "addEndCap",
            "Adds physical-only end cap cells at the ends of the site rows",
            "addEndCap ?-help? ?-area llx lly urx ury? ?-coreBoundaryOnly? ?-powerDomain <powerDomainName>? ?-prefix <prefixName>?",
        ),
        # man1/addFiller.1
        _syn(
            "addFiller",
            "Inserts filler cell instances in the gaps between standard cell instances",
            "addFiller ?-area <areaBoxList>? ?-cell {<filler_cell_list>}? ?-createRows {true | false}? ?-diffCellViol {true|false}? ?-check_signal_drc {true | false}? ?-ecoMode {true | false}? ?-fitGap? ?-fixDRC? ?-fix_horizontal_max_length_violation? ?-fix_vertical_max_length_violation? ?-honorPrerouteAsObs {true | false}? ?-markFixed? ?-merge {true | false}? ?-minHole {true | false}? ?-powerDomain <powerDomainName>? ?-prefix <prefixName>? ?-prevent_vertical_stack_max_length_violation? ?-util <targetUtilization>? ?-viaEnclosure {true | false}?",
        ),
        # man1/addFillerGap.1
        _syn(
            "addFillerGap",
            "Moves placed standard cell instances to create gaps so that filler cells can be added",
            "addFillerGap <minGap > ?-effort {none | low | medium | high}? ?-radius <micron>?",
        ),
        # man1/addHaloToBlock.1
        _syn(
            "addHaloToBlock",
            "Adds a halo to a block",
            "addHaloToBlock ?-help? <left bottom right top> ?-fromInstBox? ?-snapToSite? ?-ori <orientation>? ?<inst_name> |-allMacro | -allBlackBox | -allCommitPtn | -allBlock | -allIOPad | -cell <name>?",
        ),
        # man1/addHierInst.1
        _syn(
            "addHierInst",
            "Adds a hierarchical module to the design",
            "addHierInst ?-help? -cell <cellName >?-moduleBased <parentModuleName>? {-hinst <hinstName> | -module <moduleName>}",
        ),
        # man1/addInst.1
        _syn(
            "addInst",
            "Adds an instance and places it in the design",
            "addInst ?-help? ?-dontSnapToPlacementGrid? ?-moduleBased <verilogModule>? ?-physical? -cell <cellName> -inst <instName> ?-loc {<x y>} ?-ori {R0 | R90 | R180 | R270 | MX | MX90 | MY | MY90}?? ?-place_status <placementStatus>?",
        ),
        # man1/addInstToInstGroup.1
        _syn(
            "addInstToInstGroup",
            "Adds a hierarchical instance, an instance or list of instances, or a group to a specified group",
            "addInstToInstGroup ?-help?",
        ),
        # man1/addIoFiller.1
        _syn(
            "addIoFiller",
            "Adds I/O instances in the I/O box",
            "addIoFiller ?-help? -cell {<name_list>} ?-fillAnyGap? ?-fillerOrient R0 | R90 | R180 | R270 | MX | MX90 | MY | MY90? ?-from <coord>? ?-prefix <prefix>? ?-side {top | bottom | left | right}? ?-to <coord>? ?-row <rowNumber>? ?-useSmallIoHeight? ?-logic ?-deriveConnectivity??",
        ),
        # man1/addIoInstance.1
        _syn(
            "addIoInstance",
            "Specifies constraints for insertion of power and ground I/O instances in the I/O ring or in the I/O rows",
            "addIoInstance ?-help? ?-cell {<name1 name2 ...>}? -inst {<inst1 inst2 ...>} {{-refInst <inst_name> ?-ccw?} | {-selected ?-ccw?} | {-repeat num ?-skip <num>? ?-inSelected | ?-ioRing <num>? -side {N | W | S | E} | -ioRow name?} | -loc llx lly } ?-spacing <val>? ?-orientation <orient>? ?-spread?",
        ),
        # man1/addIoRowFiller.1
        _syn(
            "addIoRowFiller",
            "Adds I/O filler cells in the I/O rows",
            "addIoRowFiller ?-help? -cell {<fillerCellNameList ...>} ?-logic? ?-prefix <prefix>? ??-ioRow <name> | -powerDomain <powerDomainName>? ?-fillerOrient R0 | R90 | R180 | R270 | MX | MX90 | MY | MY90?? ?-from <coord>? ?-to <coord>? ?-fillAnyGap? ?-useSmallIoHeight? ?-ignoreSiteType?",
        ),
        # man1/addMimCap.1
        _syn(
            "addMimCap",
            "Adds Metal-Insulator-Metal (MIM) cap cell(s) into the design",
            "addMimCap ?-help? -cell <cellName> ?-orient <orientation>? ?-prefix <prefixName>? ?{-stepX <step_in_microns> -stepY <step_in_microns>} ?-area {x1 y1 x2 y2}???{-area {x1 y1 x2 y2} | -loc {x y}}? ?-loc {x y} | -offset {x y}?",
        ),
        # man1/addModulePort.1
        _syn(
            "addModulePort",
            "Adds a port or bussed port to a module, specified as a module or a hierarchical instance",
            "addModulePort ?-help?<moduleName> <portName><portDir> ?-bus <n1>:<n2>? ?-moduleBased?",
        ),
        # man1/addModuleToFPlan.1
        _syn(
            "addModuleToFPlan",
            "Use this command to display modules in the floorplan view whose instance count is smaller than the set‐ Preference MinFPModuleSize value",
            "addModuleToFPlan ?-help?",
        ),
        # man1/addNet.1
        _syn(
            "addNet",
            "Adds a net to the design",
            "addNet ?-help? <netName> ?-bus <startID>:<endID>? ?-moduleBased <verilogModule>? ?-power | -ground?",
        ),
        # man1/addNetToNetGroup.1
        _syn(
            "addNetToNetGroup",
            "Adds a net to specified net group that was created with the createNetGroup command",
            "addNetToNetGroup ?-help?",
        ),
        # man1/addObjFPlanCutBox.1
        _syn(
            "addObjFPlanCutBox",
            "Specifies the rectilinear shape of floorplan objects by describing the cut out area",
            "addObjFPlanCutBox ?-help?",
        ),
        # man1/addPGFTV.1
        _syn(
            "addPGFTV",
            "Inserts PGFTV cells at the prePlace and postRoute stages",
            "addPGFTV ?-help? ?-area <x1> <y1> <x2> <y2>? ?-cell <cellName>? ?-prePlace? ?-prefix <prefixName>? ?-stepx <step_in_microns>? ?-stepy <step_in_microns>? ?-postRoute ?-cell_list <{> <PGFTV1 PGFTV2 PGFTV3…}>??",
        ),
        # man1/addPinToPinGroup.1
        _syn(
            "addPinToPinGroup",
            "Adds a module port to specified pin group that was created by createPinGroup command",
            "addPinToPinGroup ?-help? ?-cell <cellName>? -pinGroup <pinGroupName> -pin {<pinName> | <pinNameList>}",
        ),
        # man1/addPowerSwitch.1
        _syn(
            "addPowerSwitch",
            "The addPowerSwitch command supports five type of cells: switch cells, filler cells, corner cells (for the ring style only), and buffer cells",
            "addPowerSwitch ?-help? ?-1801PowerSwitchRuleName <string>? ?-acknowledgeTreeCell <cell_name>? ?-acknowledgeTreeHierInstance <hier_instance>? ?-allowPartialStripeRowOverlap <string>? ?-area {<x1 y1 x2 y2>}? ?-backToBackChain {LtoR | RtoL}? ?-bottomNumSwitch <integer>? ?-bottomOffset <float>? ?-bottomOrientation <orientation_syntax>? ?-bottomPattern <pattern_syntax>? ?-bottomSide ?0 | 1?? ?-bufferCellNameBottom <cell_syntax>? ?-bufferCellNameHorizontal <cell_syntax>? ?-bufferCellNameLeft <cell_syntax>? ?-bufferCellNameRight <cell_syntax>? ?-bufferCellNameTop <cell_syntax>? ?-bufferCellNameVertical <cell_syntax>? ?-bufferCellSideList {<cell_syntax ..>}? ?-bufferDelay <value_in_seconds>? ?-bufferSwitchSameDirection <string>? ?-cellEM <value_in_amps>? ?-cellEnablePin <string>? ?-chainByRow <string>? ?-checkerBoard <string>? {-column | -ring} ?-commitPrototype {0|1}? ?-connectBottomSwitchEnablePins {LtoR | RtoL}? ?-continuePattern <string>? ?-cornerCellList {<listOfCornerCells>}? ?-cornerCellListByCorner <corner_cells_name_per_corner>? ?-cornerOrientationList {<orientation_syntax>...}? ?-counterclockwise <string>? ?-cpfPowerSwitchRuleName <rule_name>? ?-deviceThresholdVolt <value_in_volts>? ?-distribute <string>? ?-enableNetIn {<listOfNets>}? ?-enableNetOut {<listOfNets>}? ?-enablePinIn {<listOfPins>}? ?-enablePinOut {<listOfPins>}? ?-endOffset <value>? ?-endOffsetBottom <value>? ?-endOffsetHorizontal <value>? ?-endOffsetLeft <value>? ?-endOffsetRight <value>? ?-endOffsetTop <value>? ?-endOffsetVertical <value>? ?-fillerCellNameBottom <cell_syntax>? ?-fillerCellNameHorizontal <cell_syntax>? ?-fillerCellNameLeft <cell_syntax>? ?-fillerCellNameRight <cell_syntax>? ?-fillerCellNameTop <cell_syntax>? ?-fillerCellNameVertical <cell_syntax>? ?-fillerCellSideList {<cell_syntax>...}? ?-firstInstanceName <instanceName>? ?-forceOffset <string>? ?-getSwitchInstances <string>? ?-globalBufferCellName <cell_syntax>? ?-globalFillerCellName <cell_syntax>? ?-globalOffset <float>? ?-globalPattern <pattern_syntax>? ?-globalSwitchCellName <cell_syntax>? ?-ground {(<GND:GND1 GND2>...)...}? ?-height <length_in_um>? ?-honorNonRegularPitchStripe <string>? ?-horizontalNumSwitch <value>? ?-horizontalOffset <float>? ?-horizontalOrientation <orientation_syntax>? ?-horizontalPattern <pattern_syntax>? ?-horizontalPitch <float>? ?-horizontalSide ?0 | 1?? ?-iLeak <value_in_amps>? ?-idSat <value_in_amps>? ?-ignoreShifterRule <string>? ?-ignoreSoftBlockage <string>? ?-incremental <string>? ?-insideCornerCellList {<cellName ...>}? ?-instancePrefix <string>? ?-leftNumSwitch <integer>? ?-leftOffset <float>? ?-leftOrientation <orientation_syntax>? ?-leftPattern <pattern_syntax>? ?-leftSide ?0 | 1?? ?-loadCapacitance <value_in_farads>? ?-logical? ?-loopbackAtEnd <string>? ?-maxChainDepth <integer>? ?-maxDistance <distance_in_microns>? ?-maxFanout <integer>? ?-maxIRPercent <float>? ?-maxLeakageCurrent <value_in_amps>? ?-maxLeakagePercent <float>? ?-maxRampUpCurrent <value_in_amps>? ?-maxSwitchIR <value_in_volts>? ?-noDoubleHeightCheck <string>? ?-noEnableChain <string>? ?-noFiller <string>? ?-noFixedStdCellOverlap <string>? ?-noMinGapAdjust <string>? ?-noPgCapacitanceEstimate ?0 | 1?? ?-noPgDecapEstimate ?0 | 1?? ?-noRowVerify <string>? ?-numSwitches <string>? ?-numberSimultaneousRampUpChain <integer>? ?-offsetX <string>? ?-orientation <orientation_syntax>? ?-parallelEnable <string>? ?-pgCapacitance <value_in_farads>? ?-pgCapacitanceFactor <value_in_farads>? ?-pgInductance <value_in_henrys>? ?-placeByNetWireIntersect {<h_net h_layer v_net v_layer>}? ?-placeUnderVerticalNet {<v_net v_layer>}? ?-placementAdjustX {<delta_in_x>}? ?-placementAdjustXY {<delta_in_x delta_in_y>}? ?-placementAdjustY {<delta_in_y>}? ?-power {(<VDD:VDD1 VDD2>...)...}? ?-powerDomain <powerDomainName>? ?-protoReportFile <fileName>? ?-prototypeChainDepth ?0 | 1?? ?-prototypeChainDepthGivenRampUpCurrent ?0 | 1?? ?-prototypeDelayGivenRampUpCurrent ?0 | 1?? ?-prototypeMaxChainDepth ?0 | 1?? ?-prototypeMinChainDepth ?0 | 1?? ?-prototypeNumberSwitches ?0 | 1?? ?-prototypeRampUpTime ?0 | 1?? ?-prototypeSweepChainDepth {<min_integer> <max_integer> <increment_integer>}? ?-prototypeSweepSwitchNumber {<min_integer> <max_integer> <increment_integer>}? ?-r0Corner <corner_syntax>? ?-r0InsideCorner {LT | TR | RB | BL}? ?-r0Side {L | T | R | B}? ?-r0SideOrientation <orientation_syntax>? ?-rOn <value_in_ohms>? ?-rampUpChainDepth <integer>? ?-rampUpRailVoltagePercent <float>? ?-rampUpTime {<min_value_in_seconds max_value_in_seconds>}? ?-readPowerSwitchCell <fileName>? ?-reportFile <filename>? ?-rightNumSwitch <integer>? ?-rightOffset <float>? ?-rightOrientation <orientation_syntax>? ?-rightPattern <pattern_syntax>? ?-rightSide ?0 | 1?? ?-shiftCellsOutsideBlockage? ?-sideEndOffsetList {<value ...>}? ?-sideNumSwitchList {<integer>...}? ?-sideOffsetList {<value ...>}? ?-sideOrientationList {<orientation_syntax>...}? ?-sidePatternList {<pattern_syntax>...}? ?-sideStartOffsetList {<value ...>}? ?-skipRows <string>? ?-skipX <string>? ?-skipY <string>? ?-snapToNearest <string>? ?-specifySideList ?0 | 1 ...?? ?-startEnableChainAtCorner {<integer>| <corner_syntax>}? ?-startOffset <value>? ?-startOffsetBottom <value>? ?-startOffsetHorizontal <value>? ?-startOffsetLeft <value>? ?-startOffsetRight <value>? ?-startOffsetTop <value>? ?-startOffsetVertical <value>? ?-switchCellNameBottom <cell_syntax>? ?-switchCellNameHorizontal <cell_syntax>? ?-switchCellNameLeft <cell_syntax>? ?-switchCellNameRight <cell_syntax>? ?-switchCellNameTop <cell_syntax>? ?-switchCellNameVertical <cell_syntax>? ?-switchCellSideList {<cell_syntax>...}? ?-switchModuleInstance <instanceName>? ?-switchPitch <value>? ?-switchPitchBottom <value>? ?-switchPitchHorizontal <value>? ?-switchPitchLeft <value>? ?-switchPitchRight <value>? ?-switchPitchSideList {<value>...}? ?-switchPitchTop <value>? ?-switchPitchVertical <value>? ?-tapFromNearestEnableNet <string>? ?-topDown <string>? ?-topNumSwitch <integer>? ?-topOffset <float>? ?-topOrientation <orientation_syntax>? ?-topPattern <pattern_syntax>? ?-topSide ?0 | 1?? ?-totalLeakagePower <value_in_watts>? ?-totalNumberPatterns <number_of_patterns>? ?-totalPower <value_in_watts>? ?-vertex {<x1 y1 x2 y1 x2 y2 x3 y2 x3 y3 x1 y3... xn yn>}? ?-verticalNumSwitch <value>? ?-verticalOffset <value>? ?-verticalOrientation <orientation_syntax>? ?-verticalPattern <pattern_syntax>? ?-verticalSide ?0 | 1?? ?-voltage <value_in_volts>? ?-width <length_in_um>?",
        ),
        # man1/addRepeaterByRule.1
        _syn(
            "addRepeaterByRule",
            "Inserts buffers and/or inverters to nets, as defined in a rule file",
            "addRepeaterByRule ?-help? ?-copyNetAttribute? ?-excNet <excludeNetFile>? ?-netMapping <fileName>? ?-nets <list_of_nets>? ?-outDir <directoryName>? ?-preRoute | -postRoute | -alongRoute? ?-reportIgnoredNets <ignoredNetFile>? ?-rule <fileName>? ?-selNet <selNetFile>? ?-selected? ?-template?",
        ),
        # man1/addRing.1
        _syn(
            "addRing",
            "Creates rings for specified nets around the core boundary or selected blocks and groups of core rows",
            "addRing ?-help? ?-around {each_block each_reef power_domain default_power_domain selected cluster shared_cluster user_defined}? ?-center {0 | 1}? ?-exclude_selected {0 | 1}? ?-extend_corner {tl tr bl br lt lb rt rb}? ?-follow {core io}? ?-jog_distance <real_value>? {-nets <name-or-value>} ?-offset_adjustment {automatic fixed}??-rectangle {0 | 1}? ?-skip_side {top | bottom | left | right}? ?-snap_wire_center_to_grid {None Grid Half_Grid Either}? ?-threshold {value | auto}? ?-type {core_rings block_rings}? ?-uda <subclass_string>? ?-use_interleaving_wire_group {0 | 1}? ?-use_wire_group {0 | 1}? ?-use_wire_group_bits <value>? ?-use_wire_group_reinforcement {0 | 1}? ?-use_wire_group_reinforcement_group_via {0 | 1}? ?-use_wire_group_reinforcement_spacing_width {spacing width}? ?-user_defined_region {x1 y1 x2 y2 ...}? {-layer {layer | {top top_layer bottom bottom_layer left left_layer right right_layer}} } {-width {value | {top top_width bottom bottom_width left left_width right right_width}} } {-spacing {value | {top top_spacing bottom bottom_spacing left left_spacing right right_spacing}} } ?-offset {value | {top top_offset bottom bottom_offset left left_offset right right_offset}}?",
        ),
        # man1/addRoutingHalo.1
        _syn(
            "addRoutingHalo",
            "Adds a routing halo for blackboxes, hard macros, or block-level designs",
            "addRoutingHalo ?-help? { {-bottom <bottomLayer> -space <haloValue> -top <topLayer>} | -lithoHalo } {-allBlocks | -block <blockNameList> | -cell <cellNameList> | -inst <instanceName> | -designHalo }",
        ),
        # man1/addSdpGroupMember.1
        _syn(
            "addSdpGroupMember",
            "Adds an object or member to an existing structured data path (SDP) group",
            "addSdpGroupMember ?-help? -group <group_name> -object <object_name_list> ?-orientation <orientStr>? ?-before <refObject> | -after <refObject>?",
        ),
        # man1/addSdpObject.1
        _syn(
            "addSdpObject",
            "Creates a placement blockage on top of the specified SDP group OR inserts one or more empty rows across the whole die above/below the specified instance",
            "addSdpObject ?-help? {-obstruct <group_name_list> | {-emptyRow <instance_name> -numRow <value>}}",
        ),
        # man1/addSizeBlockage.1
        _syn(
            "addSizeBlockage",
            "Adds a size blockage object that controls the behavior of the resize line under a covered area",
            "addSizeBlockage ?-help? ?-name <blockageName>? ?-isResizeable? -box <x1 y1 x2 y2>",
        ),
        # man1/addSpareInstance.1
        #   WARNING: unclosed bracket '[' at position 25
        _syn(
            "addSpareInstance",
            "Specifies a file that lists spare cells to add to the netlist",
            "addSpareInstance ?-help? ?-async <netName:terminalList> ?<netName:terminalList> …? ?-clock <netName>? -file <fileName>?-fix_placed_insts {TRUE|FALSE}? ?-hier <moduleName> | -powerDomain <domainName> ?-submodule <submoduleName>?? ?-prefix <prefix>? ?-tie {0 | 1}?",
        ),
        # man1/addSpecialRoute.1
        _syn(
            "addSpecialRoute",
            "Incrementally adds special route information from a file",
            "addSpecialRoute ?-help? <filename>",
        ),
        # man1/addSplitPowerVia.1
        _syn(
            "addSplitPowerVia",
            "Adds or deletes Jenga vias and does not modify vias",
            "addSplitPowerVia ?-help? ?-delete | -wires_only? ?-edgeLength {layer1 value1 layer2 value2 ...}? ?-forceCount? ?-localCheckerBoard? ?-master <cell_name>? ?-maxViaSize {x y}? ?-maxWireLength {layer1 value1 layer2 value2 ...}? ?-maxWireSpacing {layer1 value1 layer2 value2 ...}? ?-mergeCount {x y}? ?-mergeDistance {x y}? ?-minEnclosure? ?-minViaSize {x y}? ?-minWireLength {layer1 value1 layer2 value2 ...}? ?-minWireSpacing {layer1 value1 layer2 value2 ...}? ?-pinLayer {layer1 layer2 ...}? ?-prerouteAlign {none samelayer alllayer}? ?-snap_wire_center_to_grid {layer1 {none|grid|half_grid|either} layer2 {none|grid|half_grid|either}} ...? ?-stackedCheckerBoard? ?-uda <userDefinedAttribute>? ?-wireCount {layer1 value1|auto layer2 value2|auto … }? ?-wireOffset {layer1 value1 layer2 value2 ...}? ?-wireWidth {layer1 value1 layer2 value2 ...}?",
        ),
        # man1/addStripe.1
        _syn(
            "addStripe",
            "Creates power stripes within the specified area",
            "addStripe ?-help? ?-all_blocks {0 | 1}? ?-area {{<x1 y1 x2 y2>}{<x1 y1 x2 y2 x3 y3 x4 y4> ...} ...}? ?-area_blockage {{<x1 y1 x2 y2>}{<x1 y1 x2 y2 x3 y3 x4 y4> ...} ...}? ?-between_bumps {0 | 1}? ?-block_ring_bottom_layer_limit <layer>? ?-block_ring_top_layer_limit <layer>? ?-create_pins {0 | 1}? ?-direction {horizontal | vertical}? ?-extend_to {design_boundary | first_padring | last_padring | all_domains}? ?-insts <instance_name>? ?-layer <layer>? ?-master <master_cell>? ?-max_same_layer_jog_length <real_value>? ?-merge_stripes_value {auto | value}? ?-narrow_channel {0 | 1}? ?-nets {list_of_nets}? ?-number_of_sets <integer_value>? ?-over_bumps {0 | 1}? ?-over_physical_pins {0 | 1}? ?-over_pins {0 | 1}? ?-over_power_domain {0 | 1}? ?-padcore_ring_bottom_layer_limit <layer>? ?-padcore_ring_top_layer_limit <layer>? ?-pin_layer <layer>? ?-pin_offset <real_value>? ?-pin_width {<min_value max_value>}? ?-power_domains <domain_name>? ?-report_cut_stripe <filename>? ?-same_layer_target_only {0 | 1}? ?-set_to_set_distance <real_value>? ?-snap_wire_center_to_grid {None |Grid | Mask1_Grid | Mask2_Grid | Half_Grid | Either} ?-allow_snapping_override_cus‐ tom_spacing {0 | 1}?? ?-spacing <name_or_value>? ?-start <real_value>? ?-stapling {length | auto {offset layer1_pitch:n | reference_layer1 ?reference_layer2?}}? ?-start_from {left | right | bottom | top}? ?-start_offset <real_value>? ?-stop <real_value>? ?-stop_offset <real_value>? ?-switch_layer_over_obs {0 | 1}? ?-uda <subclass_string>? ?-use_interleaving_wire_group {0 | 1}? ?-use_wire_group {-1 | 0 | 1}? ?-use_wire_group_bits <integer_value>? ?-via_rows <integer>? ?-via_columns <integer>? ?-width <name_or_value>?",
        ),
        # man1/addTieHiLo.1
        _syn(
            "addTieHiLo",
            "Adds instances of specified tie-off cells to the logical hierarchy of the design and connects the tie-off pins of netlist instances to the tie-off pins of the added instances",
            "addTieHiLo ?-help? ?-cell <cellNames>? ?-createHierPort {true | false}? ?-keepExisting {true | false}? ?-matchingPDs {true | false}? ?-postMask {true | false}? ?-powerDomain <powerDomainName>? ?-prefix <prefixName>? ?-reportHierPort {true | false}? ?-cellPin <cellName:cellPin> < >| -instancePin <fileName> | -excludePin <fileName>?",
        ),
        # man1/addTSV.1
        #   WARNING: unmatched closing bracket '}' at position 688
        #   WARNING: unmatched closing bracket '}' at position 870
        _syn(
            "addTSV",
            "Adds TSVs, front-side bumps, and backside bumps under specified conditions",
            "addTSV ?-help? ?-noRouteBlkg? {?-frontBump <bumpCellName>? ?-backBump <bumpCellName>? ?-tsvViaName <viaName>?} ?-frontBump <bumpCellName> ?-loc_type {geometry_center|cell_center} -prefix <prefixName>? ?-stackViaUnderBump <stack‐ ViaName>?? ?-backBump <bumpCellName> ?-loc_type {geometry_center|cell_center} -prefix <prefixName>?? ?-tsvViaName <viaName> ?-noPlaceBlkg | -spacing s? ???-tsvFeedthru {x y} ?-stackViaTopLayer <layer>?? | ?-stripeNet <pgnetName> -stripeLayer <layerNum>?? | ?-stackViaName <stackViaName> ?-stackViaMarkerLayer <markerLayerName>??-stack_via_array {x y} -stack_via_pitch {x y}???? {-lowerLeftLoc {x y}} ?-relative_bump_cell <bumpCell> | -relative_selected_bump?} {?-pitchxy {x y}? ?-relative_bump_cell <bumpCell> | -rela‐ tive_selected_bump?} {?-upperRightLoc {x y} | -numxy {x y}? ?-relative_bump_cell <bumpCell> | -relative_selected_bump?}} ?{-relative_bump_cell <bumpCell> | -relative_selected_bump } ?-relative_min_pitch <float>? ?-relative_offset {x y}? ?-rel‐ ative_bump_type {signal power ground}?? ?-perim <n>? ?-stagger?",
        ),
        # man1/addWellTap.1
        #   WARNING: bracket mismatch: '{' at position 681 closed by ']' at position 694
        #   WARNING: unclosed bracket '[' at position 627
        _syn(
            "addWellTap",
            "Adds physical-only well-tap cells",
            "addWellTap ?-help? ?-area <x1> <y1> <x2> <y2>? ?-avoidAbutment? ?-cell <cellName>? ?-cellInterval <microns>? ?-channel_offset <offset_value>? ?-checkerBoard? ?-fixedGap? ?-inRowOffset <microns>? ?{-check_channel | -vertical_boundary_spacing <spacing_with_well_tap> | -incremental <list_of_cells>}? ?-powerDomain <powerDomainName>? ?-prefix <prefixName>? ?-siteOffset <number_of_sites>? ?-skipRow <number>? ?-startRowNum <number>? ?{{-termination_cell <termination_cell_list> | {-top_termination_cell <cell_list> -bottom_termination_cell <cell_list>}} -column_cell <tap_column_cell_list>} ?-block_boundary_only {true | false}?? ?{-wellCutCell <list_of_well_cut_cells>} ?-fixCutCell {true | false?? ?-pitch <microns> ?-pitchOffset <microns>?? ?{-insert_cells <list_of_cells> | -incremental <list_of_cells>}? ?-safety_tmr ?-safety_tmr_insts <instance_list>??",
        ),
        # man1/adjustFPlanChannel.1
        _syn(
            "adjustFPlanChannel",
            "Automatically adjusts the channel width between objects to prevent potential routing congestion",
            "adjustFPlanChannel ?-help? ?-channelUtil <utilizationValue>? ?-constraints <constraint_file>? ?-moveOnly? ?-report <output_file>? ?-reportOnly ?-report_low_utilized_channels <value>? ?-type {all fenceToFence fenceToCore fenceToMacro macroToMacro macroToCore}??",
        ),
        # man1/alias.1
        _syn(
            "alias",
            "Create command aliases for any Tcl command",
            "alias ?-help? <new_cmd> <old_cmd> ?-args {{<new> <old>} ...}?",
        ),
        # man1/alignObject.1
        _syn(
            "alignObject",
            "",
            "alignObject ?-help? -side {right | left | center | top | bottom | middle} ?-referToFirst? ?-mix?",
        ),
        # man1/alignPtnClone.1
        _syn(
            "alignPtnClone",
            "Aligns partition clones with the master partition on a power mesh and with routing tracks",
            "alignPtnClone ?-help? ?<ptnName>? ?-outFile <filename>? ?-checkOnly | -snapAllCorners? ??-stripeOffset? | ??-pgHGrid? ?-pgVGrid? ?-pgLayer {<layeridList>}? ?-updateUserGrid? ?-snapAllCorners? ?-skipFinFETGrid? ?-includeStdCellPinLayers {<layeridList>}?? | ??-symmetryPatternReference <string>?-symmetryPatternTarget <string>??-targetOrientation {R0 R90 R180 R270 MX MX90 MY MY90}? ?-targetOrigin {<x y>}????? | ?-symmetricOrientation?? ?-pgLayer {<layeridList>} ?-pgNet <pgNetName> | -pgCenterLine <float>?? ?-pgPitch <float>?-pgCenterLine <float>??",
        ),
        # man1/all_analysis_views.1
        _syn(
            "all_analysis_views",
            "Returns a Tcl list of analysis views in the design, according to type",
            "all_analysis_views ?-help? ?-type <string>?",
        ),
        # man1/all_clocks.1
        _syn(
            "all_clocks",
            "",
            "all_clocks ?-help?",
        ),
        # man1/all_connected.1
        _syn(
            "all_connected",
            "",
            "all_connected ?-help? ?-leaf? <single_object_collection_or_object>",
        ),
        # man1/all_constraint_modes.1
        _syn(
            "all_constraint_modes",
            "Returns a Tcl list of all defined constraint modes in the design",
            "all_constraint_modes ?-active | -active_setup | -active_hold?",
        ),
        # man1/all_delay_corners.1
        _syn(
            "all_delay_corners",
            "Returns a Tcl list of all defined delay calculation corner objects in the design",
            "all_delay_corners ?-help? ?-active?",
        ),
        # man1/all_fanin.1
        _syn(
            "all_fanin",
            "Returns a collection of pins, ports, or cells that exist in the fanin cone of the specified objects",
            "all_fanin ?-help? ?-hpin? ?-only_cells? ?-startpoints_only? -to {collection | <object_list>} ?-trace_through {case_disable | user_disable | all | clocks | loop_snipped}? ?-view <view_name>? ?-levels <value> | -pin_levels <value>? ?> | >>?",
        ),
        # man1/all_fanout.1
        _syn(
            "all_fanout",
            "Returns a collection of pins, ports, or cells that exist in the fanout cone of the specified objects",
            "all_fanout ?-help? ?-endpoints_only? ?-hpin? ?-only_cells? ?-trace_through {case_disable | user_disable | all | clocks | loop_snipped}? ?-view <view_name>? ?-levels <value> | -pin_levels <value>? {-from {collection | <object_list>} } ?> | >>?",
        ),
        # man1/all_hold_analysis_views.1
        _syn(
            "all_hold_analysis_views",
            "Returns a Tcl list of all active hold analysis views in the design",
            "all_hold_analysis_views",
        ),
        # man1/all_inputs.1
        _syn(
            "all_inputs",
            "Creates a collection of all the input ports in the current design",
            "all_inputs ?help? ?-clock list_of_<clocks>? ?-no_clocks? ?-edge_triggered? ?-level_sensitive?",
        ),
        # man1/all_instances.1
        _syn(
            "all_instances",
            "",
            "all_instances ?-help? <object> ?-hierarchical?",
        ),
        # man1/all_library_sets.1
        _syn(
            "all_library_sets",
            "Returns a Tcl list of all currently defined library sets in the design",
            "all_library_sets",
        ),
        # man1/all_op_conds.1
        _syn(
            "all_op_conds",
            "Returns a Tcl list of all operating conditions defined for the design",
            "all_op_conds",
        ),
        # man1/all_outputs.1
        _syn(
            "all_outputs",
            "Creates a collection of all output ports in the current design",
            "all_outputs ?-help? ?-clock <list_of_clocks>? ?-edge_triggered? ?-level_sensitive?",
        ),
        # man1/all_rc_corners.1
        _syn(
            "all_rc_corners",
            "Returns a Tcl list of all currently defined RC corner objects in the design",
            "all_rc_corners ?-help? ?-active?",
        ),
        # man1/all_registers.1
        _syn(
            "all_registers",
            "",
            "all_registers ?help? ?-clock {<clock_list>}? ?-cells? ?-rise_clock {<clock_list>}? ?-fall_clock {<clock_list>}? ?-flops | -edge_triggered? ?-no_hierarchy? ?-latches | -level_sensitive? ?-macros? ?-master_slave? ?-data_pins? ?-clock_pins? ?-output_pins? ?-async_pins? ?-slave_clock_pins?",
        ),
        # man1/all_setup_analysis_views.1
        _syn(
            "all_setup_analysis_views",
            "Returns a Tcl list of all active setup analysis views in the design",
            "all_setup_analysis_views",
        ),
        # man1/analyze_esd_network.1
        _syn(
            "analyze_esd_network",
            "Performs different types of effective resistance checks, such as bump to clamp, bump to bump, and clamp to clamp, and current density analysis during an ESD zap event",
            "analyze_esd_network ?-help? <<run_name>> ?-clamp_lowest_layer_taps {true | false}? ?-clamp_pin_short_file <pin_shorting_file>? -config_file <rule_filename> ?-output <directory>? ?-remove_layers_below <layer_name>? ?-ta | -task_assistant? -type {net | domain} ?-use_power_pad {true | false}?",
        ),
        # man1/analyze_esd_voltage.1
        _syn(
            "analyze_esd_voltage",
            "",
            "analyze_esd_voltage ?-help? -current_distribution_layer <layer> -driver_receiver_file <filename> -esd_pin_location_file <filename> ?-maximum_violations <value>? -net<NetName> ?-report <filename>? ?-threshold <value>? -total_current <value> ?-detailed_report {true | false}?",
        ),
        # man1/analyze_ir_paths.1
        _syn(
            "analyze_ir_paths",
            "",
            "analyze_ir_paths ?-help? -clock_period <float> ?-hierarchical_activity_file <string>? ?-max_slack <float>? ?-pre_simulation_period <float>? -seq_activity <float> -simulation_period <float> ?-user_defined_critical_paths <string>?",
        ),
        # man1/analyze_joule_heat.1
        _syn(
            "analyze_joule_heat",
            "Specifies to perform joule heat analysis",
            "analyze_joule_heat ?-help? ?-detail_delta_temperature_file <filename?> ?-detail_delta_temperature_region {<x1 y1 x2 y2>}? ?-domain <rail_domain_name>? ?-net <pg_net_name>? ?-report_conn_pin_wire <filename>? ?-scale_rms_limit <value>? ?-tile_delta_temperature_file <filename>? ?-tiles {<n_tile_in_x> <m_tile_in_y>}? ?-output_directory<dir_name>?",
        ),
        # man1/analyze_package.1
        _syn(
            "analyze_package",
            "",
            "analyze_package ?-help? <<domain>> ?-computer_resources <string>? ?-output <<directoryname>>? -pkg_bga_name <<bga_circuitname>> -pkg_die_name <<die_circuitname>> -pkg_pin_current_file <<filename>> -result_name <<filename>> ?-spd_file <filename>? -type <<package_analysis_type>> -workspace <<workspace_name>>",
        ),
        # man1/analyze_paths_by_basic_path_group.1
        _syn(
            "analyze_paths_by_basic_path_group",
            "Categorizes the timing paths based on basic path groups",
            "analyze_paths_by_basic_path_group ?-help? ?-master <master_category_name>? ?-predefined?",
        ),
        # man1/analyze_paths_by_bottleneck.1
        _syn(
            "analyze_paths_by_bottleneck",
            "Creates categories according to the bottleneck analysis of the critical paths and fixes the violation according to the bottleneck information",
            "analyze_paths_by_bottleneck ?-help? {-category <n> | -incr_delay {worst|total}} ?-path_num <m>? ?-max_slack <float>? ?-min_slack <float>? ?-master <master_category_name>?",
        ),
        # man1/analyze_paths_by_clock_domain.1
        _syn(
            "analyze_paths_by_clock_domain",
            "To find the possible timing issues in clock combinations, the command creates categories according to launch clocks - capture clocks combinations",
            "analyze_paths_by_clock_domain ?-help? ?-include_edges? ?-include_views? ?-include_mode? ?-master <master_category_name>?",
        ),
        # man1/analyze_paths_by_critical_false_path.1
        _syn(
            "analyze_paths_by_critical_false_path",
            "Identifies violating false paths, which are paths that appear as violations but cannot be exercised due to the structure of the netlist, and creates a category that contains them",
            "analyze_paths_by_critical_false_path ?-help? ?-critical_false_paths {false_path_only | exclude_false_path}? ?-master <string>?",
        ),
        # man1/analyze_paths_by_drv.1
        _syn(
            "analyze_paths_by_drv",
            "Reads or generates a report containing max transition, max capacitance, and max fanout violations",
            "analyze_paths_by_drv ?-help? ??-load_cap_file <capacitance_file>? | ?-generate_cap_file <fileName>?? ??-load_tran_file <transition_file>? | ?-generate_tran_file <fileName>?? ?-load_fanout_file <fanout_file> | ?-generate_fanout_file <fileName>?? ?-master <master_category_name>?",
        ),
        # man1/analyze_paths_by_hier_port.1
        _syn(
            "analyze_paths_by_hier_port",
            "Helps you to automatically group paths based on each hierarchical port of the given instances",
            "analyze_paths_by_hier_port ?-help? {{-gen_hier_file <string> ?-out_file <string>?} | {-load_hier_file <string>}} ?-master <string>?",
        ),
        # man1/analyze_paths_by_hierarchy.1
        _syn(
            "analyze_paths_by_hierarchy",
            "Creates categories according to the hierarchical characteristics of the paths",
            "analyze_paths_by_hierarchy ?-help? ?-master <string>? {-fp_file <string> ?-include_macros?} | {-use_current_floorplan ?-all? ?-types <string>? ?-port2port? ?-port2macro? ?-port2bbox? ?-port2hinst? ?-port2stdcell? ?-port2instgrp? ?-macro2port? ?-macro2macro? ?-macro2bbox? ?-macro2hinst? ?-macro2stdcell? ?-macro2instgrp? ?-bbox2port? ?-bbox2macro? ?-bbox2bbox? ?-bbox2hinst? ?-bbox2stdcell? ?-bbox2instgrp? ?-hinst2port? ?-hinst2macro? ?-hinst2bbox? ?-hinst2hinst? ?-hinst2stdcell? ?-hinst2instgrp? ?-std‐ cell2port? ?-stdcell2macro? ?-stdcell2bbox? ?-stdcell2hinst? ?-stdcell2stdcell? ?-stdcell2instgrp? ?-instgrp2port? ?-instgrp2macro? ?-instgrp2bbox? ?-instgrp2hinst? ?-instgrp2stdcell? ?-instgrp2instgrp?} | {-partitions <string> | -macros <string>}",
        ),
        # man1/analyze_paths_by_view.1
        _syn(
            "analyze_paths_by_view",
            "Categorizes the timing paths based on views which are included in the timing debug file, also known as the violation report",
            "analyze_paths_by_view ?-help? ?-prefix string? ?-master <master_category_name>?",
        ),
        # man1/analyze_rail.1
        _syn(
            "analyze_rail",
            "Runs rail analysis on a net or domain",
            "analyze_rail ?-help? ?-type {domain | net}? ?-output <directory_name>? <name>",
        ),
        # man1/analyze_resistance.1
        _syn(
            "analyze_resistance",
            "Performs effective resistance analysis",
            "analyze_resistance ?-help? ?-cell <master_cell_name>? ?-die_mode {3dic}? ?-force_reextraction {true | false}? ?-instance_list {<instance1> <pin1> <instance2> <pin2>...}? ?-instance_list_file <filename>? ?-instance_pair_list {<instance1instance2pin1 pin2> ...}? ?-instance_pair_list_file <filename>? -net <netName> | -domain <domainName> ?-node_list {<node1> <node2>..... <METAL_LAYER> <LABEL>}? ?-node_list_file <filename>? ?-node_pair_list {<node1X> <node1Y> <METAL_LAYER1> <node2X> <node2Y> <METAL_LAYER2>...<LABEL>}? ?-node_pair_list_file <filename>? ?-output <filename>? ?-output_dir <directory_name>? ?-region {<x1> <y1> <x2> <y2> <layer> <number_of_nodes> <region_name>}? ?-report_limit <value>? ?-threshold <value>? ?-print_cell_name? ?-domain_threshold<value>? ?-net_threshold<value>? ?-exclude_list_file <filename>?",
        ),
        # man1/analyze_self_heat.1
        _syn(
            "analyze_self_heat",
            "",
            "analyze_self_heat ?-help? ?-domain <rail_domain_name>? ?-output_directory <dir_name>?",
        ),
        # man1/analyze_signal_resistance.1
        _syn(
            "analyze_signal_resistance",
            "",
            "analyze_signal_resistance ?-help? ?-instance_pair_list_file <filename>? -net <net_name> ?-output_dir <directory>? ?-report <filename>? ?-threshold <value>?",
        ),
        # man1/analyze_thermal.1
        _syn(
            "analyze_thermal",
            "Specifies to invoke Celsius Thermal Solver to run die-only thermal analysis",
            "analyze_thermal",
        ),
        # man1/aocv_chip_size.1
        _syn(
            "aocv_chip_size",
            "",
            "aocv_chip_size <real_number>",
        ),
        # man1/aocv_core_size.1
        _syn(
            "aocv_core_size",
            "",
            "aocv_core_size <real_number>",
        ),
        # man1/append_to_collection.1
        _syn(
            "append_to_collection",
            "",
            "append_to_collection ?help? <var_name> <second_collection_or_list> ?-unique?",
        ),
        # man1/apply_safety_mechanism.1
        _syn(
            "apply_safety_mechanism",
            "Maps a safety mechanism to one or more failure modes",
            "apply_safety_mechanism ?-help? <safety_mechanism> ?-generated? -to <failure_mode>",
        ),
        # man1/applyGlobalNets.1
        _syn(
            "applyGlobalNets",
            "Applies or restores the global net connectivity rules to the design and creates the necessary connec‐ tions between instances and these global nets",
            "applyGlobalNets ?-help?",
        ),
        # man1/assemble_proto_model.1
        _syn(
            "assemble_proto_model",
            "Generate full chip FlexModel netlist by assembling FlexModel partition netlists back to the toplevel design for hierarchical FlexModel generation",
            "assemble_proto_model –topdir {topDesignDir ?<protoModelDirName>?} ?-blockdir {<blockDesignDir> ?<protoModeldirName>?}? -mmmc_file <mmmcfileName> ?-cpf_file <cpfFileName>? ?-help?",
        ),
        # man1/assembleDesign.1
        _syn(
            "assembleDesign",
            "Brings back specified block data to the top-level design for chip assembly",
            "assembleDesign ?-help? ?-keepPGPinGeometry? ?-keep_block_halo? ?-outFile <fileName>? ?-skipCells? ?-skipComponents? ?-skipNets? ?-skipSpecialNets? {{?-topDir <dirname> ?-mmmcFile <mmmcFile>? ?-cpfFile <cpfFile>?? {?-blockDir <dirname> ??-fe? | ?-fplan????-blockData {<defFileName netListFileName>} | {-fplan|-fe}??-noDefMerge?}} | {?-topDesign {<topLib topCell topView>} ?-mmmcFile <mmmcFile>? ?-cpfFile <cpfFile>?? {?-block {<blockLib blockCell blockView>} | -blockCell <blockCell>? ?-allTimingBlocks ?-exceptBlocks {<list of blocks>}? ?-reportOnly??}}} ?-fe | -fplan | -noDefMerge? ?-keepPinGeometry?",
        ),
        # man1/assign_clock_tree_source_groups.1
        _syn(
            "assign_clock_tree_source_groups",
            "When used on designs with clock tree source group definitions, this command assigns clock sinks to the source group roots - multi-tap assignment - and then performs the cloning and rewiring necessary to distribute the sinks among the source group roots",
            "assign_clock_tree_source_groups ?-help? ?-no_merge?",
        ),
        # man1/assignBump.1
        _syn(
            "assignBump",
            "Assigns the bumps closest to the I/O cells, using euclidean distance, and adds bump connection target prop‐ erty onto bump",
            "assignBump ?-help? ?{-area <x1 y1 x2 y2> | -selected }? ?-constraint_file <file_name>? ?-exclude_region <llx> <lly> <urx> <ury ...>? ?-maxDistance <distance>? ?-multiBumpToMultiPad? ?{??-pgnet net_list? | ?-exclude_pgnet net_list???-pginst instance_list?} ?-pgonly??",
        ),
        # man1/assignIoPins.1
        _syn(
            "assignIoPins",
            "Assigns the top I/O pin locations for a block-level design",
            "assignIoPins ?-help? ?-align? ?-debugPinAll? ?-debugPinFile <fileName>? ?-improveSI? ?{-pin { <pinNameList> } | -pin_file <fileName> | -exclude_pin_file <fileName> } ?-moveFixedPin? ?-ig‐ nore_group_pins?? ?-autoBusGroup?",
        ),
        # man1/assignPGBumps.1
        _syn(
            "assignPGBumps",
            "Assigns power and ground bumps to connect flip chip I/O pins and adds property value onto bumps",
            "assignPGBumps ?-help? ?-connectType {ioring | corering | stripe | iopin}? -nets {<name_list>} ?-selected | -floating | -bumps {<bump_name_list>}? ?-V | -H | -checkerboard ?-square {<width height>}??",
        ),
        # man1/assignPtnPin.1
        _syn(
            "assignPtnPin",
            "Assigns partition pins before the partitions are committed",
            "assignPtnPin ?-help? ?-basedOnMasterOnly? ?-blackbox? ?-debugPinAll? ?-debugPinFile <fileName>? ?-dumpVirtualPinGuide? ?-ignoreAbuttedCheck? ?-improvePinOrder? ?-improveSI? ?-layerPriority {layeridList}? ?-markFixed? ?-printPinMovementStatistics? ?-skipAutoBusBitOrder? ?-skipPlaceExternalUnconnectedPin? ?-unplacedOnly? ?<partitionName> | {{{-ptn <partitionName> {-pin {pinName list}}} | {-pin_file <fileName> ?-exclude_ptn <ptnName>?} | {-exclude_pin_file <ptnName>}} ?-moveFixedPin? ?-ignore_group_pins?}? ?-alignFeedThruPinsOptWithMasterClone? ?-autoBusGroup? ?-enforceRoute | -enforceRouteLegal | -enforceFlyline?",
        ),
        # man1/assignSigToBump.1
        _syn(
            "assignSigToBump",
            "Assigns selected or specified bumps to the specified net or pin",
            "assignSigToBump ?-help? { {{-net <net_name> | {-top_pin <port> ?-bump_pin <bump_pin_name>?}} {-bumps <bump_name_list> | -selected}} }",
        ),
        # man1/assignTSV.1
        _syn(
            "assignTSV",
            "Assigns nets to TSVs and/or frontside and backside bumps, and/or feedthrus",
            "assignTSV ?-help? ?-write_down_level_bump? ?-selected <netName> | ??-signal | -pgpad? ?-feedthru | -nonFeedthru? ?-net <netlist> | -exclude_net <excludeNetList>? ?-area <llx lly urx ury ...>? ?-exclude_region <llx lly urx ury ...>? ?-tsvViaName <tsvViaCellName>? ?-interposer??? ?{?-backBump? ?-frontBump?} ?-force_current_die??",
        ),
        # man1/attachDiode.1
        _syn(
            "attachDiode",
            "Adds an antenna diode to a post-routed design",
            "attachDiode ?-help? ?-prefix <prefix>? -diodeCell <diodeCellName> -pin <instName><termName> ?-loc <x><y> ?-orient <orient>??",
        ),
        # man1/attachIOBuffer.1
        _syn(
            "attachIOBuffer",
            "Adds buffers/inverters to the I/O pins of a block and places the buffers/inverters near the I/O pins",
            "attachIOBuffer ?-help? ?-baseName <baseName>? ?-dishonorUpfDomainBoundaryCheckForIsoLsStrategy? ?-excNetFile <excNetFileName>? ?-excludeClockNet? ?-port? ?-prePlace? ?-selNetFile <selNetFileName>? ?-skipRefinePlace? ?-suffix <suffixName>? {?-in <cellNameList>? ?-out <cellNameList>?} ?-status {placed fixed softfixed}?",
        ),
        # man1/attachModulePort.1
        _syn(
            "attachModulePort",
            "Attaches a port in the specified hinst (or top level) to a net",
            "attachModulePort ?-help? <moduleName> <portName> <netName> ?-noNewPort?",
        ),
        # man1/attachTerm.1
        _syn(
            "attachTerm",
            "Attaches a terminal to a net",
            "attachTerm ?-help? ?-moduleBased <verilogModule>? ?-noNewPort? <instName> <termName> <netName> ?-port <portName>? ?-pin <refInstName><refPinName>?",
        ),
        # man1/auto_file_dir.1
        _syn(
            "auto_file_dir",
            "",
            "auto_file_dir <directoryName>",
        ),
        # man1/auto_file_prefix.1
        _syn(
            "auto_file_prefix",
            "",
            "auto_file_prefix",
        ),
        # man1/bindKey.1
        _syn(
            "bindKey",
            "Enables you to create keyboard shortcuts",
            "bindKey <key><cmd> ?-help?",
        ),
        # man1/bit_blasted_port_style.1
        _syn(
            "bit_blasted_port_style",
            "",
            "bit_blasted_port_style %s_%d",
        ),
        # man1/bitblast_ports.1
        _syn(
            "bitblast_ports",
            "Bitblasts the specified port bus (or hport bus) of the specified design, module, or module of the speci‐ fied hinst, so they are scalars rather than bus-bits",
            "bitblast_ports ?-help? <topCell>|<vCell|hInst>+ ?-bus <busname>?",
        ),
        # man1/calculate_ccopt_cannot_clone_reason.1
        _syn(
            "calculate_ccopt_cannot_clone_reason",
            "Returns a Tcl list of reasons why the specified instance cannot be cloned in CTS",
            "calculate_ccopt_cannot_clone_reason ?-help? -inst <instName>",
        ),
        # man1/calculate_didt.1
        _syn(
            "calculate_didt",
            "Generates the on-die di/dt information from an existing dynamic rail analysis run and saves it in a text file",
            "calculate_didt ?-help? -net_name <net_name> -nworst <value> -state_directory <dir> ?-window_steps <value> | -window_size <value>?",
        ),
        # man1/calculate_differential_voltage.1
        _syn(
            "calculate_differential_voltage",
            "Determines the differential voltage between a receiver/driver pair during ramp-up analy‐ sis",
            "calculate_differential_voltage ?-help? -diffv_limit <value> -power_directory <directory_name> -state_directory <directory_name>",
        ),
        # man1/calculate_noise_margin.1
        _syn(
            "calculate_noise_margin",
            "Specifies to calculate noise margins with worst voltages on the driver-receiver pins",
            "calculate_noise_margin ?-help? -noise_limit_file <input_file> -power_directory <dir> -state_directory <dir>",
        ),
        # man1/calNegSlack.1
        _syn(
            "calNegSlack",
            "",
            "calNegSlack",
        ),
        # man1/ccopt_add_exclusion_drivers.1
        _syn(
            "ccopt_add_exclusion_drivers",
            "Removes the excluded sinks from the clock trees by adding exclusion drivers above these sinks",
            "ccopt_add_exclusion_drivers ?-help? ?-lib_cell list_library_cells?",
        ),
        # man1/ccopt_design.1
        _syn(
            "ccopt_design",
            "Performs clock concurrent optimization (CCOpt) on the current loaded design in Innovus",
            "ccopt_design ?-help? ?-check_prerequisites? ?-ckSpec? ?-cts? ?-expandedViews? ?-num_paths <number_of_paths>? ?-outDir <dirname>? ?-prefix <fileNamePrefix>? ?-timing_debug_report?",
        ),
        # man1/ccopt_pro.1
        _syn(
            "ccopt_pro",
            "Repairs clock tree design rule violations (DRVs) and skews that have occurred in the clock tree across a rout‐ ing step",
            "ccopt_pro ?-help? ?-enable_average_id_reduction {true | false}? ?-enable_downsizing_pass {true | false}? ?-enable_drv_fixing {true | false}? ?-enable_drv_fixing_by_rebuffering {true | false}? ?-enable_refine_place {true | false}? ?-enable_routing_eco {true | false}? ?-enable_skew_fixing {true | false}? ?-enable_skew_fixing_by_rebuffering {true | false}?",
        ),
        # man1/cds_lib.1
        _syn(
            "cds_lib",
            "",
            "",
        ),
        # man1/change_IB_cell_site_name.1
        _syn(
            "change_IB_cell_site_name",
            "Change sites for the cells whose site definitions do not match the site definitions used by In‐ novus",
            "change_IB_cell_site_name ?-help? ?-NF <site_name>? ?-NNF <site_name>? ?-PF <site_name>? ?-PPF <site_name>? ?-new <site_name>? ?-original <site_name>? ?-vertical?",
        ),
        # man1/changeBBoxMasterFromR0.1
        _syn(
            "changeBBoxMasterFromR0",
            "Converts the orientation of the master instance blackboxes from R0 to the specified orientation",
            "changeBBoxMasterFromR0 ?-help? <black_box_cell> {R90 R180 R270 MX MX90 MY MY90} <new_x_origin><new_y_origin>",
        ),
        # man1/changeBBoxMasterToR0.1
        _syn(
            "changeBBoxMasterToR0",
            "Converts the orientation of the master instance blackboxes to R0",
            "changeBBoxMasterToR0 ?-help? ?-checkOnly? ?<cellName> | {<cellNameList>}?",
        ),
        # man1/changeBumpMaster.1
        _syn(
            "changeBumpMaster",
            "Enables you to replace the cell master for specified bumps",
            "changeBumpMaster ?-help? -bumpMasterName <bumpMasterName> ?-fromBumpMasterName <bumpMasterName>? ?-location_type {cell_center cell_lowerleft geometry_center geometry_lowerleft}? {-netName <netName> | -allBumps | -bump_name <bump_list> | -selected}",
        ),
        # man1/changeCurrentDesign.1
        _syn(
            "changeCurrentDesign",
            "Changes the partition view",
            "changeCurrentDesign ?-help? ?<ptnName>?",
        ),
        # man1/changeFloorplan.1
        _syn(
            "changeFloorplan",
            "Changes the distances between the core box and the die box on the sides you specified",
            "changeFloorplan ?-help? ?-noSnapToGrid? ??-coreToLeft <value>??-coreToBottom <value>??-coreToRight <value>??-coreToTop <value>? | ?-coreToEdge {left bottom right top}??",
        ),
        # man1/changeIoConstraints.1
        _syn(
            "changeIoConstraints",
            "Changes the constraints of an I/O row defined in the I/O constraint file",
            "changeIoConstraints ?-help? ?-forceIt? ?-ioOrder {clockwise | counterclockwise | default} | -row <string>? ?-spacing <num> | -removeSpacing? ?-endSpace <num> | -removeEndSpace? ?-firstCellSpacing <float>| -removeFirstCellSpacing? ?-removeAll?",
        ),
        # man1/check_base_layer_density.1
        _syn(
            "check_base_layer_density",
            "Checks the CPODE density by the defined pattern",
            "check_base_layer_density ?-help? ?-layer <layerName>? ?-site_parameter <sitePara>?",
        ),
        # man1/check_bus_guides.1
        _syn(
            "check_bus_guides",
            "Checks bus guides for violations during master-clone-aware net group implementation flow",
            "check_bus_guides ?-help? ?-net_groups <list_of_net_groups>? ?-outFile <file_name>?",
        ),
        # man1/check_ccopt_clock_tree_convergence.1
        _syn(
            "check_ccopt_clock_tree_convergence",
            "This command is used to trigger a warning message for sinks that have more than the specified number of convergence paths from the clock sources to the sink",
            "check_ccopt_clock_tree_convergence ?-help? ?-warnthreshold <thresholdValue>?",
        ),
        # man1/check_ccr.1
        _syn(
            "check_ccr",
            "Enables users to check if a CCR (Cadence Change Request) created on their behalf is checked into the current release or not",
            "check_ccr ?-help? <ccr_number>",
        ),
        # man1/check_design.1
        #   WARNING: bracket mismatch: '[' at position 45 closed by '}' at position 257
        #   WARNING: bracket mismatch: '{' at position 44 closed by ']' at position 258
        #   WARNING: unmatched closing bracket '}' at position 272
        _syn(
            "check_design",
            "Checks that all prerequisites to run all or part of the hierarchical or block implementation flow are met",
            "check_design ?-help? ?-out_file <fileName>? {?-type {library netlist power_intent timing hierarchical pin_assign budget assign_statements place opt cts route signoff all} |-type_3d {tech_lib netlist power_intent timing place floorplan route report_only all}}? ?-no_check?}",
        ),
        # man1/check_design_across_hierarchy.1
        _syn(
            "check_design_across_hierarchy",
            "",
            "check_design_across_hierarchy {true | false}",
        ),
        # man1/check_design_report_async_pins.1
        _syn(
            "check_design_report_async_pins",
            "",
            "check_design_report_async_pins {true | false}",
        ),
        # man1/check_design_report_scan_pins.1
        _syn(
            "check_design_report_scan_pins",
            "",
            "check_design_report_scan_pins {true | false}",
        ),
        # man1/check_design_threshold_fanout.1
        _syn(
            "check_design_threshold_fanout",
            "",
            "check_design_threshold_fanout {true | false}",
        ),
        # man1/check_instance_library_in_views.1
        _syn(
            "check_instance_library_in_views",
            "Checks for missing libraries for instances in the active view",
            "check_instance_library_in_views",
        ),
        # man1/check_ldb_version.1
        _syn(
            "check_ldb_version",
            "Reports the LDB version, size, and the source of the software that is used to generate the library database (LDB) file",
            "check_ldb_version -ldb<string> ?-help?",
        ),
        # man1/check_library.1
        _syn(
            "check_library",
            "Checks the problematic cells that cause issues such as bad geometries for DRC and bad pin access for rout‐ ing",
            "check_library ?-help? ?-place ?-cell <cell_name>|-all_lib_cell??-legal_frequency? ?-file <fileName>??",
        ),
        # man1/check_macro_place_constraint.1
        _syn(
            "check_macro_place_constraint",
            "Checks the constraints of macros which will be honored during the macro placer",
            "check_macro_place_constraint ?-help?",
        ),
        # man1/check_module_model.1
        _syn(
            "check_module_model",
            "Checks and validates an ILM model to see if the current reduction ratio will cause any missing con‐ straints at the hinst terminal or any slack difference",
            "check_module_model ?-help? -cell <cell_name> ?-out_file <file_name>? -ref_tag <tag_name> ?-slack_threshold <threshold>? ?-type {flexIlm ilm pnr}?",
        ),
        # man1/check_noise.1
        _syn(
            "check_noise",
            "Performs several consistency and completeness checks on noise models specified for a design",
            "check_noise ?-help? ?-all? ?-check_only {receiver_no_propagation_model | receiver_no_dc_tolerence | driver_no_current_source_model | driver_no_model}? ?-instance_list <string>? ?-instance_only {true | false}? ?-pin_list <string>? ?-type {receiver_model | driver_model}? ?-unique {true | false}? ?-verbose? ?-view <string>? ??> | >>? <filename>?",
        ),
        # man1/check_pg_library.1
        _syn(
            "check_pg_library",
            "Specifies to perform a comprehensive check of power-grid views (PGV) to be used in rail analysis",
            "check_pg_library ?-help? <power_library_paths> ?-cell_list_file<file>? ?-check_compatibility {<PGV1 PGV2 ...>} | -lef_consistency? ?-check_parameters? ?-integrity_check? ?-output <file>? ?-list? ?-report? ?-rule_file <file>? ?-skip_signal_net_check {true | false}? ?-skip_layer_list_file <filename>? ?-summary? ?-tap_node_text_dump? ?-tech_layers? ?-total_currents? ?-report_detail_multiple_voltage_cap? ?-command_dump? ?-metal_density_map?",
        ),
        # man1/check_power_intent.1
        _syn(
            "check_power_intent",
            "Checks the IEEE1801 power intent coding style for the IEEE1801 partitioning",
            "check_power_intent ?-help?",
        ),
        # man1/check_safety_mechanism.1
        _syn(
            "check_safety_mechanism",
            "Checks all the safety mechanisms and prints a report, optionally writing it to the specified file as well",
            "check_safety_mechanism ?-help? ?-checks_exclude <file_ex>? ?-detailed? ?-flow_phase {prects cts route}? ?-out_file <file_name>? ?-type {dcls ser tmr}?",
        ),
        # man1/check_syntax.1
        _syn(
            "check_syntax",
            "Does the “lint type” checking of Innovus Tcl script files",
            "check_syntax ?-help? ?<file1.tcl> <file2.tcl> ...? ?<nagelfar.tcl options>? ?-options? ?-out_file <fileName>?",
        ),
        # man1/check_tcic.1
        _syn(
            "check_tcic",
            "Checks the floorplan based on the specified tCIC files and reports violations",
            "check_tcic ?-help? ?<filename>? ?-pre_opt? ?-report_area? ?-report_file <filename>? ?-report_unplaced_block? ?-include_all_rules? ?-selected_rules <rule_name>?",
        ),
        # man1/check_timing.1
        _syn(
            "check_timing",
            "Performs a variety of consistency and completeness checks on the timing constraints specified for a design",
            "check_timing ?-type <type_list>? ?-verbose? ?-check_only <warning_list>? ?-clock_crossing_output_format {summary | csv}? ?-include_warning <warning_list>? ?-exclude_warning <warning_list>? ?-view <analysis_view_name>? ?<port_or_pin_list>? ?-tcl_list? ?{> | >> } <file_name>?.gz??",
        ),
        # man1/check_tracks.1
        _syn(
            "check_tracks",
            "Checks a predefined set of tracks to verify their routing track offset, direction, and grid",
            "check_tracks ?-help? ?-direction {horiz | vert | H | V}? ?-grid <spacing>? ?-layer <layer_name>? ?-mask <mask_name>? ?-offset <string>? ?-origin {design | core | D | C}?",
        ),
        # man1/check_ufc.1
        _syn(
            "check_ufc",
            "Checks the floorplan based on the user specified UFC rules defined in the UFC file and reports violations",
            "check_ufc ?-help? <fileName> ?-include_all_rules? ?-report_file <string>? ?-report_unplaced_block? ?-selected_rules <string>?",
        ),
        # man1/checkBondPadSpacing.1
        _syn(
            "checkBondPadSpacing",
            "Checks for bond pad spacing violations after using thespaceBondPad command",
            "checkBondPadSpacing ?-help?",
        ),
        # man1/checkBump.1
        _syn(
            "checkBump",
            "Checks the legality of the bump assignment and creates a report, which is either displayed in the console win‐ dow or written to a file",
            "checkBump ?-help? ?-bumpToPinOverlap <inst>+? ?-outfile <fileName>? ?-resetViolationMarker? ?-select_violation_bumps? ?-selected | -area {<x1 y1 x2 y2>}? ?-relative_type {embedded_bump inst_pin_port} ??-relative_object {<inst_pin_port_list>}? ?-relative_assignment? ?-rela‐ tive_offset <x y>??? ???-relative_type {embedded_bump inst_pin_port}? ?-bumpToPinPitch {<pitch_value> {?<bump_name>? ?<inst_pin_name> ?<pin_x pin_y>??}}?? | -nets <net+>? ?-bumpToEdgePitch <pitch_value> ?-edgeOffset {offset ?cornerOffset?}?? ???-bumpPitch {<pitch_value> ?<bump_name>?}? ?-bumpToPinPitch {<pitch_value> {?<bump_name>? ?<inst_pin_name> ?<pin_x pin_y>??}}?? | -bumpMaxPitch <max_pitch_value> | -bumpToEdgePitch <pitch_value>? ?-onBumpGrid ?-onBumpGridTolerance <bump_grid_name value>??",
        ),
        # man1/checkDesign.1
        _syn(
            "checkDesign",
            "Checks for missing or inconsistent library and design data at any stage of the design and writes the results to a text and HTML report",
            "checkDesign ?-help? { -all ?-danglingNet ?highlight?? | ??-io? ?-netlist ?-danglingNet ?highlight??? ?-physicalLibrary? ?-timingLibrary? ?-powerGround? ?-tieHiLo? ?-floorplan? ?-place? ?-spef??-assigns?? } ??-noText? ?-outdir directoryName? ?-browser?? | ?-noHtml ?-outfile fileName??",
        ),
        # man1/checkFiller.1
        _syn(
            "checkFiller",
            "Checks for locations that are missing filler cells, after adding the cells with the addFiller command",
            "checkFiller ?-help? ?-area <llx lly urx ury>? ?-file <fileName>? ?-horizontal_max_length? ?-powerDomain <power_domain_name>? ?-vertical_stack_max_length? ?-reportGap <microns>| -adjacentFiller1?",
        ),
        # man1/checkFootPrint.1
        _syn(
            "checkFootPrint",
            "",
            "checkFootPrint ?-help?",
        ),
        # man1/checkFPlan.1
        _syn(
            "checkFPlan",
            "Checks the quality of the floorplan to detect potential problems before the design is passed on to other tools",
            "checkFPlan ?-help? ?-keep_out_distance <value>? ?-outFile <fileName>? ?-reportUtil?",
        ),
        # man1/checkFPlanSpace.1
        _syn(
            "checkFPlanSpace",
            "Checks the floorplan for spacing rule violations and saves the violation information in a report",
            "checkFPlanSpace ?-help? ?-outfile <filename>? ?-constraints <filename> | -trackUtil <layerID value layerID value ...>? ?-clearMarker?",
        ),
        # man1/checkHierRoute.1
        _syn(
            "checkHierRoute",
            "Checks and reports hierarchy violations for nets in the specified partitions",
            "checkHierRoute ?-help? ?-ptn {<ptnName> | <ptnList>}? ?-outFile <outputFileName>?",
        ),
        # man1/checkMacroLLOnTrack.1
        _syn(
            "checkMacroLLOnTrack",
            "By default, checks whether the lower left coordinates (llx, lly) of hard macros are at the intersec‐ tion of Metal1/Metal2 tracks, and reports an error in Innovus if they are not",
            "checkMacroLLOnTrack ?-help?",
        ),
        # man1/checkMultiCpuUsage.1
        _syn(
            "checkMultiCpuUsage",
            "Checks if distributed processing can work in the software environment",
            "checkMultiCpuUsage ?-help?",
        ),
        # man1/checkNetlist.1
        _syn(
            "checkNetlist",
            "Performs several checks on the design netlist and creates a report",
            "checkNetlist -outfile <filename> ?-includeSubModule?",
        ),
        # man1/checkPartitionSdc.1
        _syn(
            "checkPartitionSdc",
            "When you generate the timing budgets for partitions using the deriveTimingBudget command, the check‐ PartitionSdc command validates the results",
            "checkPartitionSdc ?-help? {?-chip <string> -partition_dir <string>? | ?-chip <string> -module_model_tag <string> ?-add_ons <string>? ?-accumulated? ?-overwrite_tag?? | ?-compare_only?} ?-cells <string>? ?-master_only? ?-no_top? ?-out_dir <string>? ?-validate_boundary_condition?",
        ),
        # man1/checkPinAssignment.1
        _syn(
            "checkPinAssignment",
            "",
            "checkPinAssignment ?-help? ?-outFile <fileName>? ?-reportSameNetPinAsOverlap? ?-reportUncoloredViolation? ?<topCellName> | -ptn <partitionName list>? ?-ptn <partitionName list> | {-pin_file <fileName> ?-exclude_ptn <fileName>?} | -exclude_pin_file <fileName>? ?-report_violating_pin? ?-ignore {bus_guide net_group pin_abutment pin_depth pin_group pin_guide pin_layer pin_min_area pin_on_fence pin_on_track pin_spacing pin_spacing_constraint pin_spacing_routeBlk pin_width clones logical_pin pin_color unplaced}? ??-preCheck ?-skipCheck {overlap layer spacingConstraint fixedIoPins multiTermNet masterClone netGroup connection rela‐ tiveOrientRelation gridTrackAlignment symmetryOffset masterCloneSize alignZone}? ?-excludeNetFile <fileName>?? | { ?-ptn <partitionName list?> ?-pin {<pinName list>}? ?-pin_file <fileName>? ?-exclude_pin_file <fileName>? ?-ignore {bus_guide net_group pin_abutment pin_depth pin_group pin_guide pin_layer pin_min_area pin_on_fence pin_on_track pin_spacing pin_spacing_constraint pin_spacing_routeBlk pin_width clones logical_pin pin_color unplaced}? ?-report_violating_pin? ?-exclude_ptn <fileName>?}?",
        ),
        # man1/checkPlace.1
        _syn(
            "checkPlace",
            "Checks FIXED and PLACED cells for violations, adds violation markers to the design display area, and gener‐ ates a violation report",
            "checkPlace ?<violationReportFileName>? ?-clearMarker? ?-honorPrerouteForFiller? ?-ignoreFillerInUtil? ?-ignoreOutOfCore? ?-inst <list_of_instances>? ?-ioPinBlockage? ?-macroBlockage? ?-noCheckPinAccess? ?-noHardFence? ?-noHalo? ?-noPreplaced? ?-selectedOnly?",
        ),
        # man1/checkSdpGroup.1
        _syn(
            "checkSdpGroup",
            "Checks current SDP placement against the SDP constraints, such as order, alignment, and orientation, which may have been originally specified via an SDP relative placement file or a set of TCL commands and reports violations",
            "checkSdpGroup ?-help? ?-file <fileName>? ?-sdpGroups {<sdp_name>...}?",
        ),
        # man1/checkTimingLibrary.1
        _syn(
            "checkTimingLibrary",
            "Checks the contents of the timing library and reports any inconsistencies in a log file",
            "checkTimingLibrary ?-outfile <string>? ?-cellName <string>? ?-library <string>? ?-checkPower? ?-reportMissingPowerOnly?",
        ),
        # man1/checkTQuantusModelFile.1
        _syn(
            "checkTQuantusModelFile",
            "",
            "checkTQuantusModelFile ?-help?",
        ),
        # man1/checkUnique.1
        _syn(
            "checkUnique",
            "Checks the uniqueness of the netlist",
            "checkUnique ?-help? ?-verbose?",
        ),
        # man1/checkWhatIfTiming.1
        _syn(
            "checkWhatIfTiming",
            "Checks that at least one timing arc is defined for every port of a blackbox or blackblob",
            "checkWhatIfTiming <blackBoxCellName> ?-outfile <fileName>?",
        ),
        # man1/ciopLoadBumpColorMapFile.1
        _syn(
            "ciopLoadBumpColorMapFile",
            "Loads the bump color map file to change the color of assigned bumps",
            "ciopLoadBumpColorMapFile ?-help? <bumpColorFile>",
        ),
        # man1/cleanupExcludeNet.1
        _syn(
            "cleanupExcludeNet",
            "",
            "cleanupExcludeNet ?-help?",
        ),
        # man1/clearActiveLogicView.1
        _syn(
            "clearActiveLogicView",
            "Resets the reduced timing graph created by createActiveLogicView back to the original timing graph",
            "clearActiveLogicView ?-help?",
        ),
        # man1/clearAllRulers.1
        _syn(
            "clearAllRulers",
            "",
            "clearAllRulers -help",
        ),
        # man1/clearDeCapCellCandidates.1
        _syn(
            "clearDeCapCellCandidates",
            "",
            "clearDeCapCellCandidates ?-help?",
        ),
        # man1/clearDrc.1
        _syn(
            "clearDrc",
            "Clears all design rule checking (DRC) markers in your design",
            "clearDrc ?-help?",
        ),
        # man1/clearGlobalNets.1
        _syn(
            "clearGlobalNets",
            "Resets the logical power net connection",
            "clearGlobalNets ?-help?",
        ),
        # man1/clearScanDisplay.1
        _syn(
            "clearScanDisplay",
            "Removes scan chains from the display",
            "clearScanDisplay ?-help? ?<chain_name>?",
        ),
        # man1/clearSpareCellDisplay.1
        _syn(
            "clearSpareCellDisplay",
            "Removes spare cell instances from the display",
            "clearSpareCellDisplay",
        ),
        # man1/clock_opt_design.1
        _syn(
            "clock_opt_design",
            "The clock_opt_design command is used in place of ccopt_design when the input DB is place_opt_design V2 (PODV2 or pod-turbo)",
            "clock_opt_design ?-help? ?-check_cts_config? ?-cts? ?-expandedViews? ?-num_paths <number_of_paths>? ?-out_dir <dirname>? ?-prefix <fileNamePrefix>? ?-timing_debug_report?",
        ),
        # man1/cloneMSVGate.1
        _syn(
            "cloneMSVGate",
            "Ensures that the cloned isolation or level shifter can drive a group of the receivers and be placed close to this group of receivers",
            "cloneMSVGate ?-help? ?-iso? ?-shifter? ?-instances <inst1 inst2 ....>? ?-maxFanout <integer>? ?-maxTran <num>? ?-maxCap <num>? ?-honorPrePlaced? ?-honorDontTouch?",
        ),
        # man1/clonePlace.1
        _syn(
            "clonePlace",
            "Places all clone instances with relative location and relative orientation according to the master partition instances",
            "clonePlace ?-help? ?-clone_list <cloneinstance(s)orientation(s)>? ?-master_inst <instance name>?",
        ),
        # man1/clonePtnObj.1
        _syn(
            "clonePtnObj",
            "Syncs up the changes made to the specified objects in the master or clone partitions in the design with other hierarchical instances (master and clones) of the same module",
            "clonePtnObj ?-help? ?-checkOnly? ?-objs {all busGuides}? ?-redo? ?-refHinsts <list_of_hinst_names>? ?-sync? ?-targetHinsts <list_of_hinst_names>? ?-undo?",
        ),
        # man1/close_ctd_win.1
        _syn(
            "close_ctd_win",
            "Closes open CTD windows",
            "close_ctd_win ?-help? ?-all | -id <WindowIDName>?",
        ),
        # man1/colorize_cell_library.1
        _syn(
            "colorize_cell_library",
            "Colors each standard cell in the library, using the pre-color method",
            "colorize_cell_library ?-help? ?-cell <cell_name>? ??-reset? | ?-enforce??",
        ),
        # man1/colorizePowerMesh.1
        _syn(
            "colorizePowerMesh",
            "",
            "colorizePowerMesh ?-help? ?-reverse_with_nondefault_width {0 | 1}?",
        ),
        # man1/commit_ccopt_clock_tree_route_attributes.1
        _syn(
            "commit_ccopt_clock_tree_route_attributes",
            "The command traces the clock tree as defined by the CCOpt spec and sets net at‐ tributes to allow early-global-route to more predictably model clock nets",
            "commit_ccopt_clock_tree_route_attributes ?-help? ?-verbose?",
        ),
        # man1/commit_module_model.1
        _syn(
            "commit_module_model",
            "Commits module models",
            "commit_module_model ?-help? ?-copy_mmmc_latencies? ?-merged_mmmc_map_file <mapFiles>? ?-merged_mmmc_sdc_files <mergedSdcFiles>? ?-mmmc_file <fullChipSdc>? ?-mmmc_module_model_tag <modelTag>? ?-propagate_clocks? ?-cpf_file <filename >| -1801 <filename>?",
        ),
        # man1/commit_power_intent.1
        _syn(
            "commit_power_intent",
            "Commits IEEE1801 power intent specifications for the design for use in verification and implementa‐ tion of the structure and behavior of the design in context of a given power management architecture",
            "commit_power_intent ?-help? ?-clpLog <string>? ?-eco <string>? ?-isolation? ?-keepRows? ?-level_shifter? ?-power_domain? ?-power_switch? ?-state_retention? ?-verbose?",
        ),
        # man1/commit_pushdown_eco.1
        _syn(
            "commit_pushdown_eco",
            "Commits ECO for a partition block by applying ECO and generating a database for the block",
            "commit_pushdown_eco ?-help? -eco_object_dir <dirName> -post_eco_dir <dirName> -pre_eco_dir <dirName> ?-ptns <ptnNameList>?",
        ),
        # man1/compare_cellview.1
        _syn(
            "compare_cellview",
            "Compares the boundary and terminal (name, direction, layer, location, size, and port) of the specified cell views",
            "compare_cellview ?-help? ?-ignore {pin_purpose}? ?-log <report_file_name>? { {{-source {<from_lib from_cell from_view>} -compare {<to_lib to_cell to_view>}} | {-lib <lib> -cell <cell> -view {<sourceView compareView>}}} }",
        ),
        # man1/compare_collections.1
        _syn(
            "compare_collections",
            "",
            "compare_collections ?-help? <collection1><collection2> ?-order_dependent?",
        ),
        # man1/compare_instance_obs.1
        _syn(
            "compare_instance_obs",
            "Compares a layer's instance obstruction shape of the current design in the memory with the speci‐ fied reference file",
            "compare_instance_obs ?-help? <ref_obs_shape_file>?-report <file_name>?",
        ),
        # man1/compare_model_timing.1
        _syn(
            "compare_model_timing",
            "Compares two reports that contain interface timing characteristics generated by the write_model_timing command",
            "compare_model_timing",
        ),
        # man1/compare_power_intent.1
        _syn(
            "compare_power_intent",
            "Compares the golden IEEE1801 and the hierarchical IEEE1801 files generated by the Innovus hierar‐ chical partition flow in terms of the low power database, and reports the mismatched category",
            "compare_power_intent ?-help? ?-domain_attr? ?-domain_boundary_port_constr? ?-domain_map_file <file_name>? ?-file_prefix <prefix>? -golden1801 <file_name> -hier1801 <file_name> ?-pin_effective_domain? ?-power_domains <list_of_domains>? ?-verbose?",
        ),
        # man1/compare_release.1
        _syn(
            "compare_release",
            "Compares two different releases and reports all the added, deleted, or modified commands, arguments, and global variables",
            "compare_release ?-help? ?-out_file <file_name>? {-base_version <release_version> | -base_file <file_name>} ?-target_version <release_version> | -target_file <file_name>?",
        ),
        # man1/comparePinAssignStatistics.1
        _syn(
            "comparePinAssignStatistics",
            "Generates a pin QoR comparison file based on a reference and a target pin QoR file",
            "comparePinAssignStatistics ?-help? ?-ignoreMinWireLength <minWireLength>? ?-outFile <pinQoRCompareFileNam> <e>? -reference <referenceFileName>-target <targetFileName>",
        ),
        # man1/compress_special.1
        _syn(
            "compress_special",
            "Compresses Power-Grid (PG) based on the specified area, layer, or net",
            "compress_special ?-help? ?-area {<x1 y1 x2 y2>}? ?-incremental? ?-layers <layer>+? ?-nets <net>+?",
        ),
        # man1/congRepair.1
        _syn(
            "congRepair",
            "Relieves the congestion of the design",
            "congRepair",
        ),
        # man1/connect_clock_tree_mesh_drivers.1
        _syn(
            "connect_clock_tree_mesh_drivers",
            "Uses the specified set of drivers and merges the nets at their outputs to form a single multi-driven net",
            "connect_clock_tree_mesh_drivers ?-help? ?-driver_pins <pin_names>? ?-driver_source_group <source_group_name>?",
        ),
        # man1/connectMacroFeedthrough.1
        _syn(
            "connectMacroFeedthrough",
            "Connects predefined feedthrough pins in custom macros to overlapping nets that have wires cross‐ ing over the custom macros, based on the routing information",
            "connectMacroFeedthrough ?-help? ?-selectNet <string> | -excludeNet <string> | -selectMarkedNet? ?-selectInst <string> | -excludeInst <string>? ?-ecoFile <string> | -checkOnly? ?-portMap <string>? ?-verbose? ?-maxSearchDistance <float?> ?-searchAllSides? ?-abutment <float>? ?-abutmentFile <string>? ?-floatingPortList <string>?",
        ),
        # man1/convert_gds_to_def.1
        _syn(
            "convert_gds_to_def",
            "A GDS2DEF utility that converts a given GDSII file to a DEF file for power/rail signoff analysis",
            "convert_gds_to_def ?-help? ?-black_box_cell_file <filename>? -gds_file <filename> -gds_layermap <filename> ?-inst_name_file <filename>? -net_location_file <filename> ?-output_components {ALL | NONE | CONN}? -output_def_file <filename> ?-output_lef_macros <filename>? -power_grid_library <libraryname> -top_cell <cellname> ?-use_gds_label {ALL | TOP | <<tech_layer_name>> | <<cell_name>>:<<tech_layer_name>> | <<cell_name>>:ALL}? ?-verilog_file <filename>? ?-spef_file<filename>? ?-esd_marker_layer_file <filename>? ?-esd_cell_bbox_file <filename>? ?-inst_name_prefix <prefix>? ?-ignore_gds_inst_name? ?-print_complete_short_path? ?-extract_signal_net_logic_info_only? ?-zero_pin_size?",
        ),
        # man1/convert_lib_clock_tree_latencies.1
        _syn(
            "convert_lib_clock_tree_latencies",
            "Converts the Liberty max_clock_tree_path and min_clock_tree_path (MCTP) data to per-pin clock latency adjustments",
            "convert_lib_clock_tree_latencies ?-help? ?-latency_file_prefix <prefix_name>? ?-pins <pin_list>? ?-views <view_list>? ?-override_existing_latencies | -sum_existing_latencies? ?-sum_existing_latencies | -override_existing_latencies_pins <pin_list>? ?-override_existing_latencies | -sum_existing_latencies_pins <pin_list>? ?-sum_existing_latencies | -sum_existing_latencies_pins <pin_list>? ?-override_existing_latencies | -override_existing_latencies_pins <pin_list>?",
        ),
        # man1/convertBlackBoxToFence.1
        _syn(
            "convertBlackBoxToFence",
            "Converts a blackbox to a fence",
            "convertBlackBoxToFence ?-help? {-cell <cellName> | -inst <instName>}",
        ),
        # man1/convertFenceToBlackBox.1
        _syn(
            "convertFenceToBlackBox",
            "Converts a fence to a blackbox",
            "convertFenceToBlackBox ?-help? {-cell <cellName> | -hinst <hinstName>} ?-noRebuildTiming? ?-size { <x><y> }?",
        ),
        # man1/convertFenceToLef.1
        _syn(
            "convertFenceToLef",
            "Converts a specified hierarchical instance or partition name to a LEF block",
            "convertFenceToLef ?-help?",
        ),
        # man1/copy_bump.1
        _syn(
            "copy_bump",
            "Copies bumps to the specified location with the same pitch constraint",
            "copy_bump ?-help? ?-assigned? ?-name_format {format}? -shift {X Y} {-bumps {bump_list} | -selected }",
        ),
        # man1/copy_collection.1
        _syn(
            "copy_collection",
            "",
            "copy_collection ?-help? <base_collection>",
        ),
        # man1/copyOaRestoreFiles.1
        _syn(
            "copyOaRestoreFiles",
            "Copies Innovus-specific restore files from one OpenAccess database to another",
            "copyOaRestoreFiles <fromLib fromCell fromView> <toLib toCell toView>",
        ),
        # man1/copyObject.1
        _syn(
            "copyObject",
            "",
            "copyObject ?-help?",
        ),
        # man1/create_analysis_view.1
        _syn(
            "create_analysis_view",
            "Creates an analysis view object that associates a delay calculation corner with a constraint mode",
            "create_analysis_view -name <viewName> -constraint_mode <modeName> -delay_corner <dcCornerObj>",
        ),
        # man1/create_buffer_psPM_table.1
        _syn(
            "create_buffer_psPM_table",
            "",
            "create_buffer_psPM_table ?-help? ?-buffers <string>? ?-file <string>? ?-inverters <string>? ?-layer <string>? -max_target_slew <float>-min_target_slew <float>?-rpt_file <string>? ?-slew_interval <float>?",
        ),
        # man1/create_bump.1
        _syn(
            "create_bump",
            "Creates bumps and instances of bump cells based on the specified pattern",
            "create_bump ?-help? ?-allow_outside_of_die? ?-allow_overlap_control {keep_all keep_existing_bumps keep_new_bumps}? -cell <bumpcell_name> ?-check_drc? ?-edge_spacing {<left bottom right top>}? ?-exclude_bump_area {<rect_list>}? ??-keep_out_region <width height>? | ?-keep_out_pitch <value>?? ?-loc <x y>? ?-loc_type {cell_center | cell_lowerleft | geometry_center | geometry_lowerleft}? ?-name_format {<string>, %i, %r, %c}? ?-orientation {R0 R90 R180 R270 MX MX90 MY MY90}? ?-respect_placement_blockage? ?-return_bumps_name? ?-start_index <index>? ?-pitch <x y> ?-pattern_full_chip | -pattern_side {<side width>} | -pattern_array {<row column>} | -pattern_ring <width> | -pattern_center {<row column>}?? ?-stagger_type <type> ?-stagger_offset <value>?? ?-relative_type {embedded_bump inst_pin_port block} ??-relative_object {<inst_pin_port_list>}? ?-relative_block <inst>+? ?-relative_block_constraint <fileName>? ?-relative_assignment? ?-relative_offset <x y>??? ?{-pattern_full_chip | -pattern_array {<row column>} | -pattern_center {<row column>}} ?-start_from {lower_left up‐ per_left lower_right upper_right}??",
        ),
        # man1/create_bump_cluster.1
        _syn(
            "create_bump_cluster",
            "Creates bump clusters according to region, layer, pitch, and size",
            "create_bump_cluster ?-help? ?-area {<x1 y1 x2 y2>}? ?-enclosure {<a b>}? -layer <name> -pitch {<x y>} -size {<n m>} ??-type {signal | power | ground}? | ?-nets {<net>+}??",
        ),
        # man1/create_bump_grid.1
        _syn(
            "create_bump_grid",
            "Creates a bump grid",
            "create_bump_grid ?-help? -grid_name <string> -layers <string> -origin {<x y>} -pitch {<x y>}",
        ),
        # man1/create_ccopt_clock_spine.1
        _syn(
            "create_ccopt_clock_spine",
            "Creates a CCOpt spine object",
            "create_ccopt_clock_spine ?-help? ?-hard? -name <spinename> ?-x <x>? ?-xmax <xmax>? ?-xmin <xmin>? ?-y <y>? ?-ymax <ymax>? ?-ymin <ymin>?",
        ),
        # man1/create_ccopt_clock_tree.1
        _syn(
            "create_ccopt_clock_tree",
            "Defines a new clock tree within the design",
            "create_ccopt_clock_tree ?-help? ?-name <clockname>? ?-no_skew_group? -source <pin> ?-stop_at_sdc_clock_roots?",
        ),
        # man1/create_ccopt_clock_tree_source_group.1
        _syn(
            "create_ccopt_clock_tree_source_group",
            "Creates a clock tree source group",
            "create_ccopt_clock_tree_source_group ?-help? -clock_trees <clock_tree_list> -name <clock_tree_source_group_name>",
        ),
        # man1/create_ccopt_clock_tree_spec.1
        _syn(
            "create_ccopt_clock_tree_spec",
            "Creates a clock tree network with associated skew groups and other clock tree synthesis (CTS) configuration settings such as ignore pins, case analysis, maxTrans, and so on based on a multi-mode timing configu‐ ration in the common timing engine (CTE)",
            "create_ccopt_clock_tree_spec ?-help? ?-file <filename>? ?-keep_all_sdc_clocks? ?-views <viewList>?",
        ),
        # man1/create_ccopt_flexible_htree.1
        _syn(
            "create_ccopt_flexible_htree",
            "Creates a design object for a flexible H-tree, under the specified pin",
            "create_ccopt_flexible_htree ?-help? ?-adjust_sink_grid_for_aspect_ratio {true | false}? -final_cell <base_cell> ?-hv_balance {true | false}? ?-image_directory <dirName>? ?-inverting? ?-layer_density <value>? ?-max_driver_distance <value>? ?-max_root_distance <value>? ?-mode {drv | distance}? -name <flexibleHtreeName> ?-omit_symmetry <string>? ?-partition_boundary_polarity {non_inverting | inverting | ignore}? ?-partition_groups {{partition ...} ?max_boundary_net_length? ?inverting | non_inverting? ?subtree? ...}? ?-power_weight <value>? -pin {pin | port} ?-sink_grid {columns rows}? ?-sink_grid_box {<xmin ymin xmax ymax>}? ?-sink_grid_exclusion_zones {{<xmin ymin xmax ymax>} ...}sink_grid_exclusion_zones? ?-sink_instance_prefix <prefixName>? ?-sink_grid_sink_area {width height}? ?-sinks {{pin_name | {<xmin ymin xmax ymax>}} ...}? ?-stop_at_sdc_clock_roots? -trunk_cell <base_cell>",
        ),
        # man1/create_ccopt_generated_clock_tree.1
        _syn(
            "create_ccopt_generated_clock_tree",
            "Defines a generated clock tree within the design",
            "create_ccopt_generated_clock_tree ?-help? ?-generated_by pins? ?-name <clockname>? ?-parents <parents>? ?-search_method <method>? -source <pin> ?-stop_at_sdc_clock_roots?",
        ),
        # man1/create_ccopt_macro_model_spec.1
        _syn(
            "create_ccopt_macro_model_spec",
            "This command is used to view, or edit, the pin insertion delays for CCOpt derived from the macro model specification",
            "create_ccopt_macro_model_spec ?-help? ?-ckSpec? ?-ediCtsSpecForMacroModels <fileName>? ?-file <filename>?",
        ),
        # man1/create_ccopt_preferred_cell_stripe.1
        _syn(
            "create_ccopt_preferred_cell_stripe",
            "This command creates an object that corresponds to a single preferred_cell_stripe",
            "create_ccopt_preferred_cell_stripe ?-help? -bbox {xmin xmax ymin ymax} -cells <list_of_cells> -name <name>",
        ),
        # man1/create_ccopt_skew_group.1
        _syn(
            "create_ccopt_skew_group",
            "Creates a new skew group within the design",
            "create_ccopt_skew_group ?-help? ?-constrains none| default | all? ?-from_clocks <clock_names>? ?-from_constraint_modes <constraint_mode_names>? ?-from_delay_corners <delay_corner_names>? -name <skew_group_name> ?-rank <rank>? ?-sinks <pins> | -shared_sinks pins | -exclusive_sinks pins | -auto_sinks | -filtered_auto_sinks <pins> | -bal‐ ance_skew_groups <skew_groups>? ?-sources <pins> | -balance_skew_groups <skew_groups>? ?-target_insertion_delay <value>? ?-target_skew <value>?",
        ),
        # man1/create_clock.1
        _syn(
            "create_clock",
            "Creates a clock object and defines its waveform in the current design",
            "create_clock -period <period_value> ?-name <clock_name>? ?-waveform <edge_list>? ?-add? ?-comment <string>? ?<sources>?",
        ),
        # man1/create_constraint_mode.1
        _syn(
            "create_constraint_mode",
            "",
            "create_constraint_mode -name <modeName> -sdc_files {<file1>.sdc <file2>.sdc ...} ?-ilm_sdc_files {<file1>.sdc <file2>.sdc ...}? ?-tcl_vars {{<var_name1> <value1>} {<var_name2> <value2>} {<var_name3> <value3>} ...}?",
        ),
        # man1/create_current_region.1
        _syn(
            "create_current_region",
            "Specifies static or dynamic current regions on global power-grids over the placed macro to accu‐ rately capture high and low current consuming regions during rail analysis",
            "create_current_region ?-help? -reset | {-region <x1 y1 x2 y2> ?-current <value>| -current_pwl_file<filename>? ?-die_instance_name <dieinstname>? ?-file <filename>? ?-label <name>? ?-layer <layername>? ?-intrinsic_cap <value>? ?-loading_cap <value>? ?-series_resistance<value>? ?-net<net_name>? ?-polygon {<x1> <y1> <x2> <y2> <x3> <y3> ..<x1> <y1>}? ?-pwrnet<net_name>? ?-gndnet<net_name>? }",
        ),
        # man1/create_delay_corner.1
        _syn(
            "create_delay_corner",
            "",
            "create_delay_corner ?-help? ?-early_estimated_worst_irdrop_factor <percent>? ?-late_estimated_worst_irdrop_factor <percent>? -name <delayCornerName> ?-si_enabled true | false? { { ?-library_set <libSetObj>? | ?-late_library_set <libSetObj >-early_library_set <libSetObj >? } ?-opcond_library <libName >? ?-opcond <opcondName>? ?-pg_net_voltages <voltage_pairs>? ?-rc_corner <rcCornerObj >| ?-late_rc_corner <rcCornerObj >-early_rc_corner <rcCornerObj>?? ?-irdrop_file <list_of_files >| -irdrop_data <files_or_directories>? ?-late_opcond_library <libName>? ?-early_estimated_worst_irDrop_factor <percent>? ?-early_opcond_library <libName>? ?-late_opcond <opCondName>? ?-early_opcond <opCondName>? ?-late_estimated_worst_irDrop_factor <percent>? ??-late_irdrop_file <list_of_files >-early_irdrop_file <libSetObj>? | ?-late_irdrop_data <files_or_directories >-early_ir‐ drop_data <files_or_directories>?? ?-temp_file <tempName> | ?-late_temp_file <tempName >-early_temp_file <tempName>?? }",
        ),
        # man1/create_die_model.1
        _syn(
            "create_die_model",
            "Specifies to generate a reduced n-port die model in the form of equivalent die parasitic and current profile after rail analysis to perform system-level analysis with extracted package and board models",
            "create_die_model ?-accuracy {xd | hd }? ?-output_directory <directory_name>? -state_directory <directory_name> ?-rail_analysis_domain <domain_name> | -net <net_name>? ?-repeat <time>? ?-probing_node_file <file_name>? ?-use_sigrity_repeat? ?-max_ports_per_net <integer>? ?-enable_reference_node? ?-enable_package_pin_map { true|false }? ?-disable_isrc_node_zero { true|false }? ?-disable_global_node_zero { true|false }? ?-multi_die {true | false}? ?-port_grouping_by_ploc_files { true|false }? ?-port_grouping_file<filename>? ?-temp_directory_name <directory>? ?-effective_rc? ?-probing_region_file<filename>? ?-effective_rc_deck? ?-port_grouping_tiles_file <filename>? ?-enable_xp {true | false}? ?-ignore_port_grouping_conflict? ?-generate_sipi_port_definition_file {true | false}? ?-grid_reduction_cut_layer <layer_name>?",
        ),
        # man1/create_esubpart.1
        _syn(
            "create_esubpart",
            "Creates an elementary subpart, which is the smallest hardware subpart considered in safety analysis",
            "create_esubpart ?-help? <esp> ?-description <description>? -inst <string> -register_endpoint <string>",
        ),
        # man1/create_failure_mode.1
        _syn(
            "create_failure_mode",
            "Defines a failure mode",
            "create_failure_mode ?-help? <FailureMode> ?-attributes <string>? ?-description <description>? ?-exclude_hinst <string>? ?-exclude_inst <string>? {?-esubpart <string>? ?-group <string>? ?-hinst <string>? ?-inst <string>? ?-pin <string>? ?-current_design? ?-subpart <string>?} ?-esubpart <string>| -current_design? ?-group <string>| -current_design | -subpart <string>? ?-hinst <string> | -current_design? ?-inst <string> | -current_design? ?-pin <string> | -current_design?",
        ),
        # man1/create_flexfiller_route_blockage.1
        _syn(
            "create_flexfiller_route_blockage",
            "Generates default congestion model to estimate routing blockages over FlexFillers based on user-specified percentage value for characterizing",
            "create_flexfiller_route_blockage ?-help?",
        ),
        # man1/create_generated_clock.1
        _syn(
            "create_generated_clock",
            "Creates a new clock signal from the clock waveform of a given pin in the design, and binds it with the pins or hierarchical pins in the <target_pin_list> argument",
            "create_generated_clock ?-help? <target_pin_list> ?-add? ?-comment <string>? ?-duty_cycle <percent>? ?-edge_shift <edge_shift_list>? ?-invert? ?-master_clock <source_clock_name>? ?-name <<clock_name>>? -source <source_pin> {?-multiply_by <factor>? ?-divide_by <factor>? ?-edges <edge_list>? ?-combinational?}",
        ),
        # man1/create_hier_view.1
        _syn(
            "create_hier_view",
            "",
            "create_hier_view ?-help? -library_name <name> ?-output_dir <dir>? ?-block_lef <lef_file>|-block_gds <gds_file>? ?-block_lef <lef_file> | -gds_port_file <gds_port_file>? ?-libgen_command_file <file>? ?-max_viacluster_mode {true | false}? ?-extraction_mode {fast | accurate}? ?-cell_name <name>? ?-def <list_of_DEF_files>? ?-oaRef <OA_reference_libs>? ?-powergrid_view_libraries <primitive_cells.cl>? ?-ground_nets {<pin1><pin2> ...<pinN>}? ?-power_nets {<pin1><value1><pin2><value2> ...<pinN><valueN>}? ?-extraction_work_directory <path_to_extraction_work_directory>? ?-compress_powergrid_database {true | false}? ?-parasitic_extractor_command_file <filename>? ?–cluster_via1_ports {true | false}? ?-cluster_via_rule { {<via_layer1> <number_of_equidistant_vias>}...}? ?-cluster_via_size <value>? ?–ignore_fillers {true | false}? ?–ignore_decaps {true | false}? ?–ignore_shorts {true | false}? ?-force_library_merging{true | false}?",
        ),
        # man1/create_histogram_png.1
        _syn(
            "create_histogram_png",
            "Dumps out the timing histogram image from global timing debug in the PNG format without bringing up the GUI",
            "create_histogram_png ?-help? ?-height <integer>? -name <string> ?-width <integer>?",
        ),
        # man1/create_inst_space_group.1
        _syn(
            "create_inst_space_group",
            "Creates space group for instances with a specific vertical or horizontal-distance constraint",
            "create_inst_space_group ?-help? <groupName> -inst <listOfInstances> {?{?-spacing_y <Distance>? ?-spacing_x <Distance>?} ?-checking_box {all|cross_only}?? | ?-spacing_radial <Distance>?}",
        ),
        # man1/create_interposer_route_block.1
        _syn(
            "create_interposer_route_block",
            "Creates the master block",
            "create_interposer_route_block ?-help? -cell <cell_name> -dir <dir_name> -inst <master_name>?{-box {<x1 y1 x2 y2>} | -polygon {<x1 y1 x2 y2 ...>} | -rects {{<lx1 ly1 ux1 uy1>} {<lx2 ly2 ux2 uy2>}...}}?",
        ),
        # man1/create_library_set.1
        _syn(
            "create_library_set",
            "Associates a TCL list of timing and cdB/UDN libraries with a specified library set name",
            "create_library_set ?-help? ?-aocv <string>? ?-library_side_file <string>? -name <libSetName> ?-si <string>? ?-socv <string>? ?-timing <string>?",
        ),
        # man1/create_module_model.1
        _syn(
            "create_module_model",
            "Creates a module model",
            "create_module_model ?-help? ?-allow_port_mismatch? ?-cell<string>? ?-phys_hier? ?-tag <tag_name>? ?-type {1801 boundary_model etm extraction_context flexIlm ilm latency lef mmmc pin_assign pnr pnr_shell scan_info spef timing_context gds}?",
        ),
        # man1/create_op_cond.1
        _syn(
            "create_op_cond",
            "Creates a set of virtual operating conditions in the specified library without actually modifying the li‐ brary",
            "create_op_cond -name <virtualOpcondName> -library_file <libraryFileName> -P <processValue> -V <voltageValue> -T <temperatureValue>",
        ),
        # man1/create_parasitic_coordinate_transform.1
        _syn(
            "create_parasitic_coordinate_transform",
            "Determines accurate location information of nodes during SPEF reading",
            "create_parasitic_coordinate_transform ?-help? {-inst <inst_name> ?-x_block_origin <value>? ?-x_offset< value>? ?-y_block_origin <value>? ?-y_offset <value>? ?-orient {R0 R90 R180 R270 MY MX90 MX MY90}? ?-relative_to_parent?} | {-reset}",
        ),
        # man1/create_partition_wrapper.1
        _syn(
            "create_partition_wrapper",
            "Creates a wrapper partition that embeds the specified partition cell to preserve its verilog module definition in the netlist",
            "create_partition_wrapper ?-help? -partitions <partition_names>?-pushdown? ?-wrapper_name <wrapper_suffix_string>?",
        ),
        # man1/create_path_category.1
        _syn(
            "create_path_category",
            "Creates path categories using conditions for grouping paths according to analyzed timing results",
            "create_path_category ?-help? ?-capture_latency <string>? ?-check_type <string>? ?-clock <string>? ?-comment <string>? ?-critical_false_path <string>? ?-delay_of_any_inst <string>? ?-delay_of_any_inst_not_of_celltype <string>? ?-delay_of_any_inst_not_of_name <string>? ?-delay_of_any_inst_of_celltype <string>? ?-delay_of_any_inst_of_name <string>? ?-delay_of_any_net <string>? ?-delay_of_any_net_not_of_name <string>? ?-delay_of_any_net_of_name <string>? ?-delay_of_every_inst <string>? ?-delay_of_every_inst_not_of_celltype <string>? ?-delay_of_every_inst_not_of_name <string>? ?-delay_of_every_inst_of_celltype <string>? ?-delay_of_every_inst_of_name <string>? ?-delay_of_every_net <string>? ?-delay_of_every_net_not_of_name <string>? ?-delay_of_every_net_of_name <string>? ?-file string? ?-from_cell <string>? ?-from_clock <string>? ?-from_clock_edge <string>? ?-from_inst <string>? ?-from_inst_pointer <string>? ?-from_pd <string>? ?-from_pin <string>? ?-from_port <string>? ?-from_port_pointer <string>? ?-incr_delay_of_any_net <string>? ?-incr_delay_of_every_net <string>? ?-launch_latency <string>? ?-master <string>? ?-name <string>? ?-not_from_cell <string>? ?-not_from_clock <string>? ?-not_from_clock_edge <string>? ?-not_from_inst <string>? ?-not_from_pd <string>? ?-not_from_pin <string>? ?-not_from_port <string>? ?-not_through_cell <string>? ?-not_through_inst <string>? ?-not_through_net <string>? ?-not_through_pd <string>? ?-not_through_pin <string>? ?-not_through_port <string>? ?-not_to_cell <string>? ?-not_to_clock <string>? ?-not_to_clock_edge <string>? ?-not_to_inst <string>? ?-not_to_pd <string>? ?-not_to_pin <string>? ?-not_to_port <string>? ?-number_of_insts <string>? ?-number_of_insts_not_of_celltype <string>? ?-number_of_insts_not_of_name <string>? ?-number_of_insts_of_celltype <string>? ?-number_of_insts_of_name <string>? ?-overwrite? ?-sdc <string>? ?-skew <string>? ?-slack <string>? ?-through_cell <string>? ?-through_inst <string>? ?-through_net <string>? ?-through_pd <string>? ?-through_pin <string>? ?-through_port <string>? ?-to_cell <string>? ?-to_clock <string>? ?-to_clock_edge <string>? ?-to_inst <string>? ?-to_inst_pointer <string>? ?-to_pd <string>? ?-to_pin <string>? ?-to_port <string>? ?-to_port_pointer <string>? ?-total_delay_of_insts <string>? ?-total_delay_of_insts_not_of_celltype <string>? ?-total_delay_of_insts_not_of_name <string>? ?-total_delay_of_insts_of_celltype <string>? ?-total_delay_of_insts_of_name <string>? ?-total_delay_of_level_of_chain_of_insttype <string>? ?-total_delay_of_nets <string>? ?-total_delay_of_nets_not_of_name <string>? ?-total_delay_of_nets_of_name <string>? ?-total_delay_of_path <string>? ?-total_incr_delay_of_path <string>? ?-uncertainty <string>? ?-view <string>?",
        ),
        # man1/create_pg_model_for_macro_place.1
        _syn(
            "create_pg_model_for_macro_place",
            "Enables you to create pg models for the concurrent macro placement",
            "create_pg_model_for_macro_place ?-help? {-file <string>}",
        ),
        # man1/create_physical_partitions.1
        _syn(
            "create_physical_partitions",
            "Creates temporary logic hierarchies for hierarchical placement and routing implementation based on the existing cell and macro placement or based on the specified hierarchical instances and/or instances",
            "create_physical_partitions ?-help? {{<partition_spec> | -logical_spec <spec>} ?-group_instance_suffix <string>? ?-check_only? ??-undo ?-pre_full_upf <string >?-incremental_block_upfs <string>????}",
        ),
        # man1/create_power_pads.1
        _syn(
            "create_power_pads",
            "Returns a list of DC sources from your design",
            "create_power_pads ?-append_to_vsrc_file? ?-auto_fetch? ?-cell {<cell_list>}? ?-cell_pin {{<cellname1> <pinname1}>...{<cellnamen> <pinnamen>}+}? ?-clear? ?-display? ?-format {padcell xy tsv}? ?-honor_pin_connection? ?-instance {<inst_list>}? ?-instance_pin {{<instname1> <pinname1}>...{<instnamen> <pinnamen>}+}? ?-layer {<layername>}? ?-net <netname>? ?-package_resistance <value>? ?-package_capacitance <value>? ?-package_inductance <value>? ?-region {<x1> <y1> <x2> <y2>}? ?-region_pitch {<xpitch> <ypitch>}? ?-snap_distance { true|false }? ?-vsrc_file <vsrc_filename>? ??-add | -delete? -loc {x y}? ?-list?",
        ),
        # man1/create_property_alias.1
        _syn(
            "create_property_alias",
            "Creates a property alias for the selected objects",
            "create_property_alias ?-help? -map <alias_propery_name_pairs> -obj_type {pin port cell net clock lib_cell lib_pin design lib timing_path timing_point timing_arc path_group lib_tim‐ ing_arc si_victim si_attacker lib_pg_pin pg_pin pg_net}",
        ),
        # man1/create_proto_model.1
        _syn(
            "create_proto_model",
            "Creates prototyping models for the modules or instance groups that are marked as FlexModels on a disk",
            "create_proto_model ?-help? ?-keep_inst_file <string>? ??-out_dir <string>? ?-module_model_tag <string>??",
        ),
        # man1/create_ps_per_micron_model.1
        _syn(
            "create_ps_per_micron_model",
            "Derives psPM.model as a separate command",
            "create_ps_per_micron_model ?-help? ?-overwrite?",
        ),
        # man1/create_pushdown_eco.1
        _syn(
            "create_pushdown_eco",
            "Creates logical and physical ECO files that are used to push down ECO objects by comparing two par‐ tition databases",
            "create_pushdown_eco ?-help? ?-gen_script_only? ?-ptn_net_dir <ptnNetDirName>? ?-ptns <ptnNameList>? {-original_dir <originalDirName> | -original_tag <tagName> } {-pushdown_dir <pushdownDirName> | -pushdown_tag <tagName> } ?-eco_object_dir <outputDirName> | -eco_tag <tagName>?",
        ),
        # man1/create_rc_corner.1
        _syn(
            "create_rc_corner",
            "Creates a named RC corner object that can be referenced later when creating a delay calculation corner object",
            "create_rc_corner",
        ),
        # man1/create_relative_floorplan.1
        _syn(
            "create_relative_floorplan",
            "The create_relative_floorplan command captures and defines the placement relationship of floorplan objects independently from the actual coordinates in a floorplan, and resizes modules or blackboxes based on other floorplan objects, even outside the core boundary",
            "create_relative_floorplan ?-help? {{{-place <obj_name_list> | -reshape <obj_name_list>} ?-ref ref_<obj_name_list>?}} ?-place <obj_name_list> {-ref_type {{object core_boundary die_boundary}...} -horizontal_edge_separate {{<ref_edge_horizontal y_offset obj_edge_horizontal>}...} -vertical_edge_separate {{<ref_edge_vertical x_offset obj_edge_vertical>}...}} ??-bbox {{none target reference both}...}? ?-orient {{R0 R90 R180 R270 MX MY MX90 MY90}...}??? ?-reshape <obj_name_list> { -dimension {{<width height>}...} } ??-fixed_edges {{<edge1 edge2>}...}? ?-density< >{<value>}? ?-offset {<value>}???",
        ),
        # man1/create_route_type.1
        _syn(
            "create_route_type",
            "Creates a new route type and sets the routing properties for the nets",
            "create_route_type ?-help? ?-em_ndr_dist <float>? ?-em_ndr_rule <rule_name>? ?-min_stack_layer <layer>? -name <string> ?-one_side_spacing_range <bottomLayerNum:topLayerNum>? ?-prefer_multi_cut_via? ?-shield_side {one_side | both_side}? ?-shield_tap_instance_insertion_effort {none | standard | high}? ?-stack_distance <float>? ??-non_default_rule <ndr_name>? ?-shield_net <net_name>? ?-bottom_shield_layer <layer>? ?-top_preferred_layer <layer>? ?-bottom_preferred_layer <layer>? ?-preferred_routing_layer_effort {low | medium | high}?? ?-mask <mask_number> ?-layer_mask_range <bottomLayerNum:topLayerNum>??",
        ),
        # man1/create_safety_mechanism.1
        _syn(
            "create_safety_mechanism",
            "Defines a new safety mechanism",
            "create_safety_mechanism ?-help? <safety_mechanism> ?-class {aou hw sw aou_hw aou_sw}? ?-description <description>? ?-type {tmr dcls ser parity}?",
        ),
        # man1/create_spice_deck.1
        _syn(
            "create_spice_deck",
            "Generates the SPICE trace for a path",
            "create_spice_deck ?-help? ?-add_driver_for_constraint_check {true | false}? ?-add_side_load_measurement {true | false}? ?-add_voltage_for_missing_sensitization? ?-bbox_cells <string>? ?-constraint_check {true | false}? ?-depth <integer>? ?-enable_arrival_measurements {true | false}? ?-enable_fast_simulation {true | false}? ?-enable_mis {tied_input | independent_input | none}? ?-enable_spectre_x {true | false}? ?-exclude_side_load_cells <string>? ?-exclude_side_load_cells_for_missing_subckt {true | false}? ?-force_delete_output_dir? ?-file_prefix <string>? ?-format <string>? ?-from <string>? ?-from_fall <string>? ?-from_rise <string>? ?-glitch_simulation_mode {input_output | output}? ?-ground <string>? ?-include_cell_variation {true | false}? ?-lsf_job_string <string>? ?-measure_point {all | path | stage}? ?-merge_spice_deck {true | false}? ?-mc_simulation_init_args <string>? ?-mc_simulation_tran_args <string>? ?-model_file <string>? ?-no_hard_stop_at_to_pins {true | false}? ?-outdir <string>? ?-power <string>? ?-receiver_pin <string>? ?-report_noise <string>? ?-report_timing <string>? ?-run_simulation? ?-segment {data_path | launch_path | launch_clock_path | capture_path all}? ?-segment_end <string>? ?-segment_start <string>? ?-side_path_level <integer>? ?-spectre <string>? ?-spectre_analysis_options <string>? ?-spectre_cmd_options <string>? ?-spectre_lang_escape_chars <string>? ?-spice_include <string>? ?-stimuli_file <string>? ?-subckt_file <string>? ?-supply_voltage_file <string>? ?-sweep_range <float>? ?-sweep_steps <integer>? ?-sweep_victim {true | false}? ?-temperature <float>? ?-through <string>? ?-to <string>? ?-use_control_param {true | false}? ?-use_distributed_load_for_side_receivers {true | false}? ?-user_defined_measure_statements {append | overwrite}? ?-user_defined_measure_statements_file <string>? ?-use_ndw_for_constraint_check {true | false}? ?-waveform_aware_pulse_width_checks {true | false}? ?-view <string>? ?-xtalk {delay | vl_glitch | vh_glitch | vlu_glitch | vho_glitch}? ??> | >>??",
        ),
        # man1/create_stress_rule.1
        _syn(
            "create_stress_rule",
            "Defines a spacing table for spacing rules",
            "create_stress_rule ?-help? { {-layer <layerName> -spacing_table <spacing_table> ?-chip_name <chipName>?} | ?-reset? }",
        ),
        # man1/create_subpart.1
        _syn(
            "create_subpart",
            "Creates a subpart, which is used to model a Dual Core Lockstep (DCLS) group in safety analysis",
            "create_subpart ?-help? <sp> -hinst <string> ?-physical_group?",
        ),
        # man1/create_thermal_model.1
        _syn(
            "create_thermal_model",
            "",
            "create_thermal_model ?-help? ?-leakage_temperature_scale_table {$<temp1> $<scalefactor1> $<temp2> $<scalefactor2> $<temp3> $<scalefactor3> .....}? ?-leakage_temperature_scale_table_file <filename>? ?-metal_density_file <filename>? ?-power_db <path_to_power_database>? ?-vtm_SI_unit {true | false}? ?-vtm_conductivity_inputs <filename>? ?-vtm_densitytable_tile {<Xint> <Yint>}? ?-vtm_file <filename>? ?-vtm_format {simple | stack}? ?-vtm_format_version {new | default}? ?-vtm_header_include_file <filename>? ?-vtm_leakage_temp {<temp1> <temp2> <temp3>}? ?-vtm_output_dir <directory>? ?-vtm_powertable_tile {<Xint> <Yint>}? ?-vtm_tile {<Xint> <Yint>}? ?-vtm_tile_size {<$X_um> <$Y_um>}?",
        ),
        # man1/create_virtual_fin_bound_marker.1
        #   WARNING: bracket mismatch: '[' at position 95 closed by '}' at position 210
        #   WARNING: unclosed bracket '{' at position 94
        _syn(
            "create_virtual_fin_bound_marker",
            "",
            "create_virtual_fin_bound_marker ?-help? ?-areas {{<lx1 ly1 ux1 uy1>} {<lx2 ly2 ux2 uy2>}...}? {?-cell {<libCell | ptnCell>} | -inst <inst_name>| ?-layer {<metal_layer_name>| <via_layer_name>} ?-net <net_name>??} ?-drc_region_layer <drc_region_layer_name>? -marker_layer <marker_layer_name>",
        ),
        # man1/create_virtual_shape_on_pg_wires.1
        _syn(
            "create_virtual_shape_on_pg_wires",
            "Generates additional virtual shapes and creates markers on PG wires, when the existing trim shapes overlap with PG wires",
            "create_virtual_shape_on_pg_wires ?-help? -layers {{virtual_layer, power_layer ?mask_num?} ...} ?-name <string>? ?-pg_width_list {<list_of_supported_width_values>} | -pg_width_range {min_width max_width}?",
        ),
        # man1/create_what_if_shape.1
        _syn(
            "create_what_if_shape",
            "Specifies to add, select, deselect, delete, list, and display the what if wires/vias to a design",
            "create_what_if_shape ?-help? ?-area {<llx lly urx ury>}? ?-display? ?-direction {hor | ver}? ?-offset {X Y}? ?-add -method {auto | exact}? ?-layer <layerName>? ?-nets<{net1net2net3…}>? ?-spacing <value>? ?-objects {selected | all}? ?-add | -select | -deselect | -delete | -list | -save <filename> | -load <filename>? ?-pitch <pitch>? ?-add -width <width>? ?-type {wire | via}? ?-format {txt def}? ?-save <filename> -append? ?-remove_existing_wires?",
        ),
        # man1/createAbuttedFPlan.1
        _syn(
            "createAbuttedFPlan",
            "",
            "createAbuttedFPlan ?-help? ?-cutToFixOverlap? ?-honorPlaceBlockage <blockageName>? ?-ptnToCoreGap <distance>? ?-ptnToPtnGap <distance>? {-hinsts <hierarchicalInstanceList> | -selected | -all}",
        ),
        # man1/createActiveLogicView.1
        _syn(
            "createActiveLogicView",
            "Trims the timing graph to ignore logic inside the first level registers in partitions to improve runtime for timing-related commands",
            "createActiveLogicView ?help? ?-type {flatTop timingBudget topIO}?-setDontTouch | -unsetDontTouch??",
        ),
        # man1/createBasicPathGroups.1
        _syn(
            "createBasicPathGroups",
            "Explicitly creates standard path groups irrespective of the design stage",
            "createBasicPathGroups ?-help? ?-expanded? ?-reset?",
        ),
        # man1/createBusGuide.1
        _syn(
            "createBusGuide",
            "Creates bus guides associated with net groups, to guide routing for all the nets of the specified net group",
            "createBusGuide ?-help? ?-type {hard | soft}? -netGroup <netGrpName> -layer {id | id1:id2} {?{-centerLine {<x1 y1 x2 y2>} -width <value>} ?-beginExt <value>? ?-endExt <value>?? | -rect {<x1 y1 x2 y2>}}",
        ),
        # man1/createBusNetGroup.1
        _syn(
            "createBusNetGroup",
            "Creates a net group for buses",
            "createBusNetGroup ?-help? ?-considerClone? ?-createBusSinkGroup? ?-dontCommit? ?-file <string>? ?-ignoreBusSize <integer>? ?-ignoreConnectivity? ?-ignoreMultiPartitionPinNet? ?-netGroupOptionsList <string>? ?-overwrite? ?-prefix <string>? ?-reverseOrder? ?-useShortName? ?-bus <string> | -all? ?-forTopOnly | -forPartitionOnly? ?-includeMacro | -forPartitionOnly? ?-checkOnly | {?-bus <string>? ?-all?}?",
        ),
        # man1/createDensityArea.1
        _syn(
            "createDensityArea",
            "Creates a density screen area",
            "createDensityArea ?-help? <box > <density>?-name <obj_name>?",
        ),
        # man1/createExclusiveGroups.1
        _syn(
            "createExclusiveGroups",
            "Creates exclusive regions",
            "createExclusiveGroups ?-help? ?<group_name>? ?-gap <float>? ?-min_gap <float>? ?-exclusiveGroups <string> | -mutuallyExclusiveGroups <string>?",
        ),
        # man1/createFence.1
        _syn(
            "createFence",
            "Creates a fence for a module or a group",
            "createFence ?-help? <obj_name > <box>?-floating?",
        ),
        # man1/createGAFillerGroup.1
        _syn(
            "createGAFillerGroup",
            "It creates gate array filler groups for the post-mask ecoPlace flow",
            "createGAFillerGroup ?-help? -ga_cells <gaCellList> -ga_fillers <gaFillerCellList > -group <groupName>",
        ),
        # man1/createGuide.1
        _syn(
            "createGuide",
            "",
            "createGuide ?-help?",
        ),
        # man1/createInstGroup.1
        _syn(
            "createInstGroup",
            "Creates a new instance group, even outside the core boundary",
            "createInstGroup ?-help? <group_name> ?<box>? ?-isPhyHier? ?-guide <box >| -region | -fence| -softGuide? ??-ar <num>? -density <num>? ?-softGuide? ?-floating | -softGuide? ?-floating | -guide <box >?",
        ),
        # man1/createInterfaceLogic.1
        _syn(
            "createInterfaceLogic",
            "Creates the specified directory containing ILM files with the appropriate level of extraction for specific model type such as timing, si, or for all models",
            "createInterfaceLogic ?-help? ?-allowIlmEco? ?-ignorePorts <ListOfPorts>? ?-keepAll??-keepSelected? ?-modelType {timing si all}? ?-noInterClockPath? ?-overwrite? ?-removePowerGround? ?-dir <dirName> | -cellview {lib | cell | view}? ??-optStage {preCTS postCTS}??",
        ),
        # man1/createIoRow.1
        #   WARNING: bracket mismatch: '[' at position 39 closed by '}' at position 231
        #   WARNING: bracket mismatch: '{' at position 20 closed by ']' at position 232
        #   WARNING: unmatched closing bracket '}' at position 292
        _syn(
            "createIoRow",
            "Creates new I/O rows and edits the existing I/O rows",
            "createIoRow ?-help? {-site <site_name> ?{-side {N | W | S | E} ?-rowMargin <value>? ?-beginOffset <value>? ?-endOffset <value> | -length <len> | -nrSites <nr>? } | {-corner {BL | BR | TR | TL} ?-xOffset <value>? ?-yOffset <value>?}}? ?-orientation {R0 | R90 | R180 | R270}? ?-name <row_name>?} | {-deriveByCells} | {-deriveBySelection}",
        ),
        # man1/createLib.1
        _syn(
            "createLib",
            "Copies or attaches a technology database to a library",
            "createLib ?-help? <libName> ?-libPath <path>? ?-noCompress? {-attachTech <techlib> | -copyTech <techlib> | -referenceTech <techliblist>}",
        ),
        # man1/createLogicHierarchy.1
        _syn(
            "createLogicHierarchy",
            "Creates a new logical hierarchy for the specified hierarchical instances",
            "createLogicHierarchy ?-help? -cell <string> ?-commit? -newHinst <string> ?-objects <string>? ?-selected?",
        ),
        # man1/createMarker.1
        #   WARNING: bracket mismatch: '[' at position 21 closed by '}' at position 103
        #   WARNING: unmatched closing bracket ']' at position 104
        _syn(
            "createMarker",
            "Creates markers for violations in the database",
            "createMarker ?-help? ?-bbox { <x1 y1 x2 y2> } | -poly {{ <x1 y1 x2 y2> ...} | { <x1 y1>} {<x2 y2>} ...}}? ?-desc <description>? ?-layer {layerName | layerNumber}? ?-rulemap? ?-subtype <subtypeName>? ?-tool <toolName>? ?-type <typeName>?",
        ),
        # man1/createNetGroup.1
        _syn(
            "createNetGroup",
            "Creates an empty net group",
            "createNetGroup ?-help? ?-mixed_signal? ?-spacing <minSpaceInTracks>? ?{?-optimizeOrder?} | -spreadPin | -compact_area? ?-excludePin {allLayer | sameLayer | allLayerInGuidedArea} ?-keep_out_spacing <integer>?? { ?<netGroupName> ?-net <netNameList>??}",
        ),
        # man1/createPGPin.1
        _syn(
            "createPGPin",
            "Creates a power/ground pin as per the specified coordinates of the physical shape",
            "createPGPin ?-help? {-onDie {-selected | -net <netName>} ?-width <float>? ?-length <float>?} | {<pgPinName> ?-net <netName>? ?-geom <layerName llx lly urx ury>?} ?-dir {undefined | input | output}?",
        ),
        # man1/createPhysicalPin.1
        _syn(
            "createPhysicalPin",
            "Adds a new physical pin-shape to a top-level term (DEF PIN)",
            "createPhysicalPin ?-help? <pinName>?-allowOutsideBoundary? ?-net <netName>? ?-samePort? {{ -layer <layerName> {-rect {<x1 y1 x2 y2>} | -polygon {<x1 y1 x2 y2 ... xn yn>}}}}",
        ),
        # man1/createPinBlkg.1
        _syn(
            "createPinBlkg",
            "Creates a pin blockage for a module",
            "createPinBlkg ?-help? ?-cell <cell_name>? ?-layer {<layer_id_list>}? { -area <{x1 y1 x2 y2>} | ?-edge <edge_number> ??-offset_start <distance>? ?-offset_end <distance>??? | ?-abutted_master_clone_channel_access_only ?-feedthru_blockage_file <file_name>?? } ?-name <blockage_name> ?-includePinPatterns {<pin_name_pattern_list>} | -excludePinPatterns {<pin_name_pattern_list>}??",
        ),
        # man1/createPinGroup.1
        _syn(
            "createPinGroup",
            "Creates a pin group for a partition or for the top-level",
            "createPinGroup ?-help? ?-cell <string>? ?-excludePin {allLayer | sameLayer | allLayerInGuidedArea}? ?-keep_out_spacing <integer>? ?-spacing <integer>? ?-width <width>? ?{?-optimizeOrder?} | -spreadPin | -compact_area? ?{<pinGroupName> ?-pin {<pinNameList>}?}?",
        ),
        # man1/createPinGuide.1
        _syn(
            "createPinGuide",
            "Creates a pin guide object",
            "createPinGuide ?-help? {?-area {<x1 y1 x2 y2>} | ?-edge <integer> ??-offset_start <float>? ?-offset_end <float>?????-layer {<layeridList>} ?-layerPriority??} ?-pin <string> | -pinGroup <string> | -net <string> | -netGroup <string> | -name <string>? ?-edge <integer> | -net <string> | -netGroup <string>? ?-cell <string> | -net <string> | -netGroup <string>?",
        ),
        # man1/createPipelineBusGuide.1
        _syn(
            "createPipelineBusGuide",
            "Generates bus-guide for the pipeline netgroup",
            "createPipelineBusGuide ?-help? ?-netGroup <netGroupNames>? ?-widthFactor <value>? ?-layer <id1:id2>? ?-report <fileName>? ?-spacing <value> {-report <filename>}?",
        ),
        # man1/createPipelineNetGroup.1
        _syn(
            "createPipelineNetGroup",
            "Creates Net Groups for Pipeline Flip-Flop (PFF) Placement and Reporting",
            "createPipelineNetGroup ?-help?",
        ),
        # man1/createPlaceBlockage.1
        _syn(
            "createPlaceBlockage",
            "createPlaceBlockage [-help] [-pushdown] {{[-box {<x1 y1 x2 y2>} | -polygon {{<x1 y1>} {<x2 y2>}...} | -boxList {{<x1 y1>} {<x2 y2>}...} | -allPartition | -allMacro ] [-inst <inst_name> | -hinst <hinst_name>] } [-name <place_blockage_name> | -prefixOn ] [{-type {hard soft partial macroOnly}} [-density <value>] [-excludeFlops ]] [-noCutByCore] [-snapToSite] } [ {-inst <inst_name> | -hinst <hinst_name> | -allPartition | -allMacro } [-cover ] [-innerRingBySide {<x1 y1 x2 y2>} | -innerRingByEdge {<edge1 edge2 edge3 ...>}] [-outerRingBySide {<x1 y1 x2 y2>} | -outerRingByEdge {<edge1 edge2 edge3 ...>}] ] Creates cell placement blockages that can be placed",
            "createPlaceBlockage ?-help? ?-pushdown? {{?-box {<x1 y1 x2 y2>} | -polygon {{<x1 y1>} {<x2 y2>}...} | -boxList {{<x1 y1>} {<x2 y2>}...} | -allPartition | -allMacro? ?-inst <inst_name> | -hinst <hinst_name>? } ?-name <place_blockage_name> | -prefixOn? ?{-type {hard soft partial macroOnly}} ?-density <value>? ?-excludeFlops?? ?-noCutByCore? ?-snapToSite? } ?{-inst <inst_name> | -hinst <hinst_name> | -allPartition | -allMacro } ?-cover? ?-innerRingBySide {<x1 y1 x2 y2>} | -innerRingByEdge {<edge1 edge2 edge3 ...>}? ?-outerRingBySide {<x1 y1 x2 y2>} | -outerRingByEdge {<edge1 edge2 edge3 ...>}??",
        ),
        # man1/createPtnCut.1
        _syn(
            "createPtnCut",
            "Creates a partition rectangular cut from a partition",
            "createPtnCut ?-help? ?-ptn <string>? <x1 y1 x2 y2>",
        ),
        # man1/createPtnFeedthrough.1
        _syn(
            "createPtnFeedthrough",
            "Creates a partition routing feedthrough object",
            "createPtnFeedthrough ?-help? <feedBox> ?<layerId>? ?-name <string>?",
        ),
        # man1/createRegion.1
        _syn(
            "createRegion",
            "Creates a region for a module or a group",
            "createRegion ?-help?",
        ),
        # man1/createRouteBlk.1
        _syn(
            "createRouteBlk",
            "Creates a routing blockage object",
            "createRouteBlk ?-help? ?-cutLayer <layerName> | {<layerNamelist ...>} | all? ?-drcRegionLayer <layerName>| {<layerNamelist ...>} | all? ?-fills? ?-inst <name>? ?-layer <layerName> | {<layerNamelist ...>} | all? ?-mask <integer>? ?-noWrongWay? ?-pushdown? ?-trimMetalLayer <layerName> | {<layerNamelist ...>} | all? ?-name <blk>| -prefixOn? {-box {<x1 y1 x2 y2>} | -cover | -polygon {{<x1 y1>} {<x2 y2>}...} | -boxList {{<x1 y1>} {<x2 y2>}...}} ?-exceptpgnet | -pgnetonly | -partial <integer>? ?-spacing <float >| -designRuleWidth <float>?",
        ),
        # man1/createRouteBlkAlongTrack.1
        _syn(
            "createRouteBlkAlongTrack",
            "Creates routing blockages that are aligned to specified tracks which are in the shrunken row area",
            "createRouteBlkAlongTrack ?-help? -align_track <string> ?-consider_cells_as_macros <string>? ?-consider_macros_as_cells <string>? ?-edge_shrink {<x y>}? -layer <string> ?-no_cut_row?",
        ),
        # man1/createRow.1
        _syn(
            "createRow",
            "Creates rows for the specified site",
            "createRow ?-help? -site <siteName> ?-area {<x1 y1 x2 y2>} | -boxList {{<x1 y1>} {<x2 y2>} <...>}< >| -polygon {{<x1 y1>} {<x2 y2>}...}? ?-spacing <distance>? ?-limitInCore? ?-noAbut | -noAbut1st? ?-flip1st? ?-noCheck? ?-noFlip?",
        ),
        # man1/createRuler.1
        _syn(
            "createRuler",
            "Adds a ruler",
            "createRuler ?-help? {{-center {<x y>} -radius <value>} | -coordinates {<x1 y1 x2 y2> ...}}",
        ),
        # man1/createSdpGroup.1
        _syn(
            "createSdpGroup",
            "Creates an SDP group",
            "createSdpGroup ?-help? ?-justifyBy {SW|SE|NW|NE|N|W|S|E|MID}? -name <sdpGroupName> ?-type {row|col|space}? {{-skip_space value} |-skip_space_by_site_width <value> <siteName >| -skip_space_by_micron <value>} | {{{-inst <WCardName>... ?-keepOrder?} | -selected } ??-spread_group <value>? | ?-spread_group_by_site_width <value siteName>? | ?-spread_group_by_micron <value>? | ??-numRow <value>? ?-numCol <value>???}",
        ),
        # man1/createShield.1
        _syn(
            "createShield",
            "Creates shield wires for the NanoRoute router",
            "createShield ?-help? ?-selected? ?-crosstie_only? ?-include_fixed?",
        ),
        # man1/createSignalPin.1
        _syn(
            "createSignalPin",
            "Promotes signal pins in the IO pad/block to the top-level design as a physical pin for specified in‐ stances or pins",
            "createSignalPin ?-help? ?-ignore_floating_pins? {-inst <inst_name_list> | -pins <pin_name_list>}",
        ),
        # man1/createSnapshot.1
        _syn(
            "createSnapshot",
            "Creates snapshots of the design for all three views (Floorplan, Amoeba, and Placement) at any stage of the design flow",
            "createSnapshot ?-help? -dir <string> -name <string> ?-overwrite?",
        ),
        # man1/createSoftGuide.1
        _syn(
            "createSoftGuide",
            "",
            "createSoftGuide ?-help?",
        ),
        # man1/createSpareModule.1
        _syn(
            "createSpareModule",
            "Creates a spare module made up of the specified cells",
            "createSpareModule ?-help? -moduleName <moduleName> -cell {<cellName>?<number>? ?<cellName> ?<number>?? …} ?-clock <netName>? ?-reset <netName>:<pinName> ?<pinName>? …? ?-tie {<tieCellName> ?<tieCellname>? }? ?-tieLo {<pinList> | *}? ?-useCellAsPrefix?",
        ),
        # man1/createSpecialDrcRegion.1
        _syn(
            "createSpecialDrcRegion",
            "DRC region layers define a special masterslice layer that is used to define the areas of a region on which a set of rules defined in the metal, cut, and/or trim metal layers with the REGION property would be applied",
            "createSpecialDrcRegion ?-help? ?-extendOuterX <float>? ?-extendOuterY <float>? ?-extendX <float>? ?-extendY <float>? ?-insts <string>? -layer <string>",
        ),
        # man1/createSpecialMarkLayerShape.1
        _syn(
            "createSpecialMarkLayerShape",
            "Creates a mark layer shape, using special route",
            "createSpecialMarkLayerShape ?-help? ?-cutOutBlockInsts <string>? ?-extendOuterX <float>? ?-extendOuterY <float>? ?-extendX <float>? ?-extendY <float>? -layer <string>",
        ),
        # man1/createStairwayBoundary.1
        _syn(
            "createStairwayBoundary",
            "Creates small stairway rectilinear edges at a specified partition corner to improve congestion",
            "createStairwayBoundary ?-help? -dx <value> -dy <value> ?-growNeighborPtnDir {<x y>}? -ptn <partition_name> -step <number_of_steps > {-corner {LL LR UL UR} | -vertex <number_of_vertex>}",
        ),
        # man1/createTBOptFile.1
        _syn(
            "createTBOptFile",
            "This command creates a target-based optimization (TBOpt) file for use with postRoute targeted optimiza‐ tion",
            "createTBOptFile ?-help? -bottleneckInstanceNumber <integer>?-early? ?-max_paths <integer>? ?-max_slack <float>? ?-min_slack <float>? -outFile <filename> ?-path_group <groupname_list>? ?-timingFile <filename>?",
        ),
        # man1/createTQuantusModelFile.1
        _syn(
            "createTQuantusModelFile",
            "Creates the RC model data and stores it in a TQuantus model file",
            "createTQuantusModelFile ?-help? -file <rc_model_file_name> ?-reset?",
        ),
        # man1/createTrack.1
        _syn(
            "createTrack",
            "Creates non-uniformed, customized tracks in selected design area",
            "createTrack ?-help? -dir <direction>-layer <layerNameList>< >-num <numOfTrack> -start <coordinate> -step <step>",
        ),
        # man1/createTSVNoLoadSPEF.1
        _syn(
            "createTSVNoLoadSPEF",
            "Creates a top-level spef that describes the connectivity between dies",
            "createTSVNoLoadSPEF <fileName>",
        ),
        # man1/createUserBundleNet.1
        _syn(
            "createUserBundleNet",
            "Creates a bundle of specified nets that can be displayed as flightlines",
            "createUserBundleNet ?-help? <name> -nets <listOfNets> <-object1> <string>-object2< > <string>",
        ),
        # man1/createUserDisableForCombLoopBreak.1
        _syn(
            "createUserDisableForCombLoopBreak",
            "Generates SDC file containing constraints for combinational loop breaking",
            "createUserDisableForCombLoopBreak -input_file <fileName> -outfile <fileName>",
        ),
        # man1/createWhatIfInternalGeneratedClock.1
        _syn(
            "createWhatIfInternalGeneratedClock",
            "Creates an internal pin on a blackbox or a blackblob, and creates a generated clock on this internal pin",
            "createWhatIfInternalGeneratedClock <blackBoxCellName> ?-help? -clockName <genClkName> -clockPin <internalPinName> -masterPin <clockInputPort> ?-edge_shift <edge_shift_list>? ?-noCreateInternalPin? ?-invert? {-multiplyBy <integer> | -divideBy <integer> | -edges <edge_list>}",
        ),
        # man1/ctd_save_histogram.1
        _syn(
            "ctd_save_histogram",
            "Saves the CTD histogram to a file",
            "ctd_save_histogram ?-help? ?-csv? -file <fileName>?-id <windowID>?",
        ),
        # man1/ctd_save_view.1
        #   WARNING: unclosed bracket '[' at position 69
        _syn(
            "ctd_save_view",
            "Saves the current snapshot of the clock tree viewer into a file",
            "ctd_save_view ?-help? -file <fileName> ?-id <windowID>? ?-legend_on? ?-type {PNG | GIF}",
        ),
        # man1/ctd_show_skew_group.1
        _syn(
            "ctd_show_skew_group",
            "Shows the specified skew group in the CTD window",
            "ctd_show_skew_group ?-help? ?-id <window_id_name>? -skew_group <skew_group_name>",
        ),
        # man1/ctd_trace.1
        _syn(
            "ctd_trace",
            "Highlights the clock tree path from the clock root to the pin or from one pin to the other if the two pins are on the same path using the specified color or color index",
            "ctd_trace ?-help? ?-color <colorname>? ?-file <fileName>? ?-from <rootclock>? ?-index <colorindex>? ?-to <sink> | -through <instancename>?",
        ),
        # man1/ctd_win.1
        _syn(
            "ctd_win",
            "Opens a Clock Tree Debugger (CTD) window with the user-defined window ID and title",
            "ctd_win ?-help? ?-id <windowIDName>? ?-include_reporting_only_skew_groups? ?-title <CTDWindowID>? ?-unit_delay?",
        ),
        # man1/cts_refine_clock_tree_placement.1
        _syn(
            "cts_refine_clock_tree_placement",
            "",
            "?-help?",
        ),
        # man1/current_design.1
        _syn(
            "current_design",
            "Sets the specified design to be the current design",
            "current_design ?-help? ?<design_name>?",
        ),
        # man1/current_instance.1
        _syn(
            "current_instance",
            "",
            "current_instance ?<hierarchical_instance>? Sets the instance given by <hierarchical_instance> to be the current instance. Design objects referenced by subsequent commands can be found relative to this instance. All searches for design objects are started in this instance. If design objects are referenced hierarchically, <hierarchical_instance> is used as the root (top) of the hierarchy.",
        ),
        # man1/cutBoxListFromPowerDomain.1
        _syn(
            "cutBoxListFromPowerDomain",
            "Cuts out default power domains from a non-default power domain",
            "cutBoxListFromPowerDomain ?-help? -powerdomain <powerDomainName> -boxList {{box1} ...}",
        ),
        # man1/cutPowerDomainByOverlaps.1
        _syn(
            "cutPowerDomainByOverlaps",
            "When you floorplan one power domain (inner domain) completely inside the other power domain (outer domain), use this command to cut the outer domain as a hollow or donut shape",
            "cutPowerDomainByOverlaps <powerDomainName> ?-help?",
        ),
        # man1/cutRectilinearInst.1
        _syn(
            "cutRectilinearInst",
            "Cuts partition or black box boundaries to rectilinear instances that fit blocks in a given die, with‐ out modifying the existing block area",
            "cutRectilinearInst ?-help? -inst <instName> {{-refInst <instName> ?-spacingX <xvalue>? ?-spacingY <yvalue>?} | {-cutBox {<x1 y1 x2 y2>}} | {-corner <cornerValue> ?-x <value> -y <value>?}} ?-pushOut <sideEdgeName>?",
        ),
        # man1/cutRow.1
        _syn(
            "cutRow",
            "Cuts site rows within an area or that intersect with the selected object(s)",
            "cutRow ?-help? ?-area <box >| -object <string >| -selected | -fromIo {<left bottom right top>}? ?-halo <float>| {-leftGap <float>| -rightGap <float >| -topGap <float >| -bottomGap <float>}? ?-site <name>? ?-keepCell?",
        ),
        # man1/cvd.1
        _syn(
            "cvd",
            "",
            "",
        ),
        # man1/db_browser.1
        _syn(
            "db_browser",
            "Launches the database browser (DB Browser)",
            "db_browser ?-help? <obj_list> | head | top | selected",
        ),
        # man1/db_pt.1
        _syn(
            "db_pt",
            "Returns the X or Y coordinate of any point",
            "db_pt {-x | -y} <pt> ?-help?",
        ),
        # man1/db_rect.1
        _syn(
            "db_rect",
            "Returns information about a rectangle, like coordinates, size, and area",
            "db_rect ?-help? <rect> {-ll | -ur | -llx | -lly | -urx | -ury | -size | -sizex | -sizey | -width | -length | -center | -area}",
        ),
        # man1/dbEdge.1
        _syn(
            "dbEdge",
            "Returns the edges of a polygon of a shape along with the direction list (N, S, E, W and NE, NW, SE, SW)",
            "dbEdge ?-clockwise | -counterclockwise? ?{<shapelist>} ?-direction <direction>? ?-d?? ?-index <index_number>?",
        ),
        # man1/dbGet.1
        _syn(
            "dbGet",
            "Returns object and attribute information for the specified database object in the design",
            "dbGet ?-help? ?. <objType>?…?. <attrName> | .? | .?? | .?h? ?-d? ?-e? ?expression? ?-i <num>? ?-l? {<obj> | <objList> | head | top | selected} ?-p <num>? ?<pattern>? ?-regexp? ?-u? ?-v?",
        ),
        # man1/dbQuery.1
        _syn(
            "dbQuery",
            "Returns a list of objects that overlap or abut specific areas by default",
            "dbQuery ?-help? ?-areas {{<llx1 lly1 urx1 ury1>} {<llx2 lly2 urx2 ury2>} <...>}? ?-bbox_overlap? ?-d? ?-layers {<layer1 layer2 ...>} ?-strict_via_inst_layer_check?? ?-objType {bump busGuide inst instAllShapes instTerm term marker net pBlkg pWire pgInstTerm rBlkg regular resizeBlkg row special sViaInst sWire viaInst wire whatIfWire whatIfVia pinShape guiRect guiLine guiPoly partition}? ?-polygons {<x11 y11 x12 y12 x13 y13> < ...>}? ?-abut_only? | ?-enclosed_only? | ?-overlap_only?",
        ),
        # man1/dbSchema.1
        _syn(
            "dbSchema",
            "Returns all of the available objects and attributes for the specified database object",
            "dbSchema ?-help? ?<objNamePattern>< >?<objAttrNamePattern>?? ?-parent <objNamePatternForParent >?-list??",
        ),
        # man1/dbSet.1
        _syn(
            "dbSet",
            "Changes the specified attribute value for a database object",
            "dbSet ?-d? {<objList> | head | top | selected} ?.<objType>?*.<attrName><attrValue> ?-help?",
        ),
        # man1/dbShape.1
        _syn(
            "dbShape",
            "Performs geometric (such as SIZE and BBOX) and logical (such as AND and ANDNOT) operations on shapes (a polygon, a rectangle, or a list of rectangles and polygons)",
            "dbShape ?-help? ?-d? ?-step step? ?-output polygon|rect|hrect|area? shapeList ?AND shapeList | ANDNOT shapeList | OR shapeList | XOR shapeList | INSIDE shapeList | OUTSIDE shapeList | ENCLOSE shapeList | STRADDLE <shapeList> | BBOX | HOLES | NOHOLES | BBOX_CIRCLE | BBOX_OCTAGON | MOVE {<dx dy>| SIZE <value> | SIZEX <value> | SIZEY <value>} | SCALE <scale_factor>? ...",
        ),
        # man1/dbTransform.1
        _syn(
            "dbTransform",
            "Takes coordinates local to a cell and returns them in context with the global design space",
            "dbTransform ?-help? ?-d?{-inst instPtr | -hInst instPtr | {-cell cellPtr -orient orientEnum -pt {x y}}} {-localPt list | -globalPt list}",
        ),
        # man1/dbu2uu.1
        _syn(
            "dbu2uu",
            "Takes an arbitrary list of values and returns it in the same form, with each database integer value converted to its user unit floating point equivalent",
            "dbu2uu ?help? <value> ?-unit {100 | 200 | 400 | 800 | 1000 | 2000 | 4000 | 8000 | 10000 | 20000}?",
        ),
        # man1/dd_get.1
        #   WARNING: unmatched closing bracket '}' at position 151
        _syn(
            "dd_get",
            "Returns OpenAccess library information",
            "dd_get {-all_lib} |{–dd <dd_objHandle> | -lib <libName> | -cell {<lib cell>} | -cellview {<lib cell view>} } ?-children | -file | -path | -type |-name?}",
        ),
        # man1/debug_irdrop.1
        _syn(
            "debug_irdrop",
            "Specifies to automatically identify the region with worst IRdrops and EM violations, and provide necessary information to determine and fix the root cause",
            "debug_irdrop ?-help? ?-nworst_instances <value>? ?-output_directory <dir>? -state_directory <dir> ?-net <netname> | -domain <domainname>? ?-region {x1 y1 x2 y2 }| -nregion <value>? ?-eco_report? ?-net_threshold <value> | -domain_threshold <value>? ?-summary_only? ?-tile_row_col {<X> <Y>}? ?-tile_size {<X> <Y>}? ?-non_violating_instslimit <value>? ?-enable_xp {true | false}?",
        ),
        # man1/debugPtnBoundaryPorts.1
        _syn(
            "debugPtnBoundaryPorts",
            "The debugPtnBoundaryPorts command prints out the boundary pins' debug information during partition in a log which shows how to assign the power domain for the partition pins",
            "debugPtnBoundaryPorts <-pins>",
        ),
        # man1/decompress_special.1
        _syn(
            "decompress_special",
            "Decompresses Power-Grid (PG) objects within the specified area, layer, or net",
            "decompress_special ?-help? ?-area {<x1 y1 x2 y2>}? ?-layers <layer>+? ?-nets <net>+?",
        ),
        # man1/decrypt.1
        _syn(
            "decrypt",
            "Decrypts and evaluates a Tcl file that was encrypted with the encrypt command",
            "decrypt ?-help? <file_name>",
        ),
        # man1/defComp.1
        _syn(
            "defComp",
            "",
            "defComp ?-help? <fileName >?-bump? ?-defAsGolden? ?-ignoreLayerFrom <layer>? ?-ignoreLayerTo <layer>? ?-ignoreLogicChange? ?-metalShapeDiff? ?-placeBlockage? ?-reportFile <reportFile>? ?-row? ?-snetPin? ?-unit <units_value>? ?-ignoreCellPlace <lef_macro_classes_list> ?-checkCellPrefix<prefix_list>??",
        ),
        # man1/defHierChar.1
        _syn(
            "defHierChar",
            "",
            "",
        ),
        # man1/defIn.1
        _syn(
            "defIn",
            "Loads the specified DEF file",
            "defIn ?-help? <fileName> ?-add_blockage? ?-allWarning? ?-components? ?-deleteBump? ?-deleteSpecialRoute? ?-ignore_drcfill? ?-ignore_pg_connectivity? ?-nets? ?-preserveShape? ?-removeHalfWireExtensionOnPin? ?-specialnets? ?-specialRouteUserClass <user_class_name>? ?-verilog_from_def_netlist_flow? ?-incremental_routing?",
        ),
        # man1/defInCheckMaskShifts.1
        _syn(
            "defInCheckMaskShifts",
            "",
            "defInCheckMaskShifts {on | off | bypass}",
        ),
        # man1/define_add_on_module_model.1
        _syn(
            "define_add_on_module_model",
            "Allows you to define the add_on types or supplemental models that can be loaded additionally with an existing model or a design",
            "define_add_on_module_model ?-help? ?-commit_callback <string>? -type <string > {?-create_callback <string>? ?-set_callback <string>? ?-restore_callback <string>? ?-write_context_callback <string>?}",
        ),
        # man1/define_bundled_bus.1
        _syn(
            "define_bundled_bus",
            "Allows you to control user-defined bus groups",
            "define_bundled_bus ?-help? ?-add_members <string>? ?-delete_members <string>? ?-name <string>?",
        ),
        # man1/define_glitch_holding_resistance.1
        _syn(
            "define_glitch_holding_resistance",
            "Allows you to specify the holding resistance",
            "define_glitch_holding_resistance ?-help? ?-glitch_type {both | vl | vh | vlu | vho | vl_vh | vlu_vho}? ?-instance_pin <string>? ?-lib_pin <string>? -value <double> ?-views <string>?",
        ),
        # man1/define_proc_arguments.1
        _syn(
            "define_proc_arguments",
            "Defines the arguments and attributes of a Tcl procedure",
            "define_proc_arguments ?-help? <command_name> ?-info <string>? ?-define_args <string>? ?-hide?",
        ),
        # man1/define_property.1
        _syn(
            "define_property",
            "Defines a new property",
            "define_property ?-help? -object_type {<object_type_list>} -type <data_type> ?-lower_bound <val>? ?-upper_bound <val>? ?-string_values {<values>}? <property_name>",
        ),
        # man1/definePartition.1
        _syn(
            "definePartition",
            "Defines a new partition corresponding to a hierarchical instance",
            "definePartition ?-help? ?-coreSpacing {left right top bottom}? ?-minPitchBottom <x>? ?-minPitchLeft <x>? ?-minPitchRight <x>? ?-minPitchTop <x>? ?-pinLayerBottom {<list_of_layers>}? ?-pinLayerLeft {<list_of_layers>}? ?-pinLayerRight {l<list_of_layers>}? ?-pinLayerTop {l<list_of_layers>}? ?-placementHalo {<left right top bottom> }? ?-railwidth <railWidth>? ?-reservedLayer {<list_of_layers>}? ?-routingHalo <floatValue>? ?-routingHaloBottomLayer <integerValue>? ?-routingHaloTopLayer <integerValue>? ?-stdCellHeight <x>? {-hinst <string> | -proto {master_hinst_name_list} | -cell <cellName>} ?-checkCloneAlignment? ?-hinst <hInstName> ?-copyFrom <refPtnName>?? ?-cell <cellName> ?-copyFrom <refPtnName>??",
        ),
        # man1/defInShapeBasedDefFile.1
        #   WARNING: unmatched closing bracket '}' at position 3
        _syn(
            "defInShapeBasedDefFile",
            "",
            "| 1}",
        ),
        # man1/defOut.1
        _syn(
            "defOut",
            "Writes the specified information to a DEF file",
            "defOut ?-help? <fileName> ?-addHalfWireExtensionOnPin? ?-allLayers? ?-bumpAsPin? ?-cutRow? ?-cut_pg_rail? ?-earlyGlobalRoute? ?-flatten_via_pillar? ?-floorplan? ?-ioRow? ?-netlist? ?-noCoreCells? ?-noPrintWildCard? ?-noSpecialNet? ?-noStdCells? ?-noTracks? ?-no_covered_wire_patch? ?-no_virtual_trim? ?-outputMaskLayers <listOfLayers>? ?-scanChain? ?-selected? ?-skip_trimmetal_layers? ?-specialRouteUserClass <user_class>? ?-trimmetal_gap_fill? ?-unit <unit_per_micron>? ?-unplaced? ?-useEEQCellWithLibertyInfo? ?-usedVia? ?-verilog_from_def_netlist_flow? ?-withShield? ?-routing ?-routing_to_specialnet | -wrongway_routing_as_specialroute??",
        ),
        # man1/defOutBySection.1
        _syn(
            "defOutBySection",
            "Writes information to the specified sections in a DEF file",
            "defOutBySection ?-help? <filename> ?-addHalfWireExtensionOnPin? ?-bumpAsPin? ?-compPlacement? ?-earlyGlobalRoute? ?-fills? ?-groups ?-noPrintGroupRegex?? ?-ioRow? ?-netRouting? ?-noComps? ?-noCoreCells? ?-noDieArea? ?-nonDefaultRules? ?-noNets? ?-noPrintWildCard? ?-no_virtual_trim? ?-outputMaskLayers <layerNames>? ?-pBlockages? ?-pins? ?-rBlockages? ?-rows? ?-scanChains? ?-selected? ?-specialNetRouting? ?-specialNets? ?-specialRouteUserClass <user_class_list>? ?-specialShape <swire_type_list>? ?-tracks? ?-unit unit_per_micron? ?-unplaced? ?-usedVia? ?-verilog_from_def_netlist_flow? ?-vias?",
        ),
        # man1/defOutCompressVia.1
        _syn(
            "defOutCompressVia",
            "",
            "defOutCompressVia {0 | 1}",
        ),
        # man1/defOutLefNDR.1
        #   WARNING: unmatched closing bracket '}' at position 3
        _syn(
            "defOutLefNDR",
            "",
            "| 1}",
        ),
        # man1/defOutLefVia.1
        _syn(
            "defOutLefVia",
            "",
            "defOutLefVia {0 | 1}",
        ),
        # man1/defOutPolygonDieArea.1
        _syn(
            "defOutPolygonDieArea",
            "",
            "defOutPolygonDieArea {0 | 1}",
        ),
        # man1/defOverlapWireReportFileName.1
        _syn(
            "defOverlapWireReportFileName",
            "",
            "defOverlapWireReportFileName <fileName>",
        ),
        # man1/defStreamOutCheckUncolored.1
        _syn(
            "defStreamOutCheckUncolored",
            "",
            "defStreamOutCheckUncolored {true 1 false 0 metal_only}",
        ),
        # man1/dehighlight.1
        _syn(
            "dehighlight",
            "Removes highlights from all the highlighted objects at any stage of the design flow",
            "dehighlight ?-help? ?<objectList>? ?-all | -index <indexValue> | -original | -select?",
        ),
        # man1/delaycal_default_net_delay.1
        _syn(
            "delaycal_default_net_delay",
            "",
            "delaycal_default_net_delay <delay_value> Type: String",
        ),
        # man1/delaycal_default_net_load.1
        _syn(
            "delaycal_default_net_load",
            "",
            "delaycal_default_net_load <load_value>",
        ),
        # man1/delaycal_input_transition_delay.1
        _syn(
            "delaycal_input_transition_delay",
            "",
            "delaycal_input_transition_delay",
        ),
        # man1/delaycal_rd_rnet_fraction_threshold.1
        _syn(
            "delaycal_rd_rnet_fraction_threshold",
            "",
            "delaycal_rd_rnet_fraction_threshold",
        ),
        # man1/delaycal_support_min_max_pin_cap.1
        _syn(
            "delaycal_support_min_max_pin_cap",
            "",
            "delaycal_support_min_max_pin_cap {0 | 1}",
        ),
        # man1/delaycal_support_rise_fall_pin_cap.1
        _syn(
            "delaycal_support_rise_fall_pin_cap",
            "",
            "delaycal_support_rise_fall_pin_cap {0 | 1}",
        ),
        # man1/delaycal_support_wire_load_model.1
        _syn(
            "delaycal_support_wire_load_model",
            "",
            "delaycal_support_wire_load_model {0 | 1}",
        ),
        # man1/delaycal_use_default_delay_limit.1
        _syn(
            "delaycal_use_default_delay_limit",
            "",
            "delaycal_use_default_delay_limit",
        ),
        # man1/delete_bump_grid.1
        _syn(
            "delete_bump_grid",
            "Removes the bump grid from the design",
            "delete_bump_grid ?-help? ?-grid_names string< |> -all?",
        ),
        # man1/delete_ccopt_clock_spines.1
        _syn(
            "delete_ccopt_clock_spines",
            "This command deletes all clock spines matching the specified pattern",
            "delete_ccopt_clock_spines ?-help?",
        ),
        # man1/delete_ccopt_clock_tree_source_group.1
        _syn(
            "delete_ccopt_clock_tree_source_group",
            "This command deletes all clock tree source groups matching the specified pattern",
            "delete_ccopt_clock_tree_source_group ?-help?",
        ),
        # man1/delete_ccopt_clock_tree_spec.1
        _syn(
            "delete_ccopt_clock_tree_spec",
            "",
            "delete_ccopt_clock_tree_spec ?-help? ?-preserve_sink_insertion_delays?",
        ),
        # man1/delete_ccopt_clock_trees.1
        _syn(
            "delete_ccopt_clock_trees",
            "This command deletes all clock trees matching the specified pattern",
            "delete_ccopt_clock_trees ?-help? <pattern> ?-regexp?",
        ),
        # man1/delete_ccopt_flexible_htrees.1
        _syn(
            "delete_ccopt_flexible_htrees",
            "This command deletes all flexible H-trees matching the specified pattern",
            "delete_ccopt_flexible_htrees ?-help?",
        ),
        # man1/delete_ccopt_preferred_cell_stripe.1
        _syn(
            "delete_ccopt_preferred_cell_stripe",
            "Deletes all preferred cell stripes whose names match the specified pattern",
            "delete_ccopt_preferred_cell_stripe ?-help? <pattern> ?-regexp?",
        ),
        # man1/delete_ccopt_skew_groups.1
        _syn(
            "delete_ccopt_skew_groups",
            "This command deletes all skew groups matching the specified pattern",
            "delete_ccopt_skew_groups ?-help? ?-constrains cts | ccopt_initial | ccopt? <pattern> ?-regexp?",
        ),
        # man1/delete_cell_obs.1
        #   WARNING: bracket mismatch: '{' at position 87 closed by ']' at position 184
        #   WARNING: bracket mismatch: '[' at position 86 closed by '}' at position 202
        #   WARNING: unclosed bracket '{' at position 62
        _syn(
            "delete_cell_obs",
            "",
            "delete_cell_obs ?-help? -cells {base_cell | design | module}+ {-obs_shapes <shape>+ | ?{-rects {{<llx1 lly1 urx1 ury1>} {<llx2 lly2 urx2 ury2>}...} | -polygon {<x1 y1 x2 y2 x3 y3> ...}? -layers <layer>+}",
        ),
        # man1/delete_cell_stack_area.1
        _syn(
            "delete_cell_stack_area",
            "Deletes the cell stack area definition",
            "delete_cell_stack_area ?-help? ?-cell <cell_name>? ?-group <group_name>?",
        ),
        # man1/delete_cell_stack_group.1
        _syn(
            "delete_cell_stack_group",
            "Deletes cell stack group definition",
            "delete_cell_stack_group ?-help? ?-name <group_name>?",
        ),
        # man1/delete_cell_virtual_align.1
        _syn(
            "delete_cell_virtual_align",
            "Deletes the cells that need to be virtually aligned",
            "delete_cell_virtual_align ?-help? ?-cell <cells>?",
        ),
        # man1/delete_clock_tree_repeaters.1
        _syn(
            "delete_clock_tree_repeaters",
            "",
            "delete_clock_tree_repeaters ?-help? ?-force?",
        ),
        # man1/delete_feedthru_buffer.1
        #   WARNING: unclosed bracket '{' at position 138
        _syn(
            "delete_feedthru_buffer",
            "Removes the feedthrough buffer specified in the -bufInst option",
            "delete_feedthru_buffer ?-help? ?-dontDelDanglingPort? ?-non_preferred_keep_nets <netNamePattern>? ?-preferred_keep_nets <netNamePattern>? {{-bufInst <bufInstName>} | {-instPrefix instPrefixName}",
        ),
        # man1/delete_gui_object.1
        _syn(
            "delete_gui_object",
            "Deletes specified or selected GUI objects",
            "delete_gui_object ?-help? ?-shape | -text | -marker | -all | -selected?",
        ),
        # man1/delete_inst_space_group.1
        _syn(
            "delete_inst_space_group",
            "Deletes instance space group by a specific group name",
            "delete_inst_space_group ?-help? <groupName>",
        ),
        # man1/delete_path_category.1
        _syn(
            "delete_path_category",
            "Deletes the names of the selected categories",
            "delete_path_category ?-help? <category_name>",
        ),
        # man1/delete_pg_keepout.1
        _syn(
            "delete_pg_keepout",
            "",
            "delete_pg_keepout ?-help? {-cell <lib_cell_name> | -inst <instance_name >| -all } ?-layer <layer_name> | -layerId <layer_id>?",
        ),
        # man1/delete_relative_floorplan.1
        _syn(
            "delete_relative_floorplan",
            "Removes the relative floorplan information from the database",
            "delete_relative_floorplan ?-help? {<obj_name_list >| -all}",
        ),
        # man1/delete_route_type.1
        _syn(
            "delete_route_type",
            "This command deletes the specified route type object created using the create_route_type command",
            "delete_route_type ?-help? -name <string>",
        ),
        # man1/delete_thru_substrate_insts.1
        _syn(
            "delete_thru_substrate_insts",
            "Deletes thru-substrate instances for the specified net",
            "delete_thru_substrate_insts ?-help? {-net <net_name>}",
        ),
        # man1/deleteAIoFiller.1
        _syn(
            "deleteAIoFiller",
            "Deletes area I/O filler cell instances",
            "deleteAIoFiller ?-help? -cell <fillerCellName> ?-prefix <prefix>? -aioRowCluster <aioRowClusterName> | -allAIORowCluster ?-inst <fillerInstanceName>?",
        ),
        # man1/deleteAllCellPad.1
        _syn(
            "deleteAllCellPad",
            "Removes placement padding specified by specifyCellPad for all cells",
            "deleteAllCellPad",
        ),
        # man1/deleteAllDensityAreas.1
        _syn(
            "deleteAllDensityAreas",
            "Removes all partial placement blockages from the floorplan",
            "deleteAllDensityAreas ?-help?",
        ),
        # man1/deleteAllFPObjects.1
        _syn(
            "deleteAllFPObjects",
            "Removes all floorplan objects",
            "deleteAllFPObjects ?-help?",
        ),
        # man1/deleteAllInstGroups.1
        _syn(
            "deleteAllInstGroups",
            "Removes all instance groups",
            "deleteAllInstGroups ?-help?",
        ),
        # man1/deleteAllPowerPreroutes.1
        _syn(
            "deleteAllPowerPreroutes",
            "Removes all power preroutes from the floorplan",
            "deleteAllPowerPreroutes ?-help?",
        ),
        # man1/deleteAllPtnCuts.1
        _syn(
            "deleteAllPtnCuts",
            "Deletes all the partition cuts in the floorplan",
            "deleteAllPtnCuts ?-help?",
        ),
        # man1/deleteAllPtnFeedthroughs.1
        _syn(
            "deleteAllPtnFeedthroughs",
            "Deletes all the partition feedthrough objects in the floorplan",
            "deleteAllPtnFeedthroughs ?-help?",
        ),
        # man1/deleteAllScanCells.1
        _syn(
            "deleteAllScanCells",
            "Unassigns all assigned scan cells",
            "deleteAllScanCells ?-help?",
        ),
        # man1/deleteAllSignalPreroutes.1
        _syn(
            "deleteAllSignalPreroutes",
            "Removes all signal preroutes from the floorplan",
            "deleteAllSignalPreroutes ?-help?",
        ),
        # man1/deleteBNet.1
        _syn(
            "deleteBNet",
            "Given a bussed net or a single bit of a bussed net, logically removes the entire bussed net from a design",
            "deleteBNet ?-help? ?-moduleBased <moduleName>? {-bus busName | -busFromBit <busBitName>}",
        ),
        # man1/deleteBufferTree.1
        _syn(
            "deleteBufferTree",
            "Removes all buffers (except clock path buffers) and inverter pairs, of all footprint types, on all nets in the design",
            "deleteBufferTree ?-help? ?-excNetFile <excFileName>? ?-footprint <footPrintName>? ?-preserveRoute? ?-selNetFile <selF><ileName |>-net<list_of_nets>? ?-verbose?",
        ),
        # man1/deleteBumpConnectTargetConstraint.1
        _syn(
            "deleteBumpConnectTargetConstraint",
            "Deletes existing properties on specified, selected, or all bumps",
            "deleteBumpConnectTargetConstraint ?-help? {-bump <list_of_bumps> | -selected | -all } ?-instName <instance_name> ?-pinName <pin_name> ?-portNum <value>???",
        ),
        # man1/deleteBumps.1
        _syn(
            "deleteBumps",
            "Removes bumps from the design",
            "deleteBumps ?-help? ?-all? ?-bumps <bump+>? ?-floating? ?-overlap_areaio? ?-overlap_blockages? ?-overlap_keepout <bumpCellName>? ?-overlap_macro? ?-selected?",
        ),
        # man1/deleteBusGuide.1
        _syn(
            "deleteBusGuide",
            "Deletes a bus guide",
            "deleteBusGuide ?-help? ?-area <x1><y1><x2><y2>? ?-netGroup {<netGroup> | {<list_of_net_groups>}}? ?-layer {<id> | <id1>:<id2>}? ?-direction {H | V}? ?-all?",
        ),
        # man1/deleteCellEdgeSpacing.1
        _syn(
            "deleteCellEdgeSpacing",
            "",
            "deleteCellEdgeSpacing ?-help? <edgeType1> <edgeType2>",
        ),
        # man1/deleteCellEdgeType.1
        _syn(
            "deleteCellEdgeType",
            "Deletes the cell edge type constraint of the specified cell",
            "deleteCellEdgeType ?-help? -cell <cellName> -edgeType <edgeType>",
        ),
        # man1/deleteCellPad.1
        _syn(
            "deleteCellPad",
            "Deletes the padding for a cell or list of cells",
            "deleteCellPad ?-help? <cellNames>",
        ),
        # man1/deleteDangling1b1Or0s.1
        _syn(
            "deleteDangling1b1Or0s",
            "Deletes dangling 1'b1s or 1'b0s from the Verilog",
            "deleteDangling1b1Or0s",
        ),
        # man1/deleteDanglingNet.1
        _syn(
            "deleteDanglingNet",
            "The deleteDanglingNet command deletes all the nets with zero terms except for assign nets and p/g nets",
            "?-help? ?-hinst <string>?",
        ),
        # man1/deleteDanglingPort.1
        _syn(
            "deleteDanglingPort",
            "Deletes module ports that are disconnected on the outside",
            "deleteDanglingPort ?-help? ?-ptn?",
        ),
        # man1/deleteDeCap.1
        _syn(
            "deleteDeCap",
            "",
            "deleteDeCap ?-help?",
        ),
        # man1/deleteEmptyModule.1
        _syn(
            "deleteEmptyModule",
            "Deletes modules and their instantiations",
            "deleteEmptyModule ?-help? ?-deleteEmpty1801Modules?",
        ),
        # man1/deleteExclusiveGroups.1
        _syn(
            "deleteExclusiveGroups",
            "Deletes existing exclusive regions for groups",
            "deleteExclusiveGroups ?-help? ?-all | <group_name>?",
        ),
        # man1/deleteFiller.1
        _syn(
            "deleteFiller",
            "Removes physical cell instances, such as filler cells, end-cap cells, and well-tap cells, from standard cell rows",
            "deleteFiller ?-cell <fillerCellList>? ?-area {llx lly urx ury}? ?-inst <instanceName>? ?-prefix <prefix>? ?-keepFixed?",
        ),
        # man1/deleteFPObject.1
        _syn(
            "deleteFPObject",
            "Deletes the specified floorplan object by name",
            "deleteFPObject ?-help?",
        ),
        # man1/deleteGAFillerGroup.1
        _syn(
            "deleteGAFillerGroup",
            "Deletes the gate array filler groups created by createGAFillerGroup",
            "deleteGAFillerGroup ?-help? <groupName>",
        ),
        # man1/deleteHaloFromBlock.1
        _syn(
            "deleteHaloFromBlock",
            "Removes block halo values for specific blocks or for all blocks",
            "deleteHaloFromBlock ?-help? ?<inst_name> | -allMacro | -allBlackBox | -allCommitPtn | -allBlock | -allIOPad | -cell <name>?",
        ),
        # man1/deleteInst.1
        _syn(
            "deleteInst",
            "Deletes an instance from a design",
            "deleteInst ?-help? <listOfInst> ?-moduleBased <moduleName>? ?-verbose?",
        ),
        # man1/deleteInstFromInstGroup.1
        _syn(
            "deleteInstFromInstGroup",
            "Removes a hierarchical instance, an instance or list of instances, or a group from a specified group",
            "deleteInstFromInstGroup ?-help?",
        ),
        # man1/deleteInstGroup.1
        _syn(
            "deleteInstGroup",
            "Removes a group that was created",
            "deleteInstGroup ?-help?",
        ),
        # man1/deleteInstPad.1
        _syn(
            "deleteInstPad",
            "Deletes the padding for the specified instances, or all instance-based padding, in the design",
            "deleteInstPad ?<instName>| -all?",
        ),
        # man1/deleteIntegRouteConstraint.1
        _syn(
            "deleteIntegRouteConstraint",
            "Deletes the routing constraints in the database",
            "deleteIntegRouteConstraint ?-help? {-net <net1 net2 ...> | -name <string> | -customConstraints | -all | -additional }",
        ),
        # man1/deleteIoFiller.1
        _syn(
            "deleteIoFiller",
            "Deletes I/O filler cell instances from the design",
            "deleteIoFiller ?-help? ?-cell {<name_list>}? ?-from <coord>? ?-prefix <prefix>? ?-ring <num>? ?-side {top | bottom | left | right}? ?-to <coord>? ?-logic ?-deriveConnectivity??",
        ),
        # man1/deleteIoInstance.1
        _syn(
            "deleteIoInstance",
            "Deletes the specified I/O instance",
            "deleteIoInstance ?-help? -instName {<name1 name2 ...>}",
        ),
        # man1/deleteIoRowFiller.1
        _syn(
            "deleteIoRowFiller",
            "Deletes the I/O row filler cells",
            "deleteIoRowFiller ?-help? -cell {<fillerCellNameList> ...} ?-logic? ?-prefix <prefix>? ?-ioRow <name>? ?-from <coord>? ?-to <coord>?",
        ),
        # man1/deleteMimCap.1
        _syn(
            "deleteMimCap",
            "Deletes the mim caps from the design based on cell type or prefix",
            "deleteMimCap ?-help? ?{?-cell <cellName>? ?-prefix <prefixName>?} ?-area llx lly urx ury??",
        ),
        # man1/deleteModule.1
        _syn(
            "deleteModule",
            "Deletes a hierarchical instance and it's module and optionally, its cell",
            "deleteModule <moduleName> ?-help? ?-cell | -cells?",
        ),
        # man1/deleteModulePort.1
        _syn(
            "deleteModulePort",
            "Disconnects the specified port name from its net and deletes the port",
            "deleteModulePort ?-help? <moduleName> <portName> ?-bus <startId:endId>?",
        ),
        # man1/deleteNet.1
        _syn(
            "deleteNet",
            "Logically deletes nets from a design",
            "deleteNet ?-help? <netName> ?-bus <startId>:<endId>? ?-moduleBased <verilogModule>?",
        ),
        # man1/deleteNetFromNetGroup.1
        _syn(
            "deleteNetFromNetGroup",
            "Removes a net from a net group",
            "deleteNetFromNetGroup ?-help? <netGroupName> -net {<netName> | <netNameList>}",
        ),
        # man1/deleteNetGroup.1
        _syn(
            "deleteNetGroup",
            "Removes a net group that was created earlier",
            "deleteNetGroup ?-help? <netGroupName>",
        ),
        # man1/deleteNetWeight.1
        _syn(
            "deleteNetWeight",
            "Removes the net weight values on the specified nets",
            "deleteNetWeight ?-help? {-all | <netName> ...}",
        ),
        # man1/deleteNotchFill.1
        _syn(
            "deleteNotchFill",
            "Deletes all gaps, notches, acute angles, and hole geometries that were inserted by the fillNotch command",
            "deleteNotchFill",
        ),
        # man1/deletePartition.1
        _syn(
            "deletePartition",
            "Deletes the specified partition",
            "deletePartition ?-help? { <partition_name> | -all | -nested | -non_leaf } ?-undo_tcl_file <file_name> ?-non_leaf??",
        ),
        # man1/deletePGPin.1
        _syn(
            "deletePGPin",
            "Deletes power/ground pins as per the specified parameters and reports the number of deleted power/ground pins",
            "deletePGPin ?-help? ?-area {<x1 y1 x2 y2>}? ?-layer <layer_id> | {<list_of_layer>}? ?-net <net_name>? ?-pg_port? ?-all | -selected?",
        ),
        # man1/deletePinBlkg.1
        _syn(
            "deletePinBlkg",
            "Deletes a pin blockage or all pin blockages",
            "deletePinBlkg ?-help? {-name <pinBlkgName> | -all}",
        ),
        # man1/deletePinFromPinGroup.1
        _syn(
            "deletePinFromPinGroup",
            "Removes a port from a specified pin group",
            "deletePinFromPinGroup ?-help? ?-cell <cellName>? -pinGroup <pinGroupName> -pin {<pinName> | <pinNameList>}",
        ),
        # man1/deletePinGroup.1
        _syn(
            "deletePinGroup",
            "Deletes a pin group or all pin groups that were created earlier",
            "deletePinGroup ?-help? ?-cell <cellName>? -pinGroup <pinGroupName>",
        ),
        # man1/deletePinGuide.1
        _syn(
            "deletePinGuide",
            "Deletes a pin guide object in the floorplan",
            "deletePinGuide ?-help? { -pin <pin_name> | -pinGroup <pin_group_name> | -net <net_name> | -netGroup <net_group_name> | -name <object_name> | -all } ?-cell <ptn_name> | -net <net_name> | -netGroup <net_group_name>?",
        ),
        # man1/deletePipelineNetGroup.1
        _syn(
            "deletePipelineNetGroup",
            "Deletes pipeline net groups including the subgroups created inside the net groups",
            "deletePipelineNetGroup ?-help?",
        ),
        # man1/deletePlaceBlockage.1
        _syn(
            "deletePlaceBlockage",
            "Removes all or individual placement obstructions from the floorplan",
            "deletePlaceBlockage ?-help? ?-all | -type { hard | soft | partial | macroOnly}? ?-all | <obs_name ...>?",
        ),
        # man1/deletePowerSwitch.1
        _syn(
            "deletePowerSwitch",
            "Removes all switches and filler cells that were inserted by the addPowerSwitch command, from either columns or rings, or removes specified power switch defined in CPF",
            "deletePowerSwitch ?-help? ?-1801PowerSwitchRuleName <ruleName>? {{-column | -ring} -powerDomain <powerDomainName>} ?-instanceList {<instName ...>}? ?-isCustomChain?",
        ),
        # man1/deletePtnCut.1
        _syn(
            "deletePtnCut",
            "Deletes all the partition cuts",
            "deletePtnCut ?-help? {-ptn {<ptnName> | <ptnNameList>} | -all}",
        ),
        # man1/deleteRouteBlk.1
        _syn(
            "deleteRouteBlk",
            "Deletes a routing blockage object",
            "deleteRouteBlk ?-help? ?-box {<x1 y1 x2 y2>} | -name <blk> | -all? ?-layer <layerName> | {<layerNameList>} | all? ?-cutLayer <layerName> | {<layerNameList>} | all? ?-drcRegionLayer <layerName> | {<layerNameList>} | all? ?-trimMetalLayer layerName | {layerNameList} | all? ?-type {all | routes | fills | slots | partial}?",
        ),
        # man1/deleteRoutingHalo.1
        _syn(
            "deleteRoutingHalo",
            "Deletes a routing halo for a blackbox, hard macro, or block-level design",
            "deleteRoutingHalo ?-help? ?-lithoHalo? {-allBlocks | -block <blockNameList> | -cell <cellNameList> | -inst <instanceName> | -designHalo}",
        ),
        # man1/deleteRow.1
        _syn(
            "deleteRow",
            "Deletes the specified row(s)",
            "deleteRow ?-help? {-all | -selected | -site <string>| <row>}",
        ),
        # man1/deleteScanCell.1
        _syn(
            "deleteScanCell",
            "Removes the scan cell specification from a library cell",
            "deleteScanCell ?-help? ?<cellName>?",
        ),
        # man1/deleteScanChain.1
        _syn(
            "deleteScanChain",
            "Removes a scan chain specification from the design",
            "deleteScanChain ?-help? <?><chainName>?",
        ),
        # man1/deleteScanChainPartition.1
        _syn(
            "deleteScanChainPartition",
            "Deletes scan chain partitions",
            "deleteScanChainPartition ?-help? {-all | -partition <partitionName1 partitionName2 ...>}",
        ),
        # man1/deleteSdpObject.1
        _syn(
            "deleteSdpObject",
            "",
            "deleteSdpObject ?-help? {-object <object_name_list> ?-keepCellPlacement? | -obstruct <group_name_list> | -emptyRow <instance_name> ?-numRow <value>?}",
        ),
        # man1/deleteSecondaryPGNet.1
        _syn(
            "deleteSecondaryPGNet",
            "Deletes Power/Ground (P/G) net wire segments from specified instances",
            "deleteSecondaryPGNet ?-help? -insts <inst>+ -net <net>",
        ),
        # man1/deleteSelectedFromFPlan.1
        _syn(
            "deleteSelectedFromFPlan",
            "Deletes the currently selected floorplan objects",
            "deleteSelectedFromFPlan ?-help?",
        ),
        # man1/deleteShield.1
        _syn(
            "deleteShield",
            "Deletes physical shielding wires from the specified or selected signal nets and removes SHIELDNET attrib‐ utes from the nets",
            "deleteShield ?-help? {-nets <list_of_signal_nets> | -selected} ?-routes_only {0 | 1}?",
        ),
        # man1/deleteSizeBlockage.1
        _syn(
            "deleteSizeBlockage",
            "Deletes a size blockage object",
            "deleteSizeBlockage ?-help? ?-name <blockageName>? ?-selected? ?-all?",
        ),
        # man1/deleteSpareModule.1
        _syn(
            "deleteSpareModule",
            "Deletes the instantiation of a created spare module and all the spare instances under the hinst",
            "deleteSpareModule hInst<Name>",
        ),
        # man1/deleteTieHiLo.1
        _syn(
            "deleteTieHiLo",
            "Deletes placed tie cells from the netlist and reconnects the tie input pins back to 1'b1 and 1'b0",
            'deleteTieHiLo ?-help? ?-cell <tieCellName> | "<listOfTieCellNames>"? ?-prefix <prefixName>?',
        ),
        # man1/deleteTrack.1
        _syn(
            "deleteTrack",
            "Deletes a set of tracks in the database",
            "deleteTrack ?-help? ?-dir {<X|Y>}? ?-layer <layerNameList>?",
        ),
        # man1/deleteTSV.1
        _syn(
            "deleteTSV",
            "Deletes the specified TSVs",
            "deleteTSV {-all | -selected| -unassigned}",
        ),
        # man1/deleteUninstantiatedModules.1
        _syn(
            "deleteUninstantiatedModules",
            "Deletes uninstantiated modules",
            "deleteUninstantiatedModules ?-help? ?-reportOnly?",
        ),
        # man1/deleteUserBundleNet.1
        _syn(
            "deleteUserBundleNet",
            "Deletes the specified flightline net bundle",
            "deleteUserBundleNet ?-help? <name>",
        ),
        # man1/deleteWhatIfTimingAssertions.1
        _syn(
            "deleteWhatIfTimingAssertions",
            "Removes the timing arc specifications of the specified blackbox or blackblob",
            "deleteWhatIfTimingAssertions ?<blackBoxCellName>? ?-port <portName> | -from <port> -to <port> | -from <port> | -to <port>? ?-assertion_type {comb | setup | hold}? ?-rising | -falling?",
        ),
        # man1/deleteWorkspace.1
        _syn(
            "deleteWorkspace",
            "Deletes the specified workspace",
            "deleteWorkspace ?-help? -name <workspaceName> ?-dir <directory>?",
        ),
        # man1/deriveTimingBudget.1
        _syn(
            "deriveTimingBudget",
            "Generates timing budgets for partitions for standalone implementation",
            "deriveTimingBudget ?-help? ?-parameterized? ?-cycleRatio | -stageBased | -preliminary? ?-allIlmHinsts | -inst <instanceName >| -ptn <partitionName>? ?-verbose? ?-views <string>?",
        ),
        # man1/deselect_bump.1
        _syn(
            "deselect_bump",
            "Enables you to deselect bumps in different ways",
            "deselect_bump ?-help? ?-alternate {row column}? ?-area {{x1 y1 x2 y2} ...}? ?-assigned? ?-bump_cell {cell_list}? ?-bumps {<bump_list>}? ?-floating? ?-max_distance_to_side <distance>? ?-nets {<net_list>}? ?-side {top bottom left right}? ?-start_lower_left? ?-type {signal power ground}?",
        ),
        # man1/deselect_obj.1
        _syn(
            "deselect_obj",
            "Deselects the specified object or the list of objects from the Viewer",
            "deselect_obj ?-help? {?-all? | ?<obj_list>?}",
        ),
        # man1/deselectAll.1
        _syn(
            "deselectAll",
            "Deselects all selected nets",
            "deselectAll ?-help?",
        ),
        # man1/deselectBusGuide.1
        _syn(
            "deselectBusGuide",
            "Deselects a bus guide segment",
            "deselectBusGuide ?-help? ?-area <x1><y1><x2><y2>? ?-netGroup {<netGroup> | {<list_of_net_groups>}}? ?-layer {<id> | <id1>:<id2>}? ?-direction {H | V}? ?-all?",
        ),
        # man1/deselectGroup.1
        _syn(
            "deselectGroup",
            "Deselects a group",
            "deselectGroup <groupName> ?-help?",
        ),
        # man1/deselectInst.1
        _syn(
            "deselectInst",
            "Deselects the specified instance",
            "deselectInst ?-help?",
        ),
        # man1/deselectInstByCellName.1
        _syn(
            "deselectInstByCellName",
            "Deselects an instance by cell name",
            "deselectInstByCellName ?-help?",
        ),
        # man1/deselectInstOnNet.1
        _syn(
            "deselectInstOnNet",
            "Deselects an instance on a net",
            "deselectInstOnNet ?-help?",
        ),
        # man1/deselectIOPin.1
        _syn(
            "deselectIOPin",
            "Deselects an I/O pin",
            "deselectIOPin ?-help?",
        ),
        # man1/deselectModule.1
        _syn(
            "deselectModule",
            "",
            "deselectModule ?-help? <name>",
        ),
        # man1/deselectNet.1
        _syn(
            "deselectNet",
            "Deselects the specified net",
            "deselectNet ?-help? ?<netName>? ?-clock | -nonDefaultRule | -shield?",
        ),
        # man1/deselectPin.1
        _syn(
            "deselectPin",
            "Deselects the specified pin",
            "deselectPin ?-help? <name>",
        ),
        # man1/deselectSecondaryPGNet.1
        _syn(
            "deselectSecondaryPGNet",
            "Deselects Power/Ground (P/G) net wire segments from specified instances",
            "deselectSecondaryPGNet ?-help? -insts <inst>+ -net <net>",
        ),
        # man1/detachModulePort.1
        _syn(
            "detachModulePort",
            "Detaches the net connected to the specified port on the specified hierarchical instance",
            "detachModulePort ?-help? <hinstName> <portName>",
        ),
        # man1/detachSdpGroup.1
        _syn(
            "detachSdpGroup",
            "Detaches the specified Structured Data Path (SDP) object from the parent group",
            "detachSdpGroup ?-help? -name {<objNames>}",
        ),
        # man1/detachTerm.1
        _syn(
            "detachTerm",
            "Disconnects a terminal from a net",
            "detachTerm ?-help? ?-moduleBased <verilogModule>? <instName> <termName> ?<netName>?",
        ),
        # man1/detailRoute.1
        _syn(
            "detailRoute",
            "Uses the NanoRoute router to perform detailed routing on the entire design, an area of the design specified by the bounding box, or on selected nets",
            "detailRoute ?-help? ?-select? ?<area>?",
        ),
        # man1/disconnectDanglingPort.1
        _syn(
            "disconnectDanglingPort",
            "Disconnects dangling nets from ports in the whole design, from the top level to the bottom level",
            "disconnectDanglingPort ?-help? ?-keepInput? ?-keepOutput? ?-keepInout? ?-partitionOnly?",
        ),
        # man1/display_obj_connectivity.1
        _syn(
            "display_obj_connectivity",
            "Displays the connections of specified macros, selected macros, or specified ports",
            "display_obj_connectivity ?-help? ?-direction {in|out|all}? ?-level <level>? ?-line_to_ports? ?-min_connection <number>? {-insts <string> | -ports <string> | -selected | -reset } ?-through_registers ?-all_registers??",
        ),
        # man1/display_temperature_result.1
        _syn(
            "display_temperature_result",
            "Displays the tile-based temperature map file generated by Sigrity Celsius",
            "display_temperature_result ?-help? -layer <string>",
        ),
        # man1/display_timing_map.1
        #   WARNING: bracket mismatch: '{' at position 27 closed by ']' at position 86
        #   WARNING: unmatched closing bracket '}' at position 96
        _syn(
            "display_timing_map",
            "Sets color-coded slack threshold values for worst timing paths",
            "display_timing_map ?-help? {?-step float -threshold float? -check_type {setup | hold}? | -clear}",
        ),
        # man1/displayBufTree.1
        _syn(
            "displayBufTree",
            "Displays a buffer tree associated with the specified net",
            "displayBufTree ?-help? -net <netName> ?-outfile <fileName>?",
        ),
        # man1/displayScanChain.1
        _syn(
            "displayScanChain",
            "Displays a scan chain",
            "displayScanChain ?-help? ?<chain_name>?",
        ),
        # man1/displaySpareCell.1
        _syn(
            "displaySpareCell",
            "Displays the results of placing the spare instances",
            "displaySpareCell",
        ),
        # man1/displayUserBundleNet.1
        _syn(
            "displayUserBundleNet",
            "Displays flightlines for the specified net bundle",
            "displayUserBundleNet ?-help? ?-keepExisting? -netBundle <bundleName> ?-remove?",
        ),
        # man1/distributed_mmmc_disable_reports_auto_redirection.1
        _syn(
            "distributed_mmmc_disable_reports_auto_redirection",
            "",
            "distributed_mmmc_disable_reports_auto_redirection {true | false}",
        ),
        # man1/do_extract_model.1
        _syn(
            "do_extract_model",
            "Builds a Liberty (.lib) format model for the top cell, which is the timing model equivalent of the original design",
            "do_extract_model ?-help? <model_filename> ?-abs_tol_val <float>? ?-abs_tol_val_optimistic <float>? ?-abs_tol_val_pessimistic <float>? ?-assertions <constraint filename>? ?-cell_name <cell_name>? ?-clock_slews {<clk_slew1 clk_slew2>...}? ?-format <string>? ?-gain <integer>? ?-include_aocv_weights? ?-input_slews {<input_slew1 input_slew2>...}? ?-lib_name <lib_name>? ?-max_num_loads <value>? ?-max_num_slews <value>? ?-output_loads {<output_load1 output_load2>...}? ?-per_tol_val <float>? ?-per_tol_val_optimistic <float>? ?-per_tol_val_pessimistic <float>? ?-pg? ?-precision <integer>? ?-resolution <float>? ?-tolerance <float>? ?-validate <string>? ?-verilog_shell_file <filename>? ?-verilog_shell_module <top_module_name>? ?-view <string>? ?-check?",
        ),
        # man1/dump_histogram_view.1
        _syn(
            "dump_histogram_view",
            "Saves (dumps) the image of the histogram shown in Global Timing Debug automatically during the process",
            "dump_histogram_view ?-help? -name <string> ?-type <string>?",
        ),
        # man1/dump_unannotated_nets.1
        _syn(
            "dump_unannotated_nets",
            "Shows the percentage of nets annotated by a specific type and also prints the names of all nets that are not annotated by that type",
            "dump_unannotated_nets ?-help? ?-file <filename>? -type <annotationType>",
        ),
        # man1/dumpCongestArea.1
        _syn(
            "dumpCongestArea",
            "Writes the routing congestion information to an ASCll output file",
            "dumpCongestArea ?-help? <file_name> ?-all?",
        ),
        # man1/dumpMultiBitFlopMappingFile.1
        _syn(
            "dumpMultiBitFlopMappingFile",
            "Dumps the multi-bit flip-flop (MBFF) mapping files in the specified directory with the spec‐ ified prefix name",
            "dumpMultiBitFlopMappingFile ?-help? ?-mapOutputPins {false | true | all}? ?-output <directory>? ?-prefix <fileName_prefix>?",
        ),
        # man1/dumpNanoCongestArea.1
        _syn(
            "dumpNanoCongestArea",
            "Writes the NanoRoute routing congestion information to an ASCll output file",
            "dumpNanoCongestArea ?-help? <file_name> ?-all?",
        ),
        # man1/dumpNetsInCongestedArea.1
        _syn(
            "dumpNetsInCongestedArea",
            "Outputs the names of nets in the congested area of the design into the specified file, based on earlyGlobalRoute results",
            "dumpNetsInCongestedArea ?-help? <file_name>",
        ),
        # man1/dumpOutVias.1
        _syn(
            "dumpOutVias",
            "Helps in debugging and testing",
            "dumpOutVias ?-help? ?-autogen? ?-file <filename>? ?-all_via | -signal | -all_rule | -default | -ndr?",
        ),
        # man1/dumpPictures.1
        _syn(
            "dumpPictures",
            "Dumps images at various stages of the Innovus flow (such as congestion map, cell density map, floorplan view, colored hierarchy map), when executed in batch mode",
            "dumpPictures ?-help? -dir <string>?-fullScreen? -prefix <string>",
        ),
        # man1/dumpToGIF.1
        _syn(
            "dumpToGIF",
            "Saves a snapshot of the current screen to a GIF file with the specified name in the current directory",
            "dumpToGIF ?-help? <filename> ?-honor_umask?",
        ),
        # man1/earlyGlobalRoute.1
        _syn(
            "earlyGlobalRoute",
            "Early Global Route (earlyGlobalRoute) is a quick global routing for estimating routing-related conges‐ tion and parasitic (resistance and capacitance) values",
            "earlyGlobalRoute ?-help?",
        ),
        # man1/eco_opt_ir_aggressor.1
        _syn(
            "eco_opt_ir_aggressor",
            "",
            "eco_opt_ir_aggressor ?-help? ?-aggr_only? -domain_threshold <value> ?-effort {high||medium||low}? ?-noEcoRoute? ?-pdn_model <directoryname>? -state_directory <directoryname>",
        ),
        # man1/ecoAddBacksideConstraint.1
        _syn(
            "ecoAddBacksideConstraint",
            "Adds a new backside layer constraint on a net",
            "ecoAddBacksideConstraint ?-help? -embeddedFtvCells {list of cells} -net <netName> -topPreferredLayer <top-layer-name> ?-groupTerms {{..} {..}} | -minimumFtvs? ?-loc {xLoc yLoc} | { xLoc yLoc inv_xLoc inv_yLoc} ?-bufOrient {R0 | R90 | R180 | R270 | MX | MX90 | MY | MY90}??",
        ),
        # man1/ecoAddRepeater.1
        #   WARNING: unmatched closing bracket ']' at position 1170
        _syn(
            "ecoAddRepeater",
            "Adds either a single buffer or two inverters on a net",
            "ecoAddRepeater ?-help? {-net <netName> | -term <term1 term2>… } ?-hinstGuide <hinstName> | -spreadDist <distance> | -spreadCount <number>? ?-name <instName> | -spreadDist <distance> | -spreadCount <number>? ?-spreadDist <distance> | -spreadCount <number>? ?-newNetName <netName> | -spreadDist <distance> | -spreadCount <number>? ?-loc {xLoc yLoc} | { xLoc yLoc inv_xLoc inv_yLoc} | -offLoadAtLoc {x1a y1a x1b y1b x2a y2a x2b y2b ....} | { xLoc yLoc inv_xLoc inv_yLoc} | -offLoadSlack <slack> | -spreadDist <distance> | -spreadCount <number>? ?-radius μm | -logicalChangeOnly | -spreadDist <distance> | -spreadCount <number>? ?-offLoadAtLoc {x1a y1a x1b y1b x2a y2a x2b y2b ....} | { xLoc yLoc inv_xLoc inv_yLoc} | -offLoadSlack <slack> | -spread‐ Dist <distance> | -spreadCount <number>? ?{?-loc {xLoc yLoc} | { xLoc yLoc inv_xLoc inv_yLoc}? ?-relativeDistToSink <sinkWeight>? ?-offLoadAtLoc {x1a y1a x1b y1b x2a y2a x2b y2b ....} | { xLoc yLoc inv_xLoc inv_yLoc}?} ?-radius μm?? ?-loc {xLoc yLoc} | { xLoc yLoc inv_xLoc inv_yLoc} ?-bufOrient {R0 | R90 | R180 | R270 | MX | MX90 | MY | MY90}?? ?-net <netName> ?-spreadDist <distance>?? ?-spreadPrefix <prefix>?? ?-spreadDist <distance> ?-firstSpreadDist <distance>?? ?-cell <cell1 cell2>? ?-relativeDistToSink <sinkWeight> | -offLoadAtLoc {x1a y1a x1b y1b x2a y2a x2b y2b ....} | { xLoc yLoc inv_xLoc inv_yLoc} | -offLoadSlack <slack> | -spreadDist <distance> | -spreadCount <number>? ?-loc {xLoc yLoc} | { xLoc yLoc inv_xLoc inv_yLoc} | -noPlace?",
        ),
        # man1/ecoChangeCell.1
        _syn(
            "ecoChangeCell",
            "Upsizes or downsizes the specified instance based on the available footprint",
            "ecoChangeCell ?-help? -cell <list_of_cells >|-upsize | -downsize -inst <instNames> ?-loc {xLoc yLoc} ?-orient {R0 | R90 | R180 | R270 | MX | MX90 | MY | MY90}?? ?-pinMap <oldpin1 newpin1 oldpin2 newpin2> ...?",
        ),
        # man1/ecoClone.1
        _syn(
            "ecoClone",
            "Clones combinational logic if logic does not have any user constraints like don’t size/touch and so on",
            "ecoClone ?-help? ?-allow_sequential? ?-auto? ?-balance <num>? ?-cells <list_of_cells>? ?-delete_buffer_trees? ?-dont_legalize? ?-dont_resize? ?-force? ?-from <pin names>? ?-instances <instance names>? ?-locs <list_of_locations>? ?-loop <number>? ?-max_levels <integer>? ?-max_num_loads <integer>? ?-min_num_loads <integer>? ?-nets <list_of_nets>? ?-numClones <number>? ?-preview? ?-radius <number>? ?-same_hier_only? ?-terms <list_of_term_lists>? ?-to <pin names>? ?-verbose?",
        ),
        # man1/ecoCloneFlop.1
        _syn(
            "ecoCloneFlop",
            "",
            "ecoCloneFlop ?-help? ?-force? -instances <flopInstName> ?-max_num_loads <num_of_loads>? ?-numClones <number>? ?-radius <num_of_rows>? ?-verbose?",
        ),
        # man1/ecoCloneInstGroup.1
        _syn(
            "ecoCloneInstGroup",
            "Clones the specified instances",
            "ecoCloneInstGroup ?-help? -maxFanout <integer> Clones the specified instances. The list of instances to be cloned is specified by the setOptMode -opt_clone_insts_list { {…} … } parameter.",
        ),
        # man1/ecoCompareNetlist.1
        _syn(
            "ecoCompareNetlist",
            "Compares a specified netlist with the design in the database for structural or logical equivalence, and creates a file containing the differences found",
            "ecoCompareNetlist ?-help? -def <referenceFileName>?-logical? ?-outfile <fileName>? ?-outputPhysicalInstInFile <physicalInstFile>? ?-referenceData {inMemory | external}?",
        ),
        # man1/ecoDefIn.1
        _syn(
            "ecoDefIn",
            "Restores physical information from an old design and compares this information with the design in memory",
            "ecoDefIn ?-help? ?-postMask ?-suffix <suffixName>?? ?-useGACells <GACoreSite>? ?-reportFile <fileName>? ?-cleanFEData? ?-keepInstLoc? ?-mergeFloatingRouteToPGNet <netName>? ?-ecoDef {<new_DEF_fileName>}? <filename>",
        ),
        # man1/ecoDeleteRepeater.1
        _syn(
            "ecoDeleteRepeater",
            "Deletes a buffer or pair of inverters connected back-to-back",
            "ecoDeleteRepeater ?-help??-logicalChangeOnly? { -inst {<list_of_instances>} | -invPair {{<inv1 inv2>} {<inv3 inv4>} ...} }",
        ),
        # man1/ecoDesign.1
        _syn(
            "ecoDesign",
            "Takes an Innovus database and a modified netlist as input and performs ECO operations",
            "ecoDesign ?-help?",
        ),
        # man1/ecoDisableNetRenamingForFlatNetlist.1
        _syn(
            "ecoDisableNetRenamingForFlatNetlist",
            "",
            "ecoDisableNetRenamingForFlatNetlist",
        ),
        # man1/ecoMergeCombinationalCell.1
        _syn(
            "ecoMergeCombinationalCell",
            "Merges combinational cells into multi-bit cells for the specified instance",
            "ecoMergeCombinationalCell ?-help? ?-area? ?-cell <target_cell_name_list>? ?-force? -inst <comboInstName> | -listFile <instNamesFile> | -all ?-power? -preCTS | -postCTS",
        ),
        # man1/ecoOaDesign.1
        _syn(
            "ecoOaDesign",
            "Imports an OpenAccess database and an ECO-modified netlist",
            "ecoOaDesign ?-help? <lib cell view> -ecoVerilogFile <input_fileName> ?-postMask ?-<suffix><suffixName>?? ?-useGACells <GACoreSite>? ?-reportFile <output_fileName>?",
        ),
        # man1/ecoPlace.1
        _syn(
            "ecoPlace",
            "Incrementally places the unplaced standard cells",
            "ecoPlace ?-help? ?-fixPlacedInsts {true|false}? ?-place_detail_use_GA_filler_groups {true|false}? ?-reportSpareCells <fileName>? ?-timing_driven {true|false}? ?-useGACells <GACoreSite>? ?-useGAFillerCells <GAFillerCells>? ?-useSpareCells {true|false}?",
        ),
        # man1/ecoRemoveTiedInputs.1
        _syn(
            "ecoRemoveTiedInputs",
            "Remaps or restructures gates that have inputs connected to the same net",
            "ecoRemoveTiedInputs ?-help? ?-base_cells <cell_list>? ?-ignore_base_cells <cell_list>? ?-ignore_insts <inst_list>? ?-insts <inst_list>? ?-relaxed_placement? ?-term <term_list>? ?-verbose? ?-report?",
        ),
        # man1/ecoRoute.1
        _syn(
            "ecoRoute",
            "This command is part of an ECO flow process and is based on the NanoRoute® router",
            "ecoRoute ?-help? ?-ignore_route <string>? ?-handlePartition? ?-fix_drc ?-cut_color_flip {0 1}? ?-trim_layer_patch? ?-layer_range <bottomLayer>:<topLayer>? ?<area>?? ?-fix_filler_drc_with_patch_only ?-passive_fill? ?-layer_range <bottomLayer>:<topLayer>? ?<area>?? ?-fix_filler_drc_with_patch_only | -fix_drc? ?-target | -fix_drc | -prototype? ?-modifyOnlyLayers <bottomLayer>:<topLayer> | -fix_drc?",
        ),
        # man1/ecoSplitCombinationalCell.1
        _syn(
            "ecoSplitCombinationalCell",
            "Splits all multi-bit combinational cell instances to single-bit combinational cells",
            "ecoSplitCombinationalCell ?-help? ?-force? ?-fullSplit? ?-legal? ?-skipRoute? -inst <combInstName> | {{Mbcb1 combCell1} {Mbcb2 combCell2}...} | -listFile <fileName> | -all -preCTS | -postCTS | -postRoute",
        ),
        # man1/ecoSplitComplexFlop.1
        _syn(
            "ecoSplitComplexFlop",
            "Splits a complex flip-flop into a simple flip-flop and combinational logic for the specified in‐ stance",
            "ecoSplitComplexFlop ?-help? ?-force? {-inst {<inst1>, <inst2>,...} | -listFile <instNamesFile>| -all} ?-legal? ?-preCTS | -postCTS | -postRoute? ?-power? ?-skipRoute?",
        ),
        # man1/ecoSplitFlop.1
        _syn(
            "ecoSplitFlop",
            "Splits a multi-bit flip-flop (MBFF) into single-bit flip-flops for the specified instance",
            "ecoSplitFlop ?-help? ?-batch? ?-force? ?-fullSplit? {-inst <flopInstName> | {{Mbff1 flopCell1} {Mbff2 flopCell2}...} | -listFile <<fileName>> | -all} ?-legal? ?-power? {-preCTS | -postCTS | -postRoute} ?-skipRoute?",
        ),
        # man1/ecoSwapSpareCell.1
        _syn(
            "ecoSwapSpareCell",
            "Swaps an unplaced or placed cell with a cell in the spare cell list",
            "ecoSwapSpareCell ?-help?",
        ),
        # man1/edit_bump_name.1
        _syn(
            "edit_bump_name",
            "Modifies the names of selected or specified bumps according to the specified pattern",
            "edit_bump_name ?-help? -from <current_pattern > ?-selected? -to <new_pattern>",
        ),
        # man1/editAddFillet.1
        _syn(
            "editAddFillet",
            "Adds a tear-drop fillet between a wire and bump connection",
            "editAddFillet ?-help?",
        ),
        # man1/editAddPoly.1
        _syn(
            "editAddPoly",
            "Defines a vertex or corner of a polygon",
            "editAddPoly ?-help? <point>",
        ),
        # man1/editAddRoute.1
        _syn(
            "editAddRoute",
            "Creates a wire segment that starts or ends at the specified coordinates",
            "editAddRoute ?-help? <point>",
        ),
        # man1/editAddTrimMetal.1
        _syn(
            "editAddTrimMetal",
            "Adds trim metal at the specified location",
            "editAddTrimMetal ?-help? ?-layer <string>? -location {<x y>} ?-mask <integer>? ?-snap_to_end?",
        ),
        # man1/editAddVia.1
        _syn(
            "editAddVia",
            "Creates a via instance and places the origin at the specified coordinates",
            "editAddVia ?-help? <point>",
        ),
        # man1/editAdjust.1
        _syn(
            "editAdjust",
            "Aligns wires and pins on the basis of the specified options",
            "editAdjust ?-help? ?-adjust_size? -refer_obj {top bottom left right} {?-align_edge {left center right top middle bottom diag45_top diag45_middle diag45_bottom diag135_top diag135_middle diag135_bottom}? ?-space_mode {horizontal vertical dist_horizontal dist_vertical diag45 diag135 dist_diag45 dist_diag135} ?-space <float_value>??}",
        ),
        # man1/editBumpConnectTargetConstraint.1
        _syn(
            "editBumpConnectTargetConstraint",
            "Modifies the property values on bumps",
            "editBumpConnectTargetConstraint ?-help? {-bump <list_of_bumps> | -selected } {-instName <instance_name> {?-toInstName <instance_name>? ?-pinName <pin_name> {?-toPinName <pin_name>? ?{-portNum <value> -toPortNum <value>}?}?}}",
        ),
        # man1/editChangeLayer.1
        _syn(
            "editChangeLayer",
            "Changes the layer of selected wires and updates vias connecting to the wires that change layers",
            "editChangeLayer ?-help? ?-layer_horizontal <layer> | -layer_horizontal_movement <integer>? ?-layer_horizontal <layer> | -layer_vertical_movement <integer>? ?-layer_vertical <layer> | -layer_horizontal_movement <integer>? ?-layer_vertical <layer> | -layer_vertical_movement <integer>?",
        ),
        # man1/editChangeMask.1
        _syn(
            "editChangeMask",
            "Changes the mask for the selected wires, vias, physical pins, or trim metal to the specified color",
            "editChangeMask ?-help? {-to {0 1 2} | ??-top {0 1 2}? ?-bottom {0 1 2}? ?-cut {0 1 2}?? | -trim_metal {0 1 2}}",
        ),
        # man1/editChangeNet.1
        _syn(
            "editChangeNet",
            "Changes the net associated with selected physical pins, wires, and vias",
            "editChangeNet ?-help? -to <netName>",
        ),
        # man1/editChangeRule.1
        _syn(
            "editChangeRule",
            "Changes the LEF rule associated with selected wire segments from the <old_rule>to the <new_rule>",
            "editChangeRule ?-help? ?-from <old_rule>? -to <new_rule> Changes the LEF rule associated with selected wire segments from the <old_rule>to the <new_rule>. You must select the wires for which the rule needs to be changed before running editChangeRule. You can select wires either using the GUI or by using the editSelect command.",
        ),
        # man1/editChangeStatus.1
        _syn(
            "editChangeStatus",
            "Changes the DEF status of selected wires or vias to the specified status",
            "editChangeStatus ?-help? ?<shield_net_name>? ?-nets <net>+? -to {ROUTED | FIXED | COVER | SHIELD | NOSHIELD}",
        ),
        # man1/editChangeVia.1
        _syn(
            "editChangeVia",
            "Replaces the selected vias or the vias listed in -from with the specified vias or with vias having the specified cut class and pattern",
            "editChangeVia ?-help? ?-net <net_name>? ?-signal_only {0 | 1}? {?-from <string> ?-area {<x1 y1 x2 y2>} | -at {<x y>}?? | ?-selected?} {-to <string> | ?-via_columns <integer> -via_rows <integer> ?-cut_class <class_name>??}",
        ),
        # man1/editCommitPoly.1
        _syn(
            "editCommitPoly",
            "Ends a newly created polygon at the specified coordinates",
            "editCommitPoly ?-help? <point>",
        ),
        # man1/editCommitRoute.1
        _syn(
            "editCommitRoute",
            "Ends a newly created wire segment at the specified coordinates",
            "editCommitRoute ?-help? <point>",
        ),
        # man1/editCopy.1
        _syn(
            "editCopy",
            "Copies selected or specified objects to the specified location",
            "editCopy ?-help? ?-objects <string>? ?-orientation {R0 R90 R180 R270 MX MX90 MY MY90}? ?-net <net_name> | -net_group <string> | -keep_net_name? ?-rotate_point {x y} | -times <integer>? ?-rotate_point {x y} | ?<dx> <dy>??",
        ),
        # man1/editCutWire.1
        _syn(
            "editCutWire",
            "Cuts wires, bus guides, or rectangles at the specified location",
            "editCutWire ?-help? ?-only_visible_wires? ?-selected? {-lines {<x1 y1 x2 y2 ...>} | ?-box {x1 y1 x2 y2} ?-delete_wire_in_box?? }",
        ),
        # man1/editDelete.1
        #   WARNING: unclosed bracket '[' at position 365
        _syn(
            "editDelete",
            "Deletes physical wires, any vias connected to the wires, and violation markers associated with the wires",
            "editDelete ?-help? ?-area {<x1 y1 x2 y2>}? ?-direction {H | V | 45 | 135}? ?-duplicate_via? ?-floating_via? ?-layer {<list_of_layers>}? ?-nets <net>*? ?-parallel_routing? ?-physical_pin_only? ?-regular_wire_with_drc? ?-selected? ?-shape {RING STRIPE FOLLOWPIN IOWIRE COREWIRE BLOCKWIRE PADRING BLOCKRING FILLWIRE FILLWIREOPC DRCFILL None}? ?-shield? ?-shield_only? ?-status {FIXED NOSHIELD ROUTED SHIELD UNKNOWN} ?-subclass <sublass_name>? ?-trim_metal? ?-type {Regular| Special | Patch}? ?-use {CLOCK POWER SIGNAL}? ?-via_cell <cell_name_list>? ?-with_edit_flag {0 | 1}? ?-object_type {Wire Via}?",
        ),
        # man1/editDeleteFillet.1
        _syn(
            "editDeleteFillet",
            "Deletes the tear-drop fillet that was added between a wire and bump connection with the editAddFillet command",
            "editDeleteFillet ?-help?",
        ),
        # man1/editDeselect.1
        _syn(
            "editDeselect",
            "Deselects wires and vias based on specified parameters",
            "editDeselect ?-help? ?-area {<x1><y1><x2><y2>}? ?-direction {H | V | 45 | 135}? ?-floating_via? ?-layer <list_of_layers>? ?-nets <net>*? ?-physical_pin_only? ?-regular_wire_with_drc? ?-shape {RING STRIPE FOLLOWPIN IOWIRE COREWIRE BLOCKWIRE PADRING BLOCKRING FILLWIRE FILLWIREOPC DRCFILL None}? ?-shield? ?-shield_only? ?-status {COVER FIXED NOSHIELD ROUTED SHIELD UNKNOWN}? ?-subclass <sublass_name>? ?-type {Regular Special Patch}? ?-use {CLOCK POWER SIGNAL}? ?-via_cell <cell_name_list>? ?-with_edit_flag {0 | 1}? ?-object_type {Wire Via}? ?-from_pin <pin_name> -to_pin <pin_name>?",
        ),
        # man1/editDuplicate.1
        _syn(
            "editDuplicate",
            "Copies the geometry of selected special wires and pastes them at the same coordinates",
            "editDuplicate ?-help? -layer_horizontal <layer> -layer_vertical <layer>",
        ),
        # man1/editFixWideWires.1
        _syn(
            "editFixWideWires",
            "Splits wires that violate the MAXWIDTH value in the LEF LAYER (Routing) statement",
            "editFixWideWires ?-help?",
        ),
        # man1/editMerge.1
        _syn(
            "editMerge",
            "Merges all wires of the same width, layer, and net that are colinear with and electrically connected to a se‐ lected wire",
            "editMerge ?-help?",
        ),
        # man1/editMove.1
        _syn(
            "editMove",
            "Moves selected wires, boundary pins, or vias",
            "editMove ?-help? {??-direction {x y diag45 diag135} -distance <float>? | ?-dx <float> -dy <float>? | -to {x y}? }",
        ),
        # man1/editPin.1
        _syn(
            "editPin",
            "Modifies properties of pins, such as pin spreading, pin location, pin width and depth, spacing, snap-to loca‐ tion, and status",
            "editPin ?-help? ?-cell <cellName> | {-hinst <hinstName >?-refMaster?}? ?-end {<x y>}? ?-fixedPin? ?-global_location? ?-include_rectilinear_edge? ?-masterCloneAware? ?-offsetEnd <value>? ?-offsetStart <value>? -pin {<pinName> | <pinNameList>} ?-pinDepth <pinDepthValue>? ?-pinWidth <pinWidthValue>? ?-quiet? ?-skipWrappingPins? ?-snap {TRACK | USERGRID | MGRID}? ?-spreadDirection {clockwise | counterclockwise | both}? ?-start {<x y>}? ?-use { SIGNAL | CLOCK | ANALOG }? ?{-layer {<layerId> | <layerIdListName>} | {?-layerH <layerId>? ?-layerV <layerId>?}} ?-layer_priority? ?-assign {<x y>} | -spreadType {START | CENTER | SIDE | EDGE | RANGE} | -pattern {fill_track | fill_layer | fill_optimised | fill_diagonal | fill_sinusoidal | fill_checkerboard}?? ?-side <sideName> | -edge <edgeNumber>? ?-fixOverlap {0|1} ?-honorConstraint {0|1}?? ?-pattern {fill_track | fill_layer | fill_optimised | fill_diagonal | fill_sinusoidal | fill_checkerboard} ?-reverse_al‐ ternate?? ?-spacing <spacingValue> ?-unit {MICRON | TRACK}??",
        ),
        # man1/editPowerVia.1
        #   WARNING: unclosed bracket '[' at position 650
        #   WARNING: unclosed bracket '[' at position 671
        #   WARNING: unclosed bracket '[' at position 703
        _syn(
            "editPowerVia",
            "Modifies or deletes existing power vias or adds new power vias to the design",
            "editPowerVia ?-help? {-add_vias {0 | 1} | -modify_vias {0 | 1} | -delete_vias {0 | 1}} ?-area {{<x1 y1 x2 y2>} {<x3 y3 x4 y4>} ...}? ?-between_selected_wires {0 | 1} | -selected_blocks {0 | 1} | -selected_wires {0 | 1} | -selected_vias {0 | 1}? ?-bottom_layer <layername>? ?-cell_pins {<cell1>:<pin1> <cell2>:<pin2> ...}? ?-create_via_on_merged_target_on_layer <layerName>? ?-create_via_on_merged_target_within micron? ?-create_via_on_signal_pins {0 | 1}? ?-exclude_stack_vias {0 | 1}? ?-followpin_via_stapling {<cutclass1 weight1 cutclass2 weight2>}? ?-nets <net_list>? ?-orthogonal_only {0 | 1}? ?-split_long_via {<threshold step offset length>}? ?-split_vias {0 | 1} ?-same_sized_stack_vias {0 | 1} ?-skip_via_on_wire_shape {?Blockring? ?Stripe? ?Followpin? ?Corewire? ?Blockwire? ?Iowire? ?Padring? ?Ring? ?Fillwire? ?Noshape?} ?-skip_via_on_pin {?Pad? ?Block? ?Cover? ?Standardcell? ?Physicalpin?}? ?-skip_via_on_wire_status {?routed? ?fixed? ?cover? ?shield?}? ?-top_layer <layername>? ?-uda? ?{-via_scale_height integer -via_scale_width <integer> | -via_rows <integer> -via_columns <integer> | -via_height real_number -via_width <real_number>}? ?-via_using_exact_crossover_size {0 | 1}?",
        ),
        # man1/editResize.1
        _syn(
            "editResize",
            "Resizes wires, bus guides, and pins",
            "editResize ?-help? ?-keep_center_line {0 1 auto}? ?-no_conn? ?-polygon_edge_start {<x y>} | -to <float_value>? {???-direction {x y diag45 diag135} -side {high low}? | ?-polygon_edge_start {x y} -polygon_edge_end {<x y>}?? ?-offset <float_value> | -to <float_value>?? | ?-corner {low_left low_right up_left up_right} -dx <float_value> -dy <float_value>?}",
        ),
        # man1/editRotate.1
        _syn(
            "editRotate",
            "Flips or rotates selected wires and vias",
            "editRotate ?-help? ?-mode {group | single}? ?-rotate_point {<x y>}? {-flip {MX MY} | -rotate {R90 R180 R270}}",
        ),
        # man1/editSelect.1
        _syn(
            "editSelect",
            "Selects wires and vias using the specified parameters",
            "editSelect ?-help? ?-area {<x1> <y1> <x2> <y2>}? ?-direction {H | V | 45 | 135}? ?-floating_via? ?-layer <list_of_layers>? ?-nets <net>*? ?-physical_pin_only? ?-regular_wire_with_drc? ?-shape {RING STRIPE FOLLOWPIN IOWIRE COREWIRE BLOCKWIRE PADRING BLOCKRING FILLWIRE FILLWIREOPC DRCFILL None}? ?-shield? ?-shield_only? ?-status {COVER FIXED NOSHIELD ROUTED SHIELD UNKNOWN}? ?-subclass <sublass_name>? ?-type {Regular Special Patch}? ?-use {CLOCK POWER SIGNAL}? ?-via_cell <cell_name_list>? ?-with_edit_flag {0 | 1}? ?-object_type {Wire Via}? ?-from_pin <pin_name> -to_pin <pin_name>?",
        ),
        # man1/editSplit.1
        _syn(
            "editSplit",
            "Splits selected special wires at connection points with orthogonal wires",
            "editSplit ?-help?",
        ),
        # man1/editTrim.1
        _syn(
            "editTrim",
            "Removes or trims wires",
            "editTrim ?-help? ?-keep_floating_stubs? ?-status {COVER FIXED NOSHIELD ROUTED SHIELD}? ?-type {float}? ?-all | -selected | -nets <net>* | -layers <layer_names> | -area {<x1 y1 x2 y2>}?",
        ),
        # man1/enable_legacy_metric.1
        _syn(
            "enable_legacy_metric",
            "",
            "enable_legacy_metric {true | false}",
        ),
        # man1/enc_partial_cmd_argument_matching.1
        _syn(
            "enc_partial_cmd_argument_matching",
            "",
            "enc_partial_cmd_argument_matching",
        ),
        # man1/enc_print_full_message_summary.1
        _syn(
            "enc_print_full_message_summary",
            "",
            "enc_print_full_message_summary",
        ),
        # man1/enc_save_binary_timing_constraints.1
        _syn(
            "enc_save_binary_timing_constraints",
            "",
            "enc_save_binary_timing_constraints {true | false}",
        ),
        # man1/enc_save_timing_constraints_always.1
        _syn(
            "enc_save_timing_constraints_always",
            "",
            "enc_save_timing_constraints_always {true | false}",
        ),
        # man1/enc_source_continue_on_error.1
        _syn(
            "enc_source_continue_on_error",
            "",
            "enc_source_continue_on_error <value>",
        ),
        # man1/enc_source_echo_filename.1
        _syn(
            "enc_source_echo_filename",
            "",
            "enc_source_echo_filename <value>",
        ),
        # man1/enc_source_verbose.1
        _syn(
            "enc_source_verbose",
            "",
            "enc_source_verbose <value>",
        ),
        # man1/enc_source_verbose_cmd_print_length_limit.1
        _syn(
            "enc_source_verbose_cmd_print_length_limit",
            "",
            "enc_source_verbose_cmd_print_length_limit <value>",
        ),
        # man1/enc_source_verbose_output.1
        _syn(
            "enc_source_verbose_output",
            "",
            "enc_source_verbose_output",
        ),
        # man1/enc_tcl_error_info.1
        _syn(
            "enc_tcl_error_info",
            "",
            "enc_tcl_error_info {true | false}",
        ),
        # man1/enc_tcl_report_header_with_value.1
        _syn(
            "enc_tcl_report_header_with_value",
            "",
            "enc_tcl_report_header_with_value {true | false}",
        ),
        # man1/enc_tcl_return_display_limit.1
        _syn(
            "enc_tcl_return_display_limit",
            "",
            "enc_tcl_return_display_limit <value>",
        ),
        # man1/encEnableMetric.1
        _syn(
            "encEnableMetric",
            "",
            "",
        ),
        # man1/encMessage.1
        _syn(
            "encMessage",
            "Specifies whether to enable the display of warning, information, or debug messages",
            "encMessage ?-help? <msgType> <valStr>",
        ),
        # man1/encrypt.1
        _syn(
            "encrypt",
            "Encrypts a file in an nc-protect compatible format",
            "encrypt ?-help? <input_file_name> ?-pragma? ?> <file>? ?-tcl | -verilog?",
        ),
        # man1/encrypt_thermal_file.1
        _syn(
            "encrypt_thermal_file",
            "Specifies to encrypt the file containing the thermal conductivity value for layers, and to protect foundry's thermal conductivity parameters used for power map generation",
            "encrypt_thermal_file -input <ASCII>.txt -output $<encrypted_conductivity>.txt",
        ),
        # man1/end_parallel_edit.1
        _syn(
            "end_parallel_edit",
            "Ends parallel editing",
            "end_parallel_edit ?-help? -out_file <parallel_edit_file_name>",
        ),
        # man1/end_sai.1
        _syn(
            "end_sai",
            "Disables the SoC Architecture Information (SAI) mode",
            "end_sai ?-help?",
        ),
        # man1/endECO.1
        _syn(
            "endECO",
            "Ends logging ECO operations",
            "endECO ?-help?",
        ),
        # man1/eval_common_ui.1
        _syn(
            "eval_common_ui",
            "Runs a Stylus Common UI command in the legacy interpreter",
            "eval_common_ui ?-help? <script>",
        ),
        # man1/exportNdr.1
        _syn(
            "exportNdr",
            "Exports/saves the new rule that was created with the add_ndr command into a LEF/DEF file",
            "exportNdr ?-help?",
        ),
        # man1/exportPowerSwitch.1
        _syn(
            "exportPowerSwitch",
            "Exports power switch database",
            "exportPowerSwitch ?-help? ?-powerDomain <powerDomainName>? ?-file <fileName>?",
        ),
        # man1/extract_metal_density.1
        _syn(
            "extract_metal_density",
            "Specifies to extract the metal density information",
            "extract_metal_density",
        ),
        # man1/extract_package.1
        _syn(
            "extract_package",
            "",
            "extract_package ?-help? <<domain>> ?-output <<directoryname>>? -pkg_bga_name <<bga_circuitname>> -pkg_die_name <<die_circuitname>> ?-reference_net <<netname>>? ?-spd_file <filename>? -workspace <<workspace_name>>",
        ),
        # man1/extract_shrink_factor.1
        _syn(
            "extract_shrink_factor",
            "",
            "extract_shrink_factor <shrink_factor_value>",
        ),
        # man1/extractRC.1
        _syn(
            "extractRC",
            "",
            "extractRC ?-help?",
        ),
        # man1/fcroute.1
        #   WARNING: unclosed bracket '[' at position 684
        _syn(
            "fcroute",
            "Specifies that power routing and signal routing recognize the bumps specified in a flip chip design",
            "fcroute ?-help? -type {power | signal} ?-area {<x1 y1 x2 y2>}? ?-connectInsideArea? ?-connectTsvToBump? | ?-connectTsvToPad? | ?-connectTsvToRingStripe? ?-constraintFile <filename>? ?-deleteExistingRoutes? ?-designStyle {aio | pio}? ?-doubleBendRoute? ?-eco | -incremental? ?-extraConfig <fileName>? ?-globalOnly? ?-jogControl {preferWithChanges | preferSameLayer | preferDifferentLayer}? ?-keepDRC? ?-layerChangeBotLayer <layerName>? ?-layerChangeTopLayer <layerName>? ?-minEscapeDistance <unit>? ?-msgRate <int>? ?-nets {<net_name_list>| <filename | ~<filename}<|>-selected_bump? ?-overflowMap? ?-route_pg_style {none finger mesh}? ?-routeWidth <real>? ?-spreadWiresFactor <value>? ?-straightConnections ??straightWithDrcClean? ?straightWithChanges?? ?-subclass <subclass_string>? ?-verbose?",
        ),
        # man1/fill_setting_save.1
        _syn(
            "fill_setting_save",
            "",
            "fill_setting_save {0 | 1}",
        ),
        # man1/fillNotch.1
        _syn(
            "fillNotch",
            "Detects and fills notches, gaps, and holes, and corrects acute angle (45 degree) violations",
            "fillNotch ?-help? ?-area {<x1 y1 x2 y2>}? ?-report <filename>? ?-useExistingDrcResult? ?-useNonDefaultSpacing?",
        ),
        # man1/filter_collection.1
        _syn(
            "filter_collection",
            "Returns a collection of objects that were filtered from the specified collection of objects based on user-specified criteria (<filter_expression>)",
            "filter_collection ?-help? <base_collection> {<filter_expression>} ?-nocase? ?-quiet? ?-regexp?",
        ),
        # man1/find_global.1
        _syn(
            "find_global",
            "Returns all the public variables",
            "find_global ?-help? ?<pattern> | -non_default? ??-tcl? | ??-name? ?-value? ?-type? ?-default? ?-info? ?-range_or_enum? ?-transient???",
        ),
        # man1/findLefEquivalentCells.1
        _syn(
            "findLefEquivalentCells",
            "Provides support to debug certain cells that may be non-equivalent without detailed analysis of the LEF",
            "findLefEquivalentCells ?-help? -cells <string> ?-outfile <filename>?",
        ),
        # man1/findPinPortNumber.1
        _syn(
            "findPinPortNumber",
            "Determines suitable ports available for a bump",
            "findPinPortNumber ?-help? ?-area <x1 y1 x2 y2>? ?-bumps <bump_list>? ?-geometry_height {<min> ?<max>?}? ?-geometry_width {<min> ?<max>?}? ?-layer <string>? ?-selected? ?-cellName <cell_name> | -instName <instance_name>? {-pinName <pin_name> | -netName <net_name> }",
        ),
        # man1/finishFloorplan.1
        _syn(
            "finishFloorplan",
            "Performs advanced placement-related refinements to a floorplan, to produce a more polished floorplan",
            "finishFloorplan ?-help? ?-mask <integer>? { ?-autoHalo | ?-autoHaloBasedOnPitch ?-margin <value>?? | -addHalo <width> | ?-fillPlaceBlockage <blkgType> <maxGap> ?-density <value>? ?-excludeFlops? ?-deadArea <float>? ?-honor_placement_density?? | ?-fillRouteBlockage <maxGap> ?-layer <layerID>? ?-cutLayer <cutLayerID>? ?-fills? ?-exceptpgnet? ?-spacing <spaceValue> | -designRuleWidth <width>? ?-deadArea <maxDeadArea>?? | -addCornerBlockage <string> | ?-drcRegionLayer <layer+> ?-edgeExtend {<x y>}? ?-edgeShrink {<x y>}??| -addCoreEOLBlockage | -addBoundaryBlockage | -addRowBasedRegionBlockage| -undo? ?-area {<x1 y1 x2 y2>}? ?-namePrefix <name>? }",
        ),
        # man1/fit.1
        _syn(
            "fit",
            "Fits the entire design in the viewable window",
            "fit ?-help?",
        ),
        # man1/fix_boundary_overlaps.1
        _syn(
            "fix_boundary_overlaps",
            "Resolves the overlaps between macros or hierarchical instances (hinsts)",
            "fix_boundary_overlaps ?-help? ?-move_area {<x1 y1 x2 y2>}? ?-groups {<string1 string2 ...>}? ?-hinsts {<string1 string2 ...>}? ?-fix_area {<x1 y1 x2 y2>}?",
        ),
        # man1/fix_drc_with_patch.1
        _syn(
            "fix_drc_with_patch",
            "Fixes violations by adding trim/patch in the whole design which includes fixed cell objects, pre‐ Routed nets, and special nets on a preRoute db",
            "fix_drc_with_patch ?-help? ?<area>? ?-layer_range <bottomLayer>:<topLayer>?",
        ),
        # man1/fix_feedthru_assign.1
        _syn(
            "fix_feedthru_assign",
            "Fixes the assign statements that are associated with partitions by replacing them with the specified buffer",
            "fix_feedthru_assign ?-help? -buffer <string>?-delete_feed?",
        ),
        # man1/fix_floorplan.1
        _syn(
            "fix_floorplan",
            "Fixes the detected violations as part of the UFC methodology by adding routing blockages around macro, snapping macro location, or re-shaping core shape",
            "fix_floorplan ?-help? -file <fileName> -type {ufc tcic} ?-selected? ?-report_file <string>? ?-report_unplaced_block? ?-break_at_conflict? ?-honor_snap_block_grid? ?-selected_rules <rule_name_list>?",
        ),
        # man1/fix_multi_drivers.1
        _syn(
            "fix_multi_drivers",
            "Fixes multi-drive issues by disconnecting driving ports that do not have a real driver",
            "fix_multi_drivers ?-help? ?-exclude_net <netName> | <netNameList>? ?-replace_bus_bit? ?-report_only?",
        ),
        # man1/fix_pg_antenna.1
        _syn(
            "fix_pg_antenna",
            "Fixes the antenna violations on PG nets of backside layers",
            "fix_pg_antenna ?-help? ?-selected?",
        ),
        # man1/fixACLimitViolation.1
        _syn(
            "fixACLimitViolation",
            "Repairs violations associated with AC current density, wire-self-heat, Joules heat, or electromigra‐ tion, mostly in a postRoute stage",
            "fixACLimitViolation ?-help? ?-excludeIO {true | false}? ?-excludeNetFile <filename>? ?-fixNetCategory {dataOnly | clockOnly | clockAndData}? ?-fixingMethod {route_rule | down_size | buffer | size_or_buffer | route_size_or_buffer}? ?-postCTS? ?-selectNetFile <filename>? ?-useReportFile <filename>? ?-useSegmentBasedNDR {true | false}?",
        ),
        # man1/fixAllIos.1
        _syn(
            "fixAllIos",
            "Changes the status of all I/O pins, I/O cells, or CLASS PAD AREAIO cells to a FIXED state to keep them from being reassigned",
            "fixAllIos ?-help? ?-pinOnly | -cellOnly | -incAreaIo?",
        ),
        # man1/fixBondPad.1
        _syn(
            "fixBondPad",
            "Assigns a fixed status to a specified bond pad",
            "fixBondPad ?-help? {{-ioInstName <InstName>?-pinName <pinName>?} | -selected}",
        ),
        # man1/fixVia.1
        _syn(
            "fixVia",
            "This command fixes the following types of violations in special net vias: short, mincut, minstep, and cutspacing",
            "fixVia ?-help? {-short | -minCut | -minStep | -cutSpacing} ?-area?",
        ),
        # man1/flattenCoverCell.1
        _syn(
            "flattenCoverCell",
            "Dissolves and flattens any instance whose master has class COVER, but no subclass BUMP",
            "flattenCoverCell ?-help? ?-inst {<instanceName> | <instanceNameList>}?",
        ),
        # man1/flattenIlm.1
        _syn(
            "flattenIlm",
            "Flattens the interface logic models (ILMs) at the top level so that the entire design can be analyzed at the top",
            "flattenIlm ?-help?",
        ),
        # man1/flattenPartition.1
        _syn(
            "flattenPartition",
            "Uncommits (flattens) the partition back to normal module status",
            "flattenPartition ?-help? ?<partition_name>? ?-bringBackRow? ?-keepPinGeometry? ?-noUninheritPhysical?",
        ),
        # man1/flipchip_allow_routed_bump_edit.1
        _syn(
            "flipchip_allow_routed_bump_edit",
            "",
            "flipchip_allow_routed_bump_edit {0 | 1}",
        ),
        # man1/flipModule.1
        _syn(
            "flipModule",
            "",
            "flipModule ?-help? <moduleName> {<X> | <Y>}",
        ),
        # man1/flipOrRotateObject.1
        _syn(
            "flipOrRotateObject",
            "Flips or rotates the selected objects",
            "flipOrRotateObject ?-help? ?-keepRelative? {-flip {MX | MY} | -rotate {R90 | R180 | R270}} ?-group? ?-name <object>?",
        ),
        # man1/flipSdpObject.1
        _syn(
            "flipSdpObject",
            "Flips an SDP group on X or Y axis along with its elements",
            "flipSdpObject ?-help? -object <object_name_list> ?-x | -y?",
        ),
        # man1/floorPlan.1
        _syn(
            "floorPlan",
            "Specifies the floorplan dimensions by size; or by die, I/O, or core coordinates",
            "floorPlan ?-help? ?-adjustToSite? ?-coreMarginsBy {io | die}? ?-dieSizeByIoHeight {min |max}? ?-flip {f | s | n}? ?-fplanOrigin {center | llcorner}? ?-noResize? ?-noSnapToGrid? ?-overlapSameSiteRow? {-b {<die_box io_box core_box>} | -s {<W H Left Bottom Right Top>} | -d {<W H Left Bottom Right Top>} | -r {<aspectRatio >?<rowDensity> ?<Left Bottom Right Top>??}| -su {<aspectRatio> ?<stdCellDensity> ?<Left Bottom Right Top>??}| -keepShape <util>} ?-site <name >| -siteOnly <name>?",
        ),
        # man1/foreach_in_collection.1
        _syn(
            "foreach_in_collection",
            "",
            "foreach_in_collection ?-help? <var_name><collection><body>",
        ),
        # man1/fp_vertical_row.1
        _syn(
            "fp_vertical_row",
            "",
            "fp_vertical_row {0 | 1}",
        ),
        # man1/free_memory_of_compressed_objects.1
        _syn(
            "free_memory_of_compressed_objects",
            "Releases all the excess memory used by dbGet",
            "free_memory_of_compressed_objects ?-help?",
        ),
        # man1/free_power_intent.1
        _syn(
            "free_power_intent",
            "The command deletes all the power intent data stored by the commit_power_intent command in current session and cleans up the design",
            "free_power_intent ?-help? ?-keep_fence?",
        ),
        # man1/generate_esd_rlrp_report.1
        _syn(
            "generate_esd_rlrp_report",
            "Reports the least-resistance path (RLRP) for the bump-to-clamp rule type in the ESD flow",
            "generate_esd_rlrp_report ?-help? -net <netname> ?-instance_pair_list {{inst1 inst2 ?pin1 pin2?}+} | -instance_pair_list_file <filename>? ?-number_threads <value>? -state_directory <directory>",
        ),
        # man1/generate_fence.1
        _syn(
            "generate_fence",
            "Automatically draws partition fences that enclose all their children FlexModel guides",
            "generate_fence ?-help? ?-flow {2G}? ?-for_partition? ?-rectangle_shape? ?-target_util <float>? ??-hInst {<hInst(s)>}? | ?-module {<module(s)>}? | ?-inst_group {<instGroup(s)>}??",
        ),
        # man1/generate_pg_library.1
        _syn(
            "generate_pg_library",
            "Generates the output for power-grid library generation",
            "generate_pg_library ?-help? ?-output <dir_name>? ?-library_prefix <prefix>?",
        ),
        # man1/generate_power_up_report.1
        _syn(
            "generate_power_up_report",
            "",
            "generate_power_up_report ?-help? ?-switch_net <net_name>? -output_directory <directory_name> -state_directory <directory_name>",
        ),
        # man1/generate_tech_pg_lib.1
        _syn(
            "generate_tech_pg_lib",
            "Generates the technology power-grid library on the fly",
            "generate_tech_pg_lib ?-help? ?-decap_cells <cell_list>? ?-default_power_voltage <value>? ?-esd_cells <cell_list>? ?-filler_cells <cell_list>? ?-keep {true | false}? ?-lef_layermap <filename>? ?-output_dir <dir_name>? ?-power_gate_file <filename>?",
        ),
        # man1/generate_vertical_cell_edge_constraint.1
        _syn(
            "generate_vertical_cell_edge_constraint",
            "Generates the bottom and top cell edge constraints for 10nm libraries to avoid vertical cell abutment that may cause pin access issue on M1 and M2",
            "generate_vertical_cell_edge_constraint ?-help? {-file <tclFile> | -updateDB } ??-check_m2_only? | ?-check_m2_to_m1_only??",
        ),
        # man1/generate_xpgv.1
        _syn(
            "generate_xpgv",
            "Creates power-grid view (xPGV) models for large digital blocks.The block xPGV can be generated either af‐ ter the signoff dynamic IR drop analysis or after the dynamic Early Rail Analysis (ERA) of the block",
            "generate_xpgv -cell <cell_name> ?-inst_list <inst1> inst2 .. <instn>? ?-libgen_include <file_name>? ?-output_dir <directory_name>? ?-rail_include <file_name>? ?-reuse_block_state_directory <directory_name>? -state_directory <directory_name> ?-mvmf_config <config_file>?",
        ),
        # man1/generateCapTbl.1
        _syn(
            "generateCapTbl",
            "Reads in the interconnect technology (ICT) process file and generates a Capacitance table file",
            "generateCapTbl ?-help? ?-cap <totalCapFactor>? ?-encrypt? -output <fileName> ?-res <resistanceFactor>? ?-xcap <crossCouplingFactor>? ?-lef <fileName> ?-shrinkFactor <value>?? {-ict <fileName> | -incaptable <fileName>}",
        ),
        # man1/generateFFSetupFile.1
        _syn(
            "generateFFSetupFile",
            "Starts the foundation flow on Innovus",
            "generateFFSetupFile ?-help?",
        ),
        # man1/generateLef.1
        _syn(
            "generateLef",
            "Uses input data to create an optimized LEF file with generated vias for the NanoRoute® router",
            "generateLef ?-help? <outputLefFileName> ?-clfFile <clfFileName>? ?-lefFile <lefFileName>? ?-lefFileList {<technology.lef> <cell1.lef> <cell2.lef> ...}? ?-noWE? ?-techFile <technologyFileName>?",
        ),
        # man1/generateRCFactor.1
        _syn(
            "generateRCFactor",
            "Generates the resistance and capacitance scale factors for optimal RC correlation by comparing the SPEF files generated by native extraction either with the user-specified reference RC data or with the automatic running of ex‐ traction in the higher accuracy mode",
            "generateRCFactor ?-help? ?-outputFile <file_name>? ?-preroute {true | false}? ?-postroute {low | medium}? ?-reference {low | medium | high | signoff | externalSpef}? ?-spefMapFile <file_name>? ?-useSameRouting {true | false}? ?-use_ostrich_filters <file_name>?",
        ),
        # man1/generateVias.1
        _syn(
            "generateVias",
            "Auto-generates vias required by nanoroute for the default and non-default rules (NDRs)",
            "generateVias",
        ),
        # man1/genPinText.1
        _syn(
            "genPinText",
            "Generates a file containing pin text information for nets and cells",
            "genPinText ?-format {assura dracula pvs}? ?-help? ?-layerMap <fileName>? ?-offset {<x> <y>}? {?-nets {<nets…>}? ?-cells {<cells>…}?} <pin_text_file>",
        ),
        # man1/get_abstract_mode.1
        _syn(
            "get_abstract_mode",
            "Retrieves the current settings of all or specific set_abstract_mode parameters",
            "get_abstract_mode ?-help? ?-abstract_blockage_cut_around_pin? ?-antenna_connectivity? ?-antenna_diffusion_geom? ?-antenna_gate_geom? ?-blockage_detailed_layers? ?-boundary_layers? ?-cell_symmetry? ?-export_lef_version? ?-extract_layers_power? ?-extract_layers_signal? ?-extract_pin_layers_power? ?-extract_pin_layers_signal? ?-input_cell_type? ?-input_gds_layer_map_file? ?-input_lef_tech_file? ?-keep_temp_files? ?-pins_analog_names? ?-pins_clock_names? ?-pins_ground_names? ?-pins_output_names? ?-pins_power_names? ?-pins_text_pin_map? ?-pre_skill? ?-selected_cells? ?-site_name? ?-verbose?",
        ),
        # man1/get_activity.1
        _syn(
            "get_activity",
            "",
            "get_activity ?-help? ?-instance <<string>>? ?-list_of_nets_based_on_driver <<string>>? ?-list_of_nets_based_on_source_of_activity_info <<string>>? ?-net <<string>>? ?-outfile <<string>>? ?-pin <<string>>? ?-port <<string>>? ?-report_average_switching_activity? ?-report_cell_group_activity_summary_report? ?-summary? ?-tcl_list?",
        ),
        # man1/get_add_target_pg_mode.1
        _syn(
            "get_add_target_pg_mode",
            "Returns the information for the specified parameter",
            "get_add_target_pg_mode ?-help? ?-allow_weak_connect? ?-max_extension_distance? ?-pins? ?-pins_group_distance? ?-respect_routes? ?-share_resource? ?-quiet? ?-nonDefault?",
        ),
        # man1/get_analysis_view.1
        _syn(
            "get_analysis_view",
            "Returns the constraint mode or delay calculation corner associated with the specified analysis view",
            "get_analysis_view <viewName> {-constraint_mode | -delay_corner}",
        ),
        # man1/get_arcs.1
        _syn(
            "get_arcs",
            "",
            "get_arcs ?-help? { ?-to <to_list>? ?-from <from_list>? | -of_objects <object_list>} ?-filter <expr>? ?-quiet?",
        ),
        # man1/get_capacitance_unit.1
        _syn(
            "get_capacitance_unit",
            "",
            "get_capacitance_unit",
        ),
        # man1/get_ccopt_clock_spines.1
        _syn(
            "get_ccopt_clock_spines",
            "This command returns a list of clock spines whose names match the specified pattern",
            "get_ccopt_clock_spines ?-help? ?<pattern>? ?-regexp?",
        ),
        # man1/get_ccopt_clock_tree_capacitance.1
        _syn(
            "get_ccopt_clock_tree_capacitance",
            "This command retrieves the capacitance on the specified pin",
            "get_ccopt_clock_tree_capacitance ?-help? <pin> | <port> ?-delay_corner <corner>? ?-delay_type {early | late}? ?-edge {rise | fall | both}? ?-load | -wire?",
        ),
        # man1/get_ccopt_clock_tree_cells.1
        _syn(
            "get_ccopt_clock_tree_cells",
            "This command returns a list of clock tree cells - cell instances that form a part of the clock tree network - whose names match the specified pattern",
            "get_ccopt_clock_tree_cells ?-help? ?<pattern>? ?-in_clock_trees <list_of_trees>? ?-net_types leaf | trunk | top? ?-node_types buffer | inverter | clock_gate | logic | source | generator | all? ?-not_in_clock_trees <list_of_trees>? ?-regexp?",
        ),
        # man1/get_ccopt_clock_tree_nets.1
        _syn(
            "get_ccopt_clock_tree_nets",
            "This command returns a list of clock tree nets whose names match the specified pattern",
            "get_ccopt_clock_tree_nets ?-help? ?<pattern>? ?-in_clock_trees <list_of_trees>? ?-net_types leaf | trunk | top? ?-not_in_clock_trees <list_of_trees>? ?-regexp?",
        ),
        # man1/get_ccopt_clock_tree_sinks.1
        _syn(
            "get_ccopt_clock_tree_sinks",
            "This command returns a list of clock tree sinks whose names match the specified pattern",
            "get_ccopt_clock_tree_sinks ?-help? ?<pattern>? ?-in_clock_trees <list_of_trees>? ?-not_in_clock_trees <list_of_trees>? ?-regexp?",
        ),
        # man1/get_ccopt_clock_tree_slew.1
        _syn(
            "get_ccopt_clock_tree_slew",
            "This command returns the slew information for the user-specified pin",
            "get_ccopt_clock_tree_slew ?-help?",
        ),
        # man1/get_ccopt_clock_tree_source_groups.1
        _syn(
            "get_ccopt_clock_tree_source_groups",
            "This command returns a list of clock tree source group objects matching the supplied pattern",
            "get_ccopt_clock_tree_source_groups ?-help? ?<pattern>? ?-regexp?",
        ),
        # man1/get_ccopt_clock_trees.1
        _syn(
            "get_ccopt_clock_trees",
            "This command returns the names of the clock trees whose names match the specified pattern",
            "get_ccopt_clock_trees ?-help? ?<pattern>? ?-regexp?",
        ),
        # man1/get_ccopt_dag_traversal.1
        _syn(
            "get_ccopt_dag_traversal",
            "This command traverses the clock tree network DAG, starting at the specified pins and traversing to their fanin or fanout, returning a list of the resulting pins",
            "get_ccopt_dag_traversal ?-help? ?-fanin? ?-fanout? ?-of_insts instances? ?-of_pins pins? ?-skew_group skew_group_name? ?-skip buffers inverters drivers clock_gates logics generators generated_roots all? ?-transitive?",
        ),
        # man1/get_ccopt_delay_corner.1
        _syn(
            "get_ccopt_delay_corner",
            "",
            "get_ccopt_delay_corner ?-help?",
        ),
        # man1/get_ccopt_effective_max_capacitance.1
        _syn(
            "get_ccopt_effective_max_capacitance",
            "Returns the value of the frequency-dependent effective maximum capacitance con‐ straint that the software will apply at a given pin in the clock tree",
            "get_ccopt_effective_max_capacitance ?-help? pin | port ?-delay_corner <corner>? ?-delay_type {early | late}? ?-source? ?-value?",
        ),
        # man1/get_ccopt_flexible_htrees.1
        _syn(
            "get_ccopt_flexible_htrees",
            "This command returns the names of the flexible H-trees whose names match the specified pattern",
            "get_ccopt_flexible_htrees ?-help? ?<pattern>? ?-regexp?",
        ),
        # man1/get_ccopt_preferred_cell_stripe.1
        _syn(
            "get_ccopt_preferred_cell_stripe",
            "Returns a list of preferred cell stripes objects matching the supplied pattern",
            "get_ccopt_preferred_cell_stripe ?-help? ?<pattern>? ?-regexp?",
        ),
        # man1/get_ccopt_property.1
        _syn(
            "get_ccopt_property",
            "Retrieves the value of the specified CCOpt property",
            "get_ccopt_property ?-help?",
        ),
        # man1/get_ccopt_skew_group_delay.1
        _syn(
            "get_ccopt_skew_group_delay",
            "By default, this command returns the longest source-to-sink delay for the specified skew group",
            "get_ccopt_skew_group_delay ?-help? ?-check_type {setup | hold}? ?-delay_corner delay_corner? ?-delay_type {early | late}? ?-edge {rise | fall}? ?-exclude_pin_insertion_delays? -skew_group <skew_group_name> ?-skew | -longest | -shortest? ?-path_length <distance_metric> | -summarize_stage_depth <cell_type_list>? ?-all_active_sinks | -to pin | -from pin | -through pin? ?-virtual_delays_only | -real_delays_only? ?-wire_delays_only | -cell_delays_only?",
        ),
        # man1/get_ccopt_skew_group_path.1
        _syn(
            "get_ccopt_skew_group_path",
            "This command returns the path delay information for the specified skew group",
            "get_ccopt_skew_group_path ?-help? ?-check_type {setup | hold}? ?-delay_corner delay_corner? ?-delay_type {early | late}? ?-show_generator_paths? -skew_group <skew_group_name> ?-longest | -shortest? ?-summarize_stage_depth <cell_type_list>? ?-virtual_delays_only | -real_delays_only? ?-wire_delays_only | -cell_delays_only? ?-sink <pin> | -below <pin>?",
        ),
        # man1/get_ccopt_skew_groups.1
        _syn(
            "get_ccopt_skew_groups",
            "This command returns a list of skew groups whose names match the specified pattern",
            "get_ccopt_skew_groups ?-help? ?<pattern>? ?-regexp?",
        ),
        # man1/get_cells.1
        _syn(
            "get_cells",
            "Creates a collection of instances in the current design whose name matches the supplied pattern list",
            "get_cells ?-help? ?-hierarchical? ?-hsc <char>? ?-filter <expr>? ?-leaf? ?-regexp? ?-nocase? ?-quiet? ?<<patterns>> | -of_objects <<object_list>>?",
        ),
        # man1/get_clock_network_objects.1
        _syn(
            "get_clock_network_objects",
            "Returns the cells or pins that exist in the clock network of the specified clocks",
            "get_clock_network_objects ?-help? ?-clocks <clock_list>? ?-type {cell | pin}?",
        ),
        # man1/get_clocks.1
        _syn(
            "get_clocks",
            "Returns a collection of clocks whose names match the supplied patterns, filtered by the filter expression",
            "get_clocks ?-help? ?-filter <expr>? ?-regexp? ?-nocase? ?-quiet? ?<patterns>?",
        ),
        # man1/get_constant_for_timing.1
        _syn(
            "get_constant_for_timing",
            "Queries the design database for the state of the specified pin or the state propagated through the combinational logic cone to that pin",
            "get_constant_for_timing ?-bidi_input | -bidi_output? <pin_name>",
        ),
        # man1/get_constraint_mode.1
        _syn(
            "get_constraint_mode",
            "Returns a Tcl list of the regular SDC constraint files, or the ILM SDC constraint files associated with the specified constraint mode",
            "get_constraint_mode <modeName> {-sdc_files | -ilm_sdc_files | -tcl_vars}",
        ),
        # man1/get_ctd_win_id.1
        _syn(
            "get_ctd_win_id",
            "Retrieves the IDs of the CTD windows",
            "get_ctd_win_id ?-help? ?-all? ?-detail?",
        ),
        # man1/get_ctd_win_title.1
        _syn(
            "get_ctd_win_title",
            "Retrieves the titles of the CTD windows",
            "get_ctd_win_title ?-help? ?-all | -id <WindowIDName>?",
        ),
        # man1/get_default_switching_activity.1
        _syn(
            "get_default_switching_activity",
            "",
            "get_default_switching_activity ?-help? ?-clip_activity_to_domain_freq? ?-clock_gates_enable? ?-clock_gates_output? ?-clock_gates_output_ratio? ?-comb_clockgate_ratio? ?-duty? ?-global_activity? ?-icg_ratio? ?-input_activity? ?-macro_activity? ?-period? ?-seq_activity?",
        ),
        # man1/get_delay_corner.1
        _syn(
            "get_delay_corner",
            "Returns attribute information for the specified delay calculation corner object, or for one of its power domains",
            "get_delay_corner ?-help? <delayCornerName>?-early_irdrop_data? ?-early_irdrop_file? ?-early_library_set? ?-early_opcond? ?-early_opcond_library? ?-early_rc_corner? ?-early_temp_file? ?-irdrop_data? ?-irdrop_file? ?-late_irdrop_data? ?-late_irdrop_file? ?-late_library_set? ?-late_opcond? ?-late_opcond_library? ?-late_rc_corner? ?-late_temp_file? ?-library_set? ?-opcond? ?-opcond_library? ?-power_domain <powerDomainName>? ?-power_domain_list? ?-rc_corner? ?-si_enabled? ?-supply_set <supplySetName>? ?-supply_set_list? ?-temp_file?",
        ),
        # man1/get_designs.1
        _syn(
            "get_designs",
            "Creates a collection of modules and assigns this collection to a variable or pass it as an argument to an another command",
            "get_designs ?-help? ?-quiet? <patterns>",
        ),
        # man1/get_dynamic_power_simulation.1
        _syn(
            "get_dynamic_power_simulation",
            "",
            "get_dynamic_power_simulation ?-help? ?-activity_pattern? ?-period? ?-resolution?",
        ),
        # man1/get_equivalent_cells.1
        _syn(
            "get_equivalent_cells",
            "Returns equivalent cells from minimum/maximum libraries or from libraries of specific power domains",
            "get_equivalent_cells ?-help? -cell <string >??{ { -delay_corner <string> ?-early_only | -late_only? } | -max |-min } ?-power_domain <string >?? | -library <string >?",
        ),
        # man1/get_generated_clocks.1
        _syn(
            "get_generated_clocks",
            "",
            "get_generated_clocks ?-help? ?-filter <expr>? ?-regexp | -exact? ?-nocase? ?<patterns>?",
        ),
        # man1/get_glitch_threshold.1
        _syn(
            "get_glitch_threshold",
            "Displays information for the specified set_glitch_threshold parameters for the current Tempus ses‐ sion",
            "get_glitch_threshold ?<parameter_names>?",
        ),
        # man1/get_global.1
        _syn(
            "get_global",
            "",
            "get_global <global_variable_name>",
        ),
        # man1/get_interactive_constraint_modes.1
        _syn(
            "get_interactive_constraint_modes",
            "",
            "get_interactive_constraint_modes ?-help?",
        ),
        # man1/get_ir_insight.1
        _syn(
            "get_ir_insight",
            "",
            "get_ir_insight ?-help? -domain <domainname> -domain_threshold <value> ?-eco_list <list_of_instances>? ?-eco_mode {violation | aggressor | both}? ?-ir_drop_histogram_bin_size <absolute_value_in_volts>? ?-ir_drop_histogram_lower_limit <absolute_value_in_volts>? ?-ir_drop_histogram_upper_limit <absolute_value_in_volts>? ?-mode summary_only | report_by_region | predict_ir | report_aggressor | eco_report? ?-nregion <value>? ?-nworst_aggressors <value>? ?-nworst_instances <value>? -output_directory <directoryname> ?-pdn_model <directoryname>? ?-reset_predict? -state_directory <directoryname> ?-watch_box <filename>? ?-watch_inst <filename>?",
        ),
        # man1/get_lib_arcs.1
        _syn(
            "get_lib_arcs",
            "Creates a collection of library timing arcs",
            "get_lib_arcs ?-help? { ?-to <to_lib_pins>? ?-from <from_lib_pins>? | -of_objects {<lib_cell_list> | <timing_arcs>} } ?-filter <expr>? ?-quiet?",
        ),
        # man1/get_lib_cell_leakage_power.1
        _syn(
            "get_lib_cell_leakage_power",
            "",
            "get_lib_cell_leakage_power ?-help? -cell <string> ?-file <string>? ?-stateleakagegrp? ?{-view <string> | -delay_corner <string>} ?-power_domain <string>?? ?-early | -late?",
        ),
        # man1/get_lib_cells.1
        _syn(
            "get_lib_cells",
            "Creates a collection of library cells from the loaded libraries whose name matches the supplied pattern list",
            "get_lib_cells ?-help? ?-filter <expr>? ?-regexp? ?-nocase? ?-quiet? {<pattern_list> | -of_objects <object_list>}",
        ),
        # man1/get_lib_clock_tree_path_delay.1
        _syn(
            "get_lib_clock_tree_path_delay",
            "This command retrieves information about the Liberty max_clock_tree_path and min_clock_tree_path delay attributes for a library pin",
            "get_lib_clock_tree_path_delay ?-help? -base_pin <base_pin_name> ?-delay_type {max | min}? ?-edge {rise | fall}? ?-mode <analysis_mode_name>? ?-power_domain <power_domain_name>? -transition <transition_time> -view <analysis>_<view_name>",
        ),
        # man1/get_lib_pg_pins.1
        _syn(
            "get_lib_pg_pins",
            "Returns a collection of library-level PG pins from the loaded libraries",
            "get_lib_pg_pins ?-help? ?-filter <expr>? {-of_objects <object_list>}",
        ),
        # man1/get_lib_pins.1
        _syn(
            "get_lib_pins",
            "",
            "get_lib_pins ?-help? ?-filter expr? ?-regexp? ?-nocase? ?-quiet? {<pattern_list> | -of_objects <object_list>}",
        ),
        # man1/get_library_set.1
        _syn(
            "get_library_set",
            "Returns a Tcl list of the timing or cdB libraries for the specified library set",
            "get_library_set <libSetName>{-timing | -si | -aocv | -socv}",
        ),
        # man1/get_libs.1
        _syn(
            "get_libs",
            "",
            "get_libs ?-help? ?-filter <expr>? ?-quiet? ?-regexp? ?-nocase? {-of_objects <object_list> | <pattern_list>}",
        ),
        # man1/get_macro_place_constraint.1
        _syn(
            "get_macro_place_constraint",
            "Gets the current value of the macro constraints that are honored by the macro placer",
            "get_macro_place_constraint ?-help? ?-cell <string>? ?-macro_corner_keepout? ?-power_domain_as_core? ??-array <array_name>? | ?-inst <string> -orientation? | ?-cell_obs? | ?-track_adjustment? | ?-max_io_pin_group_keep_out? | ?-forbidden_space_to_core? | ?-forbidden_space_to_macro? | ?-min_space_to_core? | ?-min_space_to_macro? | ?-parallel_run_length? | ?-horizontal_stacking? | ?-vertical_stacking? | ?-honor_strict_spacing_constraint? | ?-avoid_abut_macro_edge_with_pins? | ?-same_length_site? | ?-pg_resource_model? | ?-non_default? | ?-halo_sharing?| ?-parallel_run_length_for_stacking??",
        ),
        # man1/get_message.1
        _syn(
            "get_message",
            "Gets the limit, severity, or suppression for a message",
            "get_message",
        ),
        # man1/get_metal_fill_signoff_mode.1
        _syn(
            "get_metal_fill_signoff_mode",
            "Returns information about the signoff metal fill flow global variables set by the set_metal_fill_signoff_mode command",
            "get_metal_fill_signoff_mode ?-help? ?-and_area_size? ?-area? ?-attach_instance_name? ?-attach_net_name? ?-attach_net_prop? ?-auto_load_fills? ?-bg? ?-clock? ?-common_blockage? ?-control? ?-delete_area? ?-delete_point? ?-die_area_as_boundary? ?-dp? ?-dp_timeout? ?-excl_area_size? ?-fill_cell? ?-fill_layer? ?-fill_output_mode? ?-layer_map_file? ?-license_timeout? ?-license_dp_continue? ?-lib_name? ?-lsf? ?-master_lsf? ?-merge? ?-min_density? ?-net? ?-no_structure_name? ?-no_via_fills? ?-offset? ?-output_macros? ?-quiet? ?-report_file? ?-reset? ?-rule_file? ?-slack_threshold? ?-spacing? ?-spacing_above? ?-spacing_below? ?-stripes? ?-structure_name? ?-tech_lib? ?-tech_set? ?-technology? ?-temp_working_dir? ?-trim_effort? ?-trim_layer? ?-trim_mf? ?-union_density? ?-uniquify_cell_names? ?-units? ?-window_size? ?-window_step?",
        ),
        # man1/get_metric.1
        _syn(
            "get_metric",
            "Gets the current state of metric(s)",
            "get_metric",
        ),
        # man1/get_multi_input_switching_mode.1
        _syn(
            "get_multi_input_switching_mode",
            "Reports the MIS (multi-input switching) analysis settings configured using the set_multi_input_switching_mode command",
            "get_multi_input_switching_mode ?-help? {?-disable_lib_cells? ?-switching_alignment_factor? ?-mis_alignment_mode?}",
        ),
        # man1/get_nets.1
        _syn(
            "get_nets",
            "Creates a collection of nets in the current design whose name matches the supplied pattern list",
            "get_nets ?-help? ?-hierarchical? ?-hsc <char>? ?-filter <expr>? ?-regexp? ?-nocase? ?-quiet? ?<patterns> | -of_objects <object_list>?",
        ),
        # man1/get_oa_default_rule_lib.1
        _syn(
            "get_oa_default_rule_lib",
            "Searches through a specified library (or libraries) to check whether a specified LDRS exists or not",
            "get_oa_default_rule_lib ?-help? ?-rule <rule_name>? ?-libs <lib_list>? ?-verbose?",
        ),
        # man1/get_object_name.1
        _syn(
            "get_object_name",
            "Returns the name of the object(s) contained in the specified collections",
            "get_object_name ?-help? <collection>",
        ),
        # man1/get_op_cond.1
        _syn(
            "get_op_cond",
            "",
            "get_op_cond <virtualOpcondName> {-library_file | -P | -V | -T}",
        ),
        # man1/get_path_groups.1
        _syn(
            "get_path_groups",
            "",
            "get_path_groups ?-help? ?-regexp? ?-nocase? <patterns>",
        ),
        # man1/get_pba_mode.1
        _syn(
            "get_pba_mode",
            "Displays information for the IPBA mode set using the set_pba_mode command",
            "get_pba_mode ?-help? ?-quiet? ?-nonDefault?",
        ),
        # man1/get_pg_fill_config.1
        _syn(
            "get_pg_fill_config",
            "Prints the parameters of the add_pg_fill command",
            "get_pg_fill_config ?-help? ?-attach_instance_name? ?-attach_net_name? ?-attach_net_prop? ?-core_license? ?-die_area_as_boundary? ?-dp? ?-dp_dir? ?-dp_timeout? ?-extra_options? ?-format? ?-layer_map_file? ?-license_dp_continue? ?-license_timeout? ?-merge? ?-no_structure_name? ?-offset? ?-output_macros? ?-pg_fill_config_file? ?-pg_hookup_flow? ?-report_file? ?-stripes? ?-structure_name? ?-uniquify_cell_names? ?-units? ?-working_dir?",
        ),
        # man1/get_pg_nets.1
        _syn(
            "get_pg_nets",
            "Creates a collection of netlist-level instance PG nets of leaf cells/pins in the current design",
            "get_pg_nets ?-help? ?-filter <expr>? ?-of_objects <object_list>?",
        ),
        # man1/get_pg_pins.1
        _syn(
            "get_pg_pins",
            "Returns a collection of netlist-level instance PG pins in the current design",
            "get_pg_pins ?-help? ?-filter <expr>? ?-of_objects <object_list>?",
        ),
        # man1/get_physical_info.1
        _syn(
            "get_physical_info",
            "Gets the physical connection or routing path between IO pads and bumps",
            "get_physical_info ?-help? {-object <string> | -selected } ?-highlight? ?-shapes {RING STRIPE FOLLOWPIN IOWIRE COREWIRE BLOCKWIRE PADRING BLOCKRING FILLWIRE FILLWIREOPC DRCFILL None}? ?-subclass {<subclass_name_list>}? ?-type {connection | routing_path}?",
        ),
        # man1/get_pins.1
        _syn(
            "get_pins",
            "Creates a collection of instance pins whose name matches the supplied pattern list",
            "get_pins ?-help? ?-hierarchical? ?-hsc <char>? ?-filter <expr>? ?-leaf? ?-regexp? ?-nocase? ?-quiet? {<patterns> | -of_objects <object_list>}",
        ),
        # man1/get_ports.1
        _syn(
            "get_ports",
            "Creates a collection of ports whose name matches the supplied pattern list",
            "get_ports ?-help? ?-filter <expr>? ?-regexp? ?-nocase? ?-quiet? ?<patterns> | -of_objects <object_list>?",
        ),
        # man1/get_power.1
        _syn(
            "get_power",
            "Queries various power related properties of design objects like nets, pins, and instances",
            "get_power ?-help? ?-outfile <filename>? ?-nets <nets_list>| -pins <pins_list>| -instances <instances_list>? ?-attribute <attributes_list>? ?-include_unit? ?-tcl_list? ?-pg_net {<pg_net_name_list> | all}?",
        ),
        # man1/get_power_analysis_mode.1
        _syn(
            "get_power_analysis_mode",
            "Use the get_power_analysis_mode command to display the current settings for the set_power_analy‐ sis_mode command",
            "get_power_analysis_mode ?-help? ?-quiet?",
        ),
        # man1/get_power_intent_restricted_hinsts.1
        _syn(
            "get_power_intent_restricted_hinsts",
            "Reports the Hinsts, which cannot be ungrouped or split through the create_physi‐ cal_partitions command",
            "get_power_intent_restricted_hinsts ?-help? ?-out_file <fileName>?",
        ),
        # man1/get_propagated_clock.1
        _syn(
            "get_propagated_clock",
            "",
            "get_propagated_clock ?-clock <clock_list>? ?-pin <pin_list>? ?> <filename>?",
        ),
        # man1/get_property.1
        _syn(
            "get_property",
            "Retrieves the attribute value for the specified object(s) property",
            "get_property ?-help? <var_name> <property> ?-clock <clock_name>? ?-view <view_name>? ?-quiet?",
        ),
        # man1/get_proto_design_mode.1
        _syn(
            "get_proto_design_mode",
            "Returns information about a specified set_proto_design_mode parameter in the Innovus log file and the console",
            "get_proto_design_mode ?-help? ?-effort? ?-cover_fixed_macros? ?-flexmodel_constraint_type? ?-keep_guide? ?-place_macro? ?-remove_overlap? ?-quiet? ?-nonDefault?",
        ),
        # man1/get_proto_mode.1
        _syn(
            "get_proto_mode",
            "Returns information about a specified set_proto_mode parameter in the Innovus log file and the console",
            "get_proto_mode ?-help? ?-allow_model_with_io? ?-allow_powerdomain_in_flexmodel? ?-create_dir? ?-create_high_fanout_psPM? ?-create_lib? ?-create_metal_fill_NDR? ?-create_metal_fill_nominal? ?-create_multi_corner_psPM? ?-create_NDR_psPM_model? ?-create_no_flex_filler? ?-create_partition_as_flexmodel? ?-create_pipeline_flop? ?-create_powerdomain_psPM? ?-create_timing_budget? ?-identify_algorithm? ?-identify_estimated_flexmodel_number? ?-identify_exclude_module? ?-identify_exclude_module_and_parent? ?-identify_exclude_module_tree? ?-identify_honor_objects_hierarchy? ?-identify_max_inst? ?-identify_min_inst? ?-keep_inst_file_only? ?-keep_instance_defined_in_sdc? ?-keep_slack_improve_NDR? ?-max_report_NDR_net? ?-route_net_NDR? ?-timing_net_delay_model? ?-timing_ps_per_micron? ?-verbose? ?-quiet? ?-nonDefault?",
        ),
        # man1/get_proto_model.1
        _syn(
            "get_proto_model",
            "Retrieves all the information that you specify on a model in a design",
            "get_proto_model ?-help? ?-committed? ?-create_optimize_effort? ?-exclude <string>? ?-file? ?-flip_table? ?-include_default? ?-tcl? {-all | -model <<string>> | {?-type_match {flex_module flex_instgroup}? ?-source_match {user auto}? }} ?-name | -type | -create_total_area | -create_gate_area | -create_gate_count | -create_area_per_gate | -create_ex‐ tra_macro | -planDesign_target_util | -flexfiller_route_blockage?",
        ),
        # man1/get_ptn_fplan_mode.1
        _syn(
            "get_ptn_fplan_mode",
            "Retrieves information about the option values set using the set_ptn_fplan_mode command",
            "get_ptn_fplan_mode ?-help? ?-export? ?-import? ?-quiet? ?-nonDefault?",
        ),
        # man1/get_rc_corner.1
        _syn(
            "get_rc_corner",
            "Returns attribute information for the specified RC corner object",
            "get_rc_corner <rcCornerName> -<rcCornerAttribute>",
        ),
        # man1/get_reinforce_pg_mode.1
        _syn(
            "get_reinforce_pg_mode",
            "Returns the information for the specified parameter",
            "get_reinforce_pg_mode ?-help? ?-auto_ir_fix_effort? ?-critical_path_slack? ?-irdrop_hierarchical_block? ?-irdrop_hierarchical_top_rail_analysis_directory? ?-nonDefault? ?-respect_defined_nets? ?-respect_routes? ?-respect_stdcell_geometry? ?-timing_aware_effort? ?-quiet?",
        ),
        # man1/get_resistance_unit.1
        _syn(
            "get_resistance_unit",
            "",
            "get_resistance_unit",
        ),
        # man1/get_sdc_mode.1
        _syn(
            "get_sdc_mode",
            "",
            "get_sdc_mode ?-help?",
        ),
        # man1/get_signal_em_analysis_mode.1
        _syn(
            "get_signal_em_analysis_mode",
            "",
            "get_signal_em_analysis_mode ?-help? ?-Ipeak_Td_method? ?-avgRecovery? ?-default_freq_for_unconstrained_nets? ?-delta_T? ?-effort_level? ?-em_temperature? ?-em_res_width? ?-error? ?-forceHoldView? ?-lifetime? ?-method? ?-minPeakDutyRatio? ?-minPeakFreq? ?-net_file? ?-toggle? ?-useQrcTech? ?-use_db_freq? ?-view? ?-net | -selected? ?-report ?-detailed?? ?-report_db? ?-set_current_file? ?-skip_net? ?-skip_net_file? ?-ict_em_models? ?-current_scale_factor? ?-em_limit_scale_factor? ?-em_threshold? ?-current_scale_table? ?-em_limit_scale_table? ?-top_scope_ignore_block_internal_nets_on_boundary_path? ?-extraction_tech_file? ?-handle_pin_obs_via?",
        ),
        # man1/get_signoff_verify_design_config.1
        #   WARNING: unclosed bracket '[' at position 206
        _syn(
            "get_signoff_verify_design_config",
            "Prints parameters for the signoff_verify_design command",
            "get_signoff_verify_design_config ?-help? ?-abort_on_layout_error? ?-abort_on_missing_rulecheck? ?-area? ?-attach_instance_name? ?-attach_net_name? ?-attach_net_prop? ?-auto_merge_base_class? ?-config_file? ?-control_file ?-core_license? ?-die_area_as_boundary? ?-dp? ?-dp_timeout? ?-error_limit? ?-extra_options? ?-format? ?-ignore_blockage? ?-ignore_fill? ?-keep_data? ?-layer_map_file? ?-layer_range? ?-layers? ?-layout_path? ?-lib_name? ?-license_dp_continue? ?-license_stacking? ?-license_timeout? ?-merge? ?-merge_path? ?-mode? ?-mp? ?-mt? ?-net_map_file? ?-nets? ?-no_structure_name? ?-offset? ?-output_macros? ?-pegasus_bin? ?-process_node? ?-pvs_fill? ?-report_file? ?-rule_file_drc? ?-rule_file_smart_verify_lvs? ?-rule_selection_options? ?-run_name? ?-selected_inst? ?-skip_auto_load_results? ?-stripes? ?-structure_name? ?-transform_to_inst_master? ?-ui_data? ?-uniquify_cell_names? ?-units? ?-working_dir?",
        ),
        # man1/get_snap_grid_info.1
        _syn(
            "get_snap_grid_info",
            "Gets information on the current snap grid settings",
            "get_snap_grid_info ?-help? ?-origin? ?-pitch_x? ?-pitch_y? -type {manufacturing | inst | placement | userdefine | layertrack | finfetInst |finfetmanufacturing | finfetplacement}",
        ),
        # man1/get_socv_rc_variation_factor.1
        _syn(
            "get_socv_rc_variation_factor",
            "Displays the variation factor for interconnect delays",
            "get_socv_rc_variation_factor ?-help? -view <viewName> {-early | -late }",
        ),
        # man1/get_socv_reporting_nsigma_multiplier.1
        _syn(
            "get_socv_reporting_nsigma_multiplier",
            "Allows you to query sigma multiplier setting for the specified view in setup or hold mode",
            "get_socv_reporting_nsigma_multiplier ?-help? -view <viewName> {?-setup | -hold?}",
        ),
        # man1/get_time_unit.1
        _syn(
            "get_time_unit",
            "",
            "get_time_unit",
        ),
        # man1/get_trace_obj_connectivity_mode.1
        _syn(
            "get_trace_obj_connectivity_mode",
            "Returns information about the specified set_trace_obj_connectivity_mode parameter in the Innovus log file and the console",
            "get_trace_obj_connectivity_mode ?-help? ?-macro_pins? ?-max_fanin_fanout? ?-register_inputs? ?-register_outputs? ?-quiet?",
        ),
        # man1/get_track_fill_config.1
        _syn(
            "get_track_fill_config",
            "Prints the parameters of the add_track_fill command",
            "get_track_fill_config ?-help? ?-attach_instance_name? ?-attach_net_name? ?-attach_net_prop? ?-core_license? ?-die_area_as_boundary? ?-dp? ?-dp_dir? ?-dp_timeout? ?-extra_options? ?-format? ?-layer_map_file? ?-license_dp_continue? ?-license_timeout? ?-merge? ?-no_structure_name? ?-offset? ?-output_macros? ?-report_file? ?-stripes? ?-structure_name? ?-track_fill_config_file <file_name>? ?-uniquify_cell_names? ?-units? ?-working_dir?",
        ),
        # man1/get_verify_drc_mode.1
        _syn(
            "get_verify_drc_mode",
            "Displays the following information about a set_verify_drc_mode parameter in the Innovus console",
            "get_verify_drc_mode ?-help? ?-area? ?-check_illegal_trim_shapes? ?-check_ndr_spacing? ?-check_only? ?-check_reverse? ?-check_routing_halo? ?-check_routing_halo_corner? ?-check_same_via_cell? ?-check_short_only? ?-check_trim_length? ?-check_uncolored? ?-disable_rules? ?-enable_post_passive_fill_check? ?-exclude_pg_net? ?-ignore_cell_blockage? ?-ignore_fill_wire? ?-ignore_non_rectangle_shapes? ?-ignore_trial_route? ?-layer_range? ?-limit? ?-max_wrong_way_halo? ?-nonDefault? ?-report? ?-use_min_spacing_on_block_obs? ?-quiet?",
        ),
        # man1/get_via_pillars.1
        _syn(
            "get_via_pillars",
            "",
            "get_via_pillars ?-help? {?-term <term >?-required?? | -instterm <instterm>}",
        ),
        # man1/get_visible_bumps.1
        _syn(
            "get_visible_bumps",
            "Returns all visible bump cells in the design if some bumps have been hidden in the design",
            "get_visible_bumps ?-help?",
        ),
        # man1/get_visible_netGroups.1
        _syn(
            "get_visible_netGroups",
            "Returns the names of the visible netGroups if some netGroups have been hidden in the design",
            "get_visible_netGroups ?-help?",
        ),
        # man1/get_visible_nets.1
        _syn(
            "get_visible_nets",
            "Returns the names of the visible nets if some nets have been hidden in the design",
            "get_visible_nets ?-help?",
        ),
        # man1/get_well_tap_mode.1
        _syn(
            "get_well_tap_mode",
            "",
            "get_well_tap_mode ?-help? ?-abut_boundary_tap_distance? ?-antenna_tap_break_cell? ?-antenna_tap_cell? ?-antenna_tap_left_cell? ?-antenna_tap_pitch? ?-antenna_tap_right_cell? ?-antenna_tap_right_top_edge_cell? ?-avoidAbutment? ?-block_boundary_only? ?-bottom_tap_cell? ?-bottom_termination_cell? ?-cell? ?-channel_offset? ?-check_channel? ?-column_cell? ?-inRowOffset? ?-insert_cells? ?-rule? ?-siteOffset? ?-tap_function_cells? ?-tap_termination_alignment? ?-termination_align? ?-termination_cell? ?-top_tap_cell? ?-top_termination_cell? ?-vertical_boundary_spacing? ?-well_cut_cell? ?-quiet? ?-nonDefault?",
        ),
        # man1/getActiveLogicViewMode.1
        _syn(
            "getActiveLogicViewMode",
            "Controls certain behaviors of active logic view commands",
            "getActiveLogicViewMode ?-help? ?-keepAsync {false | true}? ?-keepHighFanoutPorts {true| false}? ?-keepInstInSdc {true|false}? ?-keepLoopBack {false | true}? ?-quiet? ?-nonDefault?",
        ),
        # man1/getAddRingMode.1
        _syn(
            "getAddRingMode",
            "Returns information for the specified parameter",
            "getAddRingMode ?-help? ?-avoid_short? ?-break_core_ring_io_list? ?-continue_on_no_selection? ?-detailed_log? ?-extend_blockring_search_distance? ?-extend_corering_search_distance? ?-extend_merge_with_prewires? ?-extend_over_row? ?-extend_search_nets? ?-extend_stripe_search_distance? ?-gap_width_without_io? ?-ignore_rows? ?-max_via_size? ?-nonDefault? ?-orthogonal_only? ?-ring_target? ?-skip_crossing_trunks? ?-skip_via_on_pin? ?-skip_via_on_wire_shape? ?-spacing_from_block? ?-split_long_via? ?-stacked_via_bottom_layer? ?-stacked_via_top_layer? ?-via_using_exact_crossover_size? ?-wire_center_offset? ?-quiet?",
        ),
        # man1/getAddStripeMode.1
        _syn(
            "getAddStripeMode",
            "Returns the current settings of the setAddStripeMode command",
            "getAddStripeMode ?-help? ?-allow_jog? ?-allow_nonpreferred_dir? ?-area? ?-break_at? ?-color_balance? ?-continue_on_no_selection? ?-detailed_log? ?-domain_offset_from_core? ?-extend_to_closest_target? ?-extend_to_first_ring? ?-ignore_block_check? ?-ignore_blockring_when_breaking? ?-ignore_DRC? ?-ignore_nondefault_domains? ?-inside_cell_allow_shift? ?-inside_cell_only? ?-keep_pitch_after_snap? ?-max_extension_distance? ?-max_via_size? ?-merge_with_all_layers? ?-mesh_via? ?-offset_from_core? ?-optimize_stripe_for_routing_track? ?-orthogonal_offset? ?-orthogonal_only? ?-over_row_extension? ?-partial_set_thru_domain? ?-recommend_width? ?-remove_floating_stapling? ?-remove_floating_stripe_over_block? ?-remove_stripe_under_ring? ?-respect_routes? ?-route_over_rows_only? ?-rows_without_stripes_only? ?-same_sized_stack_vias? ?-skip_via_on_pin? ?-skip_via_on_wire_shape? ?-spacing_from_block? ?-spacing_type? ?-split_long_via? ?-split_vias? ?-split_wire_spacing? ?-split_wire_weight? ?-split_wire_width? ?-stacked_via_bottom_layer? ?-stacked_via_top_layer? ?-stapling_extend_to_minimum_spacing? ?-stapling_nets_style? ?-stapling_shift? ?-stop_at_closest_target? ?-stop_at_last_wire_for_area? ?-stripe_min_length? ?-stripe_min_width? ?-switch_cellname? ?-switch_layer_overlap_length? ?-trim_antenna_back_to_shape? ?-trim_antenna_max_distance? ?-trim_stripe? ?-use_exact_spacing? ?-use_point2point_router? ?-use_stripe_width? ?-via_using_exact_crossover_size? ?-quiet? ?-nonDefault?",
        ),
        # man1/getAllLayers.1
        _syn(
            "getAllLayers",
            "Returns a complete list of all layers and floorplan object settings",
            "getAllLayers ?-help? ?{object display multi internal module metal color custom oaLayout}?",
        ),
        # man1/getAnalysisMode.1
        _syn(
            "getAnalysisMode",
            "",
            "getAnalysisMode ?-analysisType? ?-aocv? ?-asyncChecks? ?-caseAnalysis? ?-checkType? ?-clkNetsMarking? ?-clkSrcPath? ?-clockGatingCheck? ?-clockPropagation? ?-cppr? ?-enableMultipleDriveNet? ?-honorActiveLogicView? ?-honorClockDomains? ?-log? ?-multi_input_switching_mode? ?-propSlew? ?-nonDefault? ?-quiet? ?-sequentialConstProp? ?-skew? ?-socv? ?-timeBorrowing? ?-timingEngine? ?-timingSelfLoopsNoSkew? ?-usefulSkew? ?-useOutputPinCap? ?-warn?",
        ),
        # man1/getAttribute.1
        _syn(
            "getAttribute",
            "Displays the current net attribute settings in the Innovus console and in the Innovus log file",
            "getAttribute ?-help? -net <netName>?-quiet?",
        ),
        # man1/getBlackBoxArea.1
        _syn(
            "getBlackBoxArea",
            "Retrieves the standard cell area, macro area, and cell utilization value for the specified blackbox",
            "getBlackBoxArea ?-help? -cell <cellName> ?-stdCellArea? ?-macroArea? ?-cellUtil?",
        ),
        # man1/getBondPad.1
        _syn(
            "getBondPad",
            "Gets the current stagger position of a bond pad on a specified I/O instance",
            "getBondPad ?-help? -ioInstName <InstName> ?-pinName <pinName>?",
        ),
        # man1/getBudgetingMode.1
        _syn(
            "getBudgetingMode",
            "Displays the following information about a specified budgeting mode parameter in the Innovus log file and in the Innovus console",
            "getBudgetingMode ?-help? ?-abutted? ?-accumulated? ?-boundaryConditionTemplatePath? ?-bufferDelayLibCell? ?-bufferDelaySelectionEffort? ?-ccd? ?-constantModel? ?-distributeMMMC? ?-dontWriteWireLoad? ?-driveConstraint? ?-fixTopLevelPaths? ?-handleComplexSDC? ?-honorPortBoundaryCondition? ?-honorPortDelays? ?-honorReportTimingFormat? ?-ignoreDontTouch? ?-includeLatency? ?-includeWireLoadsInLib? ?-inputLoad? ?-justify? ?-justifyBudgetDir? ?-keepPinListsForBlockPorts? ?-latencyOnClocks? ?-localLatency? ?-localUncertainty? ?-makeNegativeInputDelayZero? ?-masterClone? ?-noFalsePathsForUnCstrPorts? ?-noSetupView? ?-noHoldView? ?-overrideNetCap? ?-reportOrModifyBudget? ?-rptNegSlackOnPorts? ?-sdcContents? ?-snapFdBudgetTo? ?-snapInputBudgetTo? ?-snapNegativeOnly? ?-snapOutputBudgetTo? ?-stageBasedFanoutDrivingFactor? ?-stageBasedPartitionMultiplier? ?-stageBasedWeight? ?-topLevel? ?-topLevelDelayPerLen? ?-topLevelMinDelayPerNet? ?-useBoundaryCondition? ?-virtualClock? ?-virtualOptEngine? ?-writeConstraintsForClkOutputPorts? ?-writeFPForHold? ?-writeLatencyPerClock? ?-quiet?",
        ),
        # man1/getBuildArch.1
        _syn(
            "getBuildArch",
            "Reports whether the Innovus session is running in 32-bit or 64-bit mode",
            "getBuildArch ?-help?",
        ),
        # man1/getCheckMode.1
        _syn(
            "getCheckMode",
            "Returns information about the specified setCheckMode parameter in the log file and in the console",
            "getCheckMode ?-all? ?-checkIlm? ?-extraction? ?-floorplan? ?-globalNet? ?-integrity? ?-io? ?-library? ?-mgrid? ?-netlist? ?-placement? ?-route? ?-sroute? ?-tapeOut? ?-timingGraph? ?-vcellnetlist?",
        ),
        # man1/getClonePtnOrient.1
        _syn(
            "getClonePtnOrient",
            "Retrieves the orientation information of the specified partition clone",
            "getClonePtnOrient ?-help? <hinst>",
        ),
        # man1/getCmdLogFileName.1
        _syn(
            "getCmdLogFileName",
            "Reports the name of the command log file",
            "getCmdLogFileName ?-help?",
        ),
        # man1/getCompressLevel.1
        _syn(
            "getCompressLevel",
            "",
            "getCompressLevel",
        ),
        # man1/getCPFUserAttributes.1
        _syn(
            "getCPFUserAttributes",
            "Reports the user_attributes of the power domain or net specified in the CPF file",
            "getCPFUserAttributes ?-help? -domain <domainName> | -net <netName>",
        ),
        # man1/getDbGetMode.1
        _syn(
            "getDbGetMode",
            "Displays the following information about a setDbGetMode parameter in the Innovus log file and in the In‐ novus console",
            "getDbGetMode ?-help? ?-displayFormat? ?-displayLimit? ?-escapeBusChar? ?-nonDefault? ?-quiet?",
        ),
        # man1/getDelayCalMode.1
        #   WARNING: bracket mismatch: '{' at position 16 closed by ']' at position 22
        _syn(
            "getDelayCalMode",
            "Returns the current settings of the setDelayCalMode command",
            "getDelayCalMode {-help? ?-combine_mmmc? ?-enable_high_fanout? ?-enable_low_memory_mode? ?-enable_quiet_receivers_for_hold? ?-equivalent_waveform_model? ?-ewm_type? ?-honorSlewPropConstraint? ?-ignoreNetLoad? ?-pessimistic_base_timing? ?-reportOutBound? ?-SIAware? ?-slewOutBoundLimitHigh? ?-slewOutBoundLimitLow? ?-socv_accuracy_mode? ?-socv_lvf_mode? ?-socv_use_lvf_tables? ?-quiet? ?-nonDefault?",
        ),
        # man1/getDensityMapMode.1
        _syn(
            "getDensityMapMode",
            "",
            "getDensityMapMode ?-gridInMicron? ?-gridInRow? ?-ignoreBlock? ?-ignoreFiller? ?-quiet? ?-threshold?",
        ),
        # man1/getDesignMode.1
        _syn(
            "getDesignMode",
            "",
            "getDesignMode ?-help? ?-addPhysicalCell? ?-backsideBottomRoutingLayer? ?-backsideTopRoutingLayer? ?-bottomRoutingLayer? ?-compressedPGDB? ?-congEffort? ?-dual_rail_via_pitch? ?-earlyclockFlow? ?-earlyPBAMode? ?-expressRoute? ?-flowEffort? ?-idealHoldFixing? ?-ignore_followpin_vias? ?-merge_trim_shapes? ?-node? ?-optimizationDensityScreenMargin? ?-pessimisticMode? ?-powerEffort? ?-process? ?-slackWeighting? ?-topRoutingLayer? ?-trim_grid_group? ?-quiet?",
        ),
        # man1/getDistributeHost.1
        _syn(
            "getDistributeHost",
            "Displays settings for the setDistributeHost command",
            "getDistributeHost {-mode | -hosts | -queue | -resource | -custom_script | -env_script | -args | -single_cpu_lsf_args | -timeout | -shell‐ Timeout | -reportLsfInfo <file> | -waitForLsfInfo <value>} ?-help?",
        ),
        # man1/getDrawView.1
        _syn(
            "getDrawView",
            "Returns the design view that was set with the setDrawView command",
            "getDrawView ?-help?",
        ),
        # man1/getEcoMode.1
        _syn(
            "getEcoMode",
            "This command displays the following information about the parameters for the corresponding setEcoMode command in the Innovus log file and in the Innovus console: name, possible values, type (Boolean, string, and so on), and source of current setting (default, user)",
            "getEcoMode ?-help? ?-addPortAsNeeded? ?-delayCalcEffort? ?-batchMode? ?-honorDontTouch? ?-inheritNetAttr? ?-LEQCheck? ?-prefixName? ?-refinePlace? ?-spreadInverter? ?-updateTiming? ?-honorDontUse? ?-honorFixedNetWire? ?-honorFixedStatus? ?-honorPowerIntent? ?-modifyOnlyLayers? ?-quiet?",
        ),
        # man1/getEditMode.1
        _syn(
            "getEditMode",
            "Returns information about the specified setEditMode parameter in the Innovus log file and the console",
            "getEditMode ?-help? ?-align? ?-allow_45_degree? ?-arrow_increment? ?-assign_multi_pattern_color? ?-auto_distribute_bus? ?-auto_split_bus? ?-bus_honor_start_params? ?-bus_honor_width_setting? ?-bus_total_width_horizontal? ?-bus_total_width_vertical? ?-change_order_at_turn? ?-check_design_boundary? ?-circle_NDR_vias_only? ?-close_polygons? ?-color_align_with_track? ?-connect_pin? ?-connect_with_specified_layer? ?-create_crossover_vias? ?-create_is_edit_flag? ?-create_via_on_pin? ?-cut_class? ?-cut_wire_overlap? ?-debug_file? ?-delete_tsv? ?-delete_pin_with_wire? ?-delete_wire_via_deep_through? ?-display_wire_length_with_cursor? ?-draw_shield? ?-draw_with_group_centerline? ?-drawing_wire? ?-drc_aware_cross_metal? ?-drc_on? ?-drc_use_non_default_spacing? ?-extend_wires? ?-final_check_with_verify? ?-ignore_drc? ?-jog_connect_layer? ?-keep_floating_via? ?-keep_status? ?-keep_via? ?-lateral_movement_range? ?-layer? ?-layer_horizontal? ?-layer_maximum? ?-layer_minimum? ?-layer_vertical? ?-look_down_layers? ?-look_up_layers? ?-max_pointer_number? ?-mirror_bus_route? ?-nets? ?-no_merge_special_wire? ?-only_show_edit_layer? ?-orthogonal_connection_only? ?-outer_shield_spacing? ?-outer_shield_width? ?-override? ?-partial_overlap_threshold? ?-pull_back_distance? ?-reshape? ?-return_object_pointer? ?-rule? ?-shape? ?-shield? ?-shield_look_down_layers? ?-shield_look_up_layers? ?-shield_shape? ?-shielding_nets? ?-show_drc_info_for_edit_shape? ?-sibling_look_down_layers? ?-sibling_look_up_layers? ?-snap? ?-snap_align_to? ?-snap_bus_to_pin? ?-snap_end_to? ?-snap_objects_to_track? ?-snap_to? ?-snap_to_track_honor_color? ?-snap_trim_metal_to_trim_grid? ?-spacing? ?-spacing_horizontal? ?-spacing_vertical? ?-status? ?-stop_at_drc? ?-stretch_end? ?-stretch_with_intersect? ?-subclass? ?-turn_at? ?-type? ?-unrestricted_regular_wire_width? ?-update_shield_net? ?-use_fixVia? ?-use_interleaving_wire_group? ?-use_wire_group? ?-use_wire_group_bits? ?-use_wire_group_reinforcement? ?-use_wire_group_reinforcement_group_via? ?-use_wire_group_reinforcement_spacing? ?-use_wire_group_reinforcement_width? ?-verbose? ?-via_allow_geom_drc? ?-via_auto_replace? ?-via_auto_snap? ?-via_cell_name? ?-via_columns? ?-via_create_by? ?-via_cut_layer? ?-via_exclude_spec? ?-via_override_spec? ?-via_rows? ?-via_scale_height? ?-via_scale_width? ?-via_snap_honor_color? ?-via_snap_to_intersection? ?-via_type? ?-width? ?-width_horizontal? ?-width_vertical? ?-wire_override_spec? ?-quiet? ?-nonDefault?",
        ),
        # man1/getEndCapMode.1
        #   WARNING: unclosed bracket '[' at position 330
        _syn(
            "getEndCapMode",
            "",
            "getEndCapMode ?-help? ?-antenna_tap_fill_wall_cells? ?-avoidTwoSitesCellAbut? ?-barrier_border_cell_bottom_y? ?-barrier_border_cell_top_y? ?-barrier_cell_x? ?-barrier_cell_xy? ?-barrier_cell_y? ?-barrier_keepout_from_boundary? ?-barrier_pitch? ?-barrier_termination_bottom_y? ?-barrier_termination_top_y? ?-barrier_termination_x? ?-barrier_y_mode ?-bottomEdge? ?-boundary_tap? ?-boundary_tap_swap_flow? ?-cells? ?-create_rows? ?-DoubleHeightIncornerProtrusion? ?-enable_shrink_physical_cell_flow? ?-flipY? ?-incrementalLeftEdge? ?-incrementalRightEdge? ?-insert_nppp_wall? ?-nppp_wall_pitch? ?-nppp_wall_to_FILLWALL_spacing? ?-nppp_wall_to_incorner_spacing? ?-leftBottomCorner? ?-leftBottomCornerEven? ?-leftBottomCornerNeighbor? ?-leftBottomCornerOdd? ?-leftBottomEdge? ?-leftBottomEdgeEven? ?-leftBottomEdgeNeighbor? ?-leftBottomEdgeOdd? ?-leftCornerBottomBorder? ?-leftCornerTopBorder? ?-leftEdge? ?-leftEdgeBottomBorder? ?-leftEdgeEven? ?-leftEdgeOdd? ?-leftEdgeTopBorder? ?-leftTopCorner? ?-leftTopCornerEven? ?-leftTopCornerNeighbor? ?-leftTopCornerOdd? ?-leftTopEdge? ?-leftTopEdgeEven? ?-leftTopEdgeNeighbor? ?-leftTopEdgeOdd? ?-min_horizontal_channel_width? ?-min_jog_height? ?-min_jog_width? ?-min_vertical_channel_width? ?-min_horizontal_channel_width? ?-min_jog_height? ?-min_jog_width? ?-min_vertical_channel_width? ?-prefix? ?-reset? ?-rightBottomCorner? ?-rightBottomCornerEven? ?-rightBottomCornerNeighbor? ?-rightBottomCornerOdd? ?-rightBottomEdge? ?-rightBottomEdgeEven? ?-rightBottomEdgeNeighbor? ?-rightBottomEdgeOdd? ?-rightCornerBottomBorder? ?-rightCornerTopBorder? ?-rightEdge? ?-rightEdgeBottomBorder? ?-rightEdgeEven? ?-rightEdgeOdd? ?-rightEdgeTopBorder? ?-rightTopCorner? ?-rightTopCornerEven? ?-rightTopCornerNeighbor? ?-rightTopCornerOdd? ?-rightTopEdge? ?-rightTopEdgeEven? ?-rightTopEdgeNeighbor? ?-rightTopEdgeOdd? ?-topBottomEdge? ?-topEdge? ?-useEvenOddSite? ?-wall_keepout_from_vertical_boundary? ?-wall_offset? ?-wall_pitch? ?-wall_shift_step? ?-wall_to_incorner_spacing?",
        ),
        # man1/getExportMode.1
        _syn(
            "getExportMode",
            "Retrieves the current settings of all or specific setExportMode parameters",
            "getExportMode ?-help? ?-fullPinout? ?-implicitPortMapping? ?-quiet?",
        ),
        # man1/getExtractRCMode.1
        _syn(
            "getExtractRCMode",
            "Returns information about the specified setExtractRCMode parameter in the Innovus log file and the con‐ sole",
            "getExtractRCMode ?-help? ?-assumeMetFill? ?-capFilterMode? ?-cerebrus_license_only? ?-compressOptMemRCDB? ?-coupled? ?-coupling_c_th? ?-defViaCap? ?-effortLevel? ?-engine? ?-extraCmdFile? ?-extractionFillStreamMapFile? ?-extract_rc_quantus_executable? ?-hardBlockObs? ?-incremental? ?-layerIndependent? ?-lefTechFileMap? ?-localCpu? ?-pvs_fill? ?-qrcCmdFile? ?-qrcCmdType? ?-qrcOutputMode? ?-qrcRunMode? ?-relative_c_th? ?-signoff_stream_layer_map? ?-total_c_th? ?-tQuantusModelFile? ?-turboReduce? ?-tsvSubcktFile? ?-useQrcOAInterface? ?-useShieldingInDetailMode? ?-viaCap? ?-writeDefOptionsForSignoffExtract? ?-quiet?",
        ),
        # man1/getFillerMode.1
        _syn(
            "getFillerMode",
            "Returns the information about setFillerMode parameters in the Innovus log file and in the Innovus console",
            "getFillerMode ?add_fillers_with_drc true? ?avoid_abutment_patterns? ?-check_signal_drc? ?-check_trim_rule? ?-core? ?-corePrefix? ?-createRows? ?-diffCellViol? ?-distribute_implant_evenly? ?-double_height_filler_insertion? ?-ecoMode? ?-enable_restore_filler_flow? ?-fitGap? ?-honorPrerouteAsObs? ?-horizontal_exception_cell? ?-horizontal_max_length? ?-horizontal_repair_cell? ?-keepFixed? ?-merge? ?-minHole? ?-preserveUserOrder? ?-scheme? ?-swap_cell? ?-vertical_stack_exception_cell? ?-vertical_stack_left_edge_exception_cell? ?-vertical_stack_max_length? ?-vertical_stack_repair_cell? ?-vertical_stack_repair_edge? ?-vertical_stack_right_edge_exception_cell? ?-viaEnclosure? ?-y_flip_type? ?-quiet?",
        ),
        # man1/getFinishFPlanMode.1
        _syn(
            "getFinishFPlanMode",
            "Returns information about the specified setFinishFPlanMode parameter in the Innovus log file and the console",
            "getFinishFPlanMode ?-help? ?-abuttedEdgeAsNonRowArea? ?-activeObj? ?-direction? ?-drcRegionObj? ?-override? ?-quiet?",
        ),
        # man1/getFlipChipMode.1
        #   WARNING: unclosed bracket '[' at position 884
        _syn(
            "getFlipChipMode",
            "Returns information about the specified setFlipChipMode parameter in the Innovus log file and the con‐ sole",
            "getFlipChipMode ?-help? ?-allow_layer_change? ?-auto_pairing_file? ?-bump_use_oct_shape? ?-check_bump_access_directions? ?-compaction? ?-connectPowerCellToBump? ?-constraintFile? ?-drop_via_on_all_geometries? ?-drop_via_on_power_mesh? ?-extraConfig? ?-finger_direction? ?-finger_max_width? ?-finger_min_width? ?-finger_target_mesh_layer_range? ?-honor_bump_connect_target_constraint? ?-ignore_pad_type_check? ?-layerChangeBotLayer? ?-layerChangeTopLayer? ?-lower_layer_prevent_45_routing? ?-lower_layer_route_width? ?-merge_nearby_pin? ?-multi_pad_routing_style? ?-multipleConnection? ?-pg_mesh_direction? ?-pg_mesh_main_width? ?-pg_mesh_max_width? ?-pg_mesh_width? ?-prevent_diagonal_wire_access_bumps? ?-prevent_via_under_bump? ?-prevent_via_under_bump_extension? ?-route_bump_cluster? ?-route_pg_style? ?-route_style? ?-routeWidth? ?-via_abut_bump? ?-via_to_pad_honor_min_spacing? ?-wire_to_pad_honor_min_spacing ?-quiet? ?-nonDefault?",
        ),
        # man1/getFPlanMode.1
        _syn(
            "getFPlanMode",
            "Returns information about the specified setFPlanMode parameter in the Innovus log file and the console",
            "getFPlanMode ?-help? ?-autoSyncMasterClone? ?-cellsForExtraSites? ?-checkTypes? ?-cutOffPlaceBlockageOutsideDie? ?-cutOffRouteBlockageOutsideDie? ?-defaultBlockageNamePrefix? ?-defaultPowerDomainSite? ?-defaultRowPatternSite? ?-defaultTechSite? ?-enableRectilinearDesign? ?-extraRowPattern? ?-extraSites? ?-firstRowSiteIndex? ?-includeIoWhenInitArea? ?-initAllCompatibleCoreSiteRows? ?-keepRowsWhenMovingPowerDomain? ?-lastRowSiteIndex? ?-maxIoHeight? ?-minimumSites? ?-move_child_constraint_with_constraint? ?-move_macros_with_constraint? ?-move_preplaced_std_cell_only? ?-move_std_cell_with_constraint? ?-narrowChannelThreshold? ?-no_cut_row? ?-powerRailLayer? ?-rowHeightIncrementCornerToCorner? ?-rowHeightIncrementIncornerToCorner? ?-rowHeightIncrementIncornerToIncorner? ?-rowHeightMultiple? ?-rowSiteHeight? ?-rowSiteWidth? ?-snap_all_corners_to_grid? ?-snapBlockGrid? ?-snapConstraintGrid? ?-snapCoreGrid? ?-snapDieGrid? ?-snapIoGrid? ?-snapPlaceBlockageGrid? ?-snapPlaceBlockageType? ?-user_define_grid? ?-quiet? ?-nonDefault?",
        ),
        # man1/getGenerateViaMode.1
        _syn(
            "getGenerateViaMode",
            "Displays the information about the specified setGenerateViaMode parameter in the Innovus log file and in the Innovus console",
            "getGenerateViaMode ?-help? ?-auto? ?-ndr_only {true|false}? ?-quiet? ?-nonDefault?",
        ),
        # man1/getHierMode.1
        _syn(
            "getHierMode",
            "Returns information about the specified setHierMode parameter in the log file and in the console",
            "getHierMode ?-help? ?-addAntennaCell? ?-quiet? ?-trialRouteHonorReadOnly? ?-optStage {preCTS | postCTS | unset}?",
        ),
        # man1/getIlmMode.1
        _syn(
            "getIlmMode",
            "Displays information about the specified setIlmMode parameter in the Innovus log file and in the Innovus con‐ sole",
            "getIlmMode ?-filterInternalPath? ?-ilm? ?-ilm <ilmName>? ?-keepAsync {true|false}? ?-keepFlatten {true|false}? ?-keepHighFanoutPorts {true|false}? ?-keepInstInSdc {true|false}? ?-keepLoopBack {true|false}? ?-map {view|corner}? ?-maxNumInsts? ?-maxNumRegisters? ?-resetMap {view|corner}? ?-slackDriven? ?-top <topViewName>? ?-quiet?",
        ),
        # man1/getIlmType.1
        _syn(
            "getIlmType",
            "Displays information about the specified setIlmType in the Innovus log file and the Innovus console",
            "getIlmType ?-help? ?-model?",
        ),
        # man1/getImportMode.1
        _syn(
            "getImportMode",
            "Retrieves the current settings of all or specific setImportMode parameters",
            "getImportMode ?-help? ?-keepEmptyModule? ?-minDBUPerMicron? ?-syncReLativePath? ?-treatUndefinedCellAsBbox? ?-quiet?",
        ),
        # man1/getInstPowerDomain.1
        _syn(
            "getInstPowerDomain",
            "Returns the power domain of the instance",
            "getInstPowerDomain <instanceName>",
        ),
        # man1/getIntegRouteConstraint.1
        _syn(
            "getIntegRouteConstraint",
            "Displays the settings needed for the setIntegRouteConstraint command",
            "getIntegRouteConstraint ?-help? ?-net <net_name> | -name <constraint_name> | -additional?",
        ),
        # man1/getIoFlowFlag.1
        _syn(
            "getIoFlowFlag",
            "Gets the current I/O row flow flag setting",
            "getIoFlowFlag ?-help?",
        ),
        # man1/getLatencyFile.1
        _syn(
            "getLatencyFile",
            "",
            "getLatencyFile ?-help?",
        ),
        # man1/getLayerPreference.1
        _syn(
            "getLayerPreference",
            "Provides information about a single preference for a single object",
            "getLayerPreference ?-help? <layer_name> {-isVisible | -isSelectable | -color | -lineWidth | -stipple | -stippleData}",
        ),
        # man1/getLogFileName.1
        _syn(
            "getLogFileName",
            "Reports the name of the log file",
            "getLogFileName ?-help? ?-fullPath?",
        ),
        # man1/getModuleView.1
        _syn(
            "getModuleView",
            "Verifies the FlexView mode",
            "getModuleView ?-help? ?-topReadOnly? ?-hinst <list_of_partition_hinsts>? ?-partition <list_of_paritions>? ?-quiet?",
        ),
        # man1/getMsvMode.1
        _syn(
            "getMsvMode",
            "Gets the special handling for inter-domain nets and uses effective power domains for ISO/LS insertion",
            "getMsvMode ?-help? ?-allowNestedDefaultDomain? ?-allowPowerDomainMinGapZero? ?-checkAllNetsForDomainCrossing? ?-handleBackToBackIsolation? ?-handlePD {true|false}? ?-handlePDComplex {true|false}? ?-honorCpfGlobalConnectionSpecForAoBuffer? ?-honorCpfGlobalConnectionSpecForShifter? ?-honorDotLibRelatedPGPin? ?-honorEffectiveDomainForIsoLsInsertion? ?-markIsoEnablePinAsAlwaysOn? ?-notUseTopFTermDomainForVoltage? ?-nonDefault? ?-shareWellAOBufferingSupport? ?-upf_allow_shifter_voltage_mismatch? ?-upf_insert_on_floating_pins? ?-quiet?",
        ),
        # man1/getMultiCpuUsage.1
        _syn(
            "getMultiCpuUsage",
            "Displays the requested number of threads or hosts",
            "getMultiCpuUsage ?-help? ?-autoPageFaultMonitor? ?-cpuPerRemoteHost? ?-keepLicense? ?-localCpu? ?-remoteHost? ?-threadInfo? ?-verbose?",
        ),
        # man1/getNanoRouteMode.1
        _syn(
            "getNanoRouteMode",
            "Returns information about the specified setNanoRouteMode parameter in the Innovus log file and the con‐ sole",
            "getNanoRouteMode ?-help? ?-extract_keep_fill_wires? ?-route_adjust_auto_via_weight? ?-route_allow_inst_overlaps? ?-route_ignore_follow_pin_shapes? ?-route_process_node? ?-route_rc_extraction_corner? ?-route_skip_analog? ?-route_via_weight? ?-route_detail_add_passive_fill_only_on_layers? ?-route_detail_allow_passive_fill_only_in_layers? ?-route_detail_antenna_eco_list_file? ?-route_detail_auto_stop? ?-route_detail_check_mar_on_cell_pin? ?-route_detail_end_iteration? ?-route_detail_fix_antenna? ?-route_detail_fix_antenna_on_secondary_pg_nets? ?-route_detail_fix_antenna_with_gate_array_filler_mode? ?-route_detail_merge_abutting_cut? ?-route_detail_min_length_for_spread_wire? ?-route_detail_min_length_for_widen_wire? ?-route_detail_min_slack_for_opt_wire? ?-route_detail_no_taper_in_layers? ?-route_detail_no_taper_on_output_pin? ?-route_detail_on_grid_only? ?-route_detail_post_route_litho_repair? ?-route_detail_post_route_spread_wire? ?-route_detail_post_route_swap_via? ?-route_detail_postroute_via_priority? ?-route_detail_post_route_via_pillar_effort? ?-route_detail_post_route_wire_widen? ?-route_detail_post_route_wire_widen_rule? ?-route_detail_search_and_repair? ?-route_detail_signoff_effort? ?-route_detail_stub_routing_in_first_layer? ?-route_detail_use_multi_cut_via_effort? ?-route_number_fail_limit? ?-route_number_thread? ?-route_number_warning_limit? ?-route_third_party_data? ?-route_high_freq_constraint_groups? ?-route_high_freq_match_report_file? ?-route_high_freq_num_reserved_layers? ?-route_high_freq_remove_floating_shield? ?-route_high_freq_search_repair? ?-route_high_freq_shield_trim_length? ?-route_interposer_allow_diagonal_trunk? ?-route_interposer_control_options? ?-route_interposer_interlayer_shielding_layers? ?-route_interposer_interlayer_shielding_nets? ?-route_interposer_interlayer_shielding_offsets? ?-route_interposer_interlayer_shielding_widths? ?-route_interposer_same_layer_shielding_net? ?-route_interposer_same_layer_shielding_width_spacing? ?-route_interposer_trunk_routing_layers? ?-route_interposer_trunk_routing_width_spacing? ?-route_add_antenna_inst_prefix? ?-route_allow_pin_as_feedthru? ?-route_antenna_cell_name? ?-route_concurrent_minimize_via_count_effort? ?-route_connect_to_bumps? ?-route_fix_clock_nets? ?-route_route_clock_nets_first? ?-route_disable_route_rule_on_via_pillar_to_special_net_wire? ?-route_eco_ignore_existing_route? ?-route_enable_route_rule_si_limit_length? ?-route_enforce_route_rule_on_special_net_wire? ?-route_extra_via_enclosure? ?-route_honor_exclusive_region? ?-route_honor_power_domain? ?-route_ignore_antenna_top_cell_pin? ?-route_antenna_diode_insertion? ?-route_diode_insertion_for_clock_nets? ?-route_shield_tap_cell_insertion? ?-route_relaxed_route_rule_spacing_to_power_ground_nets? ?-route_reserve_space_for_multi_cut? ?-route_reverse_direction? ?-route_selected_net_only? ?-route_shield_crosstie_offset? ?-route_shield_length_threshold? ?-route_shield_report_skip_status? ?-route_shield_stripe_layer_range? ?-route_shield_tap_cell_name? ?-route_strictly_honor_1d_routing? ?-route_strict_honor_route_rule? ?-route_stripe_layer_range? ?-route_tieoff_to_shapes? ?-route_trim_pull_back_distance_from_boundary? ?-route_trunk_with_cluster_target_size? ?-route_use_auto_via? ?-route_with_eco? ?-route_with_litho_driven? ?-route_with_si_driven? ?-route_with_timing_driven? ?-route_with_trim_metal? ?-route_with_via_in_pin? ?-route_with_via_only_for_block_cell_pin? ?-route_with_via_only_for_stdcell_pin? ?-quiet? ?-nonDefault?",
        ),
        # man1/getNetWeight.1
        _syn(
            "getNetWeight",
            "Retrieves the net weight values for the specified nets",
            "getNetWeight ?-help? {-all | <netName><...> }",
        ),
        # man1/getOaxMode.1
        _syn(
            "getOaxMode",
            "",
            "getOaxMode ?-help? ?-allowAnalysisOnly? ?-allowBitConnection? ?-allowTechUpdate? ?-bindkeyFile? ?-compressLevel? ?-convertTo? ?-cutRows? ?-displayDrfFile? ?-displayDrfInLibrary? ?-drcFillPurpose? ?-encloseQuickAbstractPins? ?-fullLayerList? ?-fullPath? ?-hybridRows? ?-instPlacedIfUnknown? ?-libCreateMode? ?-locking? ?-logicOnlyImport? ?-merge_trim? ?-nonRectilinearShapes? ?-pinPurpose? ?-pushPinConstraint? ?-quickAbstractForCustomCells? ?-readSystemReservedLayers? ?-saveCdsFixedVias? ?-saveMaskDataLocked? ?-saveNetVoltage? ?-saveRelativePath? ?-saveRestoreFile? ?-silently_ignore_unsupported_vias? ?-textPurpose? ?-tieNet? ?-updateMode? ?-useVirtuosoBindkey? ?-useVirtuosoColor? ?-viewSubType? ?-quiet?",
        ),
        # man1/getObjFPlanBoxList.1
        _syn(
            "getObjFPlanBoxList",
            "Retrieves a box list of the specified rectilinear object that was created earlier with the setObjF‐ PlanBoxListcommand",
            "getObjFPlanBoxList ?-help?",
        ),
        # man1/getObjFPlanPolygon.1
        _syn(
            "getObjFPlanPolygon",
            "Retrieves polygon coordinates of the specified rectilinear object that was created earlier with the setObjFPlanPolygon command",
            "getObjFPlanPolygon ?-help?",
        ),
        # man1/getOptMode.1
        _syn(
            "getOptMode",
            "Returns information about the specified setOptMode parameter in the Innovus log file and the console",
            "getOptMode ?-help? ?-opt_activity_refresh_args list_of_<arguments>? ?-opt_add_always_on_feed_through_buffers? ?-opt_add_insts? ?-opt_add_ports? ?-opt_add_repeater_report_failure_reason? ?-opt_all_end_points? ?-opt_allow_multi_bit_on_flop_with_sdc? ?-opt_allow_only_cell_swapping? ?-opt_area_recovery? ?-opt_area_recovery_setup_target_slack? ?-opt_clone_insts_list? ?-opt_consider_routing_congestion? ?-opt_constant_inputs? ?-opt_constant_nets? ?-opt_concatenate_default_and_user_prefixes? ?-opt_delete_insts? ?-opt_detail_drv_failure_reason? ?-opt_detail_drv_failure_reason_max_num_nets? ?-opt_down_size_insts? ?-opt_drv? ?-opt_drv_margin? ?-opt_drv_with_miller_cap? ?-opt_duplicate_cte_constrained_hport? ?-opt_early_hold_fixing? ?-opt_enable_clock_pulse_width_checks? ?-opt_enable_data_to_data_checks? ?-opt_enable_podv2_clock_opt_flow? ?-opt_enable_restructure? ?-opt_enable_targeted_synthesis? ?-opt_fix_fanout_load? ?-opt_flop_pins_report? ?-opt_flops_report? ?-opt_high_effort_cells? ?-opt_hold_allow_overlap? ?-opt_hold_allow_resize? ?-opt_hold_allow_setup_tns_degradation? ?-opt_hold_cells? ?-opt_hold_on_excluded_clock_nets? ?-opt_hold_slack_threshold? ?-opt_hold_target_slack? ?-opt_honor_density_screen? ?-opt_honor_fences? ?-opt_hold_ignore_path_groups? ?-opt_icg_enable_pin_rebuffering? ?-opt_leakage_to_dynamic_ratio? ?-opt_max_density? ?-opt_max_length? ?-opt_move_insts? ?-opt_multi_bit_combinational_opt? ?-opt_multi_bit_combinational_merge_timing_effort? ?-opt_multi_bit_combinational_split_timing_effort? ?-opt_multi_bit_flop_merge_bank_label_inference? ?-opt_multi_bit_flop_merge_timing_effort? ?-opt_multi_bit_flop_name_prefix? ?-opt_multi_bit_flop_name_separator? ?-opt_multi_bit_flop_name_suffix? ?-opt_multi_bit_flop_opt? ?-opt_multi_bit_flop_reorder_bits? ?-opt_multi_bit_flop_split_report_failure_reason? ?-opt_multi_bit_flop_split_timing_effort? ?-opt_multi_bit_unused_bit_count? ?-opt_multi_bit_unused_bits? ?-opt_new_inst_prefix? ?-opt_new_net_prefix? ?-nonDefault? ?-opt_one_pass_lec? ?-opt_podv2_flow_effort? ?-opt_pin_swapping? ?-opt_post_route_allow_overlap? ?-opt_post_route_area_reclaim? ?-opt_post_route_art_flow? ?-opt_post_route_check_antenna_rules? ?-opt_post_route_drv_recovery? ?-opt_post_route_fix_clock_drv? ?-opt_post_route_fix_glitch? ?-opt_post_route_fix_si_transitions? ?-opt_post_route_hold_recovery? ?-opt_post_route_setup_recovery? ?-opt_power_effort? ?-opt_pre_route_ndr_aware? ?-opt_preserve_all_sequential? ?-opt_preserve_hpin_function? ?-opt_remove_redundant_insts? ?-opt_report_multi_bit_unmerged_reasons? ?-opt_resize_flip_flops? ?-opt_resize_level_shifter_and_iso_insts? ?-opt_resize_power_switch_insts? ?-opt_route_opt_recovery? ?-opt_sequential_genus_restructure_report_failure_reason? ?-opt_setup_target_slack? ?-opt_skew? ?-opt_skew_ccopt? ?-opt_skew_post_route? ?-opt_skew_pre_cts? ?-opt_target_based_opt_hold_file? ?-opt_target_based_opt_file? ?-opt_target_based_opt_file_only? ?-opt_tied_inputs? ?-opt_time_design_compress_reports? ?-opt_time_design_num_paths? ?-opt_time_design_expanded_view? ?-opt_time_design_report_net? ?-opt_time_design_vertical_timing_summary? ?-opt_unfix_clock_insts? ?-opt_verbose? ?-quiet?",
        ),
        # man1/getPGNetResis.1
        _syn(
            "getPGNetResis",
            "Computes the resistance of the power or ground net",
            "getPGNetResis ?-help? ?-net {netName +}? ?-outfile <fileName>? ?-temperature <temperature>? ?-view <viewName>? ?-worst | -p2p <<x1 y1 layerName1 x2 y2 layerName2>?",
        ),
        # man1/getPGPinUseSignalRoute.1
        _syn(
            "getPGPinUseSignalRoute",
            "Returns all the existing MSV settings that were set by the setPGPinUseSignalRoute command in the current database",
            "getPGPinUseSignalRoute ?-help?",
        ),
        # man1/getPinAssignMode.1
        _syn(
            "getPinAssignMode",
            "Returns information about the specified setPinAssignMode parameter in the Innovus log file and the con‐ sole",
            "getPinAssignMode ?-help? ?-advance_node_rule_support? ?-allow_unconnected_in_abutted_edge? ?-allowNonNdrNetPinsOnNdrTracks? ?-block_boundary_macro_distance? ?-force_abutment_with_fixed? ?-insidePinSearchDistance? ?-max_distance_pairing? ?-maxChannelWidthAsAbutted? ?-pinEditInBatch? ?-pinOffStripe? ?-pinToStripeDistance? ?-pinToViaDistanceNonPrefDirection? ?-pinToViaDistancePrefDirection? ?-promotedMacroMaxLayer? ?-promotedMacroMinLayer? ?-restrict_boundary_macro_distance? ?-strict_abutment? ?-quiet? ?-useCommonColorEngineForIO?",
        ),
        # man1/getPinConstraint.1
        _syn(
            "getPinConstraint",
            "Retrieves information about the constraints set for a partition pin or an I/O pin using the setPinCon‐ straint command",
            "getPinConstraint ?-help? ?-dictFile <string>? ??-global | -cell <cell_name>? ?-global | -pin <pin_name_list>??",
        ),
        # man1/getPinDensityMapMode.1
        _syn(
            "getPinDensityMapMode",
            "",
            "getPinDensityMapMode ?-gridInMicron? ?-gridInRow? ?-threshold? ?-quiet?",
        ),
        # man1/getPlaceMode.1
        _syn(
            "getPlaceMode",
            "Displays the information about setPlaceMode parameters in the Innovus log file and in the Innovus console",
            "getPlaceMode ?-place_design_enable_3d? ?-place_design_floorplan_mode? ?-place_design_integrity_ir_fix_effort? ?-place_design_refine_macro? ?-place_design_refine_place? ?-place_detail_activity_power_driven? ?-place_detail_allow_border_pin_abut? ?-place_detail_allow_single_height_row_symmetry_x? ?-place_detail_check_cut_spacing? ?-place_detail_check_inst_space_group? ?-place_detail_check_route? ?-place_detail_color_aware_legal? ?-place_detail_context_aware_legal? ?-place_detail_eco_max_distance? ?-place_detail_eco_priority_insts? ?-place_detail_fixed_shifter? ?-place_detail_honor_inst_pad? ?-place_detail_io_pin_blockage? ?-place_detail_iraware_max_drive_strength? ?-place_detail_irdrop_aware_timing_effort? ?-place_detail_irdrop_region_number? ?-place_detail_irdrop_aware_effort? ?-place_detail_legalization_inst_gap? ?-place_detail_max_shifter_column_depth? ?-place_detail_max_shifter_depth? ?-place_detail_max_shifter_row_depth? ?-place_detail_no_filler_without_implant? ?-place_detail_pad_fixed_insts? ?-place_detail_preroute_as_obs? ?-place_detail_PGFTV_insertion_cell_list? ?-place_detail_preserve_routing? ?-place_detail_remove_affected_routing? ?-place_detail_swap_eeq_cells? ?-place_detail_use_check_drc? ?-place_detail_use_diffusion_transition_fill? ?-place_detail_use_GA_filler_groups? ?-place_detail_use_no_diffusion_one_site_filler? ?-place_detail_wire_length_opt_effort? ?-place_global_activity_power_driven? ?-place_global_activity_power_driven_effort? ?-place_global_align_macro? ?-place_global_allow_3d_stack? ?-place_global_auto_blockage_in_channel? ?-place_global_clock_gate_aware? ?-place_global_clock_power_driven? ?-place_global_clock_power_driven_effort? ?-place_global_cong_effort? ?-place_global_cpg_effort? ?-place_global_cpg_file? ?-place_global_enable_advanced_pipeline? ?-place_global_enable_distributed_place? ?-place_global_group_flop_to_macro? ?-place_global_group_flop_to_macro_level? ?-place_global_group_flop_to_macro_list? ?-place_global_ignore_scan? ?-place_global_ignore_spare? ?-place_global_max_density? ?-place_global_module_aware_spare? ?-place_global_module_padding? ?-place_global_place_io_pins? ?-place_global_reorder_scan? ?-place_global_soft_guide_strength? ?-place_global_timing_effort? ?-place_global_uniform_density? ?-place_hard_fence? ?-place_hierarchical_flow? ?-place_opt_post_place_tcl? ?-place_opt_run_global_place? ?-place_spare_update_timing_graph? ?-quiet?",
        ),
        # man1/getPreference.1
        _syn(
            "getPreference",
            "Returns the current preference settings",
            "getPreference ?-help?",
        ),
        # man1/getPtnPinStatus.1
        _syn(
            "getPtnPinStatus",
            "Retrieves the pin status that was defined with the setPtnPinStatus command",
            "getPtnPinStatus ?-help? ?-cell <cellName>? ?-pin {<pinName | pinNameList>}?",
        ),
        # man1/getRailPrototypeMode.1
        _syn(
            "getRailPrototypeMode",
            "Returns information about the specified setRailPrototypeMode parameter in the Innovus log file and the console",
            "getRailPrototypeMode ?-help? ?-domain? ?-railModel? ?-totalPower? ?-quiet?",
        ),
        # man1/getResizeFPlanMode.1
        _syn(
            "getResizeFPlanMode",
            "Returns information about the specified setResizeFPlanMode parameter in the Innovus log file and the console",
            "getResizeFPlanMode ?-help? ?-congAware? ?-honorHalo? ?-ioFix? ?-ioMoveWithEdge? ?-ioProportional? ?-maintainResourceRatioAfterResize? ?-proportional? ?-shiftBased? ?-shrinkFence? ?-snapToTrack? ?-quiet?",
        ),
        # man1/getRouteMode.1
        _syn(
            "getRouteMode",
            "Returns information about the specified Early Global Route mode parameter in the Innovus log file and the console",
            "getRouteMode ?-help? ?-earlyGlobalEffortLevel? ?-earlyGlobalHonorMsvRouteConstraint? ?-earlyGlobalNumTracksPerClockWire? ?-earlyGlobalReverseDirection? ?-earlyGlobalRouteBumpNets? ?-earlyGlobalRoutePartitionAllowFeedthru? ?-earlyGlobalRoutePartitionHonorFence? ?-earlyGlobalRoutePartitionHonorPin? ?-earlyGlobalRoutePartitionPinGuide? ?-earlyGlobalRouteSecondPG? ?-earlyGlobalRouteSelectedNetsOnly? ?-earlyGlobalRouteStripeLayerRange? ?-earlyGlobalSecondPGMaxFanout? ?-quiet? ?-nonDefault?",
        ),
        # man1/getScanReorderMode.1
        _syn(
            "getScanReorderMode",
            "Returns the information about setScanReorderMode parameters in the Innovus log file and in the In‐ novus console",
            "getScanReorderMode ?-addScanPortPrefix? ?-allowSwapping? ?-clkAware? ?-compLogic {true | false}? ?-enable_for_partition? ?-keepPDPorts? ?-keepPort? ?-preferH? ?-preferV? ?-scanEffort? ?-skipMode? ?-quiet?",
        ),
        # man1/getSchedulingFile.1
        _syn(
            "getSchedulingFile",
            "",
            "getSchedulingFile ?-help?",
        ),
        # man1/getSdpGroupAttribute.1
        _syn(
            "getSdpGroupAttribute",
            "Displays the current values of various attributes of the SDP group specified with -name",
            "getSdpGroupAttribute ?-help? ?-flip? ?-justifyBy? -name <sdp_name> ?-orient? ?-origin? ?-padding? ?-skipSpace? ?-type?",
        ),
        # man1/getSdpMode.1
        _syn(
            "getSdpMode",
            "Displays the current values of various SDP-related sticky options",
            "getSdpMode ?-help? ?-clock_location? ?-disable_extended_core? ?-honor_dont_use? ?-honor_orient? ?-legalization? ?-legalization_effort? ?-max_move_distance? ?-num_column? ?-place_report? ?-pre_fixed_cells_blockage_direction? ?-quiet? ?-nonDefault?",
        ),
        # man1/getSignoffOptMode.1
        _syn(
            "getSignoffOptMode",
            "",
            "getSignoffOptMode ?-help? ?-addInst? ?-addLoad? ?-allowSkewing? ?–alongRouteBuffering? ?-bufferCellList? ?-checkType? ?-clockCellList? ?-clockMaxLevel? ?-deleteInst? ?-disableGeometryChecks? ?-drvMargin? ?-ecoFilePrefix? ?-emType? ?-fixCellEm? ?-fixClockDrv? ?-fixDataDrv? ?-fixHoldAllowSetupDegrade? ?-fixHoldAllowSetupOptimization? ?-fixHoldAllowSetupTnsDegrade? ?-fixHoldVariationAware? ?-fixHoldWithMargin? ?-fixGlitch? ?-fixIrDrop? ?-fixMaxCap? ?-fixMaxTran? ?-fixOsusGlitch? ?-fixSlackInRangeLowerLimit? ?-fixSlackInRangeUpperLimit? ?-fixSiSlew? ?-fixXtalk? ?-fixXtalkPreserveHold? ?-fixXtalkPreserveSetup? ?-holdTargetSlack? ?-holdTargetSlackPerView? ?-holdXtalkDeltaThreshold? ?-holdXtalkSlackThreshold? ?-ignoreDrvChecks? ?-keepTempFiles? ?-legalOnly? ?-loadEcoOptDb? ?-loadIrDropDb? ?-maxCapMargin? ?-maxLocalDensity? ?-maxOptRunTime? ?-maxPaths? ?-maxRunTime? ?-maxSlack? ?-maxTranMargin? ?-numReportPaths? ?-nworst? ?-optimizeCoreOnly? ?-optimizeReplicatedModules? ?-optimizeSequentialCells? ?-partitionListFile? ?-pbaEcoRoute? ?-pbaEffort? ?-postMask? ?-postStaTcl? ?-powerAware? ?-powerOptFocus? ?-prefixName? ?-preserveFiller? ?-preStaTcl? ?-resizeInst? ?-retime? ?-retimeDepth? ?-retimeDepthEarly? ?-retimeMode? ?-routingCongestionAware? ?-routeCongestionThreshold? ?-saveEcoOptDb? ?-selectDrvNetFile? ?-selectDrvPinFile? ?-selectHoldEndpoints? ?-selectSetupEndpoints? ?-setupRecovery? ?-setupTargetSlack? ?-setupTargetSlackPerView? ?-setupXtalkDeltaThreshold? ?-setupXtalkSlackThreshold? ?-skewCoreOnly? ?-skipDrvNetfile? ?-specifyHoldEndpointsMargin? ?-specifySetupEndpointsMargin? ?-swapInst? ?-upsizeInPowerOpt? ?-useGaFillerList? ?-usePfcDecapList? ?-usePfcFillerList? ?-usePfcRegularList? ?-verbose? ?-quiet? ?-nonDefault?",
        ),
        # man1/getSIMode.1
        _syn(
            "getSIMode",
            "",
            "getSIMode ?-help? ?-accumulated_small_attacker_factor? ?-accumulated_small_attacker_mode? ?-accumulated_small_attacker_threshold? ?-analysisType? ?-attacker_alignment? ?-clock_delta_delay_threshold? ?-clocks? ?-delta_delay_annotation_mode? ?-delta_delay_threshold? ?-double_switching? ?-enable_double_clocking_check? ?-enable_glitch_propagation? ?-enable_glitch_propagation_spice_deck? ?-enable_glitch_report? ?-enable_logical_correlation? ?-hold_slack? ?-individual_attacker_clock_threshold? ?-individual_attacker_simulation_filtering? ?-individual_attacker_threshold? ?-initial_si_iteration_tw? ?-input_glitch_full_propagation_threshold? ?-input_glitch_full_propagation_vh_threshold? ?-input_glitch_full_propagation_vl_threshold? ?-input_glitch_threshold? ?-input_glitch_vh_threshold? ?-input_glitch_vl_threshold? ?-nonDefault? ?-nonlinear_attacker_slew? ?-num_si_iteration? ?-pessimistic_mode? ?-receiver_clk_peak_limit? ?-receiver_latch_peak_limit? ?-receiver_peak_limit? ?-report_si_slew_max_transition? ?-secondary_attacker_decoupling_factor? ?-separate_delta_delay_on_data? ?-setup_slack? ?-si_reselection? ?-si_reselection_delay_threshold? ?-skip_tw? ?-switch_prob? ?-unconstrained_net_use_inf_tw? ?-use_infinite_TW? ?-quiet?",
        ),
        # man1/getSpecialNetResis.1
        _syn(
            "getSpecialNetResis",
            "Reports resistance values for specified nets",
            "getSpecialNetResis ?-help? ?-net {netName +}? ?-outfile <fileName>? ?-temperature <temperature>? ?-view <viewName>? ?-worst | -p2p <x1 y1 layerName1 x2 y2 layerName2?",
        ),
        # man1/getSrouteMode.1
        _syn(
            "getSrouteMode",
            "",
            "getSrouteMode ?-help? ?-allowWrongWayRoute? ?-avoidOverCoreRowLayer? ?-blockPinConnectRingPinCorners? ?-blockPinRouteWithPinWidth? ?-connectBrokenCorePin? ?-corePinIgnoreObs? ?-corePinJoinLimit? ?-corePinLength? ?-corePinLengthAsInstance? ?-corePinMaxViaScale? ?-corePinReferToFollowPin? ?-corePinReferenceMacro? ?-corePinSiteRailWidth? ?-corePinSnapTo? ?-corePinStopRoute? ?-extendNearestTarget? ?-jogThresholdRatio? ?-layerNormalCost? ?-layerWrongWayCost? ?-nonDefault? ?-padPinMinViaSize? ?-padPinSplit? ?-padRingLefConvention? ?-secondaryPinMaxGap? ?-secondaryPinRailWidth? ?-signalPinAsPG? ?-splitLongVia? ?-srpgAonCellPin? ?-targetNumber? ?-targetSearchDistance? ?-timeLimit? ?-treatEndcapAsCore? ?-treatWelltapAsEndcap? ?-viaConnectToShape? ?-viaThruToClosestRing? ?-quiet?",
        ),
        # man1/getStreamOutMode.1
        _syn(
            "getStreamOutMode",
            "Displays the following information about the specified setStreamOutMode parameter in the log file and at the console",
            "getStreamOutMode ?-help? ?-cellInstanceColor? ?-cellMasterColor? ?-cellNameUserPrefix? ?-cellNameUserSuffix? ?-convertRectToPath? ?-labelAllPinShape? ?-merge_trim_shapes? ?-mergeAppend? ?-noPinLabelOnNets? ?-oasisCompression? ?-oasisLayerName? ?-oasisSCellOffset? ?-pinTextOrientation? ?-reset? ?-remove_short_metal_within_cell_boundary? ?-removeNets? ?-SEcompatible? ?-SEvianames?e ?-snapToMGrid? ?-specifyViaName? ?-supportPathType4? ?-textSize? ?-uniquifyCellNamesPrefix? ?-version? ?-virtualConnection?",
        ),
        # man1/getTieHiLoMode.1
        _syn(
            "getTieHiLoMode",
            "Returns information about the specified setTieHiLoMode parameter in the Innovus log file and the console",
            "getTieHiLoMode ?-cell? ?-createHierPort? ?-honorDontTouch? ?-maxDistance? ?-maxFanout? ?-modulePrevention? ?-prefix? ?-reportHierPort? ?-quiet? ?-nonDefault?",
        ),
        # man1/getTimeLibFile.1
        _syn(
            "getTimeLibFile",
            "Reports the library files that match the specified library name",
            "getTimeLibFile <library_name>",
        ),
        # man1/getUPFPortAttr.1
        _syn(
            "getUPFPortAttr",
            "Returns UPF port attributes from UPF or for the specified values",
            "getUPFPortAttr ?-help? <hport_name>",
        ),
        # man1/getUsefulSkewMode.1
        _syn(
            "getUsefulSkewMode",
            "Returns the current setting of the setUsefulSkewMode command",
            "getUsefulSkewMode ?-help? ?-nonDefault? ?-opt_skew_apply_delay_limits_to_full_flow? ?-opt_skew_delay_pre_cts? ?-opt_skew_macro_only? ?-opt_skew_max_allowed_delay? ?-opt_skew_min_allowed_delay? ?-opt_skew_no_boundary? ?-quiet?",
        ),
        # man1/getValidPowerSwitchLocation.1
        _syn(
            "getValidPowerSwitchLocation",
            "Returns a valid location of the power switch cells according to the specified placement grid, cell name, and nearest location",
            "getValidPowerSwitchLocation",
        ),
        # man1/getVersion.1
        _syn(
            "getVersion",
            "Returns the Innovus software version number",
            "getVersion ?-help? ?-major?",
        ),
        # man1/getViaGenMode.1
        _syn(
            "getViaGenMode",
            "Returns the current settings of the setViaGenMode command",
            "getViaGenMode ?-help? ?-accuracy_effort? ?-add_pin_to_pin_via? ?-align_merged_stack_via_metals? ?-allow_via_expansion? ?-allow_wire_shape_change? ?-area_only? ?-bot_enclosure? ?-create_double_row_cut_via? ?-create_max_row_cut_via? ?-cut_spacing? ?-cutclass_preference? ?-disable_via_merging? ?-extend_out_wire_end? ?-full_cut_via_only? ?-genvia_naming_prefix? ?-hookup_contact_max? ?-hookup_contact_pg_track? ?-hookup_preplace_fix? ?-hookup_rail_pair? ?-hookup_via_distance? ?-hookup_via_fixed_grid? ?-hookup_via_min_distance? ?-hookup_via_style? ?-hookup_via_viarule? ?-hookup_virtual_trim_grid? ?-ignore_design_boundary? ?-ignore_DRC? ?-ignore_viarule_enclosure? ?-inherit_wire_status? ?-invoke_verifyGeometry? ?-keep_existing_via? ?-keep_fixed_via? ?-mincut_preference? ?-optimize_cross_via? ?-optimize_via_on_routing_track? ?-parameterized_via_only? ?-partial_overlap_threshold? ?-preferred_vias_only? ?-reference_boundary? ?-respect_signal_routes? ?-respect_stdcell_geometry? ?-respect_wire_ndr? ?-set_via_expansion_dir? ?-snap_via_center_to_grid? ?-split_long_via_global_grid? ?-symmetrical_via_only? ?-top_enclosure? ?-use_track_offset? ?-use_trim_metal_enclosure? ?-viarule_preference? ?-quiet? ?-nonDefault?",
        ),
        # man1/getWhatIfTimingAssertions.1
        _syn(
            "getWhatIfTimingAssertions",
            "Displays the what-if timing arc specifications of the specified port in the command window",
            "getWhatIfTimingAssertions <blackBoxCellName> -port <portName> ?-tclList?",
        ),
        # man1/getWhatIfTimingMode.1
        _syn(
            "getWhatIfTimingMode",
            "",
            "getWhatIfTimingMode ?-quiet?",
        ),
        # man1/globalDetailRoute.1
        _syn(
            "globalDetailRoute",
            "Uses the NanoRoute router to perform both global and detailed routing with one command",
            "globalDetailRoute ?-help? ?-select? ?<area>?",
        ),
        # man1/globalNetConnect.1
        _syn(
            "globalNetConnect",
            "The globalNetConnect command connects PG pins or 1'b0/1'b1 pins to the specified global net, which is either a power or ground net",
            "globalNetConnect ?-help? <globalNetName > {{-type pgpin -pin <pinNamePattern> | -type tiehi ?-pin <pinNamePattern>? | -type tielo ?-pin <pinNamePattern>?} {{-singleInstance | -singleInst | -sinst} <instName> | ?{-instanceBasename | -instBasename} <instBasenamePattern>? ?{-hierarchicalInstance | -hierInst | -module} <hierInstName> | -region <llx> <lly> <urx> <ury> | -powerDomain powerDomainName | -all?} | -type net -net <netBasenamePattern > ?{-hierarchicalInstance | -hierInst | -module} <hierInstName> | -powerDomain powerDomainName | -all?} ?-override? ?-verbose? ?-autoTie? ?-disconnect? ?-netlistOverride? ?-nonHierarchical?",
        ),
        # man1/globalRoute.1
        _syn(
            "globalRoute",
            "Plans the interconnect by breaking the routing portion of the design into rectangles called global routing cells (gcells) and assigning the signal nets to the gcells",
            "globalRoute ?-help?",
        ),
        # man1/group.1
        _syn(
            "group",
            "Creates a new module and hinst from a group of the specified hinsts or insts",
            "group ?-help? <inst>|<hInst>+ ??-module_name <module_name> -hinst_base_name <hinst_base_name>??",
        ),
        # man1/group_instance_suffix.1
        _syn(
            "group_instance_suffix",
            "",
            "group_instance_suffix suffix",
        ),
        # man1/group_path.1
        _syn(
            "group_path",
            "Groups paths in a design, and identifies them with a path group name",
            "group_path ?-help? ?-comment <string>? -name <path_group_name> ??-from <from_list>? ?-to <to_list>? ?-through <through_list>??",
        ),
        # man1/gui_attach_to_cursor.1
        _syn(
            "gui_attach_to_cursor",
            "Attaches selected or specified objects to the cursor",
            "gui_attach_to_cursor ?-help? ?-selected | <objects>?",
        ),
        # man1/gui_clear_highlight_safety_mechanism.1
        _syn(
            "gui_clear_highlight_safety_mechanism",
            "Clears the highlights on the specified type of safety mechanisms",
            "gui_clear_highlight_safety_mechanism ?-help? {?-dcls | -tmr | -ser?}",
        ),
        # man1/gui_clear_trace_flightline.1
        _syn(
            "gui_clear_trace_flightline",
            "Clears all flightlines traced through the gui_trace_flightline command",
            "gui_clear_trace_flightline ?-help?",
        ),
        # man1/gui_close_cell_view.1
        _syn(
            "gui_close_cell_view",
            "Closes the Cell Viewer",
            "gui_close_cell_view ?-help?",
        ),
        # man1/gui_deselect.1
        _syn(
            "gui_deselect",
            "Deselects objects as per the parameters you specify",
            "gui_deselect ?-help? {-all | -rect {<x1 y1 x2 y2>} | -point {<x y>} | -line {<x1 y1 x2 y2>}}",
        ),
        # man1/gui_dim_foreground.1
        _syn(
            "gui_dim_foreground",
            "Dims the display area to the specified level",
            "gui_dim_foreground ?-help? -lightness_level {default medium dark}",
        ),
        # man1/gui_dump_picture.1
        _syn(
            "gui_dump_picture",
            "Saves a snapshot of the layout or specified window with the specified name in the current directory",
            "gui_dump_picture ?-help? <filename> ?-format {BMP GIF JPG JPEG PNG PBM PGM PPM XBM XPM}? ?-honor_umask? ?-width <integer_value> -height <integer_value>? ?-window <string>?",
        ),
        # man1/gui_get_legend.1
        _syn(
            "gui_get_legend",
            "Gets the current legend setting",
            "gui_get_legend ?-help? -type {inst_density pin_density timing_map metal_density route_congestion temperature} ?-display_range | -value_range | -show_legend_on_layout | -legend_location | -enable_min_value | -enable_max_value?",
        ),
        # man1/gui_get_schematic.1
        _syn(
            "gui_get_schematic",
            "Gets the name of the current (active) schematic view",
            "gui_get_schematic ?-help? ?-current | -all?",
        ),
        # man1/gui_group_hinst.1
        _syn(
            "gui_group_hinst",
            "Moves one level up the hierarchy for the specified module guide and displays the next module",
            "gui_group_hinst ?-help? ?-type {flex_model} | <hname>?",
        ),
        # man1/gui_highlight_safety_mechanism.1
        _syn(
            "gui_highlight_safety_mechanism",
            "Highlights safety-related instances and groups based on the specified parameters",
            "gui_highlight_safety_mechanism ?-help? {?-dcls {insts nets_internal nets_interface nets_common nets_top} | -tmr {parents clones voters} | -ser {insts}?} ?-color <string> | -auto_color? ?-group <group_name> ?-exclusive_groups?? ?-dcls {insts nets_internal nets_interface nets_common nets_top} ?-group <group_name>?? ?-tmr {parents clones voters} ?-inst <inst_name>??",
        ),
        # man1/gui_open_cell_view.1
        _syn(
            "gui_open_cell_view",
            "Opens the Cell Viewer",
            "gui_open_cell_view ?-help?",
        ),
        # man1/gui_report_trace_flightline.1
        _syn(
            "gui_report_trace_flightline",
            "Saves information about the all flightlines traced through the gui_trace_flightline command to the specified file",
            "gui_report_trace_flightline ?-help? -file <report_name>",
        ),
        # man1/gui_save_flightline.1
        _syn(
            "gui_save_flightline",
            "Saves the flightline information of the selected instance to the specified file",
            "gui_save_flightline ?-help? -file <file_name> ?-netWindow?",
        ),
        # man1/gui_schematic_add_selected.1
        _syn(
            "gui_schematic_add_selected",
            "Adds the selected object to the current or specified schematic view",
            "gui_schematic_add_selected ?-help? ?-name <window_name>?",
        ),
        # man1/gui_schematic_load_view.1
        _syn(
            "gui_schematic_load_view",
            "Loads the specified schematic file",
            "gui_schematic_load_view ?-help? -file <file_name>?-name <name>?",
        ),
        # man1/gui_schematic_save_view.1
        _syn(
            "gui_schematic_save_view",
            "Saves the current schematic view into the specified file",
            "gui_schematic_save_view ?-help? -file <file_name> ?-name <string>?",
        ),
        # man1/gui_select.1
        _syn(
            "gui_select",
            "Selects objects as per the parameters you specify",
            "gui_select ?-help? {-point {x y} | -line {x1 y1 x2 y2} | -rect {x1 y1 x2 y2}} ?-toggle | -append | -next? ?-point {x y} ?-next??",
        ),
        # man1/gui_set_legend.1
        _syn(
            "gui_set_legend",
            "Specifies the legend setting",
            "gui_set_legend ?-help? ?-display_range {x y}? ?-enable_max_value {true false}? ?-enable_min_value {true false}? ?-legend_location {ne nw se sw}? ?-reset <-display_range|-value_range|-show_legend_on_layout|-legend_location|-enable_min_value|-enable_max_value>? ?-show_legend_on_layout {true false}? -type {inst_density pin_density timing_map metal_density route_congestion temperature} ?-value_range {x y}?",
        ),
        # man1/gui_show_edge_number.1
        _syn(
            "gui_show_edge_number",
            "Displays edge numbers on the sides of the selected or specified objects in the GUI",
            "gui_show_edge_number ?-help? ?-objects <string>? ?-reset?",
        ),
        # man1/gui_trace_flightline.1
        _syn(
            "gui_trace_flightline",
            "Traces flightlines for the specified instance from either the output pins (with -sink) or the input pins (with -source)",
            "gui_trace_flightline ?-help? -inst <instance_name> ?-max_inout_number <value>? {?-sink -sink_level <value> -sink_color <string>? | ?-source -source_level <value> -source_color <string>?}",
        ),
        # man1/gui_ungroup_hinst.1
        _syn(
            "gui_ungroup_hinst",
            "Displays the submodules for the specified module guide",
            "gui_ungroup_hinst ?-help? ?-display_all_constraints? ?-type {<flex_model>} | <hname>?",
        ),
        # man1/gui_verbose.1
        _syn(
            "gui_verbose",
            "",
            "gui_verbose {all db none} Type: enum {all db none}, read/write",
        ),
        # man1/gui_zoom_ctd.1
        _syn(
            "gui_zoom_ctd",
            "Zooms into or out of the CTD window",
            "gui_zoom_ctd ?-help? ?-id <string>? ?-in | -out | -selected? ?-vertical_range {<ymin> <ymax>}?",
        ),
        # man1/handlePtnAreaIo.1
        _syn(
            "handlePtnAreaIo",
            "Specifies the name of the buffer to be used for feedthrough insertion in a flip chip design",
            "handlePtnAreaIo ?-insertBuffer <bufferName> | -noInsertBuffer? ?-top <extension>? ?-bottom <extension>? ?-left <extension>? ?-right <extension>? ?-selectedCell? ?-pinOnBoundary?",
        ),
        # man1/help.1
        _syn(
            "help",
            "Displays information, such as command syntax, summary of messages, list of commands, based on the specified argu‐ ment",
            "help ?-help? ?-k <keyword>| -cmd <commandName>| -var? ?<pattern>?",
        ),
        # man1/highFreqInterposerFlow.1
        _syn(
            "highFreqInterposerFlow",
            "",
            "highFreqInterposerFlow {0 | 1}",
        ),
        # man1/highlight.1
        _syn(
            "highlight",
            "Highlights selected or specified objects with the Highlight Set available through the View - Highlight Se‐ lected menu",
            "highlight ?-help? ?<<any_object>>+? ?-index <indexValue> | -auto_color | -original? ?-color <colorValue> | -auto_color | -original? ?-pattern <patternValue> | -original?",
        ),
        # man1/highlight_pin.1
        _syn(
            "highlight_pin",
            "Highlights the shapes of all specified SIGNAL/POWER instance pins with the Highlight Set available through the Edit - Highlight Selected menu",
            "highlight_pin ?-help?",
        ),
        # man1/highlight_pin_connection.1
        _syn(
            "highlight_pin_connection",
            "Highlights the full timing path or its segment in the text format while generating the sign-off timing report",
            "highlight_pin_connection ?-help? -from_pin <pin>?-mode {wire_segment | whole_net | flight_line}? -to_pin <pin>?-with_arrow | -select_only? ?-net_color_index <index_value >| -select_only? ?-inst_color_index <index_value >| -select_only?",
        ),
        # man1/highlight_timing_report.1
        _syn(
            "highlight_timing_report",
            "This command enables you to highlight a specific number of paths in Global Timing Debug through user interface",
            "highlight_timing_report ?-help? ?-append? ?-color_index <integer>? ?-file <filename>? ?-noarrow? ?-path <path_number >| -all?",
        ),
        # man1/highlightSyncObj.1
        _syn(
            "highlightSyncObj",
            "Adds highlight color on sync objects during master-clone-aware bus guide operations",
            "highlightSyncObj ?-help? ?-obj {all busGuides}?",
        ),
        # man1/hilite_proto_model.1
        _syn(
            "hilite_proto_model",
            "Highlights objects, such as, FlexModels, partitions, and/or power domains",
            "hilite_proto_model ?-help? ?-keep_existing_hilite? ?-type {flex_module flex_instgroup partition power_domain}? ?-reset? ?-level <integer>? | {?-min_level <integer>??-max_level <integer>?}",
        ),
        # man1/hiliteFeedthroughNets.1
        _syn(
            "hiliteFeedthroughNets",
            "Highlights all nets for which feedthrough buffers were inserted with the insertPtnFeedthrough com‐ mand",
            "hiliteFeedthroughNets ?-help? <fileName> ?<netNameList>?",
        ),
        # man1/identify_proto_model.1
        _syn(
            "identify_proto_model",
            "Identifies the modules or instance groups of a design that will become FlexModels",
            "identify_proto_model ?-help? ?-skip_report?",
        ),
        # man1/ignore_max_via_stack_rule.1
        _syn(
            "ignore_max_via_stack_rule",
            "",
            "ignore_max_via_stack_rule { true | false}",
        ),
        # man1/import_ilm_data.1
        _syn(
            "import_ilm_data",
            "",
            "import_ilm_data ?-help? ?-cell <block_name>? ?-incr? -model_type {timing | cts | si} ?-overwrite? ?-xtwf <xtwf_file.spef>? {-dir <directory_name> | -cell_view <lib> <cell> <view>} ?-verilog <cell_name.v> ?-cell_prefix <cell_prefix> -uniquify_netlist?? ?-sdc <file_name> -timing_view <view_name>? ?-spef <spef_file.spef> -rc_corner <RC_corner_name>? ?-optStage <opt_stage>?",
        ),
        # man1/import_module_model.1
        _syn(
            "import_module_model",
            "Imports library files into the iHDB structure",
            "import_module_model ?-help? -cell <string> ?-idx_pair <string>? -inputs <string> -libs ?-link_only? ?-rc_corner <string>? ?-tag <string>? -type {lib lef qrc_tech qrc_conf}",
        ),
        # man1/importPowerSwitch.1
        _syn(
            "importPowerSwitch",
            "Imports power switch databases",
            "importPowerSwitch ?-help? ?-powerDomain <powerDomainName>? ?-file <fileName>?",
        ),
        # man1/Index.1
        _syn(
            "Index",
            "",
            "B C D E F G H I J L M N O P Q R S T U V W Z",
        ),
        # man1/index_collection.1
        _syn(
            "index_collection",
            "",
            "index_collection ?-help? <base_collection><index>",
        ),
        # man1/init_abstract_view.1
        _syn(
            "init_abstract_view",
            "",
            "init_abstract_view <list_of_views>",
        ),
        # man1/init_check_output_pin_constant.1
        _syn(
            "init_check_output_pin_constant",
            "",
            "init_check_output_pin_constant {0 | 1 }",
        ),
        # man1/init_cpf_file.1
        _syn(
            "init_cpf_file",
            "",
            "init_cpf_file <file_path>",
        ),
        # man1/init_design.1
        _syn(
            "init_design",
            "Initializes a design using the Tcl globals",
            "init_design ?-help? ?-setup <setup_view_list> <-hold hold_view_list>?",
        ),
        # man1/init_design_netlisttype.1
        _syn(
            "init_design_netlisttype",
            "",
            "init_design_netlisttype <netlist_source>",
        ),
        # man1/init_design_settop.1
        _syn(
            "init_design_settop",
            "",
            "init_design_settop <value>",
        ),
        # man1/init_design_uniquify.1
        _syn(
            "init_design_uniquify",
            "",
            "init_design_uniquify <value>",
        ),
        # man1/init_enable_drc_region_layer.1
        _syn(
            "init_enable_drc_region_layer",
            "",
            "init_enable_drc_region_layer {<list_of_drc_region_layer>}",
        ),
        # man1/init_gnd_net.1
        _syn(
            "init_gnd_net",
            "",
            "init_gnd_net <list_of_nets>",
        ),
        # man1/init_hier_cell.1
        _syn(
            "init_hier_cell",
            "Initializes one or more hierarchical cells based on the applicable order",
            "init_hier_cell ?-help? <cell_names> ?-dual_view?",
        ),
        # man1/init_ignore_pgpin_polarity_check.1
        _syn(
            "init_ignore_pgpin_polarity_check",
            "",
            "init_ignore_pgpin_polarity_check",
        ),
        # man1/init_import_mode.1
        _syn(
            "init_import_mode",
            "",
            "init_import_mode <import_mode_parameters>",
        ),
        # man1/init_io_file.1
        _syn(
            "init_io_file",
            "",
            "init_io_file <file_name>",
        ),
        # man1/init_layout_view.1
        _syn(
            "init_layout_view",
            "",
            "",
        ),
        # man1/init_lef_check_antenna.1
        _syn(
            "init_lef_check_antenna",
            "",
            "init_lef_check_antenna {0 | 1}",
        ),
        # man1/init_lef_check_mask_shifts.1
        _syn(
            "init_lef_check_mask_shifts",
            "",
            "init_lef_check_mask_shifts {on | off | bypass}",
        ),
        # man1/init_lef_file.1
        _syn(
            "init_lef_file",
            "",
            "init_lef_file <list_of_files>",
        ),
        # man1/init_ml.1
        _syn(
            "init_ml",
            "Initializes the environment to start writing data for JedAI",
            "init_ml ?-help? ?-comment <string>? ?-flow_phase <string>? ?-name <string>? -prefix <string> ?-scenario <string>?",
        ),
        # man1/init_mmmc_file.1
        _syn(
            "init_mmmc_file",
            "",
            "init_mmmc_file <file_name>",
        ),
        # man1/init_mmmc_version.1
        _syn(
            "init_mmmc_version",
            "",
            "init_mmmc_version {1 2}",
        ),
        # man1/init_no_new_assigns.1
        _syn(
            "init_no_new_assigns",
            "",
            "init_no_new_assigns",
        ),
        # man1/init_oa_default_rule.1
        _syn(
            "init_oa_default_rule",
            "",
            "init_oa_default_rule <ruleName>",
        ),
        # man1/init_oa_design_cell.1
        _syn(
            "init_oa_design_cell",
            "",
            "init_oa_design_cell <cellname>",
        ),
        # man1/init_oa_design_lib.1
        _syn(
            "init_oa_design_lib",
            "",
            "init_oa_design_lib <libraryname>",
        ),
        # man1/init_oa_design_view.1
        _syn(
            "init_oa_design_view",
            "",
            "init_oa_design_view <viewname>",
        ),
        # man1/init_oa_foundry_rule.1
        _syn(
            "init_oa_foundry_rule",
            "",
            "init_oa_foundry_rule <foundry_rule_name>",
        ),
        # man1/init_oa_ref_lib.1
        _syn(
            "init_oa_ref_lib",
            "",
            "init_oa_ref_lib <list_of_OA_libs>",
        ),
        # man1/init_oa_search_lib.1
        _syn(
            "init_oa_search_lib",
            "",
            "init_oa_search_lib <list_of_OA_ref_libs>",
        ),
        # man1/init_oa_special_rule.1
        _syn(
            "init_oa_special_rule",
            "",
            "init_oa_special_rule name",
        ),
        # man1/init_original_verilog_files.1
        _syn(
            "init_original_verilog_files",
            "",
            "init_original_verilog_files name",
        ),
        # man1/init_power_intent_file.1
        _syn(
            "init_power_intent_file",
            "",
            "init_power_intent_file <file_name>",
        ),
        # man1/init_pwr_net.1
        _syn(
            "init_pwr_net",
            "",
            "init_pwr_net <list_of_power_nets>",
        ),
        # man1/init_top_cell.1
        _syn(
            "init_top_cell",
            "",
            "init_top_cell <top_cell_name>",
        ),
        # man1/init_verilog.1
        _syn(
            "init_verilog",
            "",
            "init_verilog <list_of_netlist_files>",
        ),
        # man1/init_verilog_tolerate_port_mismatch.1
        _syn(
            "init_verilog_tolerate_port_mismatch",
            "",
            "init_verilog_tolerate_port_mismatch <value>",
        ),
        # man1/initCoreRow.1
        _syn(
            "initCoreRow",
            "Regenerates rows for the core area and the power domains in a design",
            "initCoreRow ?-help? ?-powerDomain <string>?",
        ),
        # man1/initECO.1
        _syn(
            "initECO",
            "Logs ECO operations in a log file",
            "initECO ?-help? <ecoFileName>",
        ),
        # man1/inn_save_lef_ignore_abstracts.1
        _syn(
            "inn_save_lef_ignore_abstracts",
            "",
            "inn_save_lef_ignore_abstracts {True | False}",
        ),
        # man1/innovus.1
        _syn(
            "innovus",
            "Launches an Innovus™ Implementation System session",
            "innovus ?-abort_on_error? ?-batch? ?-cds_lib_file <in_file>? ?-cpus <value>? ?-db <dir> | -ihdb <dir>? ?-disable_user_startup? ?-execute <list_of_Tcl_commands>? ?-files <in_file_list>? ?-help? ?-lic_multi_cpu <lic_list>? ?-lic_options <lic_list>? ?-lic_startup <lic_list>? ?-lic_startup_options <lic_list>? ?-lic_stack {1 | 2}? ?-log <prefix>? ?-no_cmd? ?-no_gui? ?-no_logv? ?-overwrite? ?-stylus? ?-version? ?-wait <minutes>?",
        ),
        # man1/insert_physical_cell.1
        _syn(
            "insert_physical_cell",
            "Provides a flexible way to insert and check physical cells",
            "insert_physical_cell ?-help? ?-cell <string>? ?-genTemplateOnly <string>? ?-inputFile <filename>? ?-insertRowAreaBoundary? ?-averageWindow | { ?-insertNearBoundary? ?-box {<x1 y1 x2 y2>}? ?-minimalNumberOfTCD <integer>?}? ?-verifyWindow {<x y>}??-verifyOnly??-xStep <float>? ?-yStep <float>???",
        ),
        # man1/insertPtnFeedthrough.1
        _syn(
            "insertPtnFeedthrough",
            "Inserts feedthrough buffers into the partitions, changing the original netlist, to avoid routing a net over a block area",
            "insertPtnFeedthrough ?-help? ?-allLowercase? ?-blockageFile <fileName>? ?-blockedEdgesFile <fileName>? ?-instPrefix <instancePrefix>? ?-netPrefix <netPrefix>? ?-repeatedSymmetricAbuttedFPlan? ?-reuseBuffer {true false 0 1}? ?-saveTopoFile <fileName>? ?-useShortName? ?-verbose? ???-selectNet <fileName> | -selectMarkedNet | -autoSelectNetsByCongestion | -autoSelectNetsBySlack | ??-excludeNet <fileName>???? | -topoFile <topologyFileName>? ?-topoFile <topologyFileName> | -routeBased | -routeBasedStrict | ?-excludePtnList {<ptnName> | <ptnNameList>}?? ?-topoFile <topologyFileName> | -routeBased | -routeBasedStrict? ?-routeBased ?-autoSelectNetsBySlack? ?-autoSelectNetsByCongestion?? ?-noBuffer | ??-bufCell {<cellName> | <cellNameList>}? ?-doubleBuffer??? ??-checkOnly? | ??-ecoFile <fileName>? ?-netMapping <fileName>??? ?-topoFile <topologyFileName>? ?-noBuffer?",
        ),
        # man1/ioInstOverlapCheck.1
        _syn(
            "ioInstOverlapCheck",
            "Checks to see if any area I/O instance is overlapped with another area I/O instance",
            "ioInstOverlapCheck ?-help?",
        ),
        # man1/is_common_ui_mode.1
        _syn(
            "is_common_ui_mode",
            "Checks if the Stylus Common UI mode is enabled",
            "is_common_ui_mode ?-help?",
        ),
        # man1/justifyBudget.1
        _syn(
            "justifyBudget",
            "Queries and verifies the timing budgets generated by the Innovus software",
            "justifyBudget ?-help? {<partitionName> | <instanceName>} {-pins <pinList>} ?-outfile <fileName>? ?-summary? ?-view <viewName>?",
        ),
        # man1/justifyException.1
        _syn(
            "justifyException",
            "Provides a debugging or justification mechanism of exceptions on ports",
            "justifyException {-pins <pinList>} ?-outfile <fileName>? {<partitionName> | <instanceName>} -view <viewName> ?-help?",
        ),
        # man1/layerNameNoAbbreviation.1
        _syn(
            "layerNameNoAbbreviation",
            "",
            "layerNameNoAbbreviation {0 | 1}",
        ),
        # man1/lef2oa.1
        _syn(
            "lef2oa",
            "The LEF to OpenAccess translator can be used to convert LEF files into equivalent OpenAccess data",
            "lef2oa -lef <file-lib library> ?-commentChar <char>? ?-compress? ?-compressLevel <zLevel>? ?-createFixedViaDefs? ?-dataModel <version>? ?-defaultRuleName <name>? ?-DMAttributes <attributeList>? ?-DMSystem <sysName>? ?-h | -help? ?-layerMap <filelist>? ?-layoutView <viewName>? ?-libDefFile <fileList>? ?-libPath path? ?-lockColors? ?-logFile <file>? ?-mapConflicts? ?-noInfo <msgIds>? ?-noWarning <msgIds>? ?-overwrite? ?-pinLabels? ?-pnrLibDataOnly? ?-shared? ?-suffix <string>? ?-techDMAttributes <attrList>? ?-techDMSystem <sysName>? ?-techLib <library>? ?-techLibPath <path>? ?-techRefs <parentTechs>? ?-templateFile <file>? ?-textHeight <value>? ?-textLayer <value>? ?-useFoundryInnovus? ?-view <viewName>? ?-v? ?-version?",
        ),
        # man1/lefdefInputCheckColoredShape.1
        _syn(
            "lefdefInputCheckColoredShape",
            "",
            "lefdefInputCheckColoredShape { true | false}",
        ),
        # man1/lefDefOutVersion.1
        _syn(
            "lefDefOutVersion",
            "",
            "lefDefOutVersion <version_num>",
        ),
        # man1/lefExtend2DCellShapes.1
        _syn(
            "lefExtend2DCellShapes",
            "",
            "lefExtend2DCellShapes { {layer extension_amount}… }",
        ),
        # man1/lefExtendCellObsShapeUnderTrim.1
        _syn(
            "lefExtendCellObsShapeUnderTrim",
            "",
            "lefExtendCellObsShapeUnderTrim <listOfRoutingLayers>",
        ),
        # man1/lefIgnoreLayerNames.1
        _syn(
            "lefIgnoreLayerNames",
            "",
            "lefIgnoreLayerNames <layerNames>",
        ),
        # man1/legalizeFPlan.1
        _syn(
            "legalizeFPlan",
            "Legalizes partition locations according to standard cell row orientations and specific design constraints",
            "legalizeFPlan ?-help? ?-checkOri? ?-checkSite?",
        ),
        # man1/legalizePin.1
        #   WARNING: unclosed bracket '[' at position 36
        _syn(
            "legalizePin",
            "Moves a pin from its existing location",
            "legalizePin ?-help? ?-auto_pairing? ?-ignore {pin_spacing pin_spacing_constraint pin_spacing_routeBlk pin_width pin_depth pin_layer pin_min_area pin_on_track pin_abutment pin_non_nbr_abutment clones pin_color} ?-internalPin? ?-keepLayer? ?-keepOrder? ?-moveFixedPin? ?-pin {<pinName>| <pinNameList>}? ?-ptn <ptnName>? ?-snapToBoundary? ?-verbose? ?-ptn <ptnName>| {-pin_file <fileName>?-exclude_ptn <ptnName>?}? ?-pin_file <fileName >| -exclude_pin_file <fileName>?",
        ),
        # man1/lib_build_asynch_de_assert_arc.1
        _syn(
            "lib_build_asynch_de_assert_arc",
            "",
            "lib_build_asynch_de_assert_arc {true | false}",
        ),
        # man1/lineSelect.1
        _syn(
            "lineSelect",
            "Selects all objects that fall across the specified line coordinates",
            "lineSelect ?-help? <mode> <ux1><uy1><ux2><uy2>",
        ),
        # man1/list_gui_marker.1
        _syn(
            "list_gui_marker",
            "Gives a list of GUI markers in the design layout",
            "list_gui_marker",
        ),
        # man1/list_libraries.1
        _syn(
            "list_libraries",
            "Lists all the libraries loaded in the session and used in the design",
            "list_libraries ?-help? ?-power_domain <<string>>? ?-used? ?-used_analysis? ?-view <<string>>?",
        ),
        # man1/list_property.1
        _syn(
            "list_property",
            "Lists all of the properties associated with the specified object type",
            "list_property ?-help? ?-type {cell clock design lib lib_cell lib_pin lib_timing_arc net path_group pin port timing_arc timing_path timing_point pg_net pg_pin lib_pg_pin si_victim si_attacker}?",
        ),
        # man1/lminus.1
        _syn(
            "lminus",
            "Subtracts the specified elements in the second list (list2) from the first specified list (list1)",
            "lminus ?-exact? <list1> <list2>",
        ),
        # man1/load_netlist_ignore_undefined_cell.1
        _syn(
            "load_netlist_ignore_undefined_cell",
            "",
            "load_netlist_ignore_undefined_cell { 1 | 0 }",
        ),
        # man1/load_path_categories.1
        _syn(
            "load_path_categories",
            "Loads the path category file in the Timing Debug form",
            "load_path_categories ?-help? -filename <filename>",
        ),
        # man1/load_timing_debug_report.1
        _syn(
            "load_timing_debug_report",
            "Loads the violation report in Innovus for debugging timing results",
            "load_timing_debug_report ?-help? ?-name report_name? ?{-proto ?-additional_slack_past_wns <number>? ?-num_path <number>?}? ?-num_path? <filename>",
        ),
        # man1/loadBlackBoxNetlist.1
        _syn(
            "loadBlackBoxNetlist",
            "Loads a netlist for a black box",
            "loadBlackBoxNetlist ?-help? <netlist>",
        ),
        # man1/loadDefFile.1
        _syn(
            "loadDefFile",
            "Reads a DEF file to build the in-memory database in Innovus",
            "loadDefFile ?-help? <defFile> ?-hier ?-stub <stubfile> | -reflib {<listOfRefLibs>}??",
        ),
        # man1/loadDrc.1
        _syn(
            "loadDrc",
            "Loads the specified Design Rule Checking (DRC) violation marker file",
            "loadDrc ?-help? <fileName> ?-incremental? ?-orient {r0 | r90 | r180 | r270 | mx | mx90 | my | my90}? ?-origin <x y>?",
        ),
        # man1/loadECO.1
        _syn(
            "loadECO",
            "Reads a file containing ECO directives and applies the changes to the current netlist",
            "loadECO ?-help? ?-postMask | -useGACells <GACoreSiteName>? ?-suffix <suffix>? ?-verbose? <fileName ... >",
        ),
        # man1/loadFootPrint.1
        _syn(
            "loadFootPrint",
            "Loads a footprint file to update the footprint information, which is obtained from the timing library file during design import",
            "loadFootPrint ?-help? -infile <fileName>",
        ),
        # man1/loadFPlan.1
        _syn(
            "loadFPlan",
            "Loads a floorplan file",
            "loadFPlan",
        ),
        # man1/loadIoFile.1
        _syn(
            "loadIoFile",
            "Loads an I/O assignment file",
            "loadIoFile ?-help? <file_name> ?-noAdjustDieSize? ?-specifiedIosOnly? ?-ECO ?-padsOnly | -bumpsOnly??",
        ),
        # man1/loadLefFile.1
        _syn(
            "loadLefFile",
            "Imports all the technology and library data that is specified in the LEF files into the Innovus environment",
            "loadLefFile ?<file1 file2 ...>?< > ?-help? ?-areaIo? ?-blackbox? ?-incremental?",
        ),
        # man1/loadPtnPin.1
        _syn(
            "loadPtnPin",
            "Loads either a partition floorplan file (from a saved partition design session) or a DEF file, and then dis‐ plays the preassigned I/O pins for the partition",
            "loadPtnPin ?-help? ?-report <string>? ?-snapModifiedToBoundary? {-ptnName <string> | -all} {-file <string >| -def <string>}",
        ),
        # man1/loadSpecialRoute.1
        _syn(
            "loadSpecialRoute",
            "Loads the spr file generated through the saveSpecialRoute command",
            "loadSpecialRoute ?-help? <filename>",
        ),
        # man1/loadViolationReport.1
        _syn(
            "loadViolationReport",
            "Loads a violation marker file or a hotspot interface format (HIF) file in one of the following for‐ mats and creates markers that the Innovus software can interpret",
            "loadViolationReport ?-help? -filename <fileName> ?-orient {<r0 r90> ...}? ?-rulemap <mapName>? -type {Assura | Calibre | PVS | Hercules | ICV | CDNLitho | CDNCMP | inShapeLitho | CalibreLitho | DRV | ClockTran | CLP | VerifyPower} ?-xoffset <value>? ?-yoffset <value>?",
        ),
        # man1/loadWorkspace.1
        _syn(
            "loadWorkspace",
            "Loads the named workspace from the specified directory",
            "loadWorkspace ?-help? -name <workspaceName> ?-dir <directory>?",
        ),
        # man1/man.1
        _syn(
            "man",
            "",
            "man <command_name> | <msg_id>",
        ),
        # man1/map_activity_file.1
        _syn(
            "map_activity_file",
            "",
            "map_activity_file ?-help? ?-golden {rtl | gate}? ?-gate_block <block_name>? ?-reset? -rtl2gate <mapping_file> ?-rtl_block <block_name>? ?-two_column_mapping_file<mapping_file>?",
        ),
        # man1/map_die_package.1
        _syn(
            "map_die_package",
            "The command launches the MCP Editor GUI to make manual connections between package and die pins",
            "map_die_package ?-help? ?-output <directory>? -package_model_file <filename> {-die_mcp_header <filename> | -net_pad_file_pair {{<<net1>> <<pad file1>>} {<<net2>> <<pad file2>>}...}}",
        ),
        # man1/map_dies.1
        _syn(
            "map_dies",
            "A utility to generate the inter die data mapping file based on the design stack configuration file and die ploc files",
            "map_dies ?-help? -3dic_design_stack_file< filename>?-component_config_file<filename>? ?-die_pad_file_pair {{<<die_name1>> <<pad file1>>} {<<die_name1>> <<pad file2>>}...}? ?-map_search_distance <distance>? ?-mode sanity_check? ?-output <directory>? ?-stacked_die_mapping <filename>?",
        ),
        # man1/mark_physical_power_domains.1
        _syn(
            "mark_physical_power_domains",
            "Marks the physical power domains that need fences in case the power domains share the same primary supply net and the available supply net setting (if specified)",
            "mark_physical_power_domains ?-help? {-domains <physical_domain_list> | -reset | -checkOnly} ?-groupPhyLogicalDomains {{<phyPd lpd1 lpd2> ...} ...}?",
        ),
        # man1/merge_clock_cells.1
        _syn(
            "merge_clock_cells",
            "When specified without any parameters, the command merges both clock gates and clock logic",
            "merge_clock_cells ?-help? ?-only_above_flops? ?-only_clock_gates? ?-only_clock_logics?",
        ),
        # man1/merge_hierarchical_def.1
        _syn(
            "merge_hierarchical_def",
            "Merges DEF data from various blocks to a single chip database",
            "merge_hierarchical_def ?-help? <defFiles <...>> ?-add_blockage? ?-delete_blockages_over_partition_macro? ?-ignore_drcfill? ?-incremental_ilm_def? ?-preserve_shape? ?-rdl_def <string>? ?-rdl_orientation <orientation>? ?-rdl_placement {<x y>}? ?-secondary {{<suffix> <def_file_list>}...}? ?-skipNets? ?-skip_filler? ?-skip_pg? ?-skip_routing {?pg|signal? ?regular|special? ?high_layer_routing?}? ?-to_layer <routing_layer_name>? ?-top_scope? ?-topcell_orientation <orientation>? ?-topcell_placement {x y}? ?-transform_file <string>? ?-use_top_def_die_area?",
        ),
        # man1/merge_model_timing.1
        _syn(
            "merge_model_timing",
            "Merges extracted timing models (ETM) for various analysis views into a single output",
            "merge_model_timing ?-help? ?-keep_separate_arc? -library_file <string> -mode_group <string> -modes <string> ?-outfile <string>? ?-pin_cap_tolerance <float>? ?-tolerance <float>?",
        ),
        # man1/merge_multi_port_to_single_port.1
        _syn(
            "merge_multi_port_to_single_port",
            "",
            "merge_multi_port_to_single_port {true | false}",
        ),
        # man1/merge_pg_library.1
        _syn(
            "merge_pg_library",
            "Specifies to merge power-grid libraries",
            "merge_pg_library ?-help? ?-force {true | false}? -library_list_file <file_name> ?-library_prefix <prefix>? ?-merge_single_voltage_pgvs {true |false}? ?-output <directory><_name>? ?-remove_tech{true | false}? ?-validate_rail_merge {true | false}?",
        ),
        # man1/merge_vtm.1
        _syn(
            "merge_vtm",
            "",
            "merge_vtm ?-help? -config <filename> ?-rundir <directory>? ?-merged_file <filename>? ?-format {simple | metal | stack}?",
        ),
        # man1/metric_advanced_url_endpoint.1
        _syn(
            "metric_advanced_url_endpoint",
            "",
            "metric_advanced_url_endpoint <value>",
        ),
        # man1/metric_capture_3d_hotspots.1
        _syn(
            "metric_capture_3d_hotspots",
            "",
            "metric_capture_3d_hotspots {true | false}",
        ),
        # man1/metric_capture_depth.1
        _syn(
            "metric_capture_depth",
            "",
            "metric_capture_depth <integer>",
        ),
        # man1/metric_capture_design_image.1
        _syn(
            "metric_capture_design_image",
            "",
            "metric_capture_design_image <string>",
        ),
        # man1/metric_capture_design_image_blockages.1
        _syn(
            "metric_capture_design_image_blockages",
            "",
            "metric_capture_design_image_blockages {true | false}",
        ),
        # man1/metric_capture_design_image_blockages_threshold.1
        _syn(
            "metric_capture_design_image_blockages_threshold",
            "",
            "metric_capture_design_image_blockages_threshold <threshholdValue>",
        ),
        # man1/metric_capture_design_image_power_intent.1
        _syn(
            "metric_capture_design_image_power_intent",
            "",
            "metric_capture_design_image_power_intent {true | false}",
        ),
        # man1/metric_capture_design_image_route_drc.1
        _syn(
            "metric_capture_design_image_route_drc",
            "",
            "metric_capture_design_image_route_drc {true | false}",
        ),
        # man1/metric_capture_max_drc_markers.1
        _syn(
            "metric_capture_max_drc_markers",
            "",
            "metric_capture_max_drc_markers <max_number>",
        ),
        # man1/metric_capture_min_count.1
        _syn(
            "metric_capture_min_count",
            "",
            "metric_capture_min_count <integer>",
        ),
        # man1/metric_capture_overwrite.1
        _syn(
            "metric_capture_overwrite",
            "",
            "metric_capture_overwrite {true | false}",
        ),
        # man1/metric_capture_pba_tns_histogram.1
        _syn(
            "metric_capture_pba_tns_histogram",
            "",
            "metric_capture_pba_tns_histogram {true | false}",
        ),
        # man1/metric_capture_per_view.1
        _syn(
            "metric_capture_per_view",
            "",
            "metric_capture_per_view {true | false}",
        ),
        # man1/metric_capture_reg2reg_metrics.1
        #   WARNING: bracket mismatch: '[' at position 31 closed by '}' at position 44
        _syn(
            "metric_capture_reg2reg_metrics",
            "",
            "metric_capture_reg2reg_metrics ?true | false}",
        ),
        # man1/metric_capture_timing_analysis_mode.1
        _syn(
            "metric_capture_timing_analysis_mode",
            "",
            "metric_capture_timing_analysis_mode {gba | ipba} Type: Enum<Default>: gba",
        ),
        # man1/metric_capture_timing_path_groups.1
        _syn(
            "metric_capture_timing_path_groups",
            "",
            "metric_capture_timing_path_groups <path_group>",
        ),
        # man1/metric_capture_timing_paths.1
        _syn(
            "metric_capture_timing_paths",
            "",
            "metric_capture_timing_paths <integer>",
        ),
        # man1/metric_capture_tns_histogram.1
        _syn(
            "metric_capture_tns_histogram",
            "",
            "metric_capture_tns_histogram {true | false}",
        ),
        # man1/metric_capture_tns_histogram_buckets.1
        _syn(
            "metric_capture_tns_histogram_buckets",
            "",
            "metric_capture_tns_histogram_buckets <integer>",
        ),
        # man1/metric_capture_tns_histogram_max_slack.1
        _syn(
            "metric_capture_tns_histogram_max_slack",
            "",
            "metric_capture_tns_histogram_max_slack <maximum_slack_value>",
        ),
        # man1/metric_capture_tns_histogram_paths.1
        _syn(
            "metric_capture_tns_histogram_paths",
            "",
            "metric_capture_tns_histogram_paths <integer>",
        ),
        # man1/metric_capture_vth_metrics.1
        #   WARNING: bracket mismatch: '[' at position 27 closed by '}' at position 40
        _syn(
            "metric_capture_vth_metrics",
            "",
            "metric_capture_vth_metrics ?true | false}",
        ),
        # man1/metric_capture_vth_per_power_domain.1
        #   WARNING: bracket mismatch: '[' at position 36 closed by '}' at position 49
        _syn(
            "metric_capture_vth_per_power_domain",
            "",
            "metric_capture_vth_per_power_domain ?true | false}",
        ),
        # man1/metric_category_default.1
        _syn(
            "metric_category_default",
            "",
            "metric_category_default <metric_category>",
        ),
        # man1/metric_current_run_id.1
        _syn(
            "metric_current_run_id",
            "",
            "metric_current_run_id",
        ),
        # man1/metric_enable.1
        _syn(
            "metric_enable",
            "",
            "metric_enable {true | false}",
        ),
        # man1/metric_summary_metrics.1
        _syn(
            "metric_summary_metrics",
            "",
            "metric_summary_metrics",
        ),
        # man1/modify_ccopt_skew_group.1
        _syn(
            "modify_ccopt_skew_group",
            "This command is used internally to add or remove sinks in existing skew groups produced automat‐ ically by the create_ccopt_skew_group command, but you can also use it to modify existing skew_group objects",
            "modify_ccopt_skew_group ?-help? ?-make_exclusive? -skew_group <skew_group_name> ?-add_sinks pins | -remove_sinks pins? ?-add_ignore_pins <pins> | -remove_ignore_pins <pins>?",
        ),
        # man1/modify_ndr.1
        _syn(
            "modify_ndr",
            "Modifies a non-default rule created by the add_ndr command, or coming in from DEF or the OpenAccess design data",
            "modify_ndr ?-help? ?-add_via {<via_name1 via_name2 ...>}? ?-generate_via? ?-hard_spacing {0|1}? ?-min_cut {<layer1>?:<layer2>? <min_cut ...>}? -name <ruleName> ?-spacing {<layer1>?:<layer2>? <spacing> ...}? ?-use_via_cut_class <string>? ?-via {<via_name1 via_name2> ...}? ?-width {<layer1>?:<layer2>? <width> ...}?",
        ),
        # man1/modifyBudget.1
        _syn(
            "modifyBudget",
            "Modifies budgets after they have been saved using the saveTimingBudget command",
            "modifyBudget {-ptn <partitionName> | -inst <instanceName>} -file <fileName> ?-setup | -hold? ?-view <viewName>? ?-help?",
        ),
        # man1/modifyPipelineNetGroup.1
        _syn(
            "modifyPipelineNetGroup",
            "Modifies the existing net group attributes or converts an existing net group added during floor‐ planning to be of type pipeline",
            "modifyPipelineNetGroup",
        ),
        # man1/modifyPowerDomainAttr.1
        _syn(
            "modifyPowerDomainAttr",
            "Renames a power domain or changes its structure",
            "modifyPowerDomainAttr ?-help? ?-addBlockBox <string>? ?-core2Left <valueInMicron>? ?-core2Right <valueInMicron>? ?-core2Top <valueInMicron>? ?-core2Bot <valueInMicron>? ?-defaultTechSite <string>? ?-disjointHInstBoxList <string>? ?-extraRowPattern {<rowPatternSiteName>...}? ?-firstRowSiteIndex <integer>? ?-lastRowSiteIndex <integer>? ?-minGaps {values}|-gapEdges {values}? <powerDomainName> ?-rowFlip {first second noflip auto}? ?-rowPatternSite <site_name>? ?-rowSpaceType {0 1 2}? ?-rowSpacing <float>? ?-rsExts {values}|-extEdges {values}?",
        ),
        # man1/monitor_hosts.1
        _syn(
            "monitor_hosts",
            "",
            "monitor_hosts ?-help? ?-log <string>? ?-overwrite? ?-period <integer>?",
        ),
        # man1/move_obj.1
        _syn(
            "move_obj",
            "Moves objects (instances, modules, groups, placement blockage, routing blockage, hard macros, special routings, I/O pins, and GUI shapes) vertically or horizontally by a specified distance",
            "move_obj ?-help? ?-group? { -point {x y} | { -direction {up down left right} { -distance value | -to {core_box die_box} }}} { <obj_list> | -selected }",
        ),
        # man1/moveGroupPins.1
        _syn(
            "moveGroupPins",
            "Changes the pin layer, the pin size, pin status, resolves pin overlap, and moves a selected pin or pin group to a specific location",
            "moveGroupPins ?-help? ?-depth <float>? ?-end_location {<x y>}? ?-expand_spacing_factor <float>? ?-layer <string>? -loc {<x y>} ?-moveOnLayer <string>? ?-noFixed? ?-spacing <float>? ?-spread_type <string>? ?-start_location {<x y>}? ?-width <float>? ?-withOverlap?",
        ),
        # man1/moveMacroInsideModule.1
        _syn(
            "moveMacroInsideModule",
            "Moves all hard macros that belong to the specified module into its boundary",
            "moveMacroInsideModule ?-help? {-hInst {hinstName(s)} | -all}",
        ),
        # man1/movePowerSwitch.1
        _syn(
            "movePowerSwitch",
            "The command is used to move power switch instances by offset value in X or Y direction",
            "movePowerSwitch ?-help? ?-area {x1 y1 x2 y2}? ?-columnx <string>? ?-fixOverlap? ?-honorSoftBlockage? ?-powerDomain <string>? ?-reportFile <string>? ?-selected? ?-switchInstances <string>? ?-xOffset <float>? ?-yOffset <float>?",
        ),
        # man1/moveSdpObject.1
        _syn(
            "moveSdpObject",
            "Moves specified SDP objects before or after the specified reference object",
            "moveSdpObject ?-help? <moveObject >{<objName> <s>} {-before <refObject> | -after <refObject>}",
        ),
        # man1/mustjoinallports_is_one_pin.1
        _syn(
            "mustjoinallports_is_one_pin",
            "",
            "mustjoinallports_is_one_pin {true | false}",
        ),
        # man1/nagelfar.1
        _syn(
            "nagelfar",
            "",
            "nagelfar ?<nagelfar.tcl options>? ?file1.tcl file2.tcl …?",
        ),
        # man1/oa2lef.1
        _syn(
            "oa2lef",
            "This translator can be used to convert OpenAccess data into equivalent LEF data",
            "oa2lef -lef <file> -lib <library> ?-cell cells? ?-h | -help? ?-libDefFile <filename>? ?-lockedColorsOnly? ?-logFile <file>? ?-noInfo <msgIds>? ?-noTech? ?-noWarning <msgIds>? ?-templateFile <file>? ?-useFoundryInnovus? ?-views <viewName>? ?-v? ?-ver <version>? ?-version?",
        ),
        # man1/oaIn.1
        _syn(
            "oaIn",
            "Restores floorplan, placement, and routing data using the OpenAccess format",
            "oaIn ?-help? <lib> <cell> <view> ?-filter {block_insts blockages boundary fixed_core_insts floorplan pad_insts pin_shapes regions regular_routing spe‐ cial_routing bump_insts}? ?-net {<netnames>}?",
        ),
        # man1/oaOut.1
        _syn(
            "oaOut",
            "Saves floorplan, placement, and routing data in the OpenAccess format",
            "oaOut ?-help? <lib> <cell> <view> ?-autoRemaster? ?-copyTechFromReflib? ?-cutRows? ?-early_global_route? ?-leafViewNames {<lefView1 lefView2 ...>}? ?-noConnectivity ?-noStdCells?? ?-noOverwriteAbstract? ?-refLibs {<refLib1 refLib2 ...>}?",
        ),
        # man1/open_gtd.1
        _syn(
            "open_gtd",
            "Opens the global timing debugger for accessing the GTD files report",
            "open_gtd ?-help?",
        ),
        # man1/open_schematic.1
        _syn(
            "open_schematic",
            "Opens the schematic view of the specified or selected objects",
            "open_schematic ?-help? ?-name <string>? ?-objects <<inst | net | instTerm | term | hinst>>+ | -selected? ?-type {module cone}?",
        ),
        # man1/optDesign.1
        _syn(
            "optDesign",
            "Performs timing optimization before or after the clock tree is built, or after routing and generates timing reports",
            "optDesign ?-help? ?-drv? ?-excludeNets <fileName>? ?-expandedViews? ?-hold ?-holdVioData <fileName>?? ?-idealClock? ?-incr? ?-noEcoRoute? ?-outDir <directoryName>? ?-preCTS | -postCTS | -postRoute? ?-prefix <fileNamePrefix>? ?-selectedNets <fileName>? ?-selectedTerms <fileName>? ?-setup? ?-targeted? ?-timingDebugReport? ?-useTransitionFiles?",
        ),
        # man1/optimizePattern.1
        _syn(
            "optimizePattern",
            "Runs LPA on the selected design to flag Litho hotspots",
            "optimizePattern ?-help? ?-backout <string>? ?-check_locally? ?-config <string>? ?-create? ?-deck <string>? ?-dir <string>? ?-envLayers <string>? ?-exclude <string>? ?-excludeHalo <string>? ?-extract? ?-extractHalo <string>? ?-extractSquish? ?-find? ?-findLimit <string>? ?-fix? ?-fixLimit <string>? ?-gdsList <string>? ?-hintsOnly? ?-include <string>? ?-incrCheck <string>? ?-input <string>? ?-layerMapFile <string>? ?-layers <string>? ?-load? ?-mapFile <string>? ?-markerLayers <string>? ?-markers <string>? ?-noCompress? ?-noViolationBrowser? ?-oasis? ?-oasisList <string>? ?-save? ?-selection <string>? ?-streamOutOptions <string>? ?-techFile <string>? ?-verify_function <string>?",
        ),
        # man1/optPower.1
        _syn(
            "optPower",
            "Optimizes the power consumption of the design by swapping gates for those with lower power, or deleting buffers/inverters without degrading timing",
            "optPower ?-help? ?-allowResizing? ?-effortLevel {high}? ?-force? ?-preCts | -postCts | -postRoute? ?-prePlace? ?-seqOnly?",
        ),
        # man1/optVirtual.1
        _syn(
            "optVirtual",
            "This command is based on the gigaOpt infrastructure and it provides prototyping capability at several steps of the hierarchical flow to specify and refine the top-level timing constraints and floorplan",
            "optVirtual ?-help? ?-outDir <dirName>? ?-timingReports?",
        ),
        # man1/pack_align_macros.1
        _syn(
            "pack_align_macros",
            "Pushes macros (or pack of macros) to core corners and marks them fixed",
            "pack_align_macros ?-help?",
        ),
        # man1/pack_module_model_libs.1
        _syn(
            "pack_module_model_libs",
            "Packs libraries for the Integrated Hierarchical Database (iHDB) flow designs",
            "pack_module_model_libs ?-help? ?-cell <cell_name>? ?-only_files <string>? ?-validate?",
        ),
        # man1/pan.1
        _syn(
            "pan",
            "Specifies that the new center of the viewing window should shift from the current center of the viewing window by (<x>, <y>) microns",
            "pan ?-help? <dx> <d><y> Specifies that the new center of the viewing window should shift from the current center of the viewing window by (<x>, <y>) microns. Use this command at any stage in the design flow to pan or move the design view in a specific direction.",
        ),
        # man1/panCenter.1
        _syn(
            "panCenter",
            "Pans in the viewable window to the center point defined by the specified coordinates",
            "panCenter ?-help? <x y>",
        ),
        # man1/panPage.1
        _syn(
            "panPage",
            "Pans the viewable window in pages defined by the offsets",
            "panPage ?-help? <x><y>",
        ),
        # man1/parse_proc_arguments.1
        _syn(
            "parse_proc_arguments",
            "Supports argument validation within a Tcl procedure and enables the use of the -help option to view the help information associated with the procedure",
            "parse_proc_arguments ?-help? <result_array> ?<forced_proc>? -args <string>",
        ),
        # man1/partition.1
        _syn(
            "partition",
            "Converts the specified module fences to be partitions, pushes down the physical cells or power routing infor‐ mation to the partition level design(s), and duplicates strips in the partition that overlap with the partition boundary at their original widths",
            "partition ?-help? ?<partitionName> {list}? ?-addPinForPGWireLayersInDistance {{<layer_name1 distance1>} {l<ayer_name2 distance2>}}? ?-inputNetsForWireDistribution <filename>? ?-noTopPushDown? ?-noViaCutSpace? ?-pgPushDownHonorUPF? ?-pushAllRoutes? ?-pushDownHonorInsidePinForSpecialNet? ?-pushDownSelectedPGWiresAsRouteBlockage? ?-pushDownSpecialNetAsObs {<SNet list>}? ?-skipRouteBlockagesOutsidePartition? ?-pinCutSpace? ?-noInheritPhysical? ?-pushRoute? ?-pushdownAllBumps | -pushDownSelectedPGBump?",
        ),
        # man1/partitionPushSpecialWires.1
        _syn(
            "partitionPushSpecialWires",
            "Note: For pushdown of special wires in master and clone partitions, it checks for the symmetry of the special wire shapes",
            "partitionPushSpecialWires ?-help? ?-checkOnly? {-nets <list_of_net_names> | -overlappingPartitions <ptn_names>}",
        ),
        # man1/pasteObject.1
        _syn(
            "pasteObject",
            "Pastes copied placement or routing blockages at the specified location",
            "pasteObject ?-help? ?-loc {<x y>}?",
        ),
        # man1/pinAlignment.1
        _syn(
            "pinAlignment",
            "Aligns pins between blocks on their facing edges",
            "pinAlignment ?-help? ?-ignore_ref_pin_shape? ?-markFixed? ?-moveFixedPin? ?-keepLayer | -newLayer <layer>? ?-legalizePin? ?-noSnap? ?-pinNames <pinList>? ?-ptnInst <ptnName>? ?-refObj <refObjName>? ?-refType {partition_pin hinst}? ?-verbose?",
        ),
        # man1/pinAnalysis.1
        _syn(
            "pinAnalysis",
            "Reports certain Quality of Results (QoR) metrics for pin assignment",
            "pinAnalysis ?-help? ?-checkLegality? ?-outFile <fileName>? ?-noHtml?",
        ),
        # man1/place_cells_at_center_for_feedthrus.1
        _syn(
            "place_cells_at_center_for_feedthrus",
            "Places all the instances corresponding to a given partition and its top interface cells at the center to facilitate feedthrough insertion in the flow during the floorplanning stage",
            "place_cells_at_center_for_feedthrus ?-help? ?-insts <list_of_selected_insts>? ?-skipTopInsts?",
        ),
        # man1/place_connected.1
        _syn(
            "place_connected",
            "Places the specified standard cells close to the specified attractor with legal location",
            "place_connected ?-help? -attractor <macro/IO list> ?-fixed? ?-move_fixed? ?-placed? {-level <integer> | -sequential all_connected | direct_connected | -stop_points <instance_name> | -before_points <in‐ stance_name> | -instance_pin <instance/pin>} ?{ -stop_points <instance_name> | -key_cell <cell_name> }? ?{ -instance_pin <instance/pin> | -key_cell <cell_name> }? ?{ -attractor_pin <pin_list> } ?-instance_pin <instance/pin>??",
        ),
        # man1/place_design.1
        _syn(
            "place_design",
            "Places standard cells based on the global settings for placement, RC extraction, timing analysis, and early global routing",
            "place_design ?-help? ?-concurrent_macros? ?-incremental? ?-noPrePlaceOpt? ?-sdp?",
        ),
        # man1/place_opt_design.1
        _syn(
            "place_opt_design",
            "",
            "place_opt_design ?-help? ?-expanded_views? ?-incremental? ?-incremental_timing? ?-num_paths <number_of_paths>? ?-out_dir <outputDirectory>? ?-predict_prects? ?-prefix <outputFileName>? ?-timing_debug_report?",
        ),
        # man1/place_partition_clone.1
        _syn(
            "place_partition_clone",
            "Places the clones, set their orientation and syncs up the data with other hierarchical instances (master and clones) of the same module",
            "place_partition_clone ?-help? -hinst <partition_clone_hinst_name> -location {<x y>} ?-orient {R0 R180 MX MY}? ?-skip_sync? ?-sync_objs {placeBlockage routeBlockage pinBlockage macros fences}?",
        ),
        # man1/placeAIO.1
        _syn(
            "placeAIO",
            "Places I/O driver cells",
            "placeAIO ?-help? ?-onlyAIO? ?-assignBump? ?-maxDistance <distance>? ?-fast? ?-packing? ?-ignoreAIOByName {<list>}? ?-ignoreAIOByCellName {<list>}? ?-hardFence?",
        ),
        # man1/placeBondPad.1
        _syn(
            "placeBondPad",
            "Places a bond pad on a specified I/O instance",
            "placeBondPad ?-help? {-ioInstName <instName> | -selected} ?-pad <padName>? ?-pinName <pinName>? ?-position {i | m | o}? ?-fix?",
        ),
        # man1/placeCursor.1
        _syn(
            "placeCursor",
            "Places the cursor at the specified location in the main window",
            "placeCursor ?-help? <x><y>",
        ),
        # man1/placeInstance.1
        _syn(
            "placeInstance",
            "Places a leaf instance in the core box",
            "placeInstance ?-help?",
        ),
        # man1/placeJtag.1
        _syn(
            "placeJtag",
            "Places JTAG cells",
            "placeJtag ?-help? -nrRow <nrRow> ?-nrRowTop <nrRowTop>? ?-nrRowBottom <nrRowBottom>? ?-nrRowLeft <nrRowLeft>? ?-nrRowRight <nrRowRight>? ?-hardMacro {true | false}? ?-areaIo {true | false}? ?-ioNetWeight <netWtValue>? ?-blockNetWeight <netWtValue>? ?-contour {true | false}? ?-ignoreScan {true | false}? ?-orientTop <orientation>? ?-orientBottom <orientation>? ?-orientLeft <orientation>? ?-orientRight <orientation>?",
        ),
        # man1/placePad.1
        _syn(
            "placePad",
            "Places an I/O pad instance",
            "placePad ?-help? <pad_name> ?<orientation>? <location >",
        ),
        # man1/placePadIO.1
        _syn(
            "placePadIO",
            "Places the I/O pads evenly from one row to multiple rows",
            "placePadIO ?-help? ?-rows <numOfRow>? ?-maxIOHeight?",
        ),
        # man1/placePIO.1
        _syn(
            "placePIO",
            "Places CLASS PAD AREA IO cells on the die boundary (periphery) in random order",
            "placePIO ?-help? ?-assignBump? ?-optIOs? ?-overflowMap? ?-maxIOHeight? ?-ioFile <fileName>? ?-rdlConstraintFile <fileName>? ?-noRandomPlacement? ?-extraConfig <fileName>? ?-cellList {<cellList>}? ?-instList {<instList>}? ?-powerDomain <powerDomainList>?",
        ),
        # man1/placePipeline.1
        #   WARNING: unclosed bracket '[' at position 69
        _syn(
            "placePipeline",
            "Places the registers of the specified pipeline flip-flops (PFF) net group(s) so that the distances between the stages of each group are roughly equal",
            "placePipeline ?-netGroup {<netGroupName>}? ?-region {true | false }? ?-status {fixed | placed} ?-timingBased? ?-utilization <utilization_value>?",
        ),
        # man1/placeSdpGroup.1
        _syn(
            "placeSdpGroup",
            "Places elements or instances of all defined SDP groups in row(s) and column(s) based on user-defined rela‐ tive placement information",
            "placeSdpGroup ?-help? ?-create_inst_group? ?-deleteOverlap {<cell...>} {<sdp name...>}? ?-sdpGroups {<name...>}? ?-noResolveOverlap | ?-keepSdpArea??",
        ),
        # man1/placeSpareModule.1
        _syn(
            "placeSpareModule",
            "Instantiates a created spare module, and places spare modules across the design",
            "placeSpareModule -moduleName <moduleName> {-numModules <integer |>-stepx <stepDistance> -stepy <stepDistance>} ?-area <llx lly urx ury>? ?-channel {-maxWidth <maxWidth>} {-minWidth <minWidth>} {-minLen <minLength>}? ?-offsetx <offsetDistance>? ?-offsety <offsetDistance>? ?-powerDomain <powerDomainName>? ?-prefix <prefix>? ?-util <utilizationFactor>?",
        ),
        # man1/power_integrity_place.1
        _syn(
            "power_integrity_place",
            "Calls Voltus to run irdrop analysis including power analysis, rail analysis, and debug IRdrop",
            "power_integrity_place ?-help?",
        ),
        # man1/predict_floorplan.1
        _syn(
            "predict_floorplan",
            "Generates an initial floorplan that can be used as a starting point for making the final floorplan",
            "predict_floorplan ?-help? ?-allow_illegal_macro? ?-enable_cpg? ?-reshape ??-post_reshape_tcl <string>??? ?{-reshape | -skip_generate_fence }?",
        ),
        # man1/prepareForEcoRoute.1
        _syn(
            "prepareForEcoRoute",
            "Converts special nets to geometrically equivalent regular nets",
            "prepareForEcoRoute ?-help? ?-exclude <net*>? ?-ignore_wire_status? ?-nets <net*>?",
        ),
        # man1/print_message.1
        _syn(
            "print_message",
            "Generates a message that is included in the report_message output if the message is designated as an error or a warning",
            "print_message",
        ),
        # man1/propagate_activity.1
        _syn(
            "propagate_activity",
            "",
            "propagate_activity ?-set_net_freq {true | false}?",
        ),
        # man1/proto_design.1
        _syn(
            "proto_design",
            "",
            "proto_design ?-help? ?-constraints <name>? ?-summary <file>_<name>?",
        ),
        # man1/pull_block_constraint.1
        _syn(
            "pull_block_constraint",
            "Pulls the routing constraints stored on the interface nets of blocks in a design, to their corre‐ sponding top-level nets",
            "pull_block_constraint ?-help? ?-file <report_file_name>? ?-override? {-all_blocks | -block <list_of_blocks> | -inst <list_of_instances> | -cellview {<list_of_libName_cellName_viewName>}}",
        ),
        # man1/push_ptn_network.1
        _syn(
            "push_ptn_network",
            "Pushes down a network (std cells and connected wires) logically and physically into overlapping parti‐ tions",
            "push_ptn_network ?-help? ?-exclude_ptn_list <ptnNameList>? ?-filter string? ?-inst_prefix <instPrefixName>? ?-logical_only? ?-net_prefix <netPrefixName>? ?-output_logical_only_nets string? ?-output_nets_for_wire_distribution <string>? ?-ptn_net_dir <fileName>? {-nets netNameList | -file <fileName> | -buf_only | -insts <instNameList> } ?-check_only ?-output<fileName>??",
        ),
        # man1/Puts.1
        _syn(
            "Puts",
            "",
            "Puts ?-help?",
        ),
        # man1/query_objects.1
        _syn(
            "query_objects",
            "Displays the names of the objects contained inside the specified collection",
            "query_objects ?-help? <collection> ?-limit <value>?",
        ),
        # man1/query_power_data.1
        _syn(
            "query_power_data",
            "The query_power_data command allows you to query the binary current files (.ptiavg/.ptipeak) that Power Calculation/Rail Analysis creates",
            "query_power_data ?-help? ?<<in_file> <<file1>?<file2>? ...>>? ?-average_current? ?-clock_average? ?-dump_pwl? ?-frame <<string>>? ?-instance_list <<inst_list>>? ?-instance_list_file <filename>? ?-list? ?-output <<string>>? ?-peak_current? ?-peak_time? ?-pin? ?-time_steps? ?-stdout? ?-total_current <<input_current_file>>? ?-output_tap_name <<tap_name>>?",
        ),
        # man1/queryDensityInBox.1
        _syn(
            "queryDensityInBox",
            "Outputs placement density for a specific area in the design",
            "queryDensityInBox <query_box>",
        ),
        # man1/queryFPlanObject.1
        _syn(
            "queryFPlanObject",
            "Prints the properties of selected objects to the console",
            "queryFPlanObject ?-help? ?-pd?",
        ),
        # man1/queryPinDensity.1
        _syn(
            "queryPinDensity",
            "Outputs pin density for the design",
            "queryPinDensity ?-help? ?-area <x1 y1 x2 y2>?",
        ),
        # man1/range_collection.1
        _syn(
            "range_collection",
            "Returns a sub-collection of the base collection",
            "range_collection ?-help? <base_collection> <from> <to>",
        ),
        # man1/rcOut.1
        _syn(
            "rcOut",
            "Reads the parasitic database and outputs the parasitics in the Standard Parasitic Exchange Format (SPEF)",
            "rcOut ?-help? ?-excludeIlm? ?-noRes? ?-useEEQCellWithLibertyInfo? {{{-spef <fileName>}?-excNetFile <fileName> | -net <fileName> | -netName <list_of_nets>?}} ?-view <viewName> | -rc_corner <rcCornerName>? ?-cUnit {pF fF}?",
        ),
        # man1/read_activity_file.1
        _syn(
            "read_activity_file",
            "Specifies the name and type of activity file to be used as input",
            "read_activity_file <name> ?-end {<time1 time2 ...timen>}? ?-format { VCD | TCF | SAIF | FSDB | PHY| SHM}? ?-hier_separator <separator>? ?-reset? ?-start {<time1 time2 ...timen>}? ?-set_net_freq {true | false}? ?-block <block_name>? ?-scope <scope_name>? ?-scale_duration <scalefactor>? ?-start_time_shift <value>? ?-rtl {true|false}? ?-name_mapping_rule <file>? ?-weight <value>? ?-zero_delay {true|false}? ?-cell <cell_name>?",
        ),
        # man1/read_codesign_die_abstract.1
        _syn(
            "read_codesign_die_abstract",
            "Reads the die abstract directly to update Innovus",
            "read_codesign_die_abstract ?-help?",
        ),
        # man1/read_design_stack_config.1
        _syn(
            "read_design_stack_config",
            "",
            "read_design_stack_config ?-help? ?-avoid_floorplan_change? ?-chipName <NameOfChip>? ?-manufacturing_grid <grid>? ?-power_config_file <PowerConnectionFile>? ?-topNetlist <VerilogFileName>? ?-xml <StackedDieFileName>?",
        ),
        # man1/read_ilm_eco_db.1
        _syn(
            "read_ilm_eco_db",
            "",
            "read_ilm_eco_db ?-help? {-dir <directoryName> | -module_model_tag <tagName>}",
        ),
        # man1/read_instance_obs.1
        _syn(
            "read_instance_obs",
            "Allows importing the OD shape (cell LEF) information and writes it in the specified output file",
            "read_instance_obs ?-help?",
        ),
        # man1/read_name_mapping.1
        _syn(
            "read_name_mapping",
            "Reads a name mapping file which records the mapping relationship between the original HDL (RTL bit level) names in Genus to the corresponding gate-level netlist names in Genus or Innovus for primary ports or reg/wire variables, and any logical phase inversions generated by Genus",
            "read_name_mapping ?-help? <in_file> ?-debug?",
        ),
        # man1/read_parallel_edit_files.1
        _syn(
            "read_parallel_edit_files",
            "Loads all the specified parallel edit files and implements the editing changes recorded in them",
            "read_parallel_edit_files ?-help? ?-check? ?-conflict_mode {only_one stop_all}? -files <list_of_files> ?-ignore_error? ?-report_file <file_name>?",
        ),
        # man1/read_parasitics.1
        _syn(
            "read_parasitics",
            "Reads the SPEF and RCDB-based RC parasitics information and information from the RCDBs already created in Innovus",
            "read_parasitics ?-help? ?-force? {?{{?-rc_corner <string>?}}?} ?-starN? ?-via_variation_file <viaVariationFile>?",
        ),
        # man1/read_path_descriptions.1
        _syn(
            "read_path_descriptions",
            "",
            "read_path_descriptions ?-help? <filename> ?-hpin? ?-path_type {end summary full full_clock end_slack_only summary_slack_only}? ?-retime {aocv ssta path_slew_propagation aocv_path_slew_propagation waveform_propagation}?",
        ),
        # man1/read_physical_context_data.1
        _syn(
            "read_physical_context_data",
            "Reads the physical context data needed for timing analysis",
            "read_physical_context_data ?-help? <fileName> ?-clear? ?-type <technologyName>?",
        ),
        # man1/read_power_intent.1
        _syn(
            "read_power_intent",
            "Reads-in power intent file and do syntax check",
            "read_power_intent ?-help? <fileName> {-cpf | -1801 | -msvDB }",
        ),
        # man1/read_power_rail_results.1
        _syn(
            "read_power_rail_results",
            "",
            "read_power_rail_results ?-help? ?-detail_delta_temperature_file <file>? ?-effective_resistance_file <file>? ?-instance_delta_temperature_file <file>? ?-power_db <file>? ?-rail_directory <dir>? ?-tile_delta_temperature_file <file>? ?-cell_library { <library1>.cl}? ?-force? ?-reset? ?-custom_value_inst_file_1<file>? ?-nets <net_names>? ?-instance_voltage_method { best | worst | avg | worstavg }? ?-instance_voltage_window { timing | whole }? ?-instances<instancenames>? ?-enable_plots <plot_names>? ?-sem_db <fil>e? ?-short_file <file>? ?-esd_directory <dir>? ?-thermal_file <filename>.txt? ?-esd_rj <dir>? ?-die_instance_name <dieinstname>? ?-data_type {rail | all}? ?-physical_db<dir_name>? ?-profiling_power_file <file>? ?-top_cell_name<topcell_name>? ?-tile_thermal_config_file<filename>? ?-power_directory <power_output_directory>?",
        ),
        # man1/read_safety_tmr.1
        _syn(
            "read_safety_tmr",
            "Reads the triple modular redundancy (TMR) information file",
            "read_safety_tmr ?-help? <tmr_info_file> -failure_mode <failure_mode_name> -safety_mechanism <safety_mechanism_name>",
        ),
        # man1/read_sai.1
        _syn(
            "read_sai",
            "",
            "read_sai ?-help? ?<name>? ?-partial? ?-reduce_by_flexfiller? ?-rule_only?",
        ),
        # man1/read_sdf.1
        _syn(
            "read_sdf",
            "Reads an OVI Standard Delay Format (SDF) file and annotates user-specified delay information from the SDF file into the timing system",
            "read_sdf ?-help? <sdf_file_name> ?-continue_on_error? ?-ilm_filter? ?-increment? ?-overwrite_incremental_delay? ?-path <instanceName>? ?-persistent? ?-print_summary? ?-scale <float>? ?-strict_cond_matching? ?-view <viewName>? ?-sdf_field {min|typ|max} | ?-early_sdf_field {min|typ|max}? ?-late_sdf_field {min|typ|max}??",
        ),
        # man1/read_spdf.1
        #   WARNING: bracket mismatch: '{' at position 10 closed by ']' at position 16
        _syn(
            "read_spdf",
            "Reads the statistical parameter distribution format (SPDF) file",
            "read_spdf {-help? <SPDF_file_name>",
        ),
        # man1/read_stream.1
        _syn(
            "read_stream",
            "Reads in-stream files or a layer map and outputs a summary of the cell names read in, and any layer/data types that have data with no map_file entry",
            "read_stream ?-help? -layer_map <layer_map_files> {?-pvs_fill? | ??<in_files>? ?-cells <cell_list> ?-offset {x y}???}",
        ),
        # man1/read_taf.1
        #   WARNING: unclosed bracket '[' at position 17
        _syn(
            "read_taf",
            "Applies additional attribute data from Genus for the user-managed exchanges",
            "read_taf ?-help? ?<filename> ?-quiet?",
        ),
        # man1/read_temperature_map_file.1
        _syn(
            "read_temperature_map_file",
            "Loads the tile-based temperature map file generated by Sigrity Celsius to be used for display‐ ing temperature",
            "read_temperature_map_file ?-help? -file <string>",
        ),
        # man1/read_twf.1
        _syn(
            "read_twf",
            "Reads the external timing window file (TWF) for noise (Signal Integrity) and power calculation (Common Power Engine - CPE)",
            "read_twf ?-help? ?<filenames>? ?-cell <string>? ?-prefix <string>? ?-quiet? ?-reset? ?-scope <string>? ?-skipconst? ?-skiptw? ?-strip_prefix <string>? ?-verbose? ?-view <string>?",
        ),
        # man1/read_usf.1
        _syn(
            "read_usf",
            "Reads in a Unified Safety Format (USF) file specifying the safety intent of your design",
            "read_usf ?-help? <USF_file>",
        ),
        # man1/readBumpLocation.1
        _syn(
            "readBumpLocation",
            "The command creates or assigns objects on the current die according to the bumps on the adjacent die",
            "readBumpLocation ?-help? <fileName> ?-allow_overlap_control {keep_all keep_existing_bumps keep_new_bumps}? ?-die_box? ?-ignore_route_blockages? ?-force_current_die? {?-frontBump <bumpCellName>? ?-backBump <backBumpCellName>? ?-bump_cell_from_bump_file?} ?{-backBump <backBumpCellName> | -bump_cell_from_bump_file } ?-rotate_bump -prefix <prefixName>?? ?{-frontBump <bumpCellName> | -bump_cell_from_bump_file }?-rotate_bump -prefix <prefixName>? ?-stackViaUnderBump <stack‐ ViaName>?? ?-prefix <prefixName> | -bump_name_from_bump_file {true | false}? ?-checkAlignment? ?-nonFeedthru? ?-feedthru? ?-tsvViaName <viaCellName> ?-feedthruSize <sizex sizey>? ?-offset {x y}??",
        ),
        # man1/readDieAbstract.1
        _syn(
            "readDieAbstract",
            "Reads the die abstract of the adjacent die",
            "readDieAbstract <DIEABSTRACTFILE>",
        ),
        # man1/readFlipChipProperty.1
        _syn(
            "readFlipChipProperty",
            "Reads the text file containing flip chip property information",
            "readFlipChipProperty ?-help? <fileName> ?-onlyBumpConnectTargetConstraint?",
        ),
        # man1/readIoUpdate.1
        _syn(
            "readIoUpdate",
            "Reads a simple ASCII file which contains the bump and instance information",
            "readIoUpdate ?-help? ?-checkOnly? <inputFile>",
        ),
        # man1/readPackage.1
        _syn(
            "readPackage",
            "Reads the package file dumped out by the System-in-Package (SiP) layout in XML format and displays the pack‐ age ball/finger location in the Innovus floorplan view",
            "readPackage ?-help? <packageFile>",
        ),
        # man1/readSdpFile.1
        _syn(
            "readSdpFile",
            "Reads in a relative placement file (in .sdp format) and then calls placeSdpGroup to place all the structured data path (SDP) elements defined in the file",
            "readSdpFile ?-help? -file <file_name> ?-hierPath <path>? ?-leftoverGroup? ?-origin <llx ><lly>? ?-skipPlacement?",
        ),
        # man1/readTransitionFile.1
        _syn(
            "readTransitionFile",
            "Reads external transition files that are used to perform maximum transition violation reporting and fixing",
            "readTransitionFile -file <fileName> ?-view <viewName>?",
        ),
        # man1/readTSVConfig.1
        _syn(
            "readTSVConfig",
            "Imports 3D IC configuration files of the whole design, including the stack die configuration file, power net configuration file and top-level netlist",
            "readTSVConfig {?-stackedDieFile <filename>? ?-powerFile <filename>?} ?-chipName <chipName>? ?-topNetlist?",
        ),
        # man1/readWriteLefCheckUncoloredShapes.1
        _syn(
            "readWriteLefCheckUncoloredShapes",
            "",
            "readWriteLefCheckUncoloredShapes {pin_only | on | off}",
        ),
        # man1/rechainPowerSwitch.1
        _syn(
            "rechainPowerSwitch",
            "Enables flexible power switch enable chaining and unchaining after power switch insertion",
            "rechainPowerSwitch ?-help? ?-backToBackChain? ?-cascade? ?-cellEnablePin? ?-chainByInstances? ?-chainByRow? ?-chainDirectionX <LtoR>|<RtoL>? ?-chainDirectionY <BtoT>|<TtoB>? ?-chainStyle {min_length_tree single_output_chain}? ?-chainXbeforeY? ?-chainYbeforeX? ?-enableNetIn? ?-enableNetOut? ?-enablePinIn? ?-enablePinOut? ?-maxDistanceX <um>? ?-maxDistanceY <um>? ?-mergeDistanceX <um>? ?-mergeDistanceY <um>? ?-parallelEnable? ?-reportFile? ?-reverseOrder? ?-selected? ?-start_location <coordinates>? ?-switchInstances? ?-unchainByInstances?",
        ),
        # man1/reclaimArea.1
        _syn(
            "reclaimArea",
            "Creates space in the design by downsizing and deleting buffers, without worsening the slack or increasing the design rule violations",
            "reclaimArea ?-help? ?-noDeclone? ?-noDeleteBuffer? ?-noDownsize? ?-maintainHold?",
        ),
        # man1/recreatePtnCellBlockage.1
        _syn(
            "recreatePtnCellBlockage",
            "Recreates cell blockage for a specified partition, or all partitions",
            "recreatePtnCellBlockage ?-help? ?<ptnName>? ?-noPinCutSpace | -hasPinCutSpace? ?-noViaCutSpace | -hasViaCutSpace?",
        ),
        # man1/redirect.1
        _syn(
            "redirect",
            "Redirects the output to a file or variable",
            "redirect ?-help? ?<file_or_var_name>? ?<command>? ?-tee? ?-stdin | -append? ?-stdin | -variable? ?-variable? ?-stderr | -stdin?",
        ),
        # man1/redo.1
        _syn(
            "redo",
            "Returns the design to the state it was in immediately prior to issuing the undo command",
            "redo ?-help?",
        ),
        # man1/redraw.1
        _syn(
            "redraw",
            "Refreshes the display in the viewable window",
            "redraw ?-help?",
        ),
        # man1/refine_macro_place.1
        _syn(
            "refine_macro_place",
            "Legalizes the macros based on constraints such as halo and blockages, forbidden spacing, min-space, etc",
            "refine_macro_place ?-help? ?-verbose?",
        ),
        # man1/refineMacro.1
        #   WARNING: unmatched closing bracket ']' at position 170
        _syn(
            "refineMacro",
            "Refines the placement of macros in the floorplan",
            "refineMacro ?-help? {{-area {x1 y1 x2 y2} ?-selected?}| -permutePack | -markStep | -restoreStep <step_number> |-restoreMark <mark_number>} ?-adjustPack? ?-ioPinClearance??",
        ),
        # man1/refinePlace.1
        _syn(
            "refinePlace",
            "Corrects flawed cell locations and reports corrections or instance overlap problems",
            "refinePlace ?-help? ?-area {lx ly ux uy}? ?-eco {true|false}? ?-inst <list_of_instances>? ?-wire_length_reclaim {true|false}?",
        ),
        # man1/register_gui_edit_callback.1
        _syn(
            "register_gui_edit_callback",
            "Adds the callback function to the specified move action",
            "register_gui_edit_callback ?-help? -command <string> -edit_type {selection pre-move post-move}",
        ),
        # man1/registerTrigger.1
        _syn(
            "registerTrigger",
            "Registers the -pre or -post callback procedures with the specified commands",
            "registerTrigger ?-help? ?{-pre | -post} <commandName> <procName>?",
        ),
        # man1/reinforce_pg.1
        _syn(
            "reinforce_pg",
            "Reinforces PG stripes between the existing original PG stripes in Innovus to fix the IR drop violations re‐ ported from Voltus",
            "reinforce_pg ?-help? ?-area {<x1 y1 x2 y2>}? ?-area_blockage {{<x1 y1 x2 y2>} {<x1 y1 x2 y2 x3 y3 x4 y4> ...} ...}? ?-pattern_file <file_name>? ?-snap_wire_center_to_grid {default | Grid}? {-pattern_map {{<irdrop_value1> <pattern_name1>} {<irdrop_value2> <pattern_name2>}..} | -write_pattern_template <file_name> | -boxes_file <file_name >| -auto_ir_fix {preroute | postroute}} ??-tile_row_column {<x y>} | -tile_size {<x y>} | -number_region <value>? | -write_pattern_template <file_name>? ?-rail_analysis_directory {<directory>} | -write_pattern_template <file_name>?",
        ),
        # man1/relink_db_files.1
        _syn(
            "relink_db_files",
            "Relinks symbolic links to library files inside a DB directory",
            "relink_db_files ?-help? -db_dir <db_directory> -new_lib_dirs {<new_lib_directory1> <new_lib_directory2> ...}",
        ),
        # man1/remove_assigns.1
        _syn(
            "remove_assigns",
            "Removes assign statements from the Verilog as much as possible while keeping the same DEF netlist",
            "remove_assigns ?-help? ?-buffer <bufName>? ?-buffering ?-buffer_tie_assigns??-includeIdealNets? ?-includeClockPath?? ?-honordonttouch? ?-ignorePortConstraints? ?-net <netName >?-netBuffer <netBufName>?? ?-prefix <bufNamePreFix>? ?-report?",
        ),
        # man1/remove_from_collection.1
        _syn(
            "remove_from_collection",
            "Creates a new collection by removing the objects specified in one collection from another collec‐ tion",
            "remove_from_collection ?-help? <base_collection>?-intersect? <object_collection_or_list>",
        ),
        # man1/remove_gui_marker.1
        _syn(
            "remove_gui_marker",
            "Removes a marker from the design layout",
            "remove_gui_marker ?-help? {-name <string> | -all }",
        ),
        # man1/rename_obj.1
        _syn(
            "rename_obj",
            "Renames the base_name of a single design object, which could only be a inst, hinst, design, module, port, hport, or hnet",
            "rename_obj ?-help? ?-escape_ok? ?-flexible? <inst|hInst|vCell|topCell|term|hTerm|hNet> <new_name>?-quiet?",
        ),
        # man1/rename_pg_library.1
        _syn(
            "rename_pg_library",
            "Specifies to copy and rename the specified power-grid view library",
            "rename_pg_library ?-help? ?-cell_list_map_file <filename>? ?-merge_library_list_file <filename>? ?-output <directory_name>? ?-output_library <new_library_name>?",
        ),
        # man1/replace_proto_model.1
        _syn(
            "replace_proto_model",
            "Converts flexmodel netlist back to the original full netlist with changes at the partition block level whenever feedthrough insertion step is needed in the flow",
            "replace_proto_model ?-help? ?-out_dir <string? > ?-ptn_dir <string>? ?-module_model_tag <string> -full_module_model_tag<string>?",
        ),
        # man1/replaceLefMacro.1
        _syn(
            "replaceLefMacro",
            "Replaces the current MACRO information in the design with the MACRO information in the specified LEF file",
            "replaceLefMacro ?-macros {<listOfMacros>}? <lefFile>",
        ),
        # man1/replacePowerSwitch.1
        _syn(
            "replacePowerSwitch",
            "Replaces the cell of a power switch instance",
            "replacePowerSwitch ?-help? -insts <inst_name_list> -cell <cell_name> ?-xoffset <value_in_microns>? ?-yoffset <value_in_microns>? ?-orientation <orienation_syntax>? ?-cellEnablePin {{<cellname> {<enableInputPinList>} {<enableOutputPinList>}}}? ?-xyRangeFromCenterInst?",
        ),
        # man1/report_analysis_coverage.1
        _syn(
            "report_analysis_coverage",
            "Provides information about the timing checks in the design",
            "report_analysis_coverage ?-help? ?<pin_port_list>? ?-check_type <check_type_list>? ?-exclude_untested <reason_list>? ?-include_dyn_checks? ?-include_parallel_check_arcs? ?-include_when_cond? ?-max_paths{type <integer>}? ?-nworst <<integer>>? ?-retime {aocv | ssta | path_slew_propagation | aocv_path_slew_propagation}? ?-sort {pin | refpin | checktype | slack | reason}? ?-tcl_list? ?-unsorted? ?-verbose <check_status_list>? ?-view <view_name>? ?> <filename?.gz?>? ?>> <filename?.gz?>?",
        ),
        # man1/report_analysis_summary.1
        _syn(
            "report_analysis_summary",
            "Generates timing slack summary reports for specified analysis view(s)",
            "report_analysis_summary ?-help? ?-csv <string>? ?-merged_views? ?-retime {path_slew_propagation | aocv_path_slew_propagation}? ?-retime_mode {exhaustive}? ?-view <viewName>? ?> <filename?.gz?>? ?>> <filename?.gz?>? ?-early | -late? ?-expanded_summary_clocks | -merged_groups?",
        ),
        # man1/report_analysis_views.1
        _syn(
            "report_analysis_views",
            "Generates a hierarchical report of the current multi-mode multi-corner configuration",
            "report_analysis_views",
        ),
        # man1/report_annotated_assertions.1
        _syn(
            "report_annotated_assertions",
            "Reports information for annotated assertions, set using the set_load or set_annotated_tran‐ sition command, according to the specified assertion type",
            "report_annotated_assertions -type {load | transition} ?-list_annotated? ?-list_non_annotated? ?-view <viewName>? ?-max_lines <number>? ?-min | -max | -min_max? <object_list> ?{> | >>} <file_name>?",
        ),
        # man1/report_annotated_check.1
        _syn(
            "report_annotated_check",
            "Reports coverage of annotated timing checks",
            "report_annotated_check ?-check_type <check_type_list>? ?-max_line <number>? ?instance_list? ?-list_annotated? ?-list_non_annotated? ?-view <viewName>? ?> | >> <filename>?.gz? | -tcl_list?",
        ),
        # man1/report_annotated_delay.1
        _syn(
            "report_annotated_delay",
            "Reports coverage of annotations on a design",
            "report_annotated_delay ?-help? ?-ignore_tied_low_high_net_arcs? ?-list_annotated? ?-list_non_annotated? ?-view <viewName>? ?-max_line <number>? ?{> | >>} <filename>?.gz? | -tcl_list? <?pin_port_list?>",
        ),
        # man1/report_annotated_parasitics.1
        _syn(
            "report_annotated_parasitics",
            "Reports the back-annotated parasitics of the design",
            "report_annotated_parasitics ?-help? ?-net_file <string>? ?-nets <string>? ?-view {viewName}? ?> {write_fileName}? ?>> {append_fileName}? ?{?-list_annotated? ?-list_broken_net? ?-list_extra_pin_net? ?-list_float_net? ?-list_nodriver_net? ?-list_noload_net? ?-list_not_annotated? ?-list_real_net? ?-list_supply_net? ?-list_zero_cap_net? ?-max_missing {max_missing_int}?}?",
        ),
        # man1/report_annotations.1
        _syn(
            "report_annotations",
            "Reports the coverage of the annotations on a design",
            "report_annotations ?-missing_resistances? ?-missing_capacitances? ?-missing_rc? ?-missing_delays? ?-missing_spf? ?-max_missing <integer>? ?-tcl_list? ?-ignore_floating_nets? ?-ignore_tied_low_high_nets? ?-ignore_tied_low_high_net_arcs? ?-list_annotated? ?-list_non_annotated? ?-view <viewName>? ?> <filename>?",
        ),
        # man1/report_aocv_derate.1
        _syn(
            "report_aocv_derate",
            "Reports the AOCV derating tables from AOCV libraries",
            "report_aocv_derate ?-help? ?-check_global_derating? ?-clock? ?-data? -file <<string>> ?-list_cell_not_annotated? ?-mesh? ?-voltage <<float>>? ?-design | -cell <<string>>? ?{-delay_corner <<string>> ?-power_domain <<string>>? } | -max | -min? ?-early | -late? ?-rise | -fall?",
        ),
        # man1/report_area.1
        _syn(
            "report_area",
            "Reports the combined standard cell area in each of the hierarchy modules and the top-level design",
            "report_area ?-help? ?-detail? ?-hierarchical_instance <hinst_name>? ?-include_physical? ?-min_area <area_per_module>? ?-min_count <instance_count>? ?-out_file <filename>? ?-show_leaf_cells? ?-show_msv_cells? ?-sort_by {name count area}? ?-table_style {horizontal vertical}? ?-summary | -depth <depth_of_hierarchy>?",
        ),
        # man1/report_bundled_bus.1
        _syn(
            "report_bundled_bus",
            "Generates a report for bundled buses",
            "report_bundled_bus ?-help? ?-name <string>? ?-nets <string>? ?-type {user_defined | tool_inferred}? ??> | >>??",
        ),
        # man1/report_case_analysis.1
        _syn(
            "report_case_analysis",
            "Generates a User Case Analysis table, which reports ports and pin that have a set_case_analysis constraint",
            "report_case_analysis ?-all? ?-nosplit? ?-dir? ?-view <view_name>? ?-propagated? ?-verbose? ?<pins_and_ports_list>? ?{> | >>}<filename> | -tcl_list?",
        ),
        # man1/report_ccopt_cell_filtering_reasons.1
        _syn(
            "report_ccopt_cell_filtering_reasons",
            "Reports the reasons for filtering the specified cell types",
            "report_ccopt_cell_filtering_reasons ?-help? ?-cell_type buffer | inverter | logic | delay | clock_gate? ?-clock_trees {string1 string2 ...}? ?-file <file_name>? ?-power_domain <power_domain_name>? ?-tcl_list?",
        ),
        # man1/report_ccopt_cell_halo_violations.1
        _syn(
            "report_ccopt_cell_halo_violations",
            "This command is used to report clock instances with clock halo violations",
            "report_ccopt_cell_halo_violations ?-help? ?-add_markers | -clear_markers? ?-file <fileName>? ?-num <number>? ?-summary?",
        ),
        # man1/report_ccopt_clock_tree_convergence.1
        _syn(
            "report_ccopt_clock_tree_convergence",
            "This command is used to report a summary of the convergence above clock sinks and to identify the names of sinks with the highest number of clock path networks",
            "report_ccopt_clock_tree_convergence ?-help? ?-file< fileName>?",
        ),
        # man1/report_ccopt_clock_tree_drv.1
        _syn(
            "report_ccopt_clock_tree_drv",
            "This command is used to report design rule violations (DRVs) in the clock network",
            "report_ccopt_clock_tree_drv ?-help? ?-clock_trees {<list_of_clock_trees>}? ?-delay_corners <list_of_delay_corner_names>? ?-drv_types {transition max_cap max_source_to_sink_net_length}? ?-early? ?-exclude_violation_types {dont_touch_nets pre_routed_nets}? ?-file file_name? ?-late? ?-num_nets num | all? ?-views {<list_of_views>}?",
        ),
        # man1/report_ccopt_clock_tree_structure.1
        _syn(
            "report_ccopt_clock_tree_structure",
            "Reports the structure of the clock network as a text report",
            "report_ccopt_clock_tree_structure ?-help? ?-check_type {setup | hold}? ?-clock_trees {<list_of_clock_trees>}? ?-delay_corner <corner_name>? ?-delay_type {early | late}? ?-expand_below_logic? ?-expand_generated_clock_trees {independently | inline | independently_and_inline}? ?-include_reporting_only_skew_groups? ?-file <file>_<name>? ?-show_sinks? ?-update_timing?",
        ),
        # man1/report_ccopt_clock_trees.1
        _syn(
            "report_ccopt_clock_trees",
            "This command reports a summary of all defined clock trees",
            "report_ccopt_clock_trees ?-help? ?-clock_trees {<list_of_clock_trees>}? ?-delay_corners {<list_of_delay_corners>} | -views {<list_of_views>}? ?-file <file_name>? ?-histograms? ?-list_special_pins? ?-no_invalidate? ?-num_cap_violating_pins <number_of_pins>? ?-num_fanout_violating_nets <number_of_nets>? ?-num_length_violating_nets <number_of_nets>? ?-num_resistance_violating_nets <number_of_nets>? ?-num_slew_violating_pins <number_of_pins>? ?-skip_timing_update? ?-summary? ?-tcl_list? ?-early | -late?",
        ),
        # man1/report_ccopt_pin_insertion_delays.1
        _syn(
            "report_ccopt_pin_insertion_delays",
            "Reports pin insertion delays at clock tree sinks",
            "report_ccopt_pin_insertion_delays ?-help? ?-bin_size <string>? ?-check_type {setup | hold}? ?-clock_trees {string1 string2 ...}? ?-delay_corner <delay_corner_name>? ?-delay_type {early | late}? ?-file <file_name>? ?-skew_groups {string1 string2 ...} | -include_reporting_only_skew_groups? ?-sources {string1 string2 ...}?",
        ),
        # man1/report_ccopt_preserved_clock_tree_ports.1
        _syn(
            "report_ccopt_preserved_clock_tree_ports",
            "This command reports all currently preserved ports set using the set_ccopt_pre‐ served_clock_tree_port command",
            "report_ccopt_preserved_clock_tree_ports ?-help? ?-out_file <filename>? ?-tcl_list?",
        ),
        # man1/report_ccopt_skew_groups.1
        _syn(
            "report_ccopt_skew_groups",
            "This command displays information about skew and insertion delay in skew groups",
            "report_ccopt_skew_groups ?-help? ?-delay_corners {<list_of_delay_corners>} | -views {<list_of_views>}? ?-exclude_pin_insertion_delay? ?-exclude_source_latency? ?-file <file_name>? ?-from <sources>? ?-histograms? ?-include_voltage {on | off | auto} | -summary? ?-no_invalidate? ?-paths <number_of_paths>? ?-skew_groups <list_of_skew_groups | >-include_reporting_only_skew_groups? ?-skip_timing_update? ?-summarize_stage_depth <cell_type_list>? ?-tcl_list? ?-through <list_of_pins>? ?-to <list_of_sinks>? ?-early | -late?",
        ),
        # man1/report_ccopt_worst_chain.1
        _syn(
            "report_ccopt_worst_chain",
            "This command displays information about the worst chain, which is the chain that contains the path with the worst negative slack or WNS in the design",
            "report_ccopt_worst_chain ?-help? ?-check_type {setup | hold}? ?-file <filename>? ?-through <pin> |< >-through_file <filename>? ?-view <viewname>?",
        ),
        # man1/report_cell_edge_spacing.1
        _syn(
            "report_cell_edge_spacing",
            "Reports all the cell edge spacing rules in both terminal and log file",
            "report_cell_edge_spacing ?-help? ?-file <fileName>?",
        ),
        # man1/report_cell_edge_type.1
        _syn(
            "report_cell_edge_type",
            "Reports the edge type of the specified cell",
            "report_cell_edge_type ?-help? ?-cell <cellName>? ?-file <fileName>?",
        ),
        # man1/report_cell_instance_timing.1
        _syn(
            "report_cell_instance_timing",
            "",
            "report_cell_instance_timing ?-help? <list_of_cell_instances > ?-early | -late? ?-clock_timing? ?-tcl_list? ?-view <view_name>? ?{> | >>} <filename>?",
        ),
        # man1/report_cell_stack_area.1
        _syn(
            "report_cell_stack_area",
            "Reports the cell stack area definition for cells",
            "report_cell_stack_area ?-help? ?-cell <cell_name>? ?-file <file_name>? ?-group <group_name>?",
        ),
        # man1/report_cell_stack_group.1
        _syn(
            "report_cell_stack_group",
            "Reports the cell stack group definition",
            "report_cell_stack_group ?-help? ?-file <string>? ?-name <string>?",
        ),
        # man1/report_cell_virtual_align.1
        _syn(
            "report_cell_virtual_align",
            "Reports the cells that need to be virtually aligned",
            "report_cell_virtual_align ?-help? ?-cell <cells>?",
        ),
        # man1/report_clock_gating_check.1
        _syn(
            "report_clock_gating_check",
            "Reports information of all or specific clock gating checks of the current design",
            "report_clock_gating_check ?<object_list>? ?-view <view_name>? ?{> | >>} <file_name>?",
        ),
        # man1/report_clock_propagation.1
        _syn(
            "report_clock_propagation",
            "This command provides the ability to determine clocks that do not propagate to a particular node in the network, and report the causes for such occurrences",
            "report_clock_propagation ?-help? -clock <clock_list> ?-max_paths <number of paths>? -to <pin_port_list> ?-verbose? ?-view <viewName>? ?> <filename?.gz?>? ?>> <filename?.gz?>?",
        ),
        # man1/report_clock_timing.1
        _syn(
            "report_clock_timing",
            "",
            "report_clock_timing ?-absolute_compare? ?-cppr_relative? ?-latency_greater_than? -type ?{skew interclock_skew jitter summary latency cppr_stage_count} ??-launch | -capture? ?-rise | -fall? | ?-histogram ?-histogram_range <interval size>?? ?-logic_level ?-source {clock_root | generated_clock}???? ?-early | -late? ?-clock <clock_list>? ?-from_clock <from_clock_list>? ?-to_clock <to_clock_list>? ?-from <from_list>? ?-to <to_list>? ?-nworst <worst_entries>? ?-greater_than <lower_limit>? ?-view <view_name>? ?-verbose? ?-format <column_list>? ?-tcl_list? ?{> | >>} <filename>?",
        ),
        # man1/report_clocks.1
        _syn(
            "report_clocks",
            "",
            "report_clocks ?-description? ?-arrival_points? ?-phase_shift_table? ?-total_shift_table? ?-uncertainty_table? ?-adjustment_table? ?-delay_adjustment_table? ?-source_insertion? ?-insertion? ?-hierarchy? ?-groups? ?-clocks <clk_signame> | <clk_signame_list>? ?-view <view_name>? ?{> | >>} <filename> | -tcl_list?",
        ),
        # man1/report_command_mode.1
        _syn(
            "report_command_mode",
            "Reports the *Mode options that do not match the default value or the options that have been manually set",
            "report_command_mode ?-help? ?-filter <list_of_commands>? {-non_default | -user}",
        ),
        # man1/report_constraint.1
        _syn(
            "report_constraint",
            "Reports constraint information of current design",
            "report_constraint ?-all_violators? ?-verbose? ?-late? ?-early? ?-em_type {peak | rms | avg | all}? ?-check_type { pulse_width | clock_period | recovery | removal | clock_gating_setup | clock_gating_hold | skew | pulse_clock_max_width | pulse_clock_min_width | electromigration | rail_swing}? ?-clock? ?-connection_class? ?-data? ?-drv_fields {<field_list>}? ?-drv_output_format {txt|csv}? ?-drv_violation_type { max_capacitance | max_transition | max_fanout | min_capacitance | min_transition | min_fanout | pulse_clock_max_transition | pulse_clock_min_transition}? ?-max_pins_per_drv <integer>? ?-retime {aocv | path_slew_propagation | aocv_path_slew_propagation}? ?-retime_mode {path | exhaustive}? ?-view <viewName>? ?-worst_drv_per_net? ?<pin_port_list>? ?{> | >>} filename?.gz??",
        ),
        # man1/report_cppr.1
        _syn(
            "report_cppr",
            "Reports the clock reconvergence pessimism value at the common branching point of the early and late paths in the clock network of the specified data path",
            "report_cppr ?-help? ?-check_type {setup | hold | clock_gating_setup | clock_gating_hold | clock_gating_pulse_width | data_setup | data_hold | recovery | removal | pulse_width | clock_period | clock_separation | skew | no_change_setup | no_change_hold | time_bor‐ row}? -from <pin_or_port> -to <pin_or_port> ?-from_clock <clkname>? ?-to_clock <clkname>? ?-early | -late? ?-view <view_name>? ?> <filename>?",
        ),
        # man1/report_design.1
        _syn(
            "report_design",
            "Reports the minimum and/or maximum operating conditions and active design rules for the current design",
            "report_design ?-view <viewName>? ?{> | >>} <filename>| -tcl_list? ?-early | -late?",
        ),
        # man1/report_disk.1
        _syn(
            "report_disk",
            "Reports the disk metrics of the current working directory and the /tmp directory",
            "report_disk ?-help? ?-dir <directory_name>?",
        ),
        # man1/report_double_clocking.1
        _syn(
            "report_double_clocking",
            "",
            "report_double_clocking ?-help? ?-file <string>? ?-max_delta_delay <float>? ?-nworst <integer>? ?-reverse_slope_limit <float>? ?-reverse_voltage_change_threshold <float>? ?-view <string>?",
        ),
        # man1/report_fanin.1
        _syn(
            "report_fanin",
            "Allows a cone traversal that is not tied to the timing graph, that is, not blocked by set_disable_timing and case analysis",
            "report_fanin -to <pin_port_net_list> ?-trace_through {case_disable | user_disable | all}? ?-pin_levels <numOfPinLevels>? ?-view <viewName>? ?-nosplit? ?{> | >> } <filename>?",
        ),
        # man1/report_fanout.1
        _syn(
            "report_fanout",
            "Allows a cone traversal that is not tied to the timing graph, that is, not blocked by set_disable_timing and case analysis",
            "report_fanout {-from <pin_port_net_list> | -clock_tree} ?-trace_through {case_disable | user_disable | all}? ?-pin_levels <numOfPinLevels>? ?-view <viewName>? ?-nosplit? ?{> | >> } <filename>?",
        ),
        # man1/report_gates.1
        _syn(
            "report_gates",
            "Reports the technology library cells that were implemented (and identifies their originating libraries), the area of the cell instances, and the break up of the instances into timing models, sequential cells, integrated clockgating cells, inverters, buffers, and logic gate cells",
            "report_gates ?-help? ?-hinst <hInstName>? ?-out_file <fileName>? ?-sort {name count area leakage_power internal_power total_power switching_power}? ?-power | -leakage_power?",
        ),
        # man1/report_glitch_thresholds.1
        _syn(
            "report_glitch_thresholds",
            "Reports user-defined glitch thresholds applied on library or instance pins",
            "report_glitch_thresholds ?-help? ?-failure_point {input | output}? ?-glitch_type <<string>>? ?-instance_pins <<string>>? ?-library_pins <<string>>? ?-list_unannotated_instance_pins? ?-list_unannotated_library_pins? ?-view <string>?",
        ),
        # man1/report_globals.1
        _syn(
            "report_globals",
            "Generates a list of the officially supported global variables, with their current and default values",
            "report_globals ?-help? ?<pattern>? ?-add <global_name_list>?",
        ),
        # man1/report_gui_edit_callback.1
        _syn(
            "report_gui_edit_callback",
            "Reports the callback functions added to the specified move action",
            "report_gui_edit_callback ?-help? ?-edit_type {selection pre-move post-move}? ?-file <string>?",
        ),
        # man1/report_hidden_usage.1
        _syn(
            "report_hidden_usage",
            "Reports a summary of all the hidden application Tcl globals and mode options in the specified files",
            "report_hidden_usage <in_files>",
        ),
        # man1/report_inactive_arcs.1
        _syn(
            "report_inactive_arcs",
            "Reports information about disabled timing and timing check arcs in the design",
            "report_inactive_arcs ?-help? ?<instance_or_port_list>? ?-exclude_type {const snipped disable library_disable global_disable conditional_disable Library_Mode}? ?-include_net_arcs? ?-include_when_cond? ?-type {const snipped disable library_disable global_disable conditional_disable Library_Mode power_mode_disable}? ?-view <view_name>? ?> <filename?.gz?>? ?>> <filename?.gz?>? ?-delay_arcs_only | -check_arcs_only?",
        ),
        # man1/report_inst_space_group.1
        _syn(
            "report_inst_space_group",
            "Reports all instance space groups into the inst_space_group report file by default",
            "report_inst_space_group ?-help? ?-file <fileName>? ?-group <groupName>?",
        ),
        # man1/report_instance_cdb.1
        _syn(
            "report_instance_cdb",
            "Allows you to report the cdB associated with all the instances or a subset of instances in a design",
            "report_instance_cdb ?-help? ?-analysis_type {early | late}? ?{<instance_list> or <collection>}? ?-output_file <filename>? ?-quiet? ?-view <viewname>?",
        ),
        # man1/report_instance_library.1
        _syn(
            "report_instance_library",
            "Reports library related information for an instance(s)",
            "report_instance_library -file <fileName> ?-instance <instanceName>? ?-view <viewName> | -delay_corner <delayCornerName>? ?-power_domain <domainName>? ?-early | -late?",
        ),
        # man1/report_instance_power.1
        _syn(
            "report_instance_power",
            "Generates a text based report for the specified instance",
            "report_instance_power ?-help? <instance> ?-file <filename>? ?-inst_file <filename>?",
        ),
        # man1/report_lib_arcs.1
        _syn(
            "report_lib_arcs",
            "",
            "report_lib_arcs ?-help? -arc <string> ?-fall? ?-nldm? ?-quiet? ?-rise? ?-lvf ?-early?? ?-lvf ?-late?? ?-moments ?-mean_shift?? ?-moments ?-std_dev?? ?-moments ?-skewness?? ?-input_net_transition <float> | -constrained_pin_transition <float>? ?-input_net_transition <float> | -related_pin_transition <float>? ?-total_output_net_capacitance <float> | -constrained_pin_transition <float>? ?-total_output_net_capacitance <float> | -related_pin_transition <float>? ?-constrained_pin_transition <float> | -delay? ?-constrained_pin_transition <float> | -transition? ?-related_pin_transition <float> | -delay? ?-related_pin_transition <float> | -transition?",
        ),
        # man1/report_message.1
        _syn(
            "report_message",
            "Reports the messages that have been issued since the tool was launched",
            "report_message ?-help? ??{-errors | -warnings | -all } ?-count?? | -suppressed? ??-prefix <prefix> ?-detail? ?-summary??? ?-detail | -count | -suppressed? ?-summary | -count | -suppressed?",
        ),
        # man1/report_metal_fill.1
        _syn(
            "report_metal_fill",
            "Generates a report on metal fill to summarize the number and area of fill shapes on a per-net and perlayer basis",
            "report_metal_fill ?-help? ?-file <file_name>? ?-fill_area? ?-fill_length? ?-mesh?",
        ),
        # man1/report_metal_stack.1
        _syn(
            "report_metal_stack",
            "Reports the metal stack configuration and routing track information",
            "report_metal_stack ?-help? ?-non_preferred_direction?",
        ),
        # man1/report_min_pulse_width.1
        _syn(
            "report_min_pulse_width",
            "Reports a set of minimum pulse width violations on pins and ports on the clock network",
            "report_min_pulse_width ?-verbose? ?-clock <object_list>? ?-path_type {summary | short | full_clock}? ?-pins <object_list>? ?-net? ?-violation_only? ?-view <view_name>? ?-waveform_aware_type {regular | waveform_aware | both}? ?{ > | >> } <filename> | -tcl_list?",
        ),
        # man1/report_mode.1
        _syn(
            "report_mode",
            "Reports the status of library modes associated with a specified instance",
            "report_mode <instance_list > ?-view viewName?",
        ),
        # man1/report_module_model.1
        _syn(
            "report_module_model",
            "Reports the module models that are currently loaded/committed at top-level design",
            "report_module_model ?-help? ?-active_rc_corners? ?-default_dir? ?-non_committed_hinst? ?-type {flexilm lef ilm pnr pnr_shell}?",
        ),
        # man1/report_mutex_condition.1
        _syn(
            "report_mutex_condition",
            "Reports mutex nets of a victim net",
            "report_mutex_condition ?-help? ?-filename <<string>>? ?-net <<string>>?",
        ),
        # man1/report_narrow_channel.1
        #   WARNING: unmatched closing bracket '}' at position 230
        _syn(
            "report_narrow_channel",
            "Creates a report that contains a list of narrow channels",
            "report_narrow_channel ?-help? {-width <width>} ?-ignore_placement_blockage? ?-no_merge_channel_check? ?-direction {x y xy}? ?-active_objects {macro macroHalo ioPad ioCell core fence hardBlkg softBlkg partialBlkg routeBlkg row}? }",
        ),
        # man1/report_net.1
        _syn(
            "report_net",
            "Reports the net information on the current module",
            "report_net ?-min_fanout <int>? ?-max_fanout <int>? {-net <list_of_net_name_or_id> | -pin <list_of_pin_name_or_id>} ?-tcl_list? ?-hier? ??{> | >>} <filename> | -output <filename>? | -tcl_list?",
        ),
        # man1/report_net_parasitics.1
        _syn(
            "report_net_parasitics",
            "Reports the RC parasitics of the specified net",
            "report_net_parasitics <net_name> ?-help? -rc_corner <rc_corner_name> ?-file_name <output_file_name>?",
        ),
        # man1/report_net_wires.1
        _syn(
            "report_net_wires",
            "Displays information about the regular net wires",
            "report_net_wires ?-help? ?-file <fileName>? ?-net <netName>?",
        ),
        # man1/report_noise.1
        _syn(
            "report_noise",
            "Generates text-based noise reports",
            "report_noise ?-help? ?-bumpy_waveform? ?-cell_type {bbox | clock | data | latch}? ?-delay {min | max}? ?-double_clocking? ?-double_switching? ?-exclude_failures? ?-expand_virtual_attacker_bus? ?-failure? ?-gui_victim_nets_file? ?-format <string>? ?-histogram? ?-level {vl | vh | vlu | vho}? ?-max_threshold <float>? ?-merge_dir <string>? ?-nets <string>? ?-output_format string? ?-output_file <string>? ?-overshoot_undershoot? ?-pins <string>? ?-precision <integer>? ?-quiet_nets? ?-remove_status_row <string>? ?-report_virtual_attacker_constituents? ?-reverse_voltage_change_threshold <float>? ?-slack <float>? ?-skip_nets_or_pins_in_header? ?-sort_by <string>? ?-style {default | extended}? ?-threshold <float>? ?-txtfile <filename?.gz?>? ?-view?",
        ),
        # man1/report_noise_lib_pin.1
        _syn(
            "report_noise_lib_pin",
            "Generates a report providing information on all the user-specified noise mappings in the design",
            "report_noise_lib_pin ?-help? ?> <filename>?",
        ),
        # man1/report_noise_propagation.1
        _syn(
            "report_noise_propagation",
            "Prints text-based noise propagation reports that show glitch-source tracing for all the userspecified or all-violating receiver pins",
            "report_noise_propagation ?-help? ?-level {VL | VH | worst | all}? ?-max_paths <integer>? ?-max_slack <float>? ?-nets <string>? ?-nworst <integer>? ?-pins <string>? ?-source_depth <integer>? ?-views <string>? ??> | >>??",
        ),
        # man1/report_oa_lib.1
        _syn(
            "report_oa_lib",
            "Reports information about OpenAccess libraries from within Innovus",
            "report_oa_lib ?-help? <lib_name> ?-header? ?-filter {cdsinfo | compression | constraint_groups | property | tech_graph}?",
        ),
        # man1/report_obj_connectivity.1
        _syn(
            "report_obj_connectivity",
            "Reports the connections of specified macros, selected macros, or specified ports",
            "report_obj_connectivity ?-help? ?-direction {in|out|all}? ?-file <file_name>? ?-level <level>? ?-no_split? ?-through_registers? ?-to_ports? ?-insts <inst+>? | ?-ports <port+>? | ?-selected?",
        ),
        # man1/report_partitions.1
        _syn(
            "report_partitions",
            "Reports the partitions and clones in a correct tree like format",
            "report_partitions ?-help? ?<topCell>?",
        ),
        # man1/report_path_exceptions.1
        _syn(
            "report_path_exceptions",
            "Generates a report about path exceptions specified using the set_false_path, set_min_delay, set_max_delay, and set_multicycle_path commands",
            "report_path_exceptions ?-help? ?-all? ?-early | -late? ?-ignored? ?-view <view_name>? ?{> | >>} <filename> | -tcl_list?",
        ),
        # man1/report_path_groups.1
        _syn(
            "report_path_groups",
            "Lists the names of all path groups with the corresponding paths",
            "report_path_groups ?-name <group_name>? ?{> | >>} <filename> | -tcl_list?",
        ),
        # man1/report_pg_keepout.1
        _syn(
            "report_pg_keepout",
            "",
            "report_pg_keepout ?-help? ?-file <file_name>? {-cell <lib_cell_name> | -inst <instance_name>}",
        ),
        # man1/report_ports.1
        _syn(
            "report_ports",
            "Reports timing constraints on ports",
            "report_ports ?-type {?input? | ?source_insertion? | ?insertion? | ?clock_root? | ?uncertainty? | ?arrival? | ?required? | ?external? | ?clk_arrival? | ?port_cap? | ?fanout_load? | ?fanout_load_limit? | ?drive_resistance? | ?drive_cell? | ?slew_time? | ?slew_limit? | ?constant? | external_detail | drive_resistance_detail}? ?-include_pins? ?-pins <port_name_list>? ?-view <viewName>? ?> <filename> | -tcl_list?",
        ),
        # man1/report_power.1
        _syn(
            "report_power",
            "",
            "report_power ?-block <block_name>? ?-cap? ?-cell {<cell_list>}? ?-cell_type {all | {macro io combinational sequential clock_combinational clock_sequential}}? ?-clock_domain {<clock_domain_list>}? ?-clock_network {all | {<clock_list>}}? ?-count_seq_elements_in_clock_network? ?-die_instance_name <dieinstname>? ?-exclude_cells {<cell_list>}? ?-exclude_cells_file <filename>? ?-exclude_instances {<instance_list>}? ?-exclude_instances_file <filename>? ?-instances {<instance_list>}? ?-hierarchy {all | <hierarchy_level}>? ?-hierarchical_instances {<hierarchy_inst_list>}? ?-leakage? ?-net ?-nworst<number_of_nets>?? ?-no_wrap? ?-outfile <filename>? ?-pg_net {all | <pg_net_name_list>}? ?-power_domain {all | {<power_domain_list>}<}>? ?-sort {internal | switching | leakage | total}? ?-threshold <value>? ?-view <view_name>? ?-threshold_voltage_group { all | <group_name>}? ?-clock_gating_efficiency? ?-register_gating_efficiency? ?-cluster_gating_efficiency? ?-thermal_leakage_temp {<temp_list>}? ?-thermal_power_map_file <file_name>? ?-thermal_power_map_tile {<Xint> <Yint>}? ?-thermal_power_map_format {simple | stack }? ?-pg_pin? ?-thermal_conductivity_inputs <file_name>? ?-output <directory>? ?-o <directory>? ?-report_prefix <prefix>? ?-toggle_rate? ?-format { simple | detailed }? ?-comb_seq_power? ?-group_type <user_defined_group_name>? ?-distribute? ?-print_memory_power? ?-cap_unit <unit>? ?-cell_list_file <filename>? ?-float_precision <value>? ?-inst_list_file <filename>? ?-power_db_directory <directory>? ?-power_unit <unit>? ?-time_unit <unit>? ?-power_density_tiles <value>? ?-power_density_tiles_row_col {<value1> <value2>}? ?-power_density_tiles_size {<value1> <value2>}? ?-compress <compression_ratio>? ?-stat? ?-time_based_report? ?-thermal_power_map_header_include_file <filename>? ?-thermal_leakage_temperature_scale_table_file <filename>? ?-thermal_leakage_temperature_scale_table {$<temp1> $<scalefactor1> $<temp2> $<scalefactor2> $<temp3> $<scalefactor3> .....}? ?-thermal_material_file <filename>? ?-thermal_power_map_SI_unit {true | false}? ?-thermal_power_map_powertable_tile {<Xint> <Yint>}? ?-thermal_power_map_densitytable_tile {<Xint> <Yint>}? ?-thermal_power_map_format_version {new|default}? ?-thermal_power_map_bottom_layer <layer_name>? ?-thermal_power_map_top_layer <layer_name>? ?-use_geometry_cell_size {true | false}?",
        ),
        # man1/report_power_rail_results.1
        _syn(
            "report_power_rail_results",
            "Generates RLRP, region-based, and rail/power/capacitance reports",
            "report_power_rail_results ?-help? ?-append? ?-enable_filter_summary? ?-filename <file>? ?-filter_max <max_value>? ?-filter_min <min_value>? ?-ignore_limit_bound? ?-layers {All,<layer_names>}? ?-limit <N>? ?-nets {all | all_pwr | all_gnd | <net_names>}? ?-plot <plot_type>? ?-range_max <max_value>? ?-range_min <min_value>? ?-region <x1><y1><x2><y2>? ?-rlrp_inst {<instance_name>}?",
        ),
        # man1/report_precision.1
        _syn(
            "report_precision",
            "",
            "",
        ),
        # man1/report_precision_capacitance.1
        _syn(
            "report_precision_capacitance",
            "",
            "report_precision_capacitance <integer >",
        ),
        # man1/report_precision_derate.1
        _syn(
            "report_precision_derate",
            "",
            "report_precision_derate <integer >",
        ),
        # man1/report_precision_power.1
        _syn(
            "report_precision_power",
            "",
            "report_precision_power <integer >",
        ),
        # man1/report_precision_sensitivity.1
        _syn(
            "report_precision_sensitivity",
            "",
            "report_precision_sensitivity <integer >",
        ),
        # man1/report_preserves.1
        _syn(
            "report_preserves",
            "By default, this command displays all the preserves that affect optimization set in the library",
            "report_preserves ?-help? ?-computed? ?-obj_type {design | hinst | module | inst | net | hnet | pin | hpin | base_cell}? ?-dont_touch | -dont_use?",
        ),
        # man1/report_property.1
        _syn(
            "report_property",
            "Reports the properties associated with each object in the specified collection",
            "report_property ?-help? {<collection> | <list_of_collections>} ?-property_list <list of properties>? ?{> | >>} <filename>?",
        ),
        # man1/report_proto_model.1
        _syn(
            "report_proto_model",
            "Reports statistics information for models",
            "report_proto_model ?-help? ?-constraint? ?-file <string>? ?-min_inst <integer> | -identified | -created? ?-min_inst <integer>? ?-instance_ratio <float> | -min_inst <integer>?",
        ),
        # man1/report_rcdb.1
        _syn(
            "report_rcdb",
            "Displays the contents of the RCDB being read",
            "report_rcdb ?-help?",
        ),
        # man1/report_resource.1
        #   WARNING: unmatched closing bracket ']' at position 189
        _syn(
            "report_resource",
            "Displays the peak memory used during a software session",
            "report_resource ?-help? ?-peak? ?-verbose? ?-start <string> | ?-end <string> ?-session_cpu? ?-diff_memory??? ?-check_MemCpu {true | false} ?-period <integer>?? ?-memory_threshold <<float>>??",
        ),
        # man1/report_route.1
        _syn(
            "report_route",
            "",
            "report_route ?-help? ?-clock? ?-em? ?-fanout <integer>? ?-fill? ?-inst <string>? ?-multi_cut? ?-ndr? ?-net <net_name>? ?-net_length <length>? ?-patch? ?-pg_net <string>? ?-secondary_pg_nets {<cellName1:pinName1>}? ?-selected? ?-shield? ?-summary? ?-via_pillar? ?-track_utilization ?-area {{<lx1 ly1 ux1 uy1>} {<lx2 ly2 ux2 uy2>}...} | -view_window? ?-layer <string>? ?-include_regular_routes??",
        ),
        # man1/report_sai_constraint.1
        _syn(
            "report_sai_constraint",
            "",
            "report_sai_constraint ?-help? ?-area_weight <float>? ?-spacing_weight <float>? ?-order_weight <float>? ?-congestion_weight <float>? ?-rule {all | <rule_name> | <rule_name_list>}?",
        ),
        # man1/report_scan_chain.1
        _syn(
            "report_scan_chain",
            "Prints the scan chain information",
            "report_scan_chain ?-help? ?-chain <chainName>? ?-out_file <fileName>? ?-verbose {true|false}?",
        ),
        # man1/report_sequential.1
        _syn(
            "report_sequential",
            "Reports information about sequentials the design",
            "report_sequential ?-help? ?-deleted? ?-full? ?-hinst <hInst_names>? ?-mapped? ?-optimized? ?-out_file <string>?",
        ),
        # man1/report_socv_interconnect_variation.1
        _syn(
            "report_socv_interconnect_variation",
            "Reports the RC variation multiplier data provided in the SOCV files",
            "report_socv_interconnect_variation ?-help? ?-delay_corner <string>? ?-power_domain <string>?",
        ),
        # man1/report_socv_library.1
        _syn(
            "report_socv_library",
            "",
            "report_socv_library ?-help? ?-categories <string>? ?-coverage_verbose? ?-list_not_annotated? ?-libset <string> | { -delay_corner <string> ?-power_domain <string>? }| { -view <string> ?-power_domain <string>?}? ?-libs <string> | -lib_cells<string>? ?-coverage?",
        ),
        # man1/report_statistical_timing_derate_factors.1
        _syn(
            "report_statistical_timing_derate_factors",
            "Generates design specific OCV factor",
            "report_statistical_timing_derate_factors -type {arrival_time_based | slack_time_based} -ssta_view <ssta_view_name> -sta_view <sta_view_name> -path_group <groupname_list>",
        ),
        # man1/report_timing.1
        _syn(
            "report_timing",
            "",
            "report_timing ?-help? ?-analysis_summary_csv_extended_file <<string>>? ?-analysis_summary_csv_file <<string>>? ?-analysis_summary_file <<string>>? ?-check_clocks? ?-check_type {setup hold clock_gating_setup clock_gating_hold clock_gating_pulse_width data_setup data_hold recovery re‐ moval pulse_width clock_period clock_separation skew no_change_setup no_change_hold max_delay min_delay}? ?-debug {unconstrained | time_borrow | cppr_point | vt_skew}? ?-delay_limit <float>? ?-derate_summary? ?-gui? ?-format <column_list>? ?-hpin? ?-max_slack <float>? ?-min_slack <float>? ?-net? ?-output_format {text | csv | gtd | binary}? ?-path_exceptions {applied ignored all}? ?-path_group <groupname_list>? ?-path_type {end summary full full_clock end_slack_only summary_slack_only}? ?-retime {aocv path_slew_propagation aocv_path_slew_propagation}? ?-retime_delaycal_pins <<pin_list>>? ?-retime_format {manual | retime_compare | retime_replace}? ?-retime_mode {path exhaustive}? ?-skip_io_paths? ?-unique_pins? ?-view <viewName>? ?-worst_rc_corner? ?> <filename?.gz?>? ?>> <filename?.gz?>? ?-late | -early? ?-rise | -fall? ?-begin_end_pair | ??-max_paths <integer>? ?-nworst <integer>??? ?-unconstrained | -point_to_point? ?-collection | -machine_readable | -tcl_list? ?-not_through <object_list> | -not_rise_through <object_list> | -not_fall_through <object_list>? ??-from <pin_list> | -from_rise <pin_list> | -from_fall <pin_list>? ?-clock_from <clk_signame_list> ?-edge_from {lead trail}?? ?-through <pin_list> | -through_rise <pin_list> | -through_fall <pin_list>? ?-to <pin_list> | -to_rise <pin_list> | -to_fall <pin_list>? ?-clock_to <clk_signame_list> ?-edge_to {lead trail}???",
        ),
        # man1/report_timing_derate.1
        _syn(
            "report_timing_derate",
            "Reports delay scaling or derating factors for early and late clock and data paths in the current design",
            "report_timing_derate ?-delay_corner <delayCornerName>? ?-include_inherited? ?<object_list>? ?{> | >>} <filename>?.gz??",
        ),
        # man1/report_timing_format.1
        _syn(
            "report_timing_format",
            "",
            "report_timing_format {<column_list>}",
        ),
        # man1/report_tracks.1
        _syn(
            "report_tracks",
            "Reports track definitions for each layer",
            "report_tracks ?-help? ?-prefer_only?",
        ),
        # man1/report_unit_parasitics.1
        _syn(
            "report_unit_parasitics",
            "Reports unit parasitics for individual metal layers and vias",
            "report_unit_parasitics ?-help? -layer <metal_layer_name> -rc_corner <rc_corner_name> ?-space <wire_space_in_um>? ?-via_res <via_resistance>? ?-width <wire_width_in_um>?",
        ),
        # man1/report_via.1
        _syn(
            "report_via",
            "Reports the single and multi-cut via summary for special and/or regular vias",
            "report_via ?-help? ?-detail? ?-on_clock_nets? ?-on_selected_nets? ?-regular? ?-special?",
        ),
        # man1/report_voltage_scaling.1
        _syn(
            "report_voltage_scaling",
            "Reports instances whose timing data is interpolated due to voltage mismatch",
            "report_voltage_scaling ?-help? ?<objectListOrCollection>? ?-analysis_type {early | late}? ?-view <string>? ?-output_file <string>?",
        ),
        # man1/report_voltage_swing.1
        _syn(
            "report_voltage_swing",
            "Reports the voltage swings that are shorter than the user-specified thresholds for both clock and data signals",
            "report_voltage_swing ?-help? -high_threshold <float> -low_threshold <float> ?-output_file <string>? ?-required_width {all | clock}? ?-view <string>?",
        ),
        # man1/report_wire_load.1
        _syn(
            "report_wire_load",
            "Reports the wireload name, library, wire load mode and selection type for all hierarchical instances in the design",
            "report_wire_load ?-inst <name_or_collection_of_hierarchical_instances>? ?-ports <name_or_collection_of_ports>? ?-late | -early? ?> | >> <filename>?",
        ),
        # man1/reportAlwaysOnBuffer.1
        _syn(
            "reportAlwaysOnBuffer",
            "Reports the available always-on buffers and inverters per domain",
            "reportAlwaysOnBuffer ?-help? ?-all? ?-powerDomain <domainName>? ?-verbose?",
        ),
        # man1/reportCapViolation.1
        _syn(
            "reportCapViolation",
            "After timing analysis, reports nets that exceed the maximum capacitance constraints in the timing li‐ brary and timing constraints file",
            "reportCapViolation ?-help? ?-all | -noGlobalNets? ?-max? ?-min? ?-outfile <fileName>? ?-selNetFile <fileName>? ?-excNetFile <fileName>? ?-significant_digits <integer>? ?-useDrcMargin?",
        ),
        # man1/reportCellPad.1
        _syn(
            "reportCellPad",
            "Prints the number of cells, which contain user-specified padding, to the log file",
            "reportCellPad ?-help? ?-cell <cellName>? ?-file <fileName>?",
        ),
        # man1/reportCongestArea.1
        _syn(
            "reportCongestArea",
            "Reports the congestion hot spots in the design",
            "reportCongestArea ?-help? ?-num ?all | <numOfHotSpot>?? ?-cutOffRatio <cutOffRatioOfPeakHotSpot>? ?-cutOffValue <cutOffCongestNum>? ?-mode <modeName>? ?-step <num>? ?-cutoffArea <cutOffGcellNum>? ?-outfile <fileName>?",
        ),
        # man1/reportCongestion.1
        _syn(
            "reportCongestion",
            "Reports the average congestion and the local hotspot score",
            "reportCongestion ?-help? ?-3d? ?-hotSpot? ?-includeBlockage? ?-num_hotspot <number>? ?-overflow?",
        ),
        # man1/reportConnectivity.1
        _syn(
            "reportConnectivity",
            "Reports the connectivity of pins including I/O pins, partition pins, hpins, hterms, hinstterms, and instterms",
            "reportConnectivity ?-help? <pinName> ?-level <integer>? ?-pinOnly?",
        ),
        # man1/reportCritInstance.1
        _syn(
            "reportCritInstance",
            "Reports instances in critical paths where the slack is less than the target slack",
            "reportCritInstance ?-help? -outfile <fileName> ?-view <viewName>? ?-targetSlack <slackValue>?",
        ),
        # man1/reportCritNet.1
        _syn(
            "reportCritNet",
            "Generates a file containing a list of nets which have critical slack for the currently specified (setup or hold) timing analysis mode",
            "reportCritNet ?-help? ?-nrCritNets <integer>? ?-outfile <fileName>? ?-targetSlack <double>? ?-view <viewName>?",
        ),
        # man1/reportCritTerm.1
        _syn(
            "reportCritTerm",
            "Performs slack analysis and writes the names of all critical terminals to the specified file",
            "reportCritTerm ?-help? -outfile <fileName>",
        ),
        # man1/reportDanglingNet.1
        _syn(
            "reportDanglingNet",
            "Reports the number of nets with zero terms, including the PG nets",
            "reportDanglingNet ?-help? ?-outfile <fileName>?",
        ),
        # man1/reportDanglingPort.1
        _syn(
            "reportDanglingPort",
            "Reports ports that are disconnected from both the inside and outside of a module, and ports that are connected within the module but disconnected outside the module",
            "reportDanglingPort",
        ),
        # man1/reportDeCap.1
        _syn(
            "reportDeCap",
            "Reports placed decoupling capacitance cells in the specified area",
            "reportDeCap ?-help? -area <x1 y1 x2 y2>",
        ),
        # man1/reportDeCapCellCandidates.1
        _syn(
            "reportDeCapCellCandidates",
            "Reports the available cells for decoupling capacitance insertion",
            "reportDeCapCellCandidates ?-help? ?-file <outputFileName>?",
        ),
        # man1/reportDelayCalculation.1
        _syn(
            "reportDelayCalculation",
            "Reports the delay calculation information for a cell or net timing arc",
            "?-help? ?-active_arcs? -from <string> ?-max? ?-min? ?-mis? ?-outfile <filename>? ?-show_all_attackers? ?-si? ?-thresholds? -to <string> ?-view <string>? ?-voltage? ?-waveform?",
        ),
        # man1/reportDensityMap.1
        _syn(
            "reportDensityMap",
            "Generates a map that uses colors to represent placement density and generates a placement density re‐ port",
            "reportDensityMap ?-help? ?-gridInMicron <microns>? ?-gridInRow <numberRows>? ?-ignoreBlock {true|false}? ?-ignoreFiller {true|false}? ?-threshold <density>?",
        ),
        # man1/reportFanoutViolation.1
        _syn(
            "reportFanoutViolation",
            "After timing analysis, reports all the pins that exceed the fanout constraints in the timing li‐ brary and timing constraints file",
            "reportFanoutViolation ?-help? ?-all | -noGlobalNets? ?-excNetFile f<ileName>? ?-min? ?-max? ?-outfile <fileName>? ?-selNetFile <f><ileName>? ?-significant_digits <integer>? ?-useDrcMargin?",
        ),
        # man1/reportFootPrint.1
        _syn(
            "reportFootPrint",
            "Creates a file that contains footprint attribute information from the timing library",
            "reportFootPrint ?-help? ?-outfile <fileName>? ?-dontTouchNUse? ?<footprint>?",
        ),
        # man1/reportFreqViolation.1
        _syn(
            "reportFreqViolation",
            "Runs electromigration (EM) analysis based on the frequency table defined in the Liberty library and generates a frequency violation report",
            "reportFreqViolation ?-help? ?-outfile <fileName>? ?-selInstFile <selInstFileName>? ?-em_type {avg | peak | rms | all}? ?-excInstFile <excInstFileName>? ?-tableScale <float>? ?-detailed? ?-slew {min | max}? ?-sort {name | freq | minDiff | maxDiff | minFreq | maxFreq}? ?-reportFormat <integer>? ?-view <viewName>?",
        ),
        # man1/reportGateCount.1
        _syn(
            "reportGateCount",
            "Reports the size of the imported design, measured in gate counts",
            "reportGateCount ?-help? ?-hinst <hinst_name>? ?-level <level>? ?-limit <gateCount>? ?-stdCellOnly? ?-outfile <fileName>?",
        ),
        # man1/reportIgnoredNets.1
        _syn(
            "reportIgnoredNets",
            "Generates a report that lists the nets that are ignored by timing optimization (optDesign) or that might impact timing closure",
            "reportIgnoredNets ?-help? -outfile <fileName>",
        ),
        # man1/reportIlmStatus.1
        _syn(
            "reportIlmStatus",
            "Reports ILM status information including ILM block names, ILM data locations, and if the design is in the flattened or unflattened state",
            "reportIlmStatus ?-help?",
        ),
        # man1/reportInstPad.1
        _syn(
            "reportInstPad",
            "Reports the padding for a specific instance, or all instance padding in the design",
            "reportInstPad {<instName> | -all}",
        ),
        # man1/reportIsolation.1
        _syn(
            "reportIsolation",
            "Reports or shows the added isolation cells and instances",
            "reportIsolation ?-help? ?-highlight? ?-outfile <fileName>? ?-from <powerDomain>? ?-to <powerDomain>?",
        ),
        # man1/reportJtagInst.1
        _syn(
            "reportJtagInst",
            "Displays JTAG information specified by the specifyJtag command or creates an output file that contains the information",
            "reportJtagInst ?-outfile?",
        ),
        # man1/reportLegalWireWidthForBump.1
        _syn(
            "reportLegalWireWidthForBump",
            "Reports two legal widths for a 45-degree wire to connect to the 45-degree side of an octa‐ gon-shaped bump in the wire editor",
            "reportLegalWireWidthForBump ?-help? -location <x y> -width <value>",
        ),
        # man1/reportLengthViolation.1
        _syn(
            "reportLengthViolation",
            "Runs timing analysis and reports nets that exceed the maximum length constraint set by setOptMode –opt_max_length parameter",
            "reportLengthViolation ?-help? ?-all | -noGlobalNets? ?-selNetFile <selNetFileName>? ?-excNetFile <excNetFileName>? ?-histogram? ?-outfile <fileName>? ?-significant_digits <integer>?",
        ),
        # man1/reportMultibit.1
        _syn(
            "reportMultibit",
            "Reports all the multi-bit flip-flops that have been identified during loading the design",
            "reportMultibit ?-help? ?-bit <bit_width>? ?-outFile <file_name>? ?-cell <cell_name> | -library | -reasonNotMerged <unmerged_reason> | -notMergedSummary | -equiv? ?-cell <cell_name> | -type {comb | latch | flop | seq | iso | ls}? ?-hinst <hinst_name> | -library | -cell <cell name> | -equiv?",
        ),
        # man1/reportNetGroup.1
        _syn(
            "reportNetGroup",
            "Creates a report that contains net groups and their nets",
            "reportNetGroup ?-help? ?-outfile <fileName>?",
        ),
        # man1/reportNetStat.1
        _syn(
            "reportNetStat",
            "",
            "reportNetStat",
        ),
        # man1/reportPathGroupOptions.1
        _syn(
            "reportPathGroupOptions",
            "",
            "reportPathGroupOptions ?-help?",
        ),
        # man1/reportPinAssignStatistics.1
        _syn(
            "reportPinAssignStatistics",
            "Generates the pin QoR data for a specified partition(s)",
            "reportPinAssignStatistics ?-help? ?-maxFanOut <fanOutCount>? ?-maxRegisterFanOut <registerFanOutCount>? ?-outFile <pinQoRFileName>? ?-hinst <hinstNameList> | -ptn <ptnNameList>?",
        ),
        # man1/reportPinDensityMap.1
        _syn(
            "reportPinDensityMap",
            "Generates a map that uses colors to represent pin density and generates a pin density report",
            "reportPinDensityMap ?-help? ?-displayStep <step_value>? ?-gridInMicron <micron>? ?-gridInRow <numberRow>? ?-threshold <density>?",
        ),
        # man1/reportPipeline.1
        _syn(
            "reportPipeline",
            "The command can be used for analysis before the flops exist in the netlist; or it can be used post flop insertion to either report expected average wire-length between stages of a pipeline net group, or to report the achieved average distance between the placed stages of the pipeline",
            "reportPipeline ?-help? ?-netGroup <netGroupNames>? ?{-spacing <value > | -timingBased | -psPMBased } -file <fileName>?",
        ),
        # man1/reportPowerDomain.1
        _syn(
            "reportPowerDomain",
            "Reports information about power domains",
            "reportPowerDomain ?-help? ?-bindLib? ?-file <outFile>? ?-inst <inst_name>? ?-isoInst? ?-module {list_of_modules}? ?-net <net_name>? ?-partitionHports <pin> | <port> | <hpin>+? ?-pgNet? ?-pin? ?-powerDomain <powerDomainName >?-checkPgScope?? ?-powerDomainBoundaryPort <string>? ?-powerDomainCoverage <pd1 pd2>? ?-shifter? ?-supplyCrossing <supp1 supp2>? ?-verbose? ?-voltage?",
        ),
        # man1/reportPowerRoute.1
        _syn(
            "reportPowerRoute",
            "Reports the cut ratio when two types of cuts are inserted between two parallel followpin rails with ed‐ itPowerVia -followpin_via_stapling to maximize the effective number of cuts",
            "reportPowerRoute ?-help? ?-followpin_cut_ratio {<cutClass1 weight1 cutClass2 weight2>}? ?-net <string>?",
        ),
        # man1/reportPowerSwitch.1
        _syn(
            "reportPowerSwitch",
            "Reports each power switch instance, the location, and pin/net connections",
            "reportPowerSwitch ?-help? -outFile <file_name>",
        ),
        # man1/reportProbePins.1
        _syn(
            "reportProbePins",
            "Generates a report of all probe pins that are used for package-level design and testing",
            "reportProbePins ?-help?",
        ),
        # man1/reportRC.1
        _syn(
            "reportRC",
            "Calculates the first and second RC values",
            "reportRC ?-help? <fileName> ?-inst <string>? ?-layer <string>? ?-max_second_rc <float>?",
        ),
        # man1/reportRoute.1
        _syn(
            "reportRoute",
            "",
            "reportRoute ?-help? ?-clock? ?-em? ?-ndr? ?-selected_net_only? ?-via_pillar?",
        ),
        # man1/reportRouteTypeConstraints.1
        _syn(
            "reportRouteTypeConstraints",
            "Reports the route type constraints that are being added on nets during the Innovus flow",
            "reportRouteTypeConstraints ?-help? ?-file <fileName>? ?-svr? ?-svrOnly? ?-threshold value? ?-summary | -detailed? ?-detailed ?-timing??",
        ),
        # man1/reportScanCell.1
        _syn(
            "reportScanCell",
            "Displays a list of the scan cells that are read from the timing library or by the specifyScanCell command",
            "reportScanCell",
        ),
        # man1/reportScanChainPartition.1
        _syn(
            "reportScanChainPartition",
            "Generates a report that lists compatible scan chains in scan chain partitions",
            "reportScanChainPartition ?-help?",
        ),
        # man1/reportSeedConnection.1
        _syn(
            "reportSeedConnection",
            "Reports the number of connections between user-specified seeds",
            "reportSeedConnection ?-help? ?-constraints <filename>? ?-excNetFile <filename>? ?-file <outfile>?",
        ),
        # man1/reportSelect.1
        _syn(
            "reportSelect",
            "Reports the properties of one or more selected objects in the design display area in the main console win‐ dow and the Innovus log file",
            "reportSelect ?-help? -file <filename>",
        ),
        # man1/reportShield.1
        _syn(
            "reportShield",
            "Reports shield coverage for nets routed by the NanoRoute router",
            "reportShield ?-help? ?-crosstie? ?-include_layer? ?-out_file <fileName>? ?-selected? ?-tap_cells? ?-verbose?",
        ),
        # man1/reportShifter.1
        _syn(
            "reportShifter",
            "Reports the level shifters that have been read into or defined for the Innovus software",
            "reportShifter ?-help? ?-cell <cellName>? ?-from <powerDomainName>? ?-to <powerDomainName>? ?-outfile <fileName>? ?-highlight?",
        ),
        # man1/reportSpecialRoute.1
        _syn(
            "reportSpecialRoute",
            "Reports the length of all RDL routes (SPECIALNETS) created with the fcroute command",
            "reportSpecialRoute ?-help? ?<reportName>? ?-center_line? ?-net <netName>? ?-interposer_ndr_check ?-exclude_nets <netName>?? ?-interposer_route ?-exclude_nets <netName>?? ?-interposer_route ??-interposer_layers <layerName>? ?-interposer_route_constraint_file <ircFileName>??? ?-interposer_shielding_ratio ?-exclude_nets <netName>?? ???-by_layer? ?-highlight45layer <layerName>? ?-lengththreshold <value>? ?-resfile <resFileName>? ?-selected? ?-summary? ?-wire_segment? ?-wirelength?? | ?-interposer_ndr_check? | ?-interposer_route? | ?-interposer_shielding_ratio??",
        ),
        # man1/reportTimingLib.1
        _syn(
            "reportTimingLib",
            "Reports the contents of the timing library",
            "reportTimingLib -outfile <fileName> ?-byLib? ?-all | -pin | -threshold | -sibling? ?-lib <library_name>? ?<cellName>?",
        ),
        # man1/reportTranViolation.1
        _syn(
            "reportTranViolation",
            "After timing analysis, reports pins and ports that exceed the transition constraints in the timing constraints file",
            "reportTranViolation ?-help? ?-all | -noGlobalNets? ?-max? ?-min? ?-selNetFile <fileName>? ?-excNetFile <fileName>? ?-significant_digits? ?-useDrcMargin? ?-outfile <fileName>?",
        ),
        # man1/reportTwoPinChain.1
        _syn(
            "reportTwoPinChain",
            "",
            "reportTwoPinChain ?-help? ?-reset | ??-output <fileName>? ?-through <string>? ?-noOverwrite? ?-showAll? ?-strict? ?-tolerance <value>???",
        ),
        # man1/reportUnalignedNets.1
        _syn(
            "reportUnalignedNets",
            "Reports the names of the nets where the pins are not aligned",
            "reportUnalignedNets ?-help? ?-alignDistance <distance>? ?-alignFeedThruPins? ?-considerMacroPinWithinDistance <distance>? ?-ignoreLength <length>? ?-noHighlight? ?-reportAllWithinChannelWidth <width>? ?-rptFile <filename>? ?-statistics? ?-steinerBox? ?-verbose? ??-ptnToPtn {aligned unaligned layerMismatch samePtn nonNbr multiFanout all unplaced none}? ?-topToPtn {aligned unaligned layerMismatch samePtn nonNbr multiFanout all unplaced none}?? ?-pin_file <filename >| -exclude_pin_file <filename>?",
        ),
        # man1/reportUnsnapBlocks.1
        _syn(
            "reportUnsnapBlocks",
            "Reports unsnapped blocks based on the snap preferences (as defined in the Floorplan Tab of the Pref‐ erences form)",
            "reportUnsnapBlocks ?-help?",
        ),
        # man1/reportVoltage.1
        _syn(
            "reportVoltage",
            "This command reports the voltage for the net/pin (term)/inst in the specific view under a specific corner",
            "reportVoltage ?-help? ?-early? ?-inst <string>? ?-late? ?-net <string>? ?-quiet? ?-term <string>? ?-view <string>?",
        ),
        # man1/reportVtInstCount.1
        _syn(
            "reportVtInstCount",
            "Reports the instance distribution across the VT partitions in the design",
            "reportVtInstCount ?-help? ?-area? ?-detailed? ?-leakage? ?-outFile <fileName>?",
        ),
        # man1/reportWire.1
        _syn(
            "reportWire",
            "Creates a report file that contains wire statistics for signal nets with a real wire length or minimum wire length that is greater than the specified threshold ratio",
            "reportWire ?-help? ?<fileName>? ?<threshold>? ?-detail? ?-maxFanout<integer>? ?-minWireLength <float>? ?-sort {ratio wire_length half_perimeter}? ?-summary?",
        ),
        # man1/reportWirePath.1
        _syn(
            "reportWirePath",
            "Extracts the routing topology report in a point-to-point manner (for example between routing layer, wire length, via, resistor, and capacitance)",
            "reportWirePath ?-help? ?-detail? -end <string>?-include_pin? -start <string> ?-tcl ?-no_output??",
        ),
        # man1/reset_all_ccopt_preserved_clock_tree_ports.1
        _syn(
            "reset_all_ccopt_preserved_clock_tree_ports",
            "This command resets all preservation settings that have been specified using theset_ccopt_preserved_clock_tree_port command",
            "reset_all_ccopt_preserved_clock_tree_ports ?-help?",
        ),
        # man1/reset_annotated_check.1
        _syn(
            "reset_annotated_check",
            "",
            "reset_annotated_check ?-clock ?rise | fall?? ?-cond <sdf_condtion>? ?-setup | -recovery? ?-hold | -removal? ?-nochange_high | -nochange_low? ?-rise? ?-fall? {??-from <from_pins>??-to <to_pins>?? | -all} ?<object_list>?",
        ),
        # man1/reset_annotated_delay.1
        _syn(
            "reset_annotated_delay",
            "",
            "reset_annotated_delay {?-all? | ??-from <from_pins>? ?-to <to_pins>?? | ?<object_list>?}",
        ),
        # man1/reset_annotated_transition.1
        _syn(
            "reset_annotated_transition",
            "Resets annotated transitions previously asserted by the set_annotated_transition command",
            "reset_annotated_transition {-all | <port_or_pin_list>}",
        ),
        # man1/reset_aocv_stage_weight.1
        _syn(
            "reset_aocv_stage_weight",
            "",
            "reset_aocv_stage_weight <port_list> ?-early? ?-late?",
        ),
        # man1/reset_case_analysis.1
        _syn(
            "reset_case_analysis",
            "Removes the assertions set by the set_case_analysis command",
            "reset_case_analysis <list_of_ports_or_pins>",
        ),
        # man1/reset_ccopt_config.1
        _syn(
            "reset_ccopt_config",
            "",
            "reset_ccopt_config ?-help? ?-preserve_sink_insertion_delays?",
        ),
        # man1/reset_ccopt_preserved_clock_tree_port.1
        _syn(
            "reset_ccopt_preserved_clock_tree_port",
            "This command resets the preservation settings for the specified preserved port that have been specified using the set_ccopt_preserved_clock_tree_port command",
            "reset_ccopt_preserved_clock_tree_port ?-help? {<portname>}",
        ),
        # man1/reset_ccopt_routing_state.1
        _syn(
            "reset_ccopt_routing_state",
            'Resets the status of the CCOpt clock nets to "routed"',
            "reset_ccopt_routing_state ?-help? ?-excluded {<netname1 netname2>.....}? ?-no_delete_routes? ?-reset_preroutes?",
        ),
        # man1/reset_clock.1
        _syn(
            "reset_clock",
            "Removes previously created clock assertions",
            "reset_clock {-all | <clock_list>}",
        ),
        # man1/reset_clock_exclusivity.1
        _syn(
            "reset_clock_exclusivity",
            "Allows to reset the set_clock_exclusivity constraints applied on pins",
            "reset_clock_exclusivity ?-help? <<pin_name>>",
        ),
        # man1/reset_clock_gating_check.1
        _syn(
            "reset_clock_gating_check",
            "",
            "reset_clock_gating_check ?-setup? ?-hold? ?-rise? ?-fall? ?-high | -low? ?<object_list>?",
        ),
        # man1/reset_clock_groups.1
        _syn(
            "reset_clock_groups",
            "Resets clock groups that have been set using the set_clock_groups command",
            "reset_clock_groups ?-help? {-physically_exclusive | -logically_exclusive | -asynchronous} {-name <name_list> | -all}",
        ),
        # man1/reset_clock_latency.1
        _syn(
            "reset_clock_latency",
            "Resets assertions made by previous set_clock_latency commands",
            "reset_clock_latency ?-source? ?-clock <clock_list>? <pin_or_clock_list>",
        ),
        # man1/reset_clock_sense.1
        #   WARNING: unmatched closing bracket ']' at position 70
        _syn(
            "reset_clock_sense",
            "Resets clock sense constraint(s) specified using the set_clock_sense command",
            "reset_clock_sense ?-all? | ??-clocks <clock_list>? <pin_or_port_list>??",
        ),
        # man1/reset_clock_transition.1
        _syn(
            "reset_clock_transition",
            "Removes the clock transition assertions you had set on the specified list of clock waveforms",
            "reset_clock_transition",
        ),
        # man1/reset_clock_tree_latency.1
        _syn(
            "reset_clock_tree_latency",
            "Resets all network clock latency set using the set_clock_latency command in the fanout of the specified clock or pins and ports",
            "reset_clock_tree_latency ?<object_list>?",
        ),
        # man1/reset_clock_uncertainty.1
        _syn(
            "reset_clock_uncertainty",
            "Removes the assertions that were made by previous set_clock_uncertainty commands",
            "reset_clock_uncertainty ?-setup? ?-hold? ?-half_cycle_jitter | -full_cycle_jitter? { {-from | -rise_from | -fall_from} <clksig_from_list> {-to | -rise_to | -fall_to} <clksig_to_list> | <pin_or_clock_list> }",
        ),
        # man1/reset_data_check.1
        _syn(
            "reset_data_check",
            "Removes specified data-to-data checks that you have specified using the set_data_check command",
            "reset_data_check {-from | -rise_from | -fall_from} <pin_or_port_list> {-to | -rise_to | -fall_to} <pin_or_port_list> ?-setup? ?-hold? ?-clock <clock_object>?",
        ),
        # man1/reset_disable_clock_gating_check.1
        _syn(
            "reset_disable_clock_gating_check",
            "",
            "reset_disable_clock_gating_check <object_list>",
        ),
        # man1/reset_disable_timing.1
        _syn(
            "reset_disable_timing",
            "Restores timing arcs that were disabled using the set_disable_timing command",
            "reset_disable_timing ?-help? ?-from <pin_name> -to <pin_name>? <object_list>",
        ),
        # man1/reset_drive.1
        _syn(
            "reset_drive",
            "",
            "reset_drive <port_list>",
        ),
        # man1/reset_driving_cell.1
        _syn(
            "reset_driving_cell",
            "",
            "reset_driving_cell ?-rise? ?-fall? ?-min? ?-max? <port_list>",
        ),
        # man1/reset_generated_clock.1
        _syn(
            "reset_generated_clock",
            "Removes generated clock assertions previously created using the create_generated_clock command",
            "reset_generated_clock ?-help? {-all | <clock_list>}",
        ),
        # man1/reset_glitch_derate.1
        _syn(
            "reset_glitch_derate",
            "Removes the derating factors for glitch waveforms that were previously set using the set_glitch_der‐ ate command",
            "reset_glitch_derate ?-help? ?-derate_height? ?-derate_width? ?-glitch_type <string>? ?-instance_pin <string>? ?-offset? ?-pin <string>? ?-view <string>?",
        ),
        # man1/reset_ideal_latency.1
        _syn(
            "reset_ideal_latency",
            "Resets the ideal latency constraints, specified using the set_ideal_latency command, on instance pins or ports",
            "reset_ideal_latency ?-min? ?-max? ?-rise? ?-fall? <object_list>",
        ),
        # man1/reset_ideal_network.1
        _syn(
            "reset_ideal_network",
            "Resets the ideal network constraints, specified using the set_ideal_network command, on pins, ports, or nets",
            "reset_ideal_network <object_list>",
        ),
        # man1/reset_ideal_transition.1
        _syn(
            "reset_ideal_transition",
            "Resets the ideal transition constraint, specified using the set_ideal_transition command, on in‐ stance pins or ports",
            "reset_ideal_transition ?-min? ?-max? ?-rise? ?-fall? <object_list>",
        ),
        # man1/reset_input_delay.1
        _syn(
            "reset_input_delay",
            "",
            "reset_input_delay ?-help? ?-clock <clk_name>? ?-clock_fall? ?-rise? ?-fall? ?-max? ?-min? ?-level_sensitive? <pin_or_port_list>",
        ),
        # man1/reset_instance_library.1
        _syn(
            "reset_instance_library",
            "Resets the settings/binding done using the set_instance_library command",
            "reset_instance_library ?-help?",
        ),
        # man1/reset_load.1
        _syn(
            "reset_load",
            "Resets the existing set_load assertions specified on nets or ports",
            "reset_load <object_list>",
        ),
        # man1/reset_macro_place_constraint.1
        _syn(
            "reset_macro_place_constraint",
            "Resets the macro constraints that are honored by the macro placer",
            "reset_macro_place_constraint ?-help? ?-array? ?-avoid_abut_macro_edge_with_pins? ?-cell_obs? ?-cpg? ?-forbidden_space_to_core? ?-forbidden_space_to_macro? ?-honor_strict_spacing_constraint? ?-horizontal_stacking? ?-instance_orientation? ?-macro_corner_keepout? ?-max_io_pin_group_keep_out? ?-min_space_to_core? ?-min_space_to_macro? ?-parallel_run_length? ?-parallel_run_length_for_stacking? ?-pg_resource_model? ?-power_domain_as_core? ?-same_length_site? ?-track_adjustment? ?-vertical_stacking?",
        ),
        # man1/reset_max_capacitance.1
        _syn(
            "reset_max_capacitance",
            "Resets maximum capacitance limit specified (using the the set_max_capacitance command) on the ob‐ jects in the object list",
            "reset_max_capacitance <object_list>",
        ),
        # man1/reset_max_fanout.1
        _syn(
            "reset_max_fanout",
            "Resets maximum fanout limit specified (using the set_max_fanout command) on the objects in the object list",
            "reset_max_fanout <object_list>",
        ),
        # man1/reset_max_time_borrow.1
        _syn(
            "reset_max_time_borrow",
            "Resets the specified maximum time borrow limit of the specified objects",
            "reset_max_time_borrow <object_list>",
        ),
        # man1/reset_max_transition.1
        _syn(
            "reset_max_transition",
            "",
            "reset_max_transition <object_list>",
        ),
        # man1/reset_min_capacitance.1
        _syn(
            "reset_min_capacitance",
            "Resets minimum capacitance limit specified (using the the set_min_capacitance command) on objects in the object list",
            "reset_min_capacitance <object_list>",
        ),
        # man1/reset_min_fanout.1
        _syn(
            "reset_min_fanout",
            "",
            "reset_min_fanout <object_list>",
        ),
        # man1/reset_min_pulse_width.1
        _syn(
            "reset_min_pulse_width",
            "Resets minimum pulse width constraint on the specified input ports of the top cell and the speci‐ fied modules",
            "reset_min_pulse_width ?-help? <object_list> ?-high? ?-low? ?-waveform_aware_type {absolute | source_width_ratio | all}?",
        ),
        # man1/reset_min_transition.1
        _syn(
            "reset_min_transition",
            "",
            "reset_min_transition <object_list>",
        ),
        # man1/reset_mode.1
        _syn(
            "reset_mode",
            "Resets the Liberty timing library modes for a specified instance",
            "reset_mode ?-type cell? <list_of_modes> <object_list>",
        ),
        # man1/reset_noise_lib_pin.1
        _syn(
            "reset_noise_lib_pin",
            "Allows you to reset any noise property mapping, specified previously using the set_noise_lib_pin command",
            "reset_noise_lib_pin ?-help? ?-all? ?-to <string>?",
        ),
        # man1/reset_output_delay.1
        _syn(
            "reset_output_delay",
            "Resets previously specified output delay assertions",
            "reset_output_delay ?-help? <port_or_pin_list> ?-clock <clock_name>? ?-clock_fall? ?-fall? ?-level_sensitive? ?-max? ?-min? ?-rise?",
        ),
        # man1/reset_parasitics.1
        _syn(
            "reset_parasitics",
            "",
            "reset_parasitics ?-help?",
        ),
        # man1/reset_path_adjust_group.1
        _syn(
            "reset_path_adjust_group",
            "Removes all path adjust groups that are set using the set_path_adjust command for setting path slack adjustment values",
            "reset_path_adjust_group ?-help? ?-name <group_name> | -all?",
        ),
        # man1/reset_path_exception.1
        _syn(
            "reset_path_exception",
            "Removes any previously set path exceptions (or path exception of the specified type) for the given paths",
            "reset_path_exception ?-exact? ?-type {false_path | multicycle | path_delay}? ?-rise? ?-fall? ?{-from | -rise_from | -fall_from} <from_list>? ?{-through | -rise_through | -fall_through} <through_list>? ?{-to | -rise_to | -fall_to} <to_list>? ?-setup | -hold? ?-all?",
        ),
        # man1/reset_path_group.1
        _syn(
            "reset_path_group",
            "Removes the specified path groups or completely removes all the groups",
            "reset_path_group ?-name <group_name>? ?-all?",
        ),
        # man1/reset_physical_context_data.1
        _syn(
            "reset_physical_context_data",
            "Clears the physical context data in the DB",
            "reset_physical_context_data ?-help?",
        ),
        # man1/reset_pll_timing.1
        _syn(
            "reset_pll_timing",
            "Resets the delay offset settings applied to a PLL (phase locked loop) output clock",
            "reset_pll_timing ?-help? <inst_name>",
        ),
        # man1/reset_power_activity.1
        _syn(
            "reset_power_activity",
            "",
            "reset_power_activity",
        ),
        # man1/reset_propagated_clock.1
        _syn(
            "reset_propagated_clock",
            "Removes the propagated clock assertion for the specified clock waveforms or pins",
            "reset_propagated_clock <pin_clock_list >",
        ),
        # man1/reset_property.1
        _syn(
            "reset_property",
            "",
            "reset_property ?-object_type {<object_type>}? {<object_list>} <property_name>",
        ),
        # man1/reset_pulse_clock_max_transition.1
        _syn(
            "reset_pulse_clock_max_transition",
            "Resets the maximum pulse clock transition constraint specified (using the set_pulse_clock_max_transition command) on the pulse generator cells, pulse generator library cells, clocks, and/or cur‐ rent design",
            "reset_pulse_clock_max_transition <object_list>?-transitive_fanout? ?-rise? ?-fall?",
        ),
        # man1/reset_pulse_clock_max_width.1
        _syn(
            "reset_pulse_clock_max_width",
            "",
            "reset_pulse_clock_max_width <object_list> ?-transitive_fanout?",
        ),
        # man1/reset_pulse_clock_min_transition.1
        _syn(
            "reset_pulse_clock_min_transition",
            "",
            "reset_pulse_clock_min_transition <object_list> ?-transitive_fanout? ?-rise? ?-fall?",
        ),
        # man1/reset_pulse_clock_min_width.1
        _syn(
            "reset_pulse_clock_min_width",
            "Resets the minimum pulse clock width constraint specified (using the set_pulse_clock_min_width command) on the pulse generator cells, pulse generator library cells, clocks, and/or current de‐ sign",
            "reset_pulse_clock_min_width <object_list> ?-transitive_fanout?",
        ),
        # man1/reset_resistance.1
        _syn(
            "reset_resistance",
            "Resets the existing set_resistance assertions specified on nets",
            "reset_resistance <net_list>",
        ),
        # man1/reset_sdf_assertions.1
        _syn(
            "reset_sdf_assertions",
            "",
            "reset_sdf_assertions",
        ),
        # man1/reset_sense.1
        _syn(
            "reset_sense",
            "Resets clock sense constraint(s) specified using the set_sense command",
            "reset_sense ?-help? ?-all | ??-clocks <<clock_list>>? <<pin_or_port_list>>??",
        ),
        # man1/reset_spare_insts.1
        _syn(
            "reset_spare_insts",
            "Asserts the specified instance is not a spare gate",
            "reset_spare_insts ?-help? {-cell <cellName> | -inst <instName> | -hinst <hinstName>}",
        ),
        # man1/reset_timing_derate.1
        _syn(
            "reset_timing_derate",
            "Resets derate factors specified on a design or a list of instances (cells, net, or library cells)",
            "reset_timing_derate ?-delay_corner <delayCornerName>? ?-increment? ?<object_list>?",
        ),
        # man1/reset_usf.1
        _syn(
            "reset_usf",
            "Resets the Unified Safety Format (USF) Physical safety information and related database attributes completely",
            "reset_usf ?-help?",
        ),
        # man1/reset_wire_load_mode.1
        _syn(
            "reset_wire_load_mode",
            "",
            "reset_wire_load_mode",
        ),
        # man1/reset_wire_load_model.1
        _syn(
            "reset_wire_load_model",
            "Resets wireload models for the specified list of objects",
            "reset_wire_load_model ?-help? ?{ <list_of_instances_or_ports> }?",
        ),
        # man1/reset_wire_load_selection_group.1
        _syn(
            "reset_wire_load_selection_group",
            "Removes the wireload selection group for the specified list of objects",
            "reset_wire_load_selection_group ?{ <list_of_objects> }?",
        ),
        # man1/resetBusGuideMultiColors.1
        _syn(
            "resetBusGuideMultiColors",
            "Clears the highlighted bus guide colors",
            "resetBusGuideMultiColors",
        ),
        # man1/resetModifiedBudget.1
        _syn(
            "resetModifiedBudget",
            "Resets the budget that was modified using the modifyBudget command",
            "resetModifiedBudget {-ptn <partitionName> | -inst <instanceName>} -pin <pinName> ?-setup | -hold? ?-view <viewName>? ?-help?",
        ),
        # man1/resetMultiColorsHier.1
        _syn(
            "resetMultiColorsHier",
            "Resets the color Id for all or the specified hierarchical instances",
            "resetMultiColorsHier ?-help? ?<colorID> ?<hInstName>??",
        ),
        # man1/resetPathGroupOptions.1
        _syn(
            "resetPathGroupOptions",
            "Resets the parameters of a specified path group, or of all path groups, to their default values",
            "resetPathGroupOptions ?-help? ?<pathGroupName>? ?-early? ?-effortLevel? ?-late? ?-skewingSlackConstraint? ?-slackAdjustment? ?-slackAdjustmentPriority? ?-targetSlack? ?-view?",
        ),
        # man1/resizeBlackBox.1
        _syn(
            "resizeBlackBox",
            "Resizes a blackbox",
            "resizeBlackBox <blackBoxName> ?-help? ?-width <width>? ?-height <height>? ?-aspectRatio <ratio>?",
        ),
        # man1/resizeFloorplan.1
        _syn(
            "resizeFloorplan",
            "Resizes the floorplan while maintaining the relative locations of the existing floorplan",
            "resizeFloorplan ?-help? ?-xSize <xAxisSize>? ?-ySize <yAxisSize>? ?-xPercent <xAxisPercent>? ?-yPercent <yAxisPercent>? ?-undo? ?-pushCore? ?-forceResize?",
        ),
        # man1/restore_ccopt_config.1
        _syn(
            "restore_ccopt_config",
            "Reads the CCOpt configuration from the specified directory path",
            "restore_ccopt_config ?-help?",
        ),
        # man1/restore_db_directory.1
        _syn(
            "restore_db_directory",
            "",
            "restore_db_directory <directory_name>",
        ),
        # man1/restore_db_file_check.1
        _syn(
            "restore_db_file_check",
            "",
            "restore_db_file_check {true | false}",
        ),
        # man1/restore_db_stop_at_design_in_memory.1
        _syn(
            "restore_db_stop_at_design_in_memory",
            "",
            "restore_db_stop_at_design_in_memory { 0| 1}",
        ),
        # man1/restore_db_tool.1
        _syn(
            "restore_db_tool",
            "",
            "restore_db_tool",
        ),
        # man1/restore_db_version.1
        _syn(
            "restore_db_version",
            "",
            "restore_db_version <string>",
        ),
        # man1/restore_module_model.1
        _syn(
            "restore_module_model",
            "Restores a design from a default module model repository",
            "restore_module_model ?-help? ?-dynamic_view <string>? ?-hold_views <string>? ?-leakage_view <string>? ?-lef_files <string>? ?-mmmcFile <string>? ?-noTiming? ?-noTimingGraph? ?-setup_views <string>? ?-tag <tag_name>? {<cell_name> | -cell <cell_name>} ?<options>? ?-add_ons {1801 mmmc spef eco latency scan_info timing_context extraction_context pin_assign}?",
        ),
        # man1/restore_power_database.1
        _syn(
            "restore_power_database",
            "Restores any power.db file in the Voltus/Innovus session",
            'restore_power_database ?-help? -file {<file1><file2><file3><...>} ?-hierarchy {<prefix1><prefix2><prefix3><...>}? ?-hierarchy_separator "/"?',
        ),
        # man1/restoreDesign.1
        _syn(
            "restoreDesign",
            "Restores a saved database created by saveDesign in a previous session",
            "restoreDesign ?-help? ?<design>? ?-dynamic_view <analysis_view>? ?-hold_views <hold_views>? ?-leakage_view <analysis_view>? ?-lef_tech_file_map <fileName>? ?-noBinaryConstraint? ?-noTiming? ?-readGlobals <tcl_file_name>? ?-setup_views <setup_views>? ?{{<session>} | {-cellview <lib cell view>}} ?-mmmcFile <fileName>? ?-lef_files <list_of_files>?? ?-noTimingGraph?",
        ),
        # man1/restorePowerSwitch.1
        _syn(
            "restorePowerSwitch",
            "Restores the information stored in the power switch databases",
            "restorePowerSwitch ?-help? ?-file <string>?",
        ),
        # man1/restoreRC.1
        _syn(
            "restoreRC",
            "Restores the RC extraction data that was previously saved either with the saveDesign name -rc or the saveRC command",
            "restoreRC ?-help?",
        ),
        # man1/resume.1
        _syn(
            "resume",
            "Resumes a suspended script from the point where it had stopped",
            "resume ?-help?",
        ),
        # man1/route_ccopt_clock_tree_nets.1
        _syn(
            "route_ccopt_clock_tree_nets",
            "Performs routing of CCOpt clock tree nets using the CCOpt route guides",
            "route_ccopt_clock_tree_nets ?-help? ?-mesh?",
        ),
        # man1/route_ccopt_flexible_htrees.1
        _syn(
            "route_ccopt_flexible_htrees",
            "Routes CCOpt flexible h-tree nets as a separate step after running the synthe‐ size_ccopt_flexible_htrees command",
            "route_ccopt_flexible_htrees ?-help? ?nets <net>+?",
        ),
        # man1/route_fix_ir.1
        _syn(
            "route_fix_ir",
            "Fixes IR Drop (voltage drop) violations with the NanoRoute engine",
            "route_fix_ir ?-help? ?-concurrent_pg_and_signal {0 1}? -ground_net <string> ?-hotspot_boxes {{<lx1 ly1 ux1 uy1>} {<lx2 ly2 ux2 uy2>}...}? ?-irdrop_threshold <float>? -power_net <string> ?-rail_path <string>? -top_layer <string>",
        ),
        # man1/route_fix_signoff_drc.1
        _syn(
            "route_fix_signoff_drc",
            "Fixes sign-off DRC",
            "route_fix_signoff_drc ?-help? ?-fix_rule <ruleName> | -exclude_rule <ruleName>?",
        ),
        # man1/route_opt_design.1
        _syn(
            "route_opt_design",
            "Combines the routing and post-route optimization flows into a single flow",
            "route_opt_design ?-help? ?-drv? ?-hold? ?-ideal_clock? ?-incremental? ?-num_paths <number_of_paths>? ?-opt? ?-out_dir <directory_name>? ?-prefix <file_name_prefix>? ?-route? ?-setup? ?-timing_debug_report?",
        ),
        # man1/route_pg.1
        _syn(
            "route_pg",
            "",
            "route_pg ?-help? ?-check_psdl_only? ?-delete_floating? ?-fast? ?-psdl_file <file_name>? ?-skip_block_pin? ?-skip_partial_overlap_via? ?-skip_physical_pin? ?-skip_via? ?-use_full_pattern? ?-use_namespace? ?-write_psdl <output_file>?",
        ),
        # man1/routeDesign.1
        _syn(
            "routeDesign",
            "Runs routing or postroute via or wire optimization using the NanoRoute router",
            "routeDesign ?-help? ?-backside? ?-bump? ?-fill_area {<x1 y1 x2 y2>}? ?-highFrequency? ?-selected? ?-viaPillarOpt? ???-clockEco? ?-globalDetail? ?-placementCheck | -noPlacementCheck? ??-trackOpt? ?-idealClock?? ?-viaOpt? ?-wireOpt?? | ?-passiveFill??",
        ),
        # man1/routePGPinUseSignalRoute.1
        _syn(
            "routePGPinUseSignalRoute",
            "Routes the secondary power/ground pins of always-on cells to the specified power/ground nets in signal route",
            "routePGPinUseSignalRoute ?help? ?-all? ?-maxFanout number? ?-nets {listofNets}? ?-nonDefaultRule ruleName? ?-pattern {trunk | steiner}? ?-well?",
        ),
        # man1/routePointToPoint.1
        _syn(
            "routePointToPoint",
            "Specifies routing constraints to perform point-to-point routing between I/O pad pins and bumps, and wires and bumps for SPECIALNETS (only) that are defined in the DEF file",
            "routePointToPoint ?-help? ?-constraintFile <filename>? ?-drop_via_in_trace? ?-net {?<netName> | -1? ?<layerName> | -1? ?(<x> <y>)?}? ?-pin {?<instName> | -1? ?<pinName> | -1? ?(<x> <y>)?}? ?-routeLayer {bot?:top?:step?? ?,bot?:top?:step???}? ?-routeStyle {manhattan | doubleBend | diagonal}? ?-spacing <spacingValue>? ?-split {<layerBase> maxWidth:<value> ?gap:<value>? ?style:RIVER|MESH?}? ?-subclass <subclass_name>? ?-width <widthValue>? ?{?-useExactLoc? ?-guidePoint {{<x1> <y1>} {<x2> <y2>}...} ?-keep_partial??} ?-offset {<x> <y>}??",
        ),
        # man1/run_abstract.1
        _syn(
            "run_abstract",
            "Runs abstract to generate LEF from GDSII",
            "run_abstract ?-help? -gds_files <file_list> ?-gen_script_only <file.il>? ?-lib_files <file_list>? ?-output_lef_file <file.lef>? ?-run_script_only <file.il>? ?-verilog_stub_files <file_list>?",
        ),
        # man1/run_pegasus_drc.1
        _syn(
            "run_pegasus_drc",
            "Calls the Cadence Pegasus application to check DRC rules with a sign-off Pegasus rule deck",
            "run_pegasus_drc ?-help? <pvlFile> ?-area {<x1 y1 x2 y2>}? ?-dp <N>? ?-error <integer?> ?-gds_file <fileName> | -oasis_file <fileName>? -mapfile <fileName> ?-merge <list_files>? ?-noclean? ?-oa_view <view_name>? ?-output <fileName>? ?-repRoutingOnly? ?-report <string>? ?-stream_out? ?-units <integer>? ?-version? ?-work_directory <working_directory>?",
        ),
        # man1/run_pvs_drc_rules.1
        _syn(
            "run_pvs_drc_rules",
            "Calls the Cadence Physical Verification System application to check DRC rules with a sign-off PVS rule deck",
            "run_pvs_drc_rules ?-help? <pvlFile > ?-area {<x1 y1 x2 y2>}? ?-dp <N>? ?-error <integer>? ?-extraPvsOptions <pvs_option_string>? ?-gds_file <fileName> | -oasis_file <fileName>? -mapfile <fileName> ?-merge <list_files>? ?-noclean? ?-oa_view <view_name>? ?-output <fileName>? ?-repRoutingOnly? ?-report <string>? ?-stream_out? ?-units <integer>? ?-version? ?-work_directory <working_directory>?",
        ),
        # man1/run_vsr.1
        _syn(
            "run_vsr",
            "Launches the Virtuoso Space-based Router (VSR) from Innovus™ Implementation System",
            "run_vsr ?-help? ?-log_file <fileName>? ?-no_taper_to_pinwidth? ?-post_load_script <scriptname>? ?-pre_load_script <scriptname>? ?-remove_existing_route? ?-route_type_order {bus diffPair match nets shield}? ?-run_VSR_Script <scriptname>? ?-share_shields? ?-sel_net <list_of_selected_nets> | -incl_net_type {bus diffPair match nets shield} | -nets_file <fileName>?",
        ),
        # man1/runCLP.1
        _syn(
            "runCLP",
            "Verifies the current design with the power intent file (CPF and 1801) using Conformal Low Power (CLP)",
            "runCLP ?-cpf <fileName>? ?-cmd <cmdFile>? ?-extraLib <lib …>? ?-extraVlog <fileName …>? ?-post_synthesis? ?-setupOnly? ?-useEEQCellWithLibertyInfo? ?-user_config <ConfigurationFile>?",
        ),
        # man1/save_abstract.1
        _syn(
            "save_abstract",
            "Generates hierarchical design abstract information for the current block-level design",
            "save_abstract ?-help? ?-PGpinLayers <layerNameList>? ?-cutObs? ?-cutObsMinSpacing? ?-extractBlockObs? ?-extractBlockPGPinLayers <layerNameList>? ?-lib <lib>? ?-specifyTopLayer <topLayerName>? ?-stripePin {top all none}? ?-view <view>?",
        ),
        # man1/save_ccopt_config.1
        _syn(
            "save_ccopt_config",
            "Writes the CCOpt configuration to the specified directory",
            "save_ccopt_config ?-help? <output_path>",
        ),
        # man1/save_cmd_file_limit.1
        _syn(
            "save_cmd_file_limit",
            "",
            "save_cmd_file_limit <limit>",
        ),
        # man1/save_db_restrict_under_batch_mode.1
        _syn(
            "save_db_restrict_under_batch_mode",
            "",
            "save_db_restrict_under_batch_mode {true | false}",
        ),
        # man1/save_global.1
        _syn(
            "save_global",
            "Saves the current global variable settings in a file",
            "save_global ?-help? <file_name>",
        ),
        # man1/save_path_categories.1
        _syn(
            "save_path_categories",
            "Saves the selected categories in a path category file",
            "save_path_categories ?-help? -filename <filename>",
        ),
        # man1/saveBlackBox.1
        _syn(
            "saveBlackBox",
            "Creates a blackbox LEF file containing the pin definitions and obstructions",
            "saveBlackBox ?-help? {<instName> | -all} ?-5.6? ?-lefFile <string>?",
        ),
        # man1/saveColorPreference.1
        _syn(
            "saveColorPreference",
            "Saves color preferences for the Innovus main display as specified in the Color Preferences form",
            "saveColorPreference ?-help? ?-dir <string>? ?-include_customized? -name <string>",
        ),
        # man1/saveDesign.1
        _syn(
            "saveDesign",
            "Saves the complete design database in the native Innovus format if fileName is specified, or as an OpenAccess database (OA DB) if -cellview or -view are specified",
            "saveDesign ?-help? ?-addTiming? ?-current_top_cell_only? ?-mmmc2? ?-noFill? ?-no_pvs_fill? ?-skip_file {metric cmd}? ?-no_wait <out_file>? {{<fileName> } | {{{-cellview {<libname> <cellname> <viewname>} | -view <viewname>} ?-saveRestoreFile <file_name>? ?-oaUsedLibsOnly | -oaLibs?} }} ?-timingGraph ?-noConstraint?? ??-user_path ?-keep_input_path??? ?-tcon? ?-rc? ?-libs? ?-lib2ldb? ?-def? ?-verilog? ?-tgz?",
        ),
        # man1/saveDrc.1
        _syn(
            "saveDrc",
            "Saves DRC violation markers in the specified file",
            "saveDrc ?-help? <fileName>?-force? ?-selected?",
        ),
        # man1/saveExcludeNet.1
        _syn(
            "saveExcludeNet",
            "Reports the list of nets that are excluded from delay calculation",
            "saveExcludeNet ?-help? -file <fileName>",
        ),
        # man1/saveFPlan.1
        _syn(
            "saveFPlan",
            "Saves the floorplan information to a file",
            "saveFPlan <file> ?-help? ?-noName? ?-objType {macro | pin | bndry | special_route | pin_constraint}?",
        ),
        # man1/saveHInstColor.1
        _syn(
            "saveHInstColor",
            "Saves the current color setting for a hierarchical instance from the Module Color Preference form to a file",
            "saveHInstColor ?-help? <fileName>",
        ),
        # man1/saveIoFile.1
        _syn(
            "saveIoFile",
            "Saves the current I/O information to a Version:3 file by default",
            "saveIoFile ?-help? ?-v2? ?-locations | -byOrder? ?-includeCellName? ?-only_selected_bump? ?-temp ?-ioOrder {default | clockwise | counterclockwise}?? ?-relativeOrient?",
        ),
        # man1/saveModel.1
        _syn(
            "saveModel",
            "Saves block level design information for top level implementation",
            "saveModel ?-help? -dir <string> ?-ilm? ?-sdf? ?-spef? ?-stream ?-mapFile string??-outputMacros??",
        ),
        # man1/saveNetlist.1
        _syn(
            "saveNetlist",
            "Writes a netlist file of the design",
            "saveNetlist",
        ),
        # man1/saveOaBlackboxes.1
        _syn(
            "saveOaBlackboxes",
            "Saves the specified blackbox abstracts, using the OpenAccess database format",
            "saveOaBlackboxes ?-help? -cell <list_of_cells> -lib <libName> ?-view <viewName>?",
        ),
        # man1/savePartition.1
        _syn(
            "savePartition",
            "Saves the partition information to the current directory or a specified directory",
            "savePartition ?-help? ?<partitionName> {<list>}? ?-fplan? ?-verilog? ??-dir <dirName>? ?-module_model_tag <tag_name>??{?-noFPlan | { ?-noNetlist? ?-savePlacement? }??-def_netlist_for_eco | {?-def ?-savePlacement??}? ?-defNoCutRow? ?-ptnSite? ?-topLevelNoPtnModule? } | { { ?-ptnLib <ptnLibName>? ?-ptnView <ptnViewName>? ?-topView <topViewName>? } }?? ?-def_no_std_cells? ?-def_no_trial_route?",
        ),
        # man1/savePowerSwitch.1
        _syn(
            "savePowerSwitch",
            "Stores the power switch database information, which can later be restored in the same floorplan through the restorePowerSwitch command",
            "savePowerSwitch ?-help? ?-outFile <string>?",
        ),
        # man1/savePreference.1
        _syn(
            "savePreference",
            "Saves the preference file",
            "savePreference ?-help? ?-include_window_font? {?-directory {home current} | -file_name <PreferenceFileName>?}",
        ),
        # man1/savePtnPin.1
        _syn(
            "savePtnPin",
            "Saves the pin assignment information for one or more partitions",
            "savePtnPin ?-help? {-ptn <partitionName> | -all | -design | -selected} <fileName>",
        ),
        # man1/saveRC.1
        _syn(
            "saveRC",
            "Saves the RC extraction data in the specified directory",
            "saveRC ?-help?",
        ),
        # man1/saveRouteGuide.1
        _syn(
            "saveRouteGuide",
            "Saves the routing information to a route guide format file",
            "saveRouteGuide ?-help? ?-rguide <routeGuideFileName>? ?-selNetFile <selNetFileName>?",
        ),
        # man1/saveSignalStormConstraint.1
        _syn(
            "saveSignalStormConstraint",
            "Translates constraint information from the Innovus software, such as boundary slews and loads, into signalStorm constraint syntax, and outputs it into a specified file",
            "saveSignalStormConstraint ?-help? -outfile <fileName>",
        ),
        # man1/saveSpecialRoute.1
        _syn(
            "saveSpecialRoute",
            "Saves special route information in a file",
            "saveSpecialRoute ?-help? <filename>",
        ),
        # man1/saveTimingBudget.1
        _syn(
            "saveTimingBudget",
            "Saves the previously derived timing budgets to a specified directory",
            "saveTimingBudget ?-help? ?-dir <dirName>? ?{<instList>}? ?-inst <string> | -ptn <string>? ?-module_model_tag <string>?",
        ),
        # man1/saveWhatIfConstraints.1
        _syn(
            "saveWhatIfConstraints",
            "Saves the what-if timing constraints in Design Compiler format",
            "saveWhatIfConstraints ?<blackBoxCellName>? ?-pt | -dc? ?-dir <dirName>? ?-filePrefix <prefix>?",
        ),
        # man1/saveWhatIfTimingAssertions.1
        _syn(
            "saveWhatIfTimingAssertions",
            "Writes timing arcs to the specified file or Tcl list",
            "saveWhatIfTimingAssertions ?<blackBoxCellName>? -outfile <fileName> | -tclList",
        ),
        # man1/saveWhatIfTimingModel.1
        _syn(
            "saveWhatIfTimingModel",
            "Saves the specification of black boxes or black blobs at the top level, including the timing arc specifications in the dotlib library file format",
            "saveWhatIfTimingModel ?-help? <blackBoxCellName> ?-outfile <fileName>?",
        ),
        # man1/saveWorkspace.1
        _syn(
            "saveWorkspace",
            "Saves the named workspace to the specified directory",
            "saveWorkspace ?-help? -name <workspaceName> ?-dir <directory>?",
        ),
        # man1/scale_what_if_capacitance.1
        _syn(
            "scale_what_if_capacitance",
            "Scales the intrinsic cell capacitance value to determine how much additional capacitance can be added in a region to reduce dynamic IR drop",
            "scale_what_if_capacitance ?-help? -reset | {{-global | -region <x1 y1 x2 y2> | -cell <cell_name> | -instance <inst_name>| -file <filename>} ?-instrinsic_cap <value>? ?-loading_cap <value>? ?-grid_cap <value>? ?-add? ?-layer <name>? ?-net <net_name>? }",
        ),
        # man1/scale_what_if_current.1
        _syn(
            "scale_what_if_current",
            "Scales current to do what-if analysis for a hierarchical partition and assess its effect on IR drop",
            "scale_what_if_current ?-help? ?-hierarchy <hier_name> | -region <x1 y1 x2 y2> | -global | -inst_list <filename>? ?-scale_clock_network? ?-scale <value> | -current <value>? ?-net <net_name>? ?-reset?",
        ),
        # man1/scale_what_if_resistance.1
        _syn(
            "scale_what_if_resistance",
            "Scales resistance globally or in a region to determine how much resistance can be modified in a region to reduce the entire IR drop",
            "scale_what_if_resistance ?-help? -reset | {-net <netname> {-global | -region <x1 y1 x2 y2> | -instance <instancename> | -cell <cellname> | -file <filename>} ?-scale value | -scale_ron {<R_ON_scale_factor> | R_OFF}? ?-auto_scale_adjacent_via_layers {true | false}? ?-layer {<layername>| all}? }",
        ),
        # man1/scanReorder.1
        _syn(
            "scanReorder",
            "Reorders the scan cells after running placement",
            "scanReorder ?-help? ?-addScanPortPrefix <prefix>? ?-clkAware {true|false}? ?-preferH {true|false}? ?-preferV {true|false}? ?-keepPDPorts {true|false}? ?-scanEffort {low|medium|high|auto}? ?-skipMode {skipNone|skipBuffer}?",
        ),
        # man1/scanTrace.1
        _syn(
            "scanTrace",
            "Records the total number of elements in the scan chain in the log file, and records the starting and ending scan points if the -verbose option is used",
            "scanTrace ?-help? ?-compLogic | -noCompLogic? ?-lockup | -noLockup? ?-verbose?",
        ),
        # man1/script_search_path.1
        _syn(
            "script_search_path",
            "",
            "script_search_path",
        ),
        # man1/select_bump.1
        _syn(
            "select_bump",
            "Enables you to select bumps in different ways",
            "select_bump ?-help? ?-alternate {row column}? ?-area {{x1 y1 x2 y2} ...}? ?-assigned? ?-bump_cell {<cell_list>}? ?-bumps {<bump_list>}? ?-floating? ?-max_distance_to_side <distance>? ?-nets {<net_list>}? ?-side {top bottom left right}? ?-start_lower_left? ?-type {signal power ground}?",
        ),
        # man1/select_highlighted.1
        _syn(
            "select_highlighted",
            "Selects highlighted objects",
            "select_highlighted ?-help? ?-type <string>?",
        ),
        # man1/select_obj.1
        _syn(
            "select_obj",
            "Selects the object or the list of objects for putting into a set",
            "select_obj ?-help? <any_object>+",
        ),
        # man1/select_row.1
        _syn(
            "select_row",
            "Selects the specified row(s), enabling you to issue an additional command for the row",
            "select_row ?-help? ?-all | -name <string> | -site <string>?",
        ),
        # man1/selectBusGuide.1
        _syn(
            "selectBusGuide",
            "Selects a bus guide segment",
            "selectBusGuide ?-help? ?-all? ?-area {<x1><y1><x2><y2>}? ?-direction {H | V}? ?-layer { <id> | <id1> : <id2> }? ?-netGroup {<netGroup> | {<list_of_net_groups>}}?",
        ),
        # man1/selectBusGuideSegment.1
        _syn(
            "selectBusGuideSegment",
            "Selects a bus guide segment with its specified bounding box",
            "selectBusGuideSegment ?-help? ?-box <x1><y1><x2><y2>? ?-layer {<id> | <id1>:<id2>}? ?-netGroup {<netGroup>}?",
        ),
        # man1/selectGroup.1
        _syn(
            "selectGroup",
            "Selects a group",
            "selectGroup ?-help? <groupName>",
        ),
        # man1/selectInst.1
        _syn(
            "selectInst",
            "Selects an instance and highlights it in the design display window",
            "selectInst ?-help? <instName> | {<list_of_instNames>}",
        ),
        # man1/selectInstByCellName.1
        _syn(
            "selectInstByCellName",
            "Selects instances and hierarchical instances by cell name",
            "selectInstByCellName ?-help? <cellName>",
        ),
        # man1/selectInstOnNet.1
        _syn(
            "selectInstOnNet",
            "Selects an instance on a net",
            "selectInstOnNet ?-help? <netName>",
        ),
        # man1/selectIOPin.1
        _syn(
            "selectIOPin",
            "Selects an I/O pin",
            "selectIOPin ?-help? <pinName>",
        ),
        # man1/selectModule.1
        _syn(
            "selectModule",
            "Selects the specified module",
            "selectModule ?-help? <name>",
        ),
        # man1/selectNet.1
        _syn(
            "selectNet",
            "Selects a net and highlights it in the design display window",
            "selectNet ?-help? {<netName> | {<list_of_netNames>} | -allDefClock | -clock | -nonDefaultRule | -shield}",
        ),
        # man1/selectObjByProp.1
        _syn(
            "selectObjByProp",
            "Logs the select operations performed through the Find/Select Object form (View -- Find/Select Object)",
            "selectObjByProp ?-help? {Instance Pin Net Module InstanceGroup Bump} expression< >",
        ),
        # man1/selectPGPin.1
        _syn(
            "selectPGPin",
            "Selects power/ground pins as per the specified parameters and reports the number of selected power/ground pins",
            "selectPGPin ?-help? ?-area <llx lly urx ury>? ?-net <netName>? ?-layer <layerId> | {<layerIdList>}? ?-all?",
        ),
        # man1/selectPin.1
        _syn(
            "selectPin",
            "Selects the specified pin",
            "selectPin ?-help? <name>",
        ),
        # man1/selectPtnPinGuide.1
        _syn(
            "selectPtnPinGuide",
            "Selects a partition pin guide and highlights it in the design display window",
            "selectPtnPinGuide ?-help? <x1 y1 x2 y2> <pinGuideName> <metalLayer> <minSpace> ?<pinGroupCell>?",
        ),
        # man1/selectRouteBlk.1
        _syn(
            "selectRouteBlk",
            "",
            "selectRouteBlk ?-help? ?-box <llx lly urx ury>?",
        ),
        # man1/selectSecondaryPGNet.1
        _syn(
            "selectSecondaryPGNet",
            "Selects Power/Ground (P/G) net wire segments from specified instances",
            "selectSecondaryPGNet ?-help? -insts <inst>+ {-net <net_name> | -pin <pin_name>}",
        ),
        # man1/set_abstract_mode.1
        _syn(
            "set_abstract_mode",
            "Sets options for the run_abstract command",
            "set_abstract_mode ?-help? ?-reset? ?-abstract_blockage_cut_around_pin <layer_list>? ?-antenna_connectivity {<layer1> <connect_layer> <layer2>}? ?-antenna_diffusion_geom {{<layer_name>} {<logical_expression>}}? ?-antenna_gate_geom {{<layer_name>} {<logical_expression>}}? ?-blockage_detailed_layers <layer_list>? ?-boundary_layers<layer_list>? ?-cell_symmetry {R0 | X | Y | R90 | X Y | X R90 | Y R90 | X Y R90}? ?-export_lef_version {5.3 | 5.4 | 5.5 | 5.6 | 5.7 | 5.8}? ?-extract_layers_power <layer_list>? ?-extract_layers_signal<layer_list>? ?-extract_pin_layers_power<layer_list>? ?-extract_pin_layers_signal <layer_list>? ?-input_cell_type {std | io | block}? ?-input_gds_layer_map_file <file.map>? ?-input_lef_tech_file <file.lef>? ?-keep_temp_files {true|false}? ?-pins_analog_names <pattern>? ?-pins_clock_names <pattern>? ?-pins_ground_names <pattern>? ?-pins_output_names <pattern>? ?-pins_power_names <pattern>? ?-pins_text_pin_map <pattern>? ?-pre_skill<file.il>? ?-selected_cells <pattern>? ?-site_name<site_names>? ?-verbose {true | false}?",
        ),
        # man1/set_active_clocks.1
        _syn(
            "set_active_clocks",
            "Defines a list of active clocks in the design",
            "set_active_clocks ?-help? active_clock_list | all_clocks",
        ),
        # man1/set_add_target_pg_mode.1
        _syn(
            "set_add_target_pg_mode",
            "Sets global variables for the add_target_pg command",
            "set_add_target_pg_mode ?-help? ?-allow_weak_connect {true | false}? ?-max_extension_distance <value>? ?-pins {<cell1>:<pin1> <cell1>:<pin2> <cell2>:<pin1> ...}? ?-pins_group_distance <value>? ?-reset? ?-respect_routes {none | fixed | fixed_and_clock | all}? ?-share_resource {true | false}?",
        ),
        # man1/set_advanced_package_options.1
        _syn(
            "set_advanced_package_options",
            "",
            "set_advanced_package_options ?-help? -reset | {?-tool_path <<binary_path>>? ?-net_mapping_file <<filename>>?}",
        ),
        # man1/set_advanced_pg_library_mode.1
        _syn(
            "set_advanced_pg_library_mode",
            "Specifies the advanced power-grid library generation features",
            "set_advanced_pg_library_mode ?-abort_on_extraction_errors {true|false}? ?-add_port_labels <file_name>? ?-assume_foreigns {true | false}? ?-assume_foreigns_mode ?1 | 0?? ?-cell_accura_data_file <file>? ?-cell_per_distributed_host <value>? ?-cell_pinnet_map_file <file>? ?-circuit_include_file <thunder.inc>? ?-cluster_via_rule {{<via_layer1 number_of_equidistant_vias>}...}? ?-cluster_via_size <value>? ?-common_supply_pins {<net_name+>}? ?-create_static_view_from_dynamic_view {true | false}? ?-damping_decap_cell_list {<cell1> <cell2> ..}? ?-damping_decap_frequency <value>? ?-decap_frequency <value>? ?-default_frequency <value>? ?-default_power_voltage <value>? ?-delete_ddv_fsdb_files {true|false}? ?-disable_powergate_rampup_simulation {true | false}? ?-distribute_current_to_switch_net {true | false}? ?-enable_ac_simulation_for_IO_characterization {true | false}? ?-enable_spectre_netlist_flow {true | false}? ?-enable_subconductor_layers {true | false}? ?-enable_via_based_current_distribution {true | false}? ?-esd_cells {<cell_list>}? ?-esd_cells_list_file <filename>? ?-esd_device_list {<device1> <device2> .... <deviceN>}? ?-esd_parameters_file <filename>? ?-esd_pin_list {<pin1> <pin2> .... <pinN>}? ?-exclude_tap_region_file <filename>? ?-extraction_command_file <file>? ?-followpins_tap_layer {lowest_lef_pin_layer | highest_lef_pin_layer | all_lef_pin_layers}? ?-followpins_interface_node_layer {lowest_lef_pin_layer | highest_lef_pin_layer | all_lef_pin_layers}? ?-generate_bulk_pin_cap_separately {true | false}? ?-generate_graybox_data {true | false}? ?-generate_itfnode_x_direction {true | false}? ?-generate_itfnode_y_direction {true | false}? ?-generate_itfnodes_at_via_layer {true | false}? ?-ignore_pg_nets {{<cellname> <netname>}+}? ?-import_xdspf_list_file <filename>? ?-input_port_value_list {<pin1> <value1> <pin2> <value2> ....<pinN> <valueN>}? ?-interface_node_location_file <filename>? ?-lef_layer_ignore_list {<lef_layername> +}? ?-lef_layer_ignore_list_file <filename>? ?-lef_pin_short {true | false}? ?-lef_pin_short_cell_file <file>name? ?-lef_pin_short_cell_list {<cell1> cell2 ...}? ?-libgen_command_file <file>? ?-macro_parasitic_file <filename>? ?-marker_layermap <filename>? ?-mcpu_rerun_count <count>? ?-pgdb_layermap <filename>? ?-pgdb_list_file <filename>? ?-powergate_characterization_voltages { <val1> <val2> <val3> .... }? ?-powergate_multi_enable_characterization_method {enable_all | enable_single}? ?-process_bulk_diffusion_ports {true|false}? ?-remove_emview_dangling_resistor {true|false}? ?-retain_generated_pgv_on_error {true | false}? ?-ron_measure_threshold <value>? ?-schematic {true|false}? ?-skip_switch_net_extraction {true | false}? ?-source_location_file {<filename>}? ?-spectre_path <value>? ?-stdcell_characterization_voltage_value {<val1> <val2> <val3> ...}? ?-strict_input_check {true|false}? ?-tap_node_distance <value>? ?-techgen_dir <directory>? ?-thunder_command_file <file>? ?-trim_metal_layer_map <file>? ?-use_embedded_spectre {true | false}? ?-use_peak_current_distribution {true | false}? ?-verbosity {true | false}? ?-via_based_current_config_file filename? ?-well_cap_file <filename>? ?-xdspf_layermap <filename>? ?-xtc_command_file <filename>? ?-xtc_include_file_for_qdv <filename>?",
        ),
        # man1/set_advanced_rail_options.1
        _syn(
            "set_advanced_rail_options",
            "Provides the ability to include a file that provides a list of additional rail options that should be used for rail analysis",
            "set_advanced_rail_options ?-help? ?-reset? | ??-voltus_rail_include_file_begin <file_name1>? ?-voltus_rail_include_file_end <file_name2>??",
        ),
        # man1/set_analysis_view.1
        _syn(
            "set_analysis_view",
            "Defines the analysis views to use for setup and hold analysis and optimization.You must define at least one setup and one hold analysis view",
            "set_analysis_view ?-help? ?-drv <string>? ?-dynamic <string>? -hold <list_of_views> ?-inactive <string>? ?-leakage <string>? -setup <list_of_views> ?-update_timing?",
        ),
        # man1/set_annotated_check.1
        _syn(
            "set_annotated_check",
            "Annotates the setup, hold, recovery, or removal timing check value between two or more pins of a cell in the current design",
            "set_annotated_check ?-help? <check_value> ?-clock <clock_check>? ?-cond <sdf_condtion>? ?-fall? -from <from_pins> ?-incremental? ?-max? ?-min? ?-rise? -to <to_pins> {-setup | -hold | -recovery | -removal | -nochange_high | -nochange_low}",
        ),
        # man1/set_annotated_delay.1
        _syn(
            "set_annotated_delay",
            "Annotates delay to timing arcs",
            "set_annotated_delay ?-help? <delay_value> ?-cond <expression>? ?-delta_only? ?-fall? ?-increment? ?-max? ?-min? ?-rise? {-net | -cell } {?-from <from_pins>? ?-to <to_pins>?}",
        ),
        # man1/set_annotated_glitch.1
        _syn(
            "set_annotated_glitch",
            "",
            "set_annotated_glitch ?-help? ?-port <string>? ?-vh_glitch <string>? ?-vho_glitch <string>? ?-view <string>? ?-vl_glitch <string>? ?-vlu_glitch <string>?",
        ),
        # man1/set_annotated_transition.1
        _syn(
            "set_annotated_transition",
            "Sets the transition time to be annotated on specified ports or pins in the current design",
            "set_annotated_transition ?-rise | -fall? ?-min | -max? <slew_value> <pin_list>",
        ),
        # man1/set_aocv_interface_path_offset.1
        _syn(
            "set_aocv_interface_path_offset",
            "You can perform path-based inter power domain (IPD) timing analysis by specifying derate offset value for an entire power domain(s) and specific library cell(s) on paths crossing multiple power domains",
            "set_aocv_interface_path_offset <derateOffsetVal> ?<lib_cells>? ?-view <view_name>? ?-delay_corner <dc_corner_name>? ?-cell? ?-net? -power_domain <power_domain_name_list>",
        ),
        # man1/set_aocv_stage_weight.1
        _syn(
            "set_aocv_stage_weight",
            "",
            "set_aocv_stage_weight <stage_weight> <port_list> ?-early? ?-late? ?-input? ?-output?",
        ),
        # man1/set_aocv_thresholds.1
        _syn(
            "set_aocv_thresholds",
            "Limits the minimum AOCV stage depth in graph-based analysis (GBA) mode",
            "set_aocv_thresholds ?-help? ?-min_stage_count_setup <<int>>? ?-min_stage_count_hold <<int>>? ?-reset? ?-slack_pruning_threshold <<float>>? -view <<list_of_views>>",
        ),
        # man1/set_case_analysis.1
        _syn(
            "set_case_analysis",
            "",
            "set_case_analysis ?-help? {0 | 1 | zero | one | rising | falling | rise | fall | non_switching} <list_of_ports_or_pins>",
        ),
        # man1/set_ccopt_preserved_clock_tree_port.1
        _syn(
            "set_ccopt_preserved_clock_tree_port",
            "This command preserves module ports for the flexible h-tree feature",
            "set_ccopt_preserved_clock_tree_port ?-help? {?<portname> ?-location {x y}??}",
        ),
        # man1/set_ccopt_property.1
        _syn(
            "set_ccopt_property",
            "This command is used to set the values of various CCOpt object properties",
            "set_ccopt_property ?-help?",
        ),
        # man1/set_cdb_binding.1
        _syn(
            "set_cdb_binding",
            "Provides an overriding mechanism that allows overriding a UDN to Liberty mapping at the Tempus command file level",
            "set_cdb_binding ?-help? -from <<string>> -to <<string>>",
        ),
        # man1/set_cell_binding.1
        _syn(
            "set_cell_binding",
            "Changes the layout binding for a cell",
            "set_cell_binding ?-help? ?-abstract? ?-lib <list_of_libs>? -cell <list_of_cell_patterns> -view <list_of_views>",
        ),
        # man1/set_cell_power_domain.1
        _syn(
            "set_cell_power_domain",
            "Defines domains for multi-VDD and multi-VSS cells",
            "set_cell_power_domain ?-help? ?-reset? ?-file <file_name>?",
        ),
        # man1/set_clock_exclusivity.1
        _syn(
            "set_clock_exclusivity",
            "Controls filtering of mutually-exclusive clocks at strategic points in the design, e.g., the out‐ put of clock multiplexers",
            "set_clock_exclusivity ?-help? ?-exclude_opposite_polarity? ?-exclude_related_input_pins? ?-exclude_same_polarity? ?-group <clock_list>? ?-inputs <<string>>? <pin_name>",
        ),
        # man1/set_clock_gating_check.1
        _syn(
            "set_clock_gating_check",
            "Specifies or overrides the default setup and hold values for clock gating checks",
            "set_clock_gating_check ?-help? ?<object_list>? ?-fall? ?-hold <hold_value>? ?-rise? ?-setup <setup_value>? ?-high | -low?",
        ),
        # man1/set_clock_groups.1
        _syn(
            "set_clock_groups",
            "Defines clock groups with specified clock definitions",
            "set_clock_groups ?-name <name>? ?-comment <string>? ?-logically_exclusive? | ?-physically_exclusive? | ??-asynchronous? ?-allow_paths?? ?-group <clock_list>?",
        ),
        # man1/set_clock_latency.1
        _syn(
            "set_clock_latency",
            "Specifies ideal internal clock latency and external clock arrival delay",
            "set_clock_latency ?-source ?-early | -late?? ?-rise? ?-fall? ?-jitter <jitter_val>? ?-clock <clock_list>? ?-min? ?-max? ?-clock_gate? <latency> <pin_or_clock_list>",
        ),
        # man1/set_clock_sense.1
        _syn(
            "set_clock_sense",
            "Selects which phase of the clock to filter at the specified point",
            "set_clock_sense ?-help? <pin_or_port_list> ?-clocks <clock_list>? {-positive | -negative | -stop_propagation | -logical_stop_propagation | -stop <type_list>}",
        ),
        # man1/set_clock_transition.1
        _syn(
            "set_clock_transition",
            "Specifies the transition time of sequential endpoints of the ideal clock network",
            "set_clock_transition ?-rise? ?-fall? ?-min? ?-max? ?-min |-max? <slew_time> <clock_list>",
        ),
        # man1/set_clock_uncertainty.1
        _syn(
            "set_clock_uncertainty",
            "Specifies the clock uncertainty (skew) on the clock network",
            "set_clock_uncertainty <uncertainty_value > ?-setup? ?-hold? ?-half_cycle_jitter | -full_cycle_jitter? ?-rise | -fall? { {-from | -rise_from | -fall_from} <clksig_from_list> {-to | -rise_to | -fall_to} <clksig_to_list> | <pin_or_clock_list> }",
        ),
        # man1/set_ctd_win_title.1
        _syn(
            "set_ctd_win_title",
            "Specifies the title of the CTD window",
            "set_ctd_win_title ?-help? <title> ?-id <WindowIDName>?",
        ),
        # man1/set_data_check.1
        _syn(
            "set_data_check",
            "",
            "set_data_check ?-help? <<check_value>> ?-clock <<clock_object>>? ?-hold? ?-setup? {-from <<pin_or_port_list>> | -rise_from <<pin_or_port_list>> | -fall_from <<pin_or_port_list>>} {-to <<pin_or_port_list>> | -rise_to <<pin_or_port_list>> | -fall_to <<pin_or_port_list>>}",
        ),
        # man1/set_default_switching_activity.1
        _syn(
            "set_default_switching_activity",
            "Specifies the switching activity for all primary inputs, nets, and other devices in the design whose activity has not been previously defined through user attributes, the toggle count format (TCF) file, the value change dump (VCD) file, or the tracing of the clock network",
            "set_default_switching_activity ?-black_box_density <value>? ?-black_box_duty <value>? ?-block <master_cell_name>? ?-duty <value>? ?-global_activity <factor>? ?-hier<hierarchy_name>? ?-input_activity <factor>? ?-period <value>? ?-seq_activity <factor>? ?-reset? ?-reset_type { global_activity | seq_activity ... }? ?-clock_gates_enable {<activity_factor>}? ?-icg_ratio <num>? ?-comb_clockgate_ratio <num>? ?-clock_gates_output {<activity_factor>}? ?-clock_gates_output_ratio <num>? ?-clip_activity_to_domain_freq {true | false}? ?-name <activity_name>? ?-macro_activity <factor>?",
        ),
        # man1/set_default_view.1
        _syn(
            "set_default_view",
            "Temporarily changes the default active analysis view to a different active view",
            "set_default_view {-setup <newDefaultSetupView> | -hold <newDefaultHoldView>}",
        ),
        # man1/set_die_model.1
        _syn(
            "set_die_model",
            "Specifies to import a die model on die Interposer or on package netlist",
            "set_die_model ?-help? ?-subckt <subcircuitname>? {-reset | ??-die_instance_name <dieinstname> ?-spice <model_file> ?-mapping <mapping_file>???? }",
        ),
        # man1/set_disable_clock_gating_check.1
        _syn(
            "set_disable_clock_gating_check",
            "",
            "set_disable_clock_gating_check <object_list>",
        ),
        # man1/set_disable_timing.1
        _syn(
            "set_disable_timing",
            "Disables timing propagation through the specified arcs, or a collection of instance-specific arcs that are created using the get_arcs command",
            "set_disable_timing ?-from <pin_name> -to <pin_name>? <object_list>",
        ),
        # man1/set_dont_touch.1
        _syn(
            "set_dont_touch",
            "Prevents the specified object from being modified during optimization",
            "set_dont_touch <object_list> ?true | false?",
        ),
        # man1/set_dont_touch_network.1
        _syn(
            "set_dont_touch_network",
            "Prevents the combinational path connected to the given clocks, pins, or ports from being modified",
            "set_dont_touch_network ?-help? <obj_list>?-no_propagate?",
        ),
        # man1/set_dont_use.1
        _syn(
            "set_dont_use",
            "Prevents the specified design, hierarchical module, or library cells from being used during optimization",
            "set_dont_use ?-help? <object_list>?true | false?",
        ),
        # man1/set_drive.1
        _syn(
            "set_drive",
            "Sets the drive resistance on the specified input and/or bidirectional ports of the top cell",
            "set_drive ?-rise? ?-fall? ?-max? ?-min? <resistance_value> <port_list>",
        ),
        # man1/set_driving_cell.1
        _syn(
            "set_driving_cell",
            "Models the drive capability of an external driver connected to the input port",
            "set_driving_cell ?-library <library_name>? -lib_cell <cell_name> ?-pin <pin_name>? ?-from_pin <from_pin_name>? ?-rise? ?-fall? ?-min? ?-max? ?-multiply_by <factor>? ?-no_design_rule? ?-input_transition_rise <rise_slew_value>? ?-input_transition_fall <fall_slew_value>? <port_list>",
        ),
        # man1/set_dynamic_power_simulation.1
        _syn(
            "set_dynamic_power_simulation",
            "",
            "set_dynamic_power_simulation ?-help? ?-period <value>? ?-resolution <value>? ?-reset? ?-activity_pattern {<time1> <activity_name1> <time2> <activity_name2> .... }?",
        ),
        # man1/set_dynamic_rail_simulation.1
        _syn(
            "set_dynamic_rail_simulation",
            "An optional command to set the parameters for dynamic rail analysis",
            "set_dynamic_rail_simulation ?-help? ?-start <value>? ?-stop <value>? ?-resolution <value>? ?-reset? ?-auto_repeat?",
        ),
        # man1/set_false_path.1
        _syn(
            "set_false_path",
            "Identifies false paths in a design, and breaks or disables specific instance timing arcs in a design",
            "set_false_path ?-hold | -setup? ?-rise? ?-fall? {?{-from | -rise_from | -fall_from} <from_list>? ?{-through | -rise_through | -fall_through} <through_list>? ?{-to | -rise_to | -fall_to} <to_list>?}",
        ),
        # man1/set_fanout_load.1
        _syn(
            "set_fanout_load",
            "Specifies the fanout load on a set of ports",
            "set_fanout_load ?-help? <fanout_load> <port_list>",
        ),
        # man1/set_glitch_derate.1
        _syn(
            "set_glitch_derate",
            "Sets the derating factors for glitch waveforms and determines the effect of on-chip variation on noise",
            "set_glitch_derate ?-help? ?-derate_height <float>? ?-derate_width <float>? ?-glitch_type <string>? ?-instance_pin <string>? ?-offset <float>? ?-pin <string>? ?-view <string>?",
        ),
        # man1/set_glitch_threshold.1
        _syn(
            "set_glitch_threshold",
            "",
            "set_glitch_threshold ?-help? ?-cell <string>? ?-failure_point {none | input | internal | last}? ?-glitch_type {both | vl | vh | vlu | vho | vl_vh | vlu_vho}? ?-library_pins <string>? ?-nets <string>? ?-pins <string>? ?-pin_type {clock | data | latch | all}? ?-threshold_type {failure | reporting | propagation}? -value <float> ?-views <string>?",
        ),
        # man1/set_global.1
        _syn(
            "set_global",
            "",
            "set_global <global_variable_name> <value>",
        ),
        # man1/set_global_always_keep.1
        _syn(
            "set_global_always_keep",
            "Saves the specified UDM variable to the .global file",
            "set_global_always_keep ?-help?",
        ),
        # man1/set_ideal_latency.1
        _syn(
            "set_ideal_latency",
            "Specifies the ideal latency to use for input or output leaf-cell pins and top-level ports that are part of an ideal network",
            "set_ideal_latency ?-help? ?-min? ?-max? ?-rise? ?-fall? <latency_value> <object_list>",
        ),
        # man1/set_ideal_network.1
        _syn(
            "set_ideal_network",
            "Identifies driver pins or ports as sources of an ideal network",
            "set_ideal_network <object_list> ?-no_propagate?",
        ),
        # man1/set_ideal_transition.1
        _syn(
            "set_ideal_transition",
            "Specifies the ideal transition to use for input or output leaf-cell pins and top-level ports that are part of an ideal network",
            "set_ideal_transition ?-min? ?-max? ?-rise? ?-fall? <transition_time> <object_list>",
        ),
        # man1/set_input_delay.1
        _syn(
            "set_input_delay",
            "Defines the arrival time relative to a clock edge on input ports or internal input pins",
            "set_input_delay ?-clock <clock_name>? ?-clock_fall? ?-rise? ?-fall? ?-max? ?-min? ?-add_delay? ?-network_latency_included? ?-source_latency_included? ?-reference_pin <pin_name>? ?-level_sensitive? <delay_value> <port_or_pin_list>",
        ),
        # man1/set_input_transition.1
        _syn(
            "set_input_transition",
            "Specifies the slew time for a port on the top level module",
            "set_input_transition ?-help? ?-min? ?-max? ?-rise? ?-fall? <transition_time> <port_list>",
        ),
        # man1/set_inst_temperature_file.1
        _syn(
            "set_inst_temperature_file",
            "Specifies the instance temperature file to support thermal-aware leakage",
            "set_inst_temperature_file <file> ?-reset?",
        ),
        # man1/set_instance_library.1
        _syn(
            "set_instance_library",
            "Binds a cell library to an instance",
            "set_instance_library ?-help? -library <string> -instance <string> ?-early | -late?",
        ),
        # man1/set_interactive_constraint_modes.1
        _syn(
            "set_interactive_constraint_modes",
            "Puts the software into interactive constraint entry mode for the specified multi-mode multi-corner constraint mode objects",
            "set_interactive_constraint_modes {<list_of_constraint_modes>}",
        ),
        # man1/set_io_thresholds.1
        _syn(
            "set_io_thresholds",
            "Sets the threshold trip-points used for delay calculation to and from the primary I/Os",
            "set_io_thresholds ?-slew_lower_threshold_pct <pctValue>? ?-slew_upper_threshold_pct <pctValue>? ?-input_threshold_pct <pctValue>? ?-output_threshold_pct <pctValue>? ?-slew_lower_threshold_pct_rise <pctValue>? ?-slew_lower_threshold_pct_fall <pctValue>? ?-slew_upper_threshold_pct_rise <pctValue>? ?-slew_upper_threshold_pct_fall <pctValue>? ?-input_threshold_pct_rise <pctValue>? ?-input_threshold_pct_fall <pctValue>? ?-output_threshold_pct_rise <pctValue>? ?-output_threshold_pct_fall <pctValue>?",
        ),
        # man1/set_load.1
        _syn(
            "set_load",
            "Sets the specified capacitance on the defined ports (or nets) of the top cell",
            "set_load ?-max? ?-min? ?-pin_load? ?-wire_load? ?-subtract_pin_load? <capacitance_value> <object_list>",
        ),
        # man1/set_logic_one.1
        _syn(
            "set_logic_one",
            "",
            "set_logic_one",
        ),
        # man1/set_logic_zero.1
        _syn(
            "set_logic_zero",
            "Sets ports or pins to logic 0 in the design",
            "set_logic_zero",
        ),
        # man1/set_macro_place_constraint.1
        _syn(
            "set_macro_place_constraint",
            "Enables you to specify the constraints for placing the macros and standard cells concurrently",
            "set_macro_place_constraint ?-help? ?<array elements>? ?-array <array_name> ?-common_hier <name>??-valid_group_orients {R0 MX MY}? ?-place_order {horizontal vertical}?? ?{-insts <string> | -all_macros } {-orientation <string>} ?-common_hier <name>?? ?-cells <string> {-cell_obs <string> | -track_adjustment <string>}? ?-cpg <string>? ??-max_io_pin_group_keep_out {<depth_value> ?<side_value>?}? ?-forbidden_space_to_core {<unified_value> | <horizontal_value vertical_value>}? ?-forbidden_space_to_macro {<unified_value> | <horizontal_value vertical_value>}? ?-min_space_to_core {<unified_value> | <horizontal_value vertical_value>}? ?-min_space_to_macro {<unified_value> | <horizontal_value vertical_value>}? ?-parallel_run_length {<unified_value> | <vertical_value horizontal_value>}? ?-power_domain_as_core {true | false}? ?-horizontal_stacking {<max_macro_stack_length min_space_between_macro_stack max_space_between_macros>}? ?-vertical_stacking {<max_macro_stack_length min_space_between_macro_stack max_space_between_macros>}? ?-honor_strict_spacing_constraint {true | false}? ?-avoid_abut_macro_edge_with_pins {true | false}? ?-same_length_site <integer>? ?-pg_resource_model {<M1 value1 M2 value2 …>}? ?-macro_corner_keepout {<double_endcap_width> <double_endcap_height>}? ?-halo_sharing {true | false}? ?-parallel_run_length_for_stacking {<unified_value> | <vertical_value horizontal_value>}??",
        ),
        # man1/set_max_capacitance.1
        _syn(
            "set_max_capacitance",
            "Sets the maximum capacitance limit on the specified instance pin, ports of the top cell, the speci‐ fied designs, and/or clock waveforms",
            "set_max_capacitance ?-help? <capacitance_limit> <object_list> ?-clock_path? ?-data_path? ?-fall? ?-override? ?-rise?",
        ),
        # man1/set_max_delay.1
        _syn(
            "set_max_delay",
            "Specifies a maximum delay for a timing path",
            "set_max_delay",
        ),
        # man1/set_max_fanout.1
        _syn(
            "set_max_fanout",
            "Sets the maximum fanout load limit constraint on the specified instance pin, ports of the top cell, the specified designs, and/or clock waveforms",
            "set_max_fanout ?-help? <fanout_limit> <object_list> ?-override?",
        ),
        # man1/set_max_time_borrow.1
        _syn(
            "set_max_time_borrow",
            "Specifies the maximum time that can be borrowed by one stage from the next logic stage following a latch to meet timing constraints",
            "set_max_time_borrow ?-help? <borrow_value> <object_list>?-interface?",
        ),
        # man1/set_max_transition.1
        _syn(
            "set_max_transition",
            "Sets the maximum slew time limit (transition) on the specified instance pin, ports of the top cell, and/or clock waveforms",
            "set_max_transition ?-help? <transition_limit> <object_list> ?-clock_path? ?-data_path? ?-fall? ?-override? ?-rise?",
        ),
        # man1/set_message.1
        _syn(
            "set_message",
            "Specifies to change the message severity levels, INFO, WARNING or ERROR, at the beginning of the message",
            "set_message",
        ),
        # man1/set_metal_density_options.1
        #   WARNING: bracket mismatch: '[' at position 201 closed by '}' at position 257
        #   WARNING: unmatched closing bracket ']' at position 258
        _syn(
            "set_metal_density_options",
            "Sets the parameters for extracting the metal density information",
            "set_metal_density_options ?-metal_density_include_file <filename>? -power_grid_library <pgv_path> ?-reuse_md_db_path <MD_db_path>? -tech_file <tech_file_path> -thermal_conductivity_file <thermal_file> ?-user_defined_metal_density_file <user_defined_md_file>}? ?-vtm_densitytable_tile {<Xint> <Yint>}? ?-vtm_densitytable_tile_size {<Xsize> <Ysize>}? ?-vtm_header_include_file <user_defined_header_content_file>? -vtm_path <output_path>",
        ),
        # man1/set_metal_fill_signoff_mode.1
        _syn(
            "set_metal_fill_signoff_mode",
            "Sets option parameters for the signoff metal fill flow",
            "set_metal_fill_signoff_mode ?-help? ?-and_area_size <size_value>? ?-area {x1 y1 x2 y2}? ?-attach_instance_name <attr_num>? ?-attach_net_name <attr_num>? ?-attach_net_prop {{<prop_name attr_num>} ...}? ?-auto_load_fills? ?-bg? ?-clock? ?-common_blockage {layer_num1 <layer_datatype1> ...}? ?-control <file_name>? ?-delete_area {{<layer_list1>} {<x1 y1 x2 y2>} ...}? ?-delete_point {{<layer_list1>}{<x1 y1>}...}? ?-die_area_as_boundary? ?-dp <n>? ?-dp_timeout <value>? ?-excl_area_size <size_value>? ?-fill_cell <cell_name>? ?-fill_layer {<layers_list>}? ?-fill_output_mode {gdsii | oasis}? ?-layer_map_file <streamOut_map_file>? ?-license_timeout? ?-license_dp_continue? ?-lib_name <library_name>? ?-lsf? ?-master_lsf? ?-merge <list_of_external_stream_files>? ?-min_density <percent1 layer_list1>? ?-net <net_names>? ?-no_structure_name? ?-no_via_fills? ?-offset {<x y>}? ?-output_macros? ?-report_file? ?-reset {parameter_name | all}? ?-rule_file <rule_file_name>? ?-slack_threshold <float>? ?-spacing <float>? ?-spacing_above <float>? ?-spacing_below <float>? ?-stripes <number>? ?-structure_name <structureName>? ?-tech_lib <string>? ?-tech_set <string>? ?-technology <string>? ?-temp_working_dir <work_dir>? ?-trim_effort {high | med | low}? ?-trim_layer {<layers_list>}? ?-trim_mf <spacing_file>? ?-union_density {<percent1 layer_list1> ?{<percent2 layer_list2>}?...}? ?-uniquify_cell_names? ?-units {100 | 200 | 400 | 800 | 1000 | 2000 | 4000 | 8000 | 10000 | 20000}? ?-view_fill? ?-window_size <float>? ?-window_step <float>?",
        ),
        # man1/set_min_capacitance.1
        _syn(
            "set_min_capacitance",
            "",
            "set_min_capacitance ?-help? <capacitance_limit> <object_list> ?-clock_path? ?-data_path? ?-fall? ?-override? ?-rise?",
        ),
        # man1/set_min_delay.1
        _syn(
            "set_min_delay",
            "Specifies a minimum delay for a timing path",
            "set_min_delay <value> ?-combinational_from_to | -ignore_clock_latency? ?{-from |-rise_from | -fall_from} <from_list>? ?-no_segment? ?{-through | -rise_through | -fall_through} <through_list>? ?{-to | -rise_to | -fall_to} <to_list>? ?-rise? ?-fall? ?-comment <string>?",
        ),
        # man1/set_min_fanout.1
        _syn(
            "set_min_fanout",
            "Sets the minimum fanout load limit constraint on the specified input ports of the top cell",
            "set_min_fanout ?-help? <fanout_limit><object_>list ?-override?",
        ),
        # man1/set_min_pulse_width.1
        _syn(
            "set_min_pulse_width",
            "Selects the most restrictive value when multiple minimum pulse width checks are set",
            "set_min_pulse_width ?-help? ?-low? ?-high? ?-waveform_aware_type {absolute | source_width_ratio}? <valueobject_list>",
        ),
        # man1/set_min_transition.1
        _syn(
            "set_min_transition",
            "",
            "set_min_transition ?-help? <transition_limit> <object_list> ?-clock_path? ?-data_path? ?-fall? ?-override? ?-rise?",
        ),
        # man1/set_mode.1
        _syn(
            "set_mode",
            "Specifies the Liberty timing library modes to be active for a specific instance",
            "set_mode ?-type cell? <list_of_modes> <object_list>",
        ),
        # man1/set_model_priority.1
        _syn(
            "set_model_priority",
            "Allows you to define the priority order of models",
            "set_model_priority ?-help? ?-objects <string>? ?-priority_list <string>?",
        ),
        # man1/set_module_model.1
        _syn(
            "set_module_model",
            "Sets or configures specific block model(s) to top-level design",
            "set_module_model ?-help? ?-allow_port_mismatch? ?-dir <model_data_directory>? ?-hold_views <string>? ?-phys_hier? ?-setup_views <string>? ?-tag <flow_tag>? ?-type {flexilm lef ilm pnr pnr_shell boundary_model }? ?-update? {????-cell <moduleName>? ?-default_set_options <string>?? | ?-top <cell_name> ?-logical_only??? ?-add_ons {1801 etm latency pnr_view scan_info spef timing_context extraction_context}?? | -default_dir <default_model_data_directory> | -default_create_options <default_option> | -default_commit_options <string> | -active_rc_corners <list_of_rc_corners> }",
        ),
        # man1/set_multi_die_analysis_mode.1
        _syn(
            "set_multi_die_analysis_mode",
            "Specifies how the multi-die analysis will be performed",
            "set_multi_die_analysis_mode ?-help? -name <analysis_name> -die_list {<die_instance_name1><die_instance_name2>} ?-report_rlrp_path_instance_list <filename>? ?-stacked_die_mapping <Innovus_map_file>?",
        ),
        # man1/set_multi_input_switching_mode.1
        _syn(
            "set_multi_input_switching_mode",
            "Configures multi-input switching (MIS) mode settings",
            "set_multi_input_switching_mode ?-help? ?-disable_lib_cells <<string>>? ?-mis_alignment_mode {0 | 1}? ?-switching_alignment_factor <<float>>? ?-view <string>?",
        ),
        # man1/set_multicycle_path.1
        #   WARNING: unmatched closing bracket ']' at position 353
        #   WARNING: unmatched closing bracket ']' at position 355
        _syn(
            "set_multicycle_path",
            "Specifies multicycle paths between specific timing paths in a design or between clock domains",
            "set_multicycle_path ?-help? <<number_of_cycles>> ?-comment <<string>>? ?-fall? ?-fall_through <<through_list>>? ?-hold? ?-rise? ?-rise_through <<through_list>>? ?-setup? ?-through <<through_list>>? ?-start | -end? ?-from <<from_list>> | -rise_from <<from_list>> | -fall_from <<from_list>>? ?-to <<to_list>?> | -rise_to <<to_list>> | -fall_to <<to_list>?>?",
        ),
        # man1/set_mutex_condition.1
        _syn(
            "set_mutex_condition",
            "",
            "set_mutex_condition ?-help? ?<netNames>?",
        ),
        # man1/set_net_group.1
        _syn(
            "set_net_group",
            "Specifies the list of either power or ground nets that are isolated but need to be analyzed together as a single net",
            "set_net_group ?-help? -reset | {-name <group_name> -type ?power | ground? -nets {<net_list>} }",
        ),
        # man1/set_noise_lib_pin.1
        _syn(
            "set_noise_lib_pin",
            "Allows you to map noise properties of an instance pin to that of different library cell pin",
            "set_noise_lib_pin ?-help? -from <string> -to <string>",
        ),
        # man1/set_normalized_driver_waveform_lib.1
        _syn(
            "set_normalized_driver_waveform_lib",
            "Specifies normalized driver waveform for a library",
            "set_normalized_driver_waveform_lib ?-help? ?-fall_waveform <string>? ?-rise_waveform <string>? -ref_lib <string> -libs <string>",
        ),
        # man1/set_object_color.1
        _syn(
            "set_object_color",
            "Sets the color for objects of the specified name or type",
            "set_object_color ?-help? {?-object_name <InstOrHInstN><ame> | -object_type <typeList>? ?-multicolor | -color_id <colorID>? ?-include_children {off | color | multicolor}? ?-reset?}",
        ),
        # man1/set_offchip_package_trace.1
        _syn(
            "set_offchip_package_trace",
            "Specifies to include RDL0 (off-chip package trace) resistance effects during the static and dynamic rail analysis",
            "set_offchip_package_trace ?-help? -mapping <mapping_file> -name <switched_name> -ploc_file_list <list_of_bump_location_files> ?-reset? -spice <spice_model_name> ?-subckt <subcircuitname>?",
        ),
        # man1/set_output_delay.1
        _syn(
            "set_output_delay",
            "",
            "set_output_delay -clock <clock_name> ?-clock_fall? ?-rise? ?-fall? ?-max? ?-min? ?-add_delay? ?-network_latency_included? ?-source_latency_included? ?-reference_pin <pin_name>? ?-level_sensitive? ?-group_path <group_name>? <delay_value> <port_or_pin_list>",
        ),
        # man1/set_package.1
        _syn(
            "set_package",
            "Specifies the package model information to be used in power rail analysis",
            "set_package ?-help? -reset | {-spice <model_file> ?-mapping <mapping_file>? ?-offset {x y}? ?-die_instance_name <dieinstname>? ?-rotate <rotation_angle_in_degrees>? ?-flip {true | false}? ?-subckt <subcircuitname>? ?-scale <scaling_factor_number>? ?-mapping_type { distributed | lumped }? }",
        ),
        # man1/set_path_adjust.1
        _syn(
            "set_path_adjust",
            "Defines the slack adjustment value for timing paths",
            "set_path_adjust ?-help? <adjust_value> ?-path_adjust_group <path_adjust_group_name>? ?-view <string>? ?-setup | -hold?",
        ),
        # man1/set_path_adjust_group.1
        _syn(
            "set_path_adjust_group",
            "Allows you to specify the path that is used by the set_path_adjust command for setting path slack adjustment values",
            "set_path_adjust_group ?-help? -name <<path_adjust_group_name>> ?-from <<from_list>>? ?-to <<to_list>>? ?-through <<through_list>>?",
        ),
        # man1/set_pba_mode.1
        _syn(
            "set_pba_mode",
            "Enables IPBA infinite depth path-based analysis (IPBA)",
            "set_pba_mode ?-help? ?-reset?",
        ),
        # man1/set_pg_fill_config.1
        _syn(
            "set_pg_fill_config",
            "Sets the parameters of the add_pg_fill command",
            "set_pg_fill_config ?-help? ?-attach_instance_name <attr_num>? ?-attach_net_name <attr_num>? ?-attach_net_prop {{<prop_name attr_num>} ... }? ?-core_license <license_combination>? ?-die_area_as_boundary? ?-dp <n>? ?-dp_timeout <seconds>? ?-extra_options <options>? ?-format {stream oasis}? ?-layer_map_file <streamOut_map_file>? ?-lib_name <library_name>? ?-license_dp_continue? ?-license_timeout <seconds>? ?-merge <list_of_external_stream_files>? ?-no_structure_name? ?-offset {<x y>}? ?-output_macros? ?-pg_fill_config_file <file_name>? ?-pg_hookup_flow {ALL | PG_ONLY | FLOAT_ONLY}? ?-report_file? ?-reset {<parameter_name> |<all>}? ?-stripes <number>? ?-structure_name <structureName>? ?-uniquify_cell_names? ?-units {100 | 200 | 400 | 800 | 1000 | 2000 | 4000 | 8000 | 10000 | 20000}? ?-working_dir <working_directory>?",
        ),
        # man1/set_pg_library_mode.1
        #   WARNING: unclosed bracket '{' at position 316
        _syn(
            "set_pg_library_mode",
            "Specifies what kind of power-grid library will be created",
            "set_pg_library_mode ?-help? ?-add_ploc_cells <cell1> <cell2> ...? ?-bulk_ground_pins { <ground_pin_list> }? ?-bulk_power_pins { <pin1 voltage1 ... pinN voltageN> }? ?-calculate_metal_layer_density {true | false}? ?-cell_decap_file <filename>? ?-cell_list_file <filename>? ?-cell_ploc_details <filename>? -celltype {",
        ),
        # man1/set_pg_nets.1
        #   WARNING: unclosed bracket '{' at position 21
        _syn(
            "set_pg_nets",
            "",
            "set_pg_nets -reset | { ?-help? -net <net_name> -voltage <value> ?-threshold <value>? -tolerance <value>",
        ),
        # man1/set_pll_timing.1
        _syn(
            "set_pll_timing",
            "This command identifies phase locked loop (PLL) insertion delays and the associated generated clock(s) that require adjustment",
            "set_pll_timing ?-help? <inst_name> -feedback_pin <feedback pin name> -output_clock <clock name> -output_pin <output pin name> ?-reference_edge {rise | fall | both}? -reference_pin <reference pin name>",
        ),
        # man1/set_power.1
        _syn(
            "set_power",
            "Specifies the amount of power for all or part of the design",
            "set_power ?<value>? ?-cap <value>? ?-fanout_limit <value>? ?-reset? ?-leakage <value>? ?-pg_pin {<pg_pin>}? ?-pg_net <railname>? ?-pwl? ?-sticky? ?-dynamic_async_mode { <mode_name> }? ?-dynamic_switch_pattern <pattern>? ?-dynamic_switch_event { switching_<events> }? ?-scale_factor <value>? ?-include_ddv_modes {<pattern_list>}? ?-internal? ?-switching <value>? ?-clock {all|<clock_name>}? ?-exclude_clock? ?-exclude_ddv_modes {<pattern_list>}? ?-cell <cell_name><value>? ?-instance <inst_list><value>? ?-pin <pin_name> <pin_power>? ?-force? ?-custom_macro_pwl <filename>? ?-repeat? ?-ascii_power_file<filename>? ?-trigger_time_adjustment <time>? ?–no_propagation? ?-static_mode { <custom_label_name> | <mode_name> }? ?-slew <value>? ?-signal_net <netname>? ?-default_dynamic_pgv_mode { <mode_name> }?",
        ),
        # man1/set_power_analysis_mode.1
        _syn(
            "set_power_analysis_mode",
            "set_power_analysis_mode [-reset] [-add_simulation {true | false}] [-adjust_input_activity_in_iterations {true | false}] [-adjust_macro_activity_in_iterations {true | false}] [-annotation_detail_report {true | false}] [-auto_twf_delay_annotation {true | false}] [-average_rise_fall_cap {true | false}] [-binary_db_name <filename> ] [-block_independent_peakpower {true | false} ] [-boundary_gate_leakage_file <filenname>] [-boundary_gate_leakage_report {true | false}] [-boundary_leakage_cell_property_file <filenname>] [-boundary_leakage_edge_annotation_file <filenname>] [-boundary_leakage_multi_pgpin_support {true | false}] [-boundary_leakage_pessimism_removal {true | false}] [-boundary_leakage_pxe_support {true | false}] [–bulk_pins {<bulk_pin_list>}] [-capacity {low|medium|high}] [-case_insensitive_mapping {true | false}] [-clock_source_as_clock {true | false}] [-comprehensive_automapping {true | false}] [-constant_override {true | false}] [-corner {min|max}] [-create_binary_db {true | false}] [-create_driver_db {true | false}] [-create_gui_db {true | false}] [-current_generation_method { avg | peak }] [-decap_cell_list <cell_list> ] [-default_frequency <value>] [-default_slew <value>] [-default_supply_voltage <value>] [-detailed_view_current_only {true | false} ] [-disable_clock_gate_clipping {true | false} ] [-disable_leakage_scaling {true | false}] [-disable_static {true | false}] [-distribute_switching_power {true | false}] [-distributed_combine_report_format {none | detailed | reduced}] [-distributed_setup <file>] [-domain_based_clipping {true | false} ] [-dynamic_glitch_filter <value>] [-dynamic_scale_clock_by_frequency { <freq_A> <factor_A> <freq_B> <factor_B> <freq_C> <factor_C> ..",
            "set_power_analysis_mode ?-reset? ?-add_simulation {true | false}? ?-adjust_input_activity_in_iterations {true | false}? ?-adjust_macro_activity_in_iterations {true | false}? ?-annotation_detail_report {true | false}? ?-auto_twf_delay_annotation {true | false}? ?-average_rise_fall_cap {true | false}? ?-binary_db_name <filename>? ?-block_independent_peakpower {true | false}? ?-boundary_gate_leakage_file <filenname>? ?-boundary_gate_leakage_report {true | false}? ?-boundary_leakage_cell_property_file <filenname>? ?-boundary_leakage_edge_annotation_file <filenname>? ?-boundary_leakage_multi_pgpin_support {true | false}? ?-boundary_leakage_pessimism_removal {true | false}? ?-boundary_leakage_pxe_support {true | false}? ?–bulk_pins {<bulk_pin_list>}? ?-capacity {low|medium|high}? ?-case_insensitive_mapping {true | false}? ?-clock_source_as_clock {true | false}? ?-comprehensive_automapping {true | false}? ?-constant_override {true | false}? ?-corner {min|max}? ?-create_binary_db {true | false}? ?-create_driver_db {true | false}? ?-create_gui_db {true | false}? ?-current_generation_method { avg | peak }? ?-decap_cell_list <cell_list>? ?-default_frequency <value>? ?-default_slew <value>? ?-default_supply_voltage <value>? ?-detailed_view_current_only {true | false}? ?-disable_clock_gate_clipping {true | false}? ?-disable_leakage_scaling {true | false}? ?-disable_static {true | false}? ?-distribute_switching_power {true | false}? ?-distributed_combine_report_format {none | detailed | reduced}? ?-distributed_setup <file>? ?-domain_based_clipping {true | false}? ?-dynamic_glitch_filter <value>? ?-dynamic_scale_clock_by_frequency { <freq_A> <factor_A> <freq_B> <factor_B> <freq_C> <factor_C> ... }? ?-dynamic_scale_clock_by_name { <clk_A> <factor_A> <clk_B> <factor_B> <clk_C> <factor_C> ... }? ?-dynamic_vectorless_ranking_methods {load | clock | vector_activity}? ?-enable_auto_queue {true | false}? ?-enable_auto_mapping {true | false}? ?-enable_disk_mapping {true | false}? ?-enable_duty_prop_with_global {true | false}? ?-enable_dynamic_current_slew_load_interpolation {true | false}? ?-enable_dynamic_scaling {true | false}? ?-enable_flop_state_propagation {true | false}? ?-enable_generated_clock {true | false}? ?-enable_input_net_power {true | false}? ?-enable_interactive_reports {true | false}? ?-enable_mt_in_vectorbasedflow {true | false}? ?-enable_mt_reports {true | false}? ?-enable_mt_state_propagation {true | false}? ?-enable_pba_for_tempus_pi {true | false}? ?–enable_power_target_flow {true | false}? ?–enable_rtl_vectorbased_dynamic_analysis {true | false}? ?-enable_scan_report {true | false}? ?-enable_single_cycle_scheduling {true | false}? ?-enable_slew_based_ccs_pin_cap {true | false}? ?-enable_stable_clock_gating {true | false}? ?-enable_stable_flop_scheduling {true | false}? ?-enable_state_propagation {true | false}? ?-enable_tempus_pi {true | false}? ?-enable_xp {true | false}? ?-enhanced_blackbox_avg {true | false}? ?-enhanced_blackbox_max {true | false}? ?-equivalent_annotation {true | false}? ?-event_based_leakage_power {true | false}? ?-external_load_config_file <filename>? ?-extraction_tech_file <filename>? ?-extractor_include <filename>? ?-fanout_limit <value>? ?-flatten_xpgv_block_instances <filename>? ?-force_library_merging {true | false}? ?-from_x_transition_factor <value>? ?-from_z_transition_factor <value>? ?-generate_activity_mapping_report {true | false}? ?-generate_current_for_rail <railnames>? ?-generate_flop_ranking_data <directoryname>? ?-generate_leakage_power_map_based_on_calculated_leakage {true | false}? ?-generate_static_report_from_state_propagation {true | false}? ?-handle_glitch {true|false}? ?-handle_transport_glitch {true | false}? ?-handle_tri_state {false|true}? ?-hier_delimiter <character>? ?-honor_combinational_logic_on_clock_net {true | false}? ?-honor_negative_energy {true | false}? ?-honor_net_activity {true | false}? ?-honor_non_mission_leakage {true | false}? ?-hybrid_analysis {true | false}? ?-ignore_control_signals {true | false}? ?-ignore_data_phase_for_clk {true | false}? ?-ignore_end_toggles_in_profile {true | false}? ?-ignore_glitches_at_same_time_stamp {true | false}? ?-ignore_inout_pin_cap {true | false}? ?-ignore_macro_leakage_scale_for_temp {true | false}? ?-include_seq_clockpin_power {true | false}? ?-include_timing_in_current_file {true | false}? ?-ir_derated_timing_view <view_name>? ?-keep_clock_gate_ratio_in_iterations {true | false}? ?-leakage_scale_factor_for_temp <scale>? ?-library_preference {voltage | ecsm_ccsp}? ?-macro_pgv_leakage {true | false}? ?-macro_toggle_pin_percentage <percentage>? ?-mbff_toggle_behavior { simultaneous | independent | sbff }? ?-mbff_toggle_pin_percentage <percentage>? ?-memory_current_scaling_method {1 | 2 | 3}? ?-merge_switched_net_currents {true | false}? ?-method { static | dynamic_vectorless | dynamic_vectorbased | dynamic_mixed_mode | event_based | vector_profile}? ?-min_leaf_count <value>? ?-multi_scenario_simulation {true | false}? ?-off_pg_nets <net> _list? ?-output_current_data_prefix <prefix>? ?-partition_count <value>? ?-partition_twf {true | false}? ?-pin_based_twf {true | false}? ?-power_grid_library {<library> _list }? ?-power_include_initial_x_transitions {true | false}? ?-power_match_state_for_logic_x <value>? ?-precision <value>? ?-pre_simulation_empty_period <period>? ?-pre_simulation_period <period>? ?-pre_simulation_power_exclude_period <period>? ?-quit_on_activity_coverage_threshold <threshold_value>? ?-read_rcdb {true | false}? ?-relax_arc_match {true | false}? ?-report_black_boxes {true | false}? ?-report_clock_instance_switching_info {true | false}? ?-report_idle_instances {true | false}? ?-report_instance_switching_info {all | output_logic | none}? ?-report_instance_switching_list <filename>? ?-report_library_usage {true | false}? ?-report_missing_bulk_connectivity {true | false}? ?–report_missing_input {true | false}? ?-report_missing_nets { true|false }? ?-report_scan_chain_stats {true | false}? ?-report_stat {true | false}? ?-report_time_display_fraction_digits <value>? ?-report_twf_attributes {detailed | summary}? ?-reuse_flop_ranking_data <directoryname>? ?-reuse_flop_ranking_data_hier <blockname>? ?-save_bbox {true | false}? ?-scale_to_sdc_clock_frequency {true | false}? ?-scan_chain_activity {design_name chain_name activity_number} | {vectorless activity_number}? ?-scan_chain_name {<design_name> <chain_name> <pattern ...>}? ?-scan_control_file <filename>? ?-scan_mbff_chain_type <type>? ?-set_power_event_based {true | false}? ?-settling_buffer <value>? ?-smart_window {true | false}? ?-split_bus_power {true | false}? ?-start_time_alignment {true |false}? ?-state_dependent_leakage {true | false}? ?-stateprop_ignore_unannot_pins {true | false}? ?-static_multi_mode_scenario_file <filename>? ?-static_netlist {verilog | def}? ?-switching_power_on_rise_only {true | false}? ?-thermal_input_file <file>? ?-thermal_leakage_temperature_scale_table_file <filename>? ?-to_x_transition_factor <value>? ?-to_z_transition_factor <value>? ?-transition_factor_based_duty {true | false}? ?-transition_time_method {min | avg | max}? ?-twf_delay_annotation {min | avg | max}? ?–twf_load_cap {min | avg | max | ignore}? ?-unified_power_switch_flow {true | false}? ?-use_cell_leakage_power_density {true | false}? ?-use_fastest_clock_for_dynamic_scheduling {true | false}? ?-use_lef_for_missing_cells {true | false}? ?-use_only_ddv_current {true | false}? ?-use_physical_partition {true | false}? ?-use_twf_stable_randomized_arrival_delay {none | data_only | all}? ?-use_zero_delay_vector_file {true | false}? ?-vector_profile_mode {activity | event_based | power_density | transient}? ?-worst_case_vector_activity {true | false}? ?-worst_step_size <value>? ?-worst_window_count <value>? ?-worst_window_coverage { top | tile }? ?-worst_window_reports {full | worst | both}? ?-worst_window_size <value>? ?-worst_window_type { power | activity | delta_power | delta_activity | ir | critical_inst_power }? ?-write_boundary_leakage_edge_annotation {true | false}? ?-write_default_uti {true | false}? ?-write_dynamic_currents {true | false}? ?-write_profiling_db {true | false}? ?-write_simulation_db {true | false}? ?-write_static_currents {true | false}? ?-x_count_transition_using_3_states {true | false}? ?-x_transition_factor <value>? ?-z_transition_factor <value>? ?–zero_delay_vector_toggle_shift <value>?",
        ),
        # man1/set_power_calc_temperature.1
        _syn(
            "set_power_calc_temperature",
            "Sets the temperature for static power calculation",
            "set_power_calc_temperature <temperature>",
        ),
        # man1/set_power_data.1
        _syn(
            "set_power_data",
            "Specifies the static and dynamic power or current files for IRdrop and EM analysis",
            "set_power_data ?-help? -reset | {-format {current | ascii | area | ascii_current} ?-instance <instance_name>? ?-offset <offset_value>? ?-power <value>? ?-scale <factor>? ?-repeat <time>? ?-bias_voltage <value>? ?-die_instance_name <dieinstname>? ?-power_output_directory <dir>? ?-repeat_window {<start> <end>}? ?-strip_hier_instance <instance>? ?<filename>? }",
        ),
        # man1/set_power_include_file.1
        _syn(
            "set_power_include_file",
            "Specifies a PowerMeter include file",
            "set_power_include_file <file> ?-block <master_cell_name>? ?-reset?",
        ),
        # man1/set_power_output_dir.1
        _syn(
            "set_power_output_dir",
            "Specifies the name of the directory that power information will be output to",
            "set_power_output_dir <dir> ?-reset?",
        ),
        # man1/set_power_pads.1
        _syn(
            "set_power_pads",
            "Specifies power pad information",
            "set_power_pads -reset |{ ?-auto_voltage_source_creation {true|false}? ?-consider_partial_small_tiles_for_vsrc {true | false}? ?-def_shape_only {true | false}? ?-die_instance_name <dieinstname>? ?-enable_switchnet_ploc_generation {true | false}? ?-format {defpin | padcell | xy | boundary | xyiv}? ?-layer <vialayername>? -net <net_name>?-number_of_voltage_source <value>? ?-file <file>? ?-region {<x1> <y1> <x2> <y2>}? ?-short_pin_nodes {true | false}? ?-tile {<x> <y>}? }",
        ),
        # man1/set_power_rail_display.1
        _syn(
            "set_power_rail_display",
            "",
            "set_power_rail_display ?-help? ?-enable_result_browser {true | false}? ?-enable_rlrp {true | false}? ?-enable_voltage_sources {true | false}? ?-filter_max <max_value>? ?-filter_min <min_value>? ?-legend {off ne nw se sw}? ?-plot <plot_type>? ?-range_max <max_value>? ?-range_min <min_value>? ?-reset_color_scale {true | false}? ?-filter_color {on | off | <color_name>}? ?-enable_percentage_range {true | false}? ?-thermal_layer_name <thermal_layer>? ?-tile_count_x <value>? ?-tile_count_y <value>? ?-tile_size_x <value>? ?-tile_size_y <value>? ?-customized_range {<value1> <value2> ... <value9>}? ?-grid {on | off}? ?-enable_auto_apply{true | false}?",
        ),
        # man1/set_power_rail_layers_nets.1
        _syn(
            "set_power_rail_layers_nets",
            "Controls the visibility of the layers, the opacity of the rail analysis or design database, and the visibility of power/ground nets",
            "set_power_rail_layers_nets ?-help? ?-design_opacity <value>? ?-rail_analysis_opacity <value>? ?-nets {{all_power 0/1}{all_ground 0/1}} | -enable_nets {<names>} | -disable_nets {<names>}? ?-enable_switch_nets {all|<net_names>} | -disable_switch_nets {all|<net_names>}? ?-enable_report_layers {all|<layer_names>} | -disable_report_layers {all|<layer_names>} | -layers {{name report0/1 visible0/1}{...}}? ?-enable_visible_layers {all|<layer_names>} | -disable_visible_layers {all|<layer_names>} | -layers {{name report0/1 visible0/1}{...}}? ?-enable_visible_sem_layers {all|<layer_names>} | -disable_visible_sem_layers {all|<layer_names>}? ?-show_layer_net_setting_list {true | false}? ?-instance_voltage_method {Worst | Best | Avg | WorstAvg}? ?-instance_voltage_window {1| 0}? ?-via_size {1 | 2 | 3 | 4 | 5 | 6}?",
        ),
        # man1/set_proc_verbose.1
        _syn(
            "set_proc_verbose",
            "Makes a procedure verbose, when the procedure is called for execution",
            "set_proc_verbose ?-help? {?<procedure_name> ?-quiet?? | ?-report?}",
        ),
        # man1/set_propagated_clock.1
        _syn(
            "set_propagated_clock",
            "Puts the propagated_clock assertion on the specified pin, port, or clock object",
            "set_propagated_clock <pin_clock_list>",
        ),
        # man1/set_property.1
        _syn(
            "set_property",
            "Sets user-defined properties on objects",
            "set_property ?-object_type {<object_type>}? {<object_list>} ?-quiet? <property_name> <property_value>",
        ),
        # man1/set_proto_design_mode.1
        _syn(
            "set_proto_design_mode",
            "Controls certain aspects of how the proto_design command generates an initial floorplan",
            "set_proto_design_mode ?-help? ?-reset? ?-cover_fixed_macros {true | false}? ?-effort {low | high}? ?-flexmodel_constraint_type {guide |region |fence}? ?-keep_guide {true | false}? ?-place_macro {true | false}? ?-remove_overlap {true | false}?",
        ),
        # man1/set_proto_mode.1
        _syn(
            "set_proto_mode",
            "Sets the mode for all the prototyping model commands as well as other commands, such as place_design and timeDesign",
            "set_proto_mode ?-reset? ?-allow_model_with_io {true|false}? ?-allow_powerdomain_in_flexmodel {true|false}? ?-create_dir <directoryName>? ?-create_high_fanout_psPM {true|false}? ?-create_lib <libraryName>? ?-create_metal_fill_NDR <double>? ?-create_metal_fill_nominal <double>? ?-create_multi_corner_psPM {true|false}? ?-create_NDR_psPM_model {auto|on|off}? ?-create_partition_as_flexmodel {true|false}? ?-create_pipeline_flop {*AB*}? ?-create_powerdomain_psPM {true|false}? ?-create_timing_budget {true|false}? ?-create_no_flex_filler {true|false}? ?-identify_algorithm {auto|module_based|instgroup_based}? ?-identify_estimated_flexmodel_number <number>? ?-identify_exclude_module {<module1><module2> ...}? ?-identify_exclude_module_and_parent {<module1> <module2> ...}? ?-identify_exclude_module_tree {<module1><module2> ...}? ?-identify_honor_objects_hierarchy {<object_list>}? ?-identify_max_inst <number>? ?-identify_min_inst <number>? ?-keep_inst_file_only {true|false}? ?-keep_instance_defined_in_sdc {true|false}? ?-keep_slack_improve_NDR {true|false}? ?-max_report_NDR_net <double>? ?-route_net_NDR <ruleName>? ?-timing_net_delay_model {best_layer_no_detour|best_layer_blockage_aware|use_actual_wire}? ?-timing_ps_per_micron {M <number1>?:M <number2>? <number3> ...}? ?-verbose?",
        ),
        # man1/set_proto_model.1
        #   WARNING: unclosed bracket '[' at position 211
        _syn(
            "set_proto_model",
            "The set_proto_model command specifies the model type of a specific module",
            "set_proto_model ?-help? -model <name_list> ?-type {full | flex_module | flex_instgroup}? ?-create_total_area <number> | -create_gate_area <number> | {-create_gate_count <number> -create_area_per_gate <number>}? ?-create_extra_macro {macro_name <number> ?macro_name <number>? ...} ?-planDesign_target_util number? ?-reset?",
        ),
        # man1/set_proto_model_physical_constraint.1
        _syn(
            "set_proto_model_physical_constraint",
            "Sets FlexModels to specific physical constraints to guide placement",
            "set_proto_model_physical_constraint ?-help? -type {guide | fence | region | soft_guide | none} ?-model <string>?",
        ),
        # man1/set_proto_timing_settings.1
        _syn(
            "set_proto_timing_settings",
            "",
            "set_proto_timing_settings ?-help? ?-reset?",
        ),
        # man1/set_ptn_fplan_mode.1
        #   WARNING: bracket mismatch: '[' at position 36 closed by '}' at position 85
        #   WARNING: unmatched closing bracket ']' at position 86
        #   WARNING: bracket mismatch: '[' at position 88 closed by '}' at position 137
        #   WARNING: unmatched closing bracket ']' at position 138
        _syn(
            "set_ptn_fplan_mode",
            "Sets what floorplan objects will be written-out and/or read back in",
            "set_ptn_fplan_mode ?-help? ?-reset? ?-export {macro | special_route | pin_constraint}}? ?-import {macro | special_route | pin_constraint}}?",
        ),
        # man1/set_pulse_clock_max_transition.1
        _syn(
            "set_pulse_clock_max_transition",
            "Sets the maximum pulse clock transition constraint on the specified pulse generator cells, pulse generator library cells, clocks, and/or current design",
            "set_pulse_clock_max_transition <transition_limit> <object_list> ?-transitive_fanout? ?-rise? ?-fall?",
        ),
        # man1/set_pulse_clock_max_width.1
        _syn(
            "set_pulse_clock_max_width",
            "Sets the maximum pulse clock width constraint on the specified pulse generator cells, pulse generator library cells, clocks, and/or current design",
            "set_pulse_clock_max_width <pulse_width> <object_list> ?-transitive_fanout?",
        ),
        # man1/set_pulse_clock_min_transition.1
        _syn(
            "set_pulse_clock_min_transition",
            "Sets the minimum pulse clock transition constraint on the specified pulse generator cells, pulse generator library cells, clocks, and/or current design",
            "set_pulse_clock_min_transition <transition_limit> <object_list> ?-transitive_fanout? ?-rise? ?-fall?",
        ),
        # man1/set_pulse_clock_min_width.1
        _syn(
            "set_pulse_clock_min_width",
            "Sets the minimum pulse clock width constraint on the specified pulse generator cells, pulse generator library cells, clocks and/or current design",
            "set_pulse_clock_min_width ?-help? <pulse_width> <object_list> ?-transitive_fanout?",
        ),
        # man1/set_quiet_attacker.1
        _syn(
            "set_quiet_attacker",
            "Specifies one or more coupled nets as non-attackers (silent) for the delay and glitch analysis of a given victim net",
            "set_quiet_attacker ?-help? ?-analysis_type {early | late}? ?-attacker <string>? ?-transition {rise | fall}? ?-victim <string>? ?-view <string>?",
        ),
        # man1/set_rail_analysis_domain.1
        _syn(
            "set_rail_analysis_domain",
            "Specifies a rail analysis power domain",
            "set_rail_analysis_domain ?-help? -name <domain_name> -pwrnets <power_net>_list -gndnets <ground_net_list> ?-threshold <value>?",
        ),
        # man1/set_rail_analysis_mode.1
        #   WARNING: bracket mismatch: '[' at position 8744 closed by '}' at position 8788
        _syn(
            "set_rail_analysis_mode",
            "Specifies how the rail analysis will be performed",
            "set_rail_analysis_mode -method {static | dynamic | era_static | era_dynamic} -accuracy {xd | hd } -power_grid_library <dir_list> ?-analysis_view <view>? ?-avg_em_analysis {true | false}? ?-create_pdn_model {true | false}? ?-off_rails <net_name_list>? ?-em_models <file>? ?-em_temperature <string>? ?-default_package_resistor <value>? ?-default_package_inductor <value>? ?-default_package_capacitor <value>? ?-die_delimiter <delimiter>? ?-vsrc_search_distance <value>? ?-report_msmv_format {true | false}? ?-temp_directory_name <directory>? ?-gds_purpose {metalFill | flipChip | fullChip}? ?-gds_file <file>?-gds_offset {x y}?? ?-gds_top_cell <cell_name>? ?-decap_cell_list { <cell1 cell2 ... celln> }? ?-filler_cell_list { <cell1 cell2 ... celln> }? ?-suppress_message {<message_id> + }? ?-disable_analysis_types {<list of analysis types>}? ?-gds_map <file>? ?-enable_sensitivity_analysis {true | false}? ?-cell_ignore_file <filename>? ?-save_voltage_waveforms {true | false}? ?-read_thermal_map <thermal_map_file>? ?-temperature <value>? ?-extractor_include <filename>? ?-record_results_start_time <time>? ?-lef_map <lefMappingFile>? ?-lifetime <value>? ?-die_mode {single|multi-die|3dic} -die_instance_name <dieinstname> ?-design <designname>?? ?-dynamic_trigger_file <filename>? ?-block_powerup_rail <netname> | -powering_up_rails <net_name1... netname_n>? ?-process_techgen_em_rules {true | false}? ?-powerup_sequence_file <filename>? ?-enable_vsrc_in_gif {true | false}? ?-work_directory_name <directory>? ?-powerup_fast_mode {true | false}? ?-ignore_shorts {true | false}? ?-disable_parallel_extraction? ?-enable_distributed_processing_in_solver {true | false}? ?-extraction_tech_file <filename>? ?-generate_hier_bbv {true | false}? ?-check_vsrc_placement_on_switched_net {true | false}? ?-process_bulk_pins_for_body_bias {true | false}? ?-cluster_via_rule { {<via_layer1> <number_of_equidistant_vias>}… }? ?-cluster_via1_ports {true | false}? ?-ignore_fillers {true | false}? ?-ignore_decaps {true | false}? ?-limit_number_of_steps {true | false}? ?-check_thermal_aware_em {true | false}? ?-compress_powergrid_database {true | false}? ?-cluster_via_size <value>? ?-report_power_in_parallel {true | false}? ?-use_early_view_list <filename>? ?-use_ir_view_list <filename>? ?-use_em_view_list <filename>? ?-enable_manufacturing_effects {true|false}? ?-enable_rlrp_analysis {true|false}? ?-enable_voltage_across_vias {true|false}? ?-eiv_eval_layers {<layerlist>}? ?-eiv_eval_layer_file <filename>? ?-eiv_eval_window {switching | timing | both | elapse}? ?-eiv_method {worst best avg worstavg bestavg}? ?-reuse_state_directory <dir_name>? ?-snap_layer_for_current_taps <file_name>? ?-enable_scheduler {true | false}? ?–era_current_distribution_factor_for_placed <value>? ?-era_current_region_file <filename>? ?–era_current_distribution_layer <layer_name>? ?–era_current_distribution { unplaced | placed | all | none }? ?-era_insert_virtual_via_on_layers <value>? ?–era_lef_layermap <filename>? ?-era_power_gate_file <filename>? ?-era_insert_virtual_followpins { standard | extended | none }? ?-era_skip_virtual_via_by_type {whatif | def | all | none}? ?-era_skip_virtual_via_on_layers {{ <layer1> <layer2> } { <layer3> <layer4> } ... }? ?–import_what_if_shapes {true | false}? ?-what_if_shapes_file <filename>? ?-check_current_balanced_power_grid_em {true | false}? ?-em_threshold <value>? ?-gif_resolution {low | medium | high}? ?-era_insert_virtual_followpin_for_io {true | false}? ?-report_voltage_drop {true | false}? ?-eiv_report{auto | netonly | all}? ?-eiv_threshold<value>? ?-eiv_max_instances<value>? ?-prechain_powerup_sequence_file<filename>? ?-rdl_def <def_file>? ?-rdl_placement{X Y}? ?-rdl_orientation{ N|S|W|E|FN|FS|FE|FW }? ?-topcell_placement{X Y}? ?-topcell_orientation{ N|S|W|E|FN|FS|FE|FW }? ?-watch_location_waveform { {<layerName> <xCoord> <yCoord>}+ }? ?-enable_rc_analysis{true | false}? ?-em_peak_analysis {true | false}? ?-em_limit_scale_factor {{avg <value>} {rms <value>} {peak <value>}}? ?-em_rms_delta_t <temp>? ?-ict_em_models <file>? ?-hpgv_block_lefs <list_of_files>? ?-hpgv_generate_view {ir | em | all}? ?-era_current_distribution_unplaced_area {instance | diearea}? ?-era_current_distribution_nets {<net1> <net2> ...}? ?-era_check_wires_for_generated_current_regions {true | false}? ?-era_techlib_generation {true | false}? ?-force_library_merging {true | false}? ?-unconnected_die_pkg_pins {ignore | error | edit}? ?-mcp_model_mapping {{<<mcp model name1>> <<die DEF name1>>} {<<mcp model name2>> <<die DEF name2>>} ...}? ?-eiv_pin_based_report {true | false}? ?-gif_zoom_area { <x1> <y1> <x2> <y2> }? ?-gif_zoom_topcell_diearea {true | false}? ?-generate_instance_ir_report <file>? ?-generate_instance_pin_ir_report <file>? ?-finegrain_powergate_ron {min avg max}? ?-finegrain_powergate_ron_list <filename>? ?-ignore_incomplete_net {true | false}? ?-generate_combined_ivd_gif {true | false}? ?-gif_iv_threshold<value>? ?-verify_logical_connectivity{true | false}? ?-enable_ccs_analysis{true | false}? ?-rlrp_threshold <value>? ?-rlrp_percentage_threshold <value>? ?-rlrp_pin_based_report {true | false}? ?-probe_waveform_list <filename>? ?-probe_pin_voltage_list <filename>? ?-eiv_eval_nodes{tap | port}? ?-hier_delimiter <character>? ?-force_extraction {true | false}? ?-skip_extraction {true | false}? ?-report_power_options <option_names>? ?-package_trace_connectivity{true | false}? ?-reff_pin_report_method { best | worst }? ?-rlrp_pin_report_method { best | worst | eiv_best | eiv_worst}? ?-reff_pin_report_layer { top | bottom | all }? ?-rlrp_pin_report_layer { top | bottom | all }? ?-probing_node_file <file_name>? ?-enlarge_vsrc_in_vuvc {true | false}? ?-gif_new_color_scale {true | false}? ?-scale_initial_condition_current <filename>? ?-probe_instance_tap_waveforms {true | false}? ?-rlrp_eval_nodes {port | tap}? ?-report_shorts{true | false}? ?-extract_subconductor_layers {true | false}? ?-eiv_average_per_window_list <filename?> ?-em_ignore_pgv_resistors {true | false}? ?-eiv_eval_gnd_window {true | false}? ?-honor_negative_static_current {true | false}? ?-accumulate_overlapping_ddv_pwl_waveforms {true | false}? ?-report_layers_above_pin_for_instance_ir {true | false}? ?-switchbit_file_for_eiv_calculation<filename>? ?-rlrp_detail_report{true | false}? ?-era_instance_dynamic_current_file<filename>? ?-eiv_print_time{true | false}? ?-eiv_histogram_max <value>? ?-eiv_histogram_min <value>? ?-eiv_histogram_number_of_bucket<value>? ?-reff_detail_report {true|false}? ?-record_inst_peak_current {true | false}? ?-pre_simulation_period <value>? ?-pre_simulation_resolution <value>? ?-fine_pre_simulation_period <value>? ?-enable_instance_powergate_report {true | false}? ?-disable_em_split_ac_dc_rules {true | false}? ?-lowest_layer_for_em_check <layer_name>? ?-ignore_nets_without_vsrc {true | false}? ?-eiv_pin_location{true | false}? ?-verbosity{true | false}? ?-enable_reff_analysis {true | false}? ?-rdl_def_list {{<rdl_filename1> <x1> <y1> <orient1>} {<rdl_filename2> <x2> <y2> <orient2>} ...}? ?-remove_duplicate_inst {true | false}? ?-generate_instance_effr_report <file>? ?-generate_package_pin_current_voltage {true | false}? ?-reff_domain_report_format {1 | 2 | 3 | 4}? ?-em_report_line_threshold <value>? ?-powering_down_rails <net_name1... netname_n>? ?-flatten_xpgv_block_instances<filename>? ?-xpgv_config_file <filename>? ?-def_based_hierarchical_reports {true | false}? ?-enable_2d_partition_extraction{true | false}? ?-print_gif_range_percentage{true | false}? ?-generate_multi_voltage_library {true | false}? ?-feol_scale_factor <non_negative_integer_number>? ?-enable_seb {true | false}? ?–env_temperature <temperature>? ?-seb_lifetime <value>? ?-seb_table <table_filename>? ?-seb_temperature <temperature>? ?-use_rms_delta_t {true | false}? ?-enable_xp {true | false}? ?-xp_cpu_per_job_power <value>? ?-xp_cpu_per_job_simulation <value>? ?-xp_host_allocation_method {on_demand | at_startup}? ?-xp_purge {full}? ?-xp_resume {true | false}? ?-xp_reuse_extraction_directory <directory_name>? ?-xp_simulation_cpu_timeout <value>? ?-xp_simulation_min_cpu <value>? ?-enable_package_battery_current_probing{true | false}? ?-probe_package_interface_ports{true | false}? ?-static_multi_mode_analysis {true | false}? ?-em_temperature_layer_list {{<<LEF_layer_name>> <<em_temperature_in_C>>}+}? ?-em_rms_delta_T_layer_list {{<<LEF_layer_name>> <<delta_T_in_C>>}+}? ?-report_instances_missing_current_data{true | false}? ?-common_res_inst_pair_file_name<file>? ?-promote_pin_shapes_only {filler | decap | both}? ?-unconnectedcell_ignore_file<filename>? ?-ignore_duplicate_vsrc {true | false}? ?-write_demand_current_region_file<filename>? ?-shorting_resistance<value>? ?-probe_instance_pin_waveforms{true | false}} ?-reset? ?-tsv_subckt_modelfile_list <filename>? ?-em_cdf_percentage <value>? ?-ircx_models {RC.ircx EMIR.ircx}|{RC.ircx}? ?-enable_multi_die_connectivity_check {true | false}? ?-ignore_from_reporting <filename>? ?-enable_xpgv_scaling { true | false }? ?-static_trigger_file <filename>? ?-rlrp_cell_report_layer <filename>? ?-peak_em_analysis {true | false}? ?-rms_em_analysis {true | false}? ?-reff_eval_nodes {port | tap}? ?-reff_report_all {true | false}? ?-set_analyze_bbox {<xmin ymin xmax ymax>}? ?-off_state_powergate_instance_file <filename>? ?-override_set_power_data {true | false}? ?-unified_power_switch_flow {true | false}?",
        ),
        # man1/set_reinforce_pg_mode.1
        _syn(
            "set_reinforce_pg_mode",
            "Sets global variables for the reinforce_pg command",
            "set_reinforce_pg_mode ?-help? ?-auto_ir_fix_effort {low | medium | high}? ?-critical_path_slack {<slack>}? ?-irdrop_hierarchical_block {block1 block2 ... | *}? ?-irdrop_hierarchical_top_rail_analysis_directory {<directory_name>}? ?-reset? ?-respect_defined_nets {<file_name>}? ?-respect_routes {none | fixed | fixed_and_clock | all}? ?-respect_stdcell_geometry {none | sequential | all}? ?-timing_aware_effort {none | low | medium | high}?",
        ),
        # man1/set_resistance.1
        _syn(
            "set_resistance",
            "Sets the wire resistance value on the specified nets of the top cell, which is used to compute the net delay of the specified nets",
            "set_resistance",
        ),
        # man1/set_safety_mechanism_rules_dcls.1
        _syn(
            "set_safety_mechanism_rules_dcls",
            "Defines the separation rules to be applied to the dual core lockstep (DCLS) groups in the design",
            "set_safety_mechanism_rules_dcls ?-help? ?-isolate_halo_type {hard soft}? ?-isolate_type {hard soft}? ?-route_types {none internal interface common top}? {?-exclusive_groups {{<group_A1> {<group_A2 group_A3> ...}} {<group_B1 group_B2 group_B3> ...} ... }? ?-isolate_clock {{{*} split_net | split_network}} | {{{ group_A1 group_A2 …} split_net | split_network} {{ group_B1 group_B2 … } split_net | split_network}}? ?-isolate_inputs {{{*} split_net}} | {{{<group_A1 group_A2>} split_net}}? ?-isolate_outputs {{{*} split_net}} | {{{<group_A1 group_A2>} split_net}}? ?-isolate_pin {{{ hpin_1 hpin_2 …} split_network}}? ?-isolate_reset {{{*} split_network}} | {{{<group_A1 group_A2>} split_network}}? ?-isolate_scan_enable {{{*} split_network}} | {{{<group_A1 group_A2>} split_network}}? ?-isolate_use_halo * | {<group_A1 group_A2> ...}? ?-spacing <double>? }",
        ),
        # man1/set_safety_mechanism_rules_parity.1
        _syn(
            "set_safety_mechanism_rules_parity",
            "Defines the Parity safety-mechanism rules that need to be enforced during implementa‐ tion",
            "set_safety_mechanism_rules_parity ?-help? -endpoints <string> -group_size_max <string> -group_size_min <string> ?-parity_bit_cells <string>?",
        ),
        # man1/set_safety_mechanism_rules_ser.1
        _syn(
            "set_safety_mechanism_rules_ser",
            "Defines the Soft Error Resilience (SER) safety-mechanism rules that need to be enforced during implementation",
            "set_safety_mechanism_rules_ser ?-help?",
        ),
        # man1/set_safety_mechanism_rules_tmr.1
        _syn(
            "set_safety_mechanism_rules_tmr",
            "Defines the Triple Modular Redundancy (TMR) safety-mechanism rules that need to be en‐ forced during implementation",
            "set_safety_mechanism_rules_tmr ?-help? {?-spacing <float>? ?-spacing_x <dx>? ?-spacing_y <dy>? ?-isolate_clock {none split_net split_network}? ?-isolate_reset {none split_netsplit_network}? ?-isolate_scan_enable {none split_netsplit_network}? ?-well_tap_cells <string>?} ?-spacing <float >| -spacing_x <dx>? ?-spacing <float >| -spacing_y <dy>?",
        ),
        # man1/set_self_heat_analysis_mode.1
        _syn(
            "set_self_heat_analysis_mode",
            "Specifies the number of tiles, layer-based α coefficients, β coefficients, and list of cells with cell thermal resistances",
            "set_self_heat_analysis_mode ?-help? ?-alpha_parameters {{<layer_name> < αoverlapping > < αconnecting >}+}? ?-beta_parameters {C1 C2 C3}? ?-cell_thermal_resistance_file <filename?> ?-detail_delta_temperature_file <filename?> ?-detail_delta_temperature_region {<x1 y1 x2 y2>}? ?-die_instance_input_signal_em <filename>? ?-die_instance_name <dieinstname>? ?-instance_delta_temperature_file <filename>? ?-instance_power_file <filename>? ?-report_conn_pin_wire <filename>? ?-scale_rms_limit <value>? ?-tile_delta_temperature_file <filename>? ?-tiles {<n_tile_in_x> <m_tile_in_y>}?",
        ),
        # man1/set_sense.1
        _syn(
            "set_sense",
            "Selects which phase of the clock to filter at the specified point",
            "set_sense ?-help? <pin_or_port_list> ?-clocks <clock_list>? {?-positive | -negative | -stop_propagation? ?-type <type_list>?}",
        ),
        # man1/set_signal_em_analysis_mode.1
        _syn(
            "set_signal_em_analysis_mode",
            "Use the get_signal_em_analysis_mode command to return the current settings for the set_sig‐ nal_em_analysis_mode command",
            "set_signal_em_analysis_mode ?-help? ?-Ipeak_Td_method {effective_width_from_integration effective_half_peak_width max_equivalent_dc_peak sum_half_peak_width}? ?-avgRecovery <em_recover>? ?-default_freq_for_unconstrained_nets <freq_in_Hz>? ?-delta_T <value>? ?-effort_level {low | medium | high}? ?-em_temperature <value>? ?-em_res_width {drawn silicon}? ?-error <value>? ?-forceHoldView? ?-lifetime <value>? ?-method {rms peak avg}? ?-minPeakDutyRatio <value>? ?-minPeakFreq <value>? ?-net_file <list_file>? ?-toggle <value>? ?-useQrcTech? ?-view <viewName>? ?-net <netNames> | -selected? ?-report <filename> ?-detailed?? ?-report_db? ?-set_current_file <filename>? ?-skip_net <net_name_list>? ?-skip_net_file <list_file>? ?-ict_em_models <file>? ?-current_scale_factor {{avg <value>} {rms <value>} {peak <value>}}? ?-em_limit_scale_factor {{avg <value>} {rms <value>} {peak <value>}}? ?-em_threshold <<value>>? ?-current_scale_table <current_scale_table_file>? ?-em_limit_scale_table <em_limit_scale_table_file>? ?-extraction_tech_file <filename>? ?-handle_pin_obs_via? ?-read_detail_delta_temperature_file <filename>? ?-reset? ?-check_thermal_aware_em {true | false}? ?-enable_seb {true | false}? ?–env_temperature <temperature>? ?-seb_lifetime <value>? ?-seb_table <table_filename>? ?-seb_temperature <temperature>? ?-use_rms_delta_t {true | false}? ?-skip_category_mode{0 | 1 | 2}? ?-em_temperature_layer_list {{<<LEF_layer_name>> <<em_temperature_in_C>>}+}? ?–delta_T_layer_list {{<<LEF_layer_name>> <<delta_T_in_C>>}+}? ?-em_cdf_percentage<value>? ?-additional_individual_violation_report? ?-net_freq_file<filename>? ?-ircx_models {RC.ircx EMIR.ircx}|{RC.ircx}? ?-simulation_net <list_of_nets>? ?-simulation_net_file <filename>?",
        ),
        # man1/set_signoff_verify_design_config.1
        _syn(
            "set_signoff_verify_design_config",
            "Sets the global parameters for the signoff_verify_design command",
            "set_signoff_verify_design_config ?-help? ?-abort_on_layout_error {yes | no}? ?-abort_on_missing_rulecheck {yes | no}? ?-area {<x1 y1 x2 y2>}? ?-attach_instance_name <attribute_number>? ?-attach_net_name <attribute_number>? ?-attach_net_prop {{<prop_name> <attr_num>} ... }? ?-auto_merge_base_class <string>? ?-config_file <file_name>? ?-control_file <file_name>? ?-core_license <license_combination>? ?-die_area_as_boundary? ?-dp <n>? ?-dp_timeout <seconds>? ?-erc_checks? ?-error_limit <n>? ?-extra_options <string>? ?-format {stream | oasis}? ?-ignore_blockage? ?-ignore_fill? ?-keep_data <key_file>? ?-layer_map_file <streamOut_map_file>? ?-layers <layer_names> | -layer_range {top_layer | bottom_layer}? ?-layout_path <string>? ?-lib_name <library name>? ?-license_dp_continue? ?-license_stacking {larger_license | same_license}? ?-license_timeout <number_of_seconds>? ?-merge <string>? ?-merge_path <string>? ?-mode {ALL FILLONLY NOFILL NOINSTANCES}? ?-mp <n>? ?-mt <n>? ?-net_map_file <string>? ?-nets <string>? ?-no_query? ?-no_structure_name? ?-offset {<x y>}? ?-output_macros? ?-process_node <foundary_node>? ?-pvs_fill? ?-report_file? ?-reset {<parameter_name> | all}? ?-rule_file_drc <file_name>? ?-rule_file_smart_verify_lvs <file_name>? ?-run_name <directory_name>? ?-selected_inst? ?-skip_auto_load_results? ?-stripes <number>? ?-structure_name <structure_name>? ?-transform_to_inst_master? ?-ui_data? ?-uniquify_cell_names? ?-units {100 | 200 | 400 | 800 | 1000 | 2000 | 4000 | 8000 | 10000 | 20000}? ?-working_dir <working_directory>?",
        ),
        # man1/set_socv_constraint_config.1
        _syn(
            "set_socv_constraint_config",
            "Enhances the built-in sigma pessimism of check values for setup and hold constraints in the library",
            "set_socv_constraint_config ?-help? ?-hold_folding <float>? -libs <string> ?-nochange_hold_folding <float>? ?-nochange_setup_folding <float>? ?-setup_folding <float>?",
        ),
        # man1/set_socv_rc_variation_factor.1
        _syn(
            "set_socv_rc_variation_factor",
            "Defines the value of interconnect delay variation factor",
            "set_socv_rc_variation_factor ?-help? <variation_factor> ?-early? ?-late? ?-view <list_of_views>?",
        ),
        # man1/set_socv_reporting_nsigma_multiplier.1
        _syn(
            "set_socv_reporting_nsigma_multiplier",
            "Controls n-sigma value for reporting purposes",
            "set_socv_reporting_nsigma_multiplier ?-help? ?-view <list_of_views>? {?-setup <float>? ?-hold <float>?} ?-transition <float>?",
        ),
        # man1/set_switching_activity.1
        _syn(
            "set_switching_activity",
            "Specifies activity for nets, pins, and ports",
            "set_switching_activity ?-reset? ?-activity <factor> | -density transition_density? ?-clock clock_name? ?-duty <value>? ?-inst <instance_name>? ?-net <net_name>| -port <port_name>| -pin <pin_name>| -input_port <port_name>|-output_port <port_name>| -bidir_port <port_name>? ?-period <value>? ?-unclocked? ?-icg_ratio <num>? ?-comb_clockgate_ratio <num>? ?-hier <hierarchy_name>? ?-scale_factor <value>? ?-cell <cell_name>? ?-force? ?-quiet?",
        ),
        # man1/set_table_style.1
        _syn(
            "set_table_style",
            "Disables printing of specific columns and allows for specifying the minimum and maximum size of each column in a report",
            "set_table_style",
        ),
        # man1/set_thermal_analysis_mode.1
        _syn(
            "set_thermal_analysis_mode",
            "",
            "set_thermal_analysis_mode ?-help? ?-boundary_condition_file <filename>? ?-power_map_file <filename>? ?-temperature_map_file <filename>? ?-tool_path <path>?",
        ),
        # man1/set_threshold_voltage_group.1
        _syn(
            "set_threshold_voltage_group",
            "Groups timing libraries into different voltage threshold (Vth) classes (e.g., HVT, LVT, ULVT)",
            "set_threshold_voltage_group ?-help? ?-hinst <<string>>? -name <<group_name>> ?-override? {-libraries <<library list>> | -lib_cells <<lib cell list>>}",
        ),
        # man1/set_timing_derate.1
        _syn(
            "set_timing_derate",
            "Sets delay scaling or derating factors for early and late paths in the current design",
            "set_timing_derate ?-help? <derate_value>?<object_list>? ?-add? ?-cell_check? ?-cell_delay? ?-clock? ?-clock_period_check? ?-corner? ?-data? ?-dynamic? ?-early? ?-fall? ?-increment? ?-input_switching? ?-late? ?-mean? ?-multiply? ?-net_delay? ?-power_domain <string>? ?-pulse_width_check? ?-retain_delay? ?-rise? ?-sigma? ?-static? ?-statistical? ?-transition? ?-min | -max | -delay_corner delayCornerName?",
        ),
        # man1/set_trace_obj_connectivity_mode.1
        _syn(
            "set_trace_obj_connectivity_mode",
            "Controls certain aspects of how the connections of specified macros, selected macros, or specified ports are traced",
            "set_trace_obj_connectivity_mode ?-help? ?-reset? ?-macro_pins <list_of_pins>? ?-max_fanin_fanout <number>? ?-register_inputs <list_of_pins>? ?-register_outputs <list_of_pins>?",
        ),
        # man1/set_track_fill_config.1
        _syn(
            "set_track_fill_config",
            "Sets the parameters of the add_track_fill command",
            "set_track_fill_config ?-help? ?-attach_instance_name <attr_num>? ?-attach_net_name <attr_num>? ?-attach_net_prop {{<prop_name attr_num>} ... }? ?-core_license <license_combination>? ?-die_area_as_boundary? ?-dp <n>? ?-dp_timeout <seconds>? ?-extra_options <options>? ?-format {stream oasis}? ?-layer_map_file <streamOut_map_file>? ?-lib_name <library_name>? ?-license_dp_continue? ?-license_timeout <seconds>? ?-merge <list_of_external_stream_files>? ?-no_structure_name? ?-offset {<x y>}? ?-output_macros? ?-report_file? ?-reset {<parameter_name> |<all>}? ?-stripes <number>? ?-structure_name <structureName>? ?-track_fill_config_file <file_name>? ?-uniquify_cell_names? ?-units {100 | 200 | 400 | 800 | 1000 | 2000 | 4000 | 8000 | 10000 | 20000}? ?-working_dir <working_directory>?",
        ),
        # man1/set_twf_attribute.1
        _syn(
            "set_twf_attribute",
            "Specifies static timing analysis information",
            "set_twf_attribute ?-help? ?-clock <clock_name>? ?-clock_edge {rise | fall}? ?-clock_freq <value>? ?-fall_delay <{min:max>or<single_value}>? ?-fall_slack <{min:max>or<single_value}>? ?-fall_slew <{min:max>or<single_value}>? ?-net <net_name>? ?-pin <pin_name>? ?-reset? ?-rise_delay <{min:max>or<single_value}>? ?-rise_slack <{min:max>or<single_value}>? ?-rise_slew <{min:max>or<single_value}>? ?-type {data | clock}? ?-shift_arrival_time <time>? ?–clear_twf_attr?",
        ),
        # man1/set_verify_drc_mode.1
        _syn(
            "set_verify_drc_mode",
            "Sets the global parameters for the verify_drc command",
            "set_verify_drc_mode ?-help? ?-area {lx ly ux uy}? ?-check_illegal_trim_shapes {true | false}? ?-check_ndr_spacing {true | false | auto}? ?-check_only {all | regular | special | selected_net | selected | cell | default}? ?-check_reverse? ?-check_routing_halo {true | false}? ?-check_routing_halo_corner {true | false}? ?-check_same_via_cell {true | false}? ?-check_short_only {true | false}? ?-check_trim_length {true | false}? ?-check_uncolored {true | false}? ?-disable_rules {jog2jog_spacing|eol_spacing|cut_spacing|min_cut|enclosure|color|min_step|protru‐ sion|min_area|out_of_die|off_manufacturing_grid|off_routing_track}? ?-enable_post_passive_fill_check {true | false}? ?-exclude_pg_net {true | false}? ?-ignore_cell_blockage {true | false}? ?-ignore_fill_wire {true | false}? ?-ignore_non_rectangle_shapes {true | false}? ?-ignore_trial_route {true | false}? ?-layer_range {<layer1> ?<layer2>?}? ?-limit <value>? ?-max_wrong_way_halo <value>? ?-report<file_name>? ?-reset? ?-use_min_spacing_on_block_obs {true | false | auto}?",
        ),
        # man1/set_via_pillars.1
        _syn(
            "set_via_pillars",
            "This command sets a via pillar list for a cell term or a single via pillar for an instTerm",
            "set_via_pillars ?-help? {-term <term> | -instTerm <instTerm>} <stack_via_rule+> ?-required {0 | 1 | 2 | 3 | 4}?",
        ),
        # man1/set_virtual_clock_network_parameters.1
        _syn(
            "set_virtual_clock_network_parameters",
            "Specifies to estimate power for a virtual clock tree",
            "set_virtual_clock_network_parameters ?-help? ?-cell <cell_name>? ?-clock <list_of_clocks>? ?-library <library_name>? ?-max_fanout <value>? ?-wire_load_model <wireload_model>? ?-reset?",
        ),
        # man1/set_visible_bumps.1
        _syn(
            "set_visible_bumps",
            "Displays only the bumps with the specified bump cell names and hides all other bumps",
            "set_visible_bumps ?-help? {-bump_cells <bump_cell_name>| -all}",
        ),
        # man1/set_visible_netGroups.1
        _syn(
            "set_visible_netGroups",
            "Displays only the specified netGroups and hides all other netGroups",
            "set_visible_netGroups ?-help? {<netGroups> | -all}",
        ),
        # man1/set_visible_nets.1
        _syn(
            "set_visible_nets",
            "Displays only the specified nets and hides all other nets",
            "set_visible_nets ?-help? {<nets> | -all}",
        ),
        # man1/set_voltage_regulator_module.1
        _syn(
            "set_voltage_regulator_module",
            "",
            "set_voltage_regulator_module -component_list {<VRM_DEF_component_list>} -ground_pin_mapping {{<spice_pin_name>?<DEF_net_name>?}+} -input_pwr_pin_mapping {{<spice_pin_name>?<DEF_net_name>?}+} -name <vrm_name> -netlist <vrm_spice_netlist_file_name> -output_pwr_pin_mapping {{<spice_pin_name>?<DEF_net_name>?}+}",
        ),
        # man1/set_vt_skew_config.1
        _syn(
            "set_vt_skew_config",
            "Allows customization of the combinations of Vth classes to be analyzed",
            "set_vt_skew_config ?-help? ?-analysis_mode {setup | hold | both}? ?-clocks_only? ?-correlated_vt_groups <<corr_group>>? ?-exclude <<exclude>>? ?-exclude_nominal? ?-include_only <<include_only>>? ?-unique_vt_mode {none | slow | fast | nominal}?",
        ),
        # man1/set_vt_skew_derate.1
        _syn(
            "set_vt_skew_derate",
            "Assigns fast and slow derate factors to specific threshold voltage groups",
            "set_vt_skew_derate ?-help? ?-delay_corner <<string>>? ?-fast <<float>>? ?-hold? ?-mean? ?-resetViewListVTSkew? ?-setup? ?-sigma? ?-slow <<float>>? ?-threshold_voltage_group <<group name>>? ?-viewListVTSkew <<string>>?",
        ),
        # man1/set_well_tap_mode.1
        #   WARNING: unmatched closing bracket ']' at position 495
        _syn(
            "set_well_tap_mode",
            "Controls the behavior of addWellTap command",
            "set_well_tap_mode ?-help? ?-reset? ?-abut_boundary_tap_distance {{<cell1 cell2 distance1>} {<cell1 cell3 distance1>} {<cell2 cell3 distance3>} … }? ?-antenna_tap_break_cell <cell_list>? ?-antenna_tap_cell <cell_list>? ?-antenna_tap_left_cell <cell_list>? ?-antenna_tap_pitch <microns>? ?-antenna_tap_right_cell <cell_list>? ?-antenna_tap_right_top_edge_cell <cell_list>? ?-avoid_vertical_well_abutment {none|ntap|ptap|all_tap}? ?-avoidAbutment {true|false}? ?-block_boundary_only {true | false}?? ?-bottom_tap_cell cellName? ?-bottom_termination_cell <cellList>? ?-cell <cellName>? ?-channel_offset <offset_value>? ?-check_channel {true|false}? ?-column_cell <cellList>? ?-create_rows {true|false}? ?-disable_check_zone_at_boundary {none|vdd|vss|both}? ?-inRowOffset <offset_value>? ?-insert_cells <cellName rule dense_layer dense_rule boundary_layer boundary_rule>? ?-rule microns? ?-siteOffset <number_of_sites>? ?-tap_function_cells <cell_list>? ?-tap_termination_alignment {true|false}? ?-termination_align {left|right|center}? ?-termination_cell <cellList>? ?-top_tap_cell <cellName>? ?-top_termination_cell <cellList>? ?-vertical_boundary_spacing <spacing_with_well_tap>? ?-well_cut_cell <cellList>?",
        ),
        # man1/set_wire_load_mode.1
        _syn(
            "set_wire_load_mode",
            "Controls how the software searches through the design hierarchy to find the appropriate wire load model for a net, or a hierarchical part of a net",
            "set_wire_load_mode ?-help? {top | enclosed | segmented}",
        ),
        # man1/set_wire_load_model.1
        _syn(
            "set_wire_load_model",
            "Specifies the wire load model to be used from the technology library, and sets the wire load model on the design or on a hierarchical object (instance)",
            "set_wire_load_model ?-help? ?<list_of_instances_or_ports>? ?-library <library_name>? ?-max? ?-min? -name <wireload_model>",
        ),
        # man1/set_wire_load_selection_group.1
        _syn(
            "set_wire_load_selection_group",
            "Overrides the wire load selection table in the specified library",
            "set_wire_load_selection_group ?-help? <wireload_selection_group_name> ?<list_of_instances>? ?-library <library_name>? ?-max? ?-min?",
        ),
        # man1/setActiveLogicViewMode.1
        _syn(
            "setActiveLogicViewMode",
            "Controls certain behaviors of active logic view commands",
            "setActiveLogicViewMode ?-help? ?-reset? ?-keepAsync {false | true}? ?-keepHighFanoutPorts {true| false}? ?-keepInstInSdc {true|false}? ?-keepLoopBack {false | true}?",
        ),
        # man1/setAddRingMode.1
        _syn(
            "setAddRingMode",
            "Sets global variables for block rings and core rings when you use the addRing command",
            "setAddRingMode ?-help? ?-avoid_short {true | false}? ?-break_core_ring_io_list <io_list>? ?-continue_on_no_selection {true | false}? ?-detailed_log {true | false}? ?-extend_blockring_search_distance <distance>? ?-extend_corering_search_distance <float>? ?-extend_merge_with_prewires {true | false}? ?-extend_over_row {true | false}? ?-extend_search_nets {* | {net_names}}? ?-extend_stripe_search_distance <float>? ?-gap_width_without_io width? ?-ignore_rows {true | false}? ?-max_via_size {<shape width% height% target_penetration%>}? ?-orthogonal_only {true | false}? ?-reset? ?-ring_target {core_ring | default | first_ring | pad_ring | stripe}? ?-skip_crossing_trunks {horizontal | vertical | none}? ?-skip_via_on_pin {?Pad? ?Block? ?Cover? ?Standardcell? ?Physicalpin?}? ?-skip_via_on_wire_shape {blockring | stripe | followpin | corewire | blockwire | iowire | padring | ring | fillwire | noshape}? ?-spacing_from_block <value>? ?-split_long_via {<threshold_value step_value offset_value> <height_value>}? ?-stacked_via_bottom_layer <layername>? ?-stacked_via_top_layer <layername>? ?-via_using_exact_crossover_size {true | false}? ?-wire_center_offset {true | false}?",
        ),
        # man1/setAddStripeMode.1
        #   WARNING: unclosed bracket '[' at position 1840
        _syn(
            "setAddStripeMode",
            "Sets global variables for power stripes",
            "setAddStripeMode ?-help? ?-reset? ?-allow_jog {none|{?padcore_ring??block_ring?}}? ?-allow_nonpreferred_dir {none | ?blockring? ?corering? ?padring? ?stripe?}? ?-area {<lx ly ux uy> | <x1 y1 x2 y2 x3 y3> ...}? ?-break_at {none|{?block_ring? ?selected_block? ?unassigned_bump??overlap_ringpin? ?outer_ring??outside_ringmacro? ?blocks_without_same_net?}}? ?-color_balance {same_color|alternate_color|none}? ?-continue_on_no_selection {true | false}? ?-detailed_log {true | false}? ?-domain_offset_from_core {true | false}? ?-extend_to_closest_target {ring|stripe|same_dir_stripe|area_boundary|none}? ?-extend_to_first_ring {true | false}? ?-ignore_block_check {true | false}? ?-ignore_blockring_when_breaking {true | false}? ?-ignore_DRC {true | false}? ?-ignore_nondefault_domains {true | false}? ?-inside_cell_allow_shift {true | false}? ?-inside_cell_only {true | false}? ?-keep_pitch_after_snap {true | false}? ?-max_extension_distance distance? ?-max_via_size {shape width% height% target_penetration%}? ?-merge_with_all_layers {true | false}? ?-mesh_via {true | false}? ?-offset_from_core {true | false}? ?-optimize_stripe_for_routing_track {shift|none}? ?-orthogonal_offset {?{edge1 orthogonal_offset1} {edge2 edge3 orthogonal_offset2} {edge4 edge5 … orthogonal_offset3 } …?|?all orthogonal_offset?}? ?-orthogonal_only {true | false}? ?-over_row_extension {true | false}? ?-partial_set_thru_domain {true | false}? ?-recommend_width file_name? ?-remove_floating_stapling {true | false}? ?-remove_floating_stripe_over_block {true | false}? ?-remove_stripe_under_ring {true | false}? ?-respect_routes {none | fixed | fixed_and_clock | all}? ?-route_over_rows_only {true | false}? ?-rows_without_stripes_only {true | false}? ?-same_sized_stack_vias {true | false}? ?-skip_via_on_pin {?Pad? ?Block? ?Cover? ?Standardcell? ?Physicalpin?}? ?-skip_via_on_wire_shape {blockring | stripe | followpin | corewire | blockwire | iowire | padring | ring | fillwire | noshape} ?-spacing_type {edge_to_edge|center_to_center}? ?-spacing_from_block floating_point_value? ?-split_long_via {<threshold_value step_value offset_value height_value>}? ?-split_vias {true | false}? ?-split_wire_spacing floating_point_value? ?-split_wire_weight integer_0_to_10? ?-split_wire_width floating_point_value? ?-stacked_via_bottom_layer layerName? ?-stacked_via_top_layer layerName? ?-stapling_extend_to_minimum_spacing {true | false}? ?-stapling_nets_style {end_to_end | side_to_side | side_to_side_full_nets}? ?-stapling_shift {true | false}? ?-stop_at_closest_target {none|block_ring|core_ring|stripe}? ?-stop_at_last_wire_for_area {true | false}? ?-stripe_min_length {<floating_point_value> | stripe_width}? ?-stripe_min_width floating_point_value? ?-switch_cellname cellname? ?-switch_layer_overlap_length floating_point_value? ?-trim_antenna_back_to_shape {none | block_ring | core_ring | pad_ring | stripe}? ?-trim_antenna_max_distance distance? ?-trim_stripe {none|design_boundary|core_boundary}? ?-use_exact_spacing {true | false}? ?-use_point2point_router {true | false}? ?-use_stripe_width {true | false}? ?-via_using_exact_crossover_size {true | false}?",
        ),
        # man1/setAnalysisMode.1
        _syn(
            "setAnalysisMode",
            "Sets global analysis modes for timing analysis",
            "setAnalysisMode ?-help? ?-reset? ?-analysisType {single | bcwc | onChipVariation}? ?-asyncChecks {async | noAsync | asyncOnly}? ?-caseAnalysis {true | false}? ?-checkType {setup | hold}? ?-clkNetsMarking {beforeConstProp | afterConstProp}? ?-clkSrcPath {true | false}? ?-clockGatingCheck {true | false}? ?-clockPropagation {sdcControl | forcedIdeal | autoDetectClockTree}? ?-aocv {true | false}? ?-cppr {none | both | setup | hold}? ?-honorActiveLogicView {true | false}? ?-log {true | false}? ?-multi_input_switching_mode {0 | 1 | 2}? ?-propSlew {true | false}? ?-sequentialConstProp {true | false}? ?-skew {true | false}? ?-socv {true | false}? ?-timeBorrowing {true | false}? ?-timingEngine {statistical | static}? ?-timingSelfLoopsNoSkew {true | false}? ?-usefulSkew {true | false}? ?-useOutputPinCap {true | false}? ?-warn {true | false}?",
        ),
        # man1/setAttribute.1
        _syn(
            "setAttribute",
            "Attaches attributes to nets and subnets",
            "setAttribute ?-help? ?-max_fanout <integer>? ?-reset? ?-stripe_layer_range <minLayer>:<maxLayer>? {-net <netName> | -cell_pin <cell_name>:<pin_name>} ?-sub_net <sub_net_name> ?-comp_pin <comp>:<pin_name> <list>??-inst_pin <instance:pin_name> list?? ?-weight <integer>? ?-non_default_rule <rule_name>? ?-non_default_rule_effort {auto|soft|hard|no_taper}? ?-shield_net <special_net_name>? ?-shield_side {one_side | two_sides}? ???-em_ndr_rule <ruleName>? ?-em_ndr_dist <double>?? | ?-em_width_rule <layer> <width:dist pairs>?? ?-ndr_si_length_limit <layer:distance list>? ?-coaxial_shielded_layers <layer_number>:<layer_number>? ?-coaxial_shield_limit <layer_number:layer_number>? ?-coaxial_shield_interval <tracks_number >| <metal_layer_name>:<tracks_number …>? ?-pattern {steiner|trunk}? ?-top_preferred_routing_layer <layer_number>? ?-bottom_preferred_routing_layer <layer_number>? ?-top_preferred_shielding_layer <layer_number>? ?-bottom_preferred_shielding_layer <layer_number>? ?-preferred_routing_layer_effort {low|medium|high|hard}? ?-preferred_extra_space <integer>? ?-avoid_detour {true|false}? ?-skip_routing {true|false}? ?-skip_antenna_fix {true|false}? ?-multi_cut_via_effort {low|medium|high}? ?-si_post_route_fix {true|false}? ?-min_stack_layer <layer_number>? ?-stack_distance <distance>? ?-mask <mask_number>? ?-layer_mask <bottomLayerNum:topLayerNum>? ?-one_side_spacing <bottomLayerNum:topLayerNum>?",
        ),
        # man1/setBottomIoPadOrient.1
        _syn(
            "setBottomIoPadOrient",
            "Changes the orientation for the bottom pad (South side)",
            "setBottomIoPadOrient ?-help?",
        ),
        # man1/setBudgetingMode.1
        _syn(
            "setBudgetingMode",
            "Sets the timing budgeting mode",
            "setBudgetingMode ?-help? ?-abutted {true|false}? ?-accumulated {true|false}? ?-boundaryConditionTemplatePath <directory_path>? ?-bufferDelayLibCell <libname>/<cellname>? ?-bufferDelaySelectionEffort {low|high|none}? ?-ccd {true|false}? ?-constantModel {true|false}? ?-distributeMMMC {true|false}? ?-dontWriteWireLoad {true|false}? ?-driveConstraint {drive | drive_cell | input_transition}? ?-fixTopLevelPaths {none|all|negativeOnly|positiveOnly}? ?-handleComplexSDC {true|false}? ?-honorPortBoundaryCondition {true|false}? ?-honorPortDelays {true|false}? ?-honorReportTimingFormat {true|false}? ?-ignoreDontTouch {true|false}? ?-includeLatency {true|false}? ?-includeWireLoadsInLib {true|false}? ?-inputLoad {true|false}? ?-justify {delay|exception|lib_arc|boundary_condition|all}? ?-justifyBudgetDir <directory_name>? ?-keepPinListsForBlockPorts {true|false}? ?-latencyOnClocks {true|false}? ?-localLatency {true|false}? ?-localUncertainty {true|false}? ?-makeNegativeInputDelayZero {true | false}? ?-masterClone {masterOnly|merged|uniqueViewPerHInst}? ?-noFalsePathsForUnCstrPorts {true|false}? ?-noSetupView {true|false}? ?-noHoldView {true|false}? ?-overrideNetCap <value>? ?-reportOrModifyBudget {true|false}? ?-reset? ?-rptNegSlackOnPorts <value>? ?-sdcContents {full | pushDownOnly | boundaryConstraintsOnly | noBoundaryCondition | noBoundaryConstraints}? ?-snapFdBudgetTo <value>? ?-snapInputBudgetTo <value>? ?-snapNegativeOnly {true|false}? ?-snapOutputBudgetTo <value>? ?-stageBasedFanoutDrivingFactor <value>? ?-stageBasedPartitionMultiplier {{HInst1 m1} {HInst2 m2}..}? ?-stageBasedWeight {S | C | B}? ?-topLevel <value>? ?-topLevelDelayPerLen <value>? ?-topLevelMinDelayPerNet <value>? ?-useBoundaryCondition {optimized | template | actual | empty}? ?-virtualClock {true|false}? ?-virtualOptEngine {none|earlyTimingEngine|proto}? ?-writeConstraintsForClkOutputPorts {true|false}? ?-writeFPForHold {true|false}? ?-writeLatencyPerClock {true|false}?",
        ),
        # man1/setBufFootPrint.1
        _syn(
            "setBufFootPrint",
            "Sets the buffer cell footprint name",
            "setBufFootPrint ?-help?",
        ),
        # man1/setBumpFixed.1
        _syn(
            "setBumpFixed",
            "Fixes a specified group of assigned bumps to keep them from being reassigned",
            "setBumpFixed ?-help? {-allBumps | -byBumpName {<list>} | -byBumpSite {<list>}}",
        ),
        # man1/setBumpPlacementStatus.1
        _syn(
            "setBumpPlacementStatus",
            "Sets the bump placement status",
            "setBumpPlacementStatus ?-help? ?-bumpName <Name> | -selected? PLACED | FIXED | COVER",
        ),
        # man1/setBusGuideMultiColors.1
        _syn(
            "setBusGuideMultiColors",
            "Colors all the bus guides",
            "setBusGuideMultiColors",
        ),
        # man1/setCheckMode.1
        _syn(
            "setCheckMode",
            "Sets the data checks that the software performs",
            "setCheckMode ?-help? ?-reset? ?-all {true | false}? ?-checkIlm {true | false}? ?-extraction {true | false}? ?-floorplan {true | false}? ?-globalNet {true | false}? ?-integrity {true | false}? ?-io {true | false}? ?-library {true | false}? ?-mgrid {true | false}? ?-netlist {true | false}? ?-placement {true | false}? ?-route {true | false}? ?-sroute {true | false}? ?-tapeOut {true | false}? ?-timingGraph {true | false}? ?-vcellnetlist {true | false}?",
        ),
        # man1/setClonePtnOrient.1
        _syn(
            "setClonePtnOrient",
            "Changes the orientation of the specified partition clone",
            "setClonePtnOrient ?-help? <name> {R0 R90 R180 R270 MX MX90 MY MY90}",
        ),
        # man1/setCompressLevel.1
        _syn(
            "setCompressLevel",
            "Specifies the compression level to use when compressing large data files",
            "setCompressLevel <value>",
        ),
        # man1/setCycleBudgetRatio.1
        _syn(
            "setCycleBudgetRatio",
            "Sets the budgeting constraint based on the clock cycle, which ensures that budgeting is done in min‐ imum time and memory by deriving partition block delays from the total clock cycle time",
            "setCycleBudgetRatio ?-help? {???{-fromTop | -fromPtn {hinst ratio}} {-toTop | -toPtn {hinst ratio}}?? ?-clock <string>?? | ?-reset?}",
        ),
        # man1/setDbGetMode.1
        _syn(
            "setDbGetMode",
            "Controls certain aspects of how the dbGet command displays object information",
            "setDbGetMode ?-help? ?-reset? ?-displayFormat {simple | table}? ?-displayLimit <value>? ?-escapeBusChar {true | false}?",
        ),
        # man1/setDefaultWorkspace.1
        _syn(
            "setDefaultWorkspace",
            "Sets specified workspace as the default",
            "setDefaultWorkspace ?-help? -name <workspaceName> ?-dir <directory>?",
        ),
        # man1/setDelayCalMode.1
        _syn(
            "setDelayCalMode",
            "Sets global parameters for delay calculation",
            "setDelayCalMode ?-help? ?-accuracy_level <level>? ?-advanced_pincap_mode {0 | 1 | 2}? ?-advanced_node_pin_cap_settings {true | false}? ?-combine_mmmc {none | early_late | early_late_corner}? ?-early_irdrop_data_type {best_average | worst | best | average | worst_average}? ?-reset? ?-enable_high_fanout {true | false}? ?-enable_input_slew_sensitivity_on_constraint {true | false}? ?-enable_quiet_receivers_for_hold {true | false}? ?-equivalent_waveform_model {none | no_propagation | propagation}? ?-equivalent_waveform_model_for_timing_check {true|false}? ?-ewm_type {moments | simulation}? ?-honorSlewPropConstraint {true | false}? ?-irdrop_data_type {best_average | worst | best | average | worst_average}? ?-irDrop_window_based {none | late | early | both}? ?-late_irdrop_data_type {best_average | worst | best | average | worst_average}? ?-library_interpolation_mode {linear | non_linear}? ?-ignoreNetLoad {true | false}? ?-reportOutBound {true | false}? ?-SIAware {true | false}? ?-signoff_alignment_settings {true | false}? ?-skip_slew_merge_from_disabled_path {false | true}? ?-slewOutBoundLimitHigh <value>? ?-slewOutBoundLimitLow value? ?-socv_accuracy_mode {low | medium | high | ultra}? ?-socv_lvf_mode {moments | early_late}? ?-socv_machine_learning_level {0 | 1 | 3}? ?-socv_use_lvf_tables {all | delay | slew | constraint}?",
        ),
        # man1/setDelayFootPrint.1
        _syn(
            "setDelayFootPrint",
            "Specifies the delay cell footprint",
            "setDelayFootPrint ?-help? ?-library <libName>? <names>",
        ),
        # man1/setDensityMapMode.1
        _syn(
            "setDensityMapMode",
            "Sets global parameters for the reportDensityMap command",
            "setDensityMapMode ?-help? ?-reset? ?-gridInMicron <microns>? ?-gridInRow <numberRows>? ?-ignoreBlock {true|false}? ?-ignoreFiller {true|false}? ?-threshold <density>?",
        ),
        # man1/setDesignMode.1
        _syn(
            "setDesignMode",
            "Specifies the process technology value",
            "setDesignMode ?-help? ?-reset? ?-addPhysicalCell {hier | flat}? ?-backsideBottomRoutingLayer <layer>? ?-backsideTopRoutingLayer <layer>? ?-bottomRoutingLayer <layer>? ?-compressedPGDB {true | false}? ?-congEffort {low|medium|high|auto}? ?-dual_rail_via_pitch <min_via_pitch> <min_filler_via_pitch> <cell_boundary_spacing>? ?-earlyClockFlow {true | false}? ?-earlyPBAMode {none | high}? ?-expressRoute {true | false}? ?-flowEffort {express | standard | extreme}? ?-idealHoldFixing {true|false}? ?-ignore_followpin_vias {true | false}? ?-merge_trim_shapes {{layers <layer_name_list> gap <gap_value> max_merge_num <number_of_max_merge> masks {<mask_num> ...}} ...}? ?-node {N22|N12|N10|N7|N7Plus|N6|N5|N5Plus‐ Plus|N4|N3|N3E|N2|S11|S10|S8|S7|S5|S4|S3|S2|G7|G5|ICF|I7|I5|P1277|P1278|P1280|C12|C7|unspecified}? ?-optimizationDensityScreenMargin <margin>? ?-pessimisticMode {true | false}? ?-powerEffort {none | low | high}? ?-process <integer>? ?-slackWeighting {unityWeighting|viewBasedWeighting}? ?-topRoutingLayer <layer>? ?-trim_grid_group <group_name>?",
        ),
        # man1/setDistributeHost.1
        _syn(
            "setDistributeHost",
            "Specifies the multiple-CPU processing configuration for distributed processing or Superthreading",
            "setDistributeHost ?-help? ?-add <string>? ?-args <string>? ?-custom? ?-custom_script <string>? ?-custom_script_list <string>? ?-local? ?-lsf? ?-nc? ?-noWaitTaskComeUp? ?-queue <string>? ?-remove <string>? ?-reportLsfInfo? ?-resource <string>? ?-rsh? ?-shellTimeout <integer>? ?-single_cpu_lsf_args <string>? ?-ssh? ?-timeOut <integer>? ?-env_script <string>?",
        ),
        # man1/setDontUse.1
        _syn(
            "setDontUse",
            "Sets a dont_use attribute on a cell, prohibiting timing optimization commands from using this cell during op‐ timization",
            "setDontUse ?-help?{{<cellName ><value>} | {-reset}} ?-hinst <hinstName>?-reset??",
        ),
        # man1/setDrawView.1
        _syn(
            "setDrawView",
            "Sets the design view in the design display area",
            "setDrawView ?-help? <mode>",
        ),
        # man1/setEcoMode.1
        _syn(
            "setEcoMode",
            "Controls certain behaviors of the ecoAddRepeater, ecoChangeCell, and ecoDeleteRepeater ECO commands",
            "setEcoMode ?-help? ?-addPortAsNeeded {true|false}? ?-batchMode {true|false}? ?-reset? ?-honorDontTouch {true|false}? ?-honorDontUse {true|false}? ?-honorFixedNetWire {true|false}? ?-honorFixedStatus {true|false}? ?-honorPowerIntent {true|false}? ?-inheritNetAttr {true|false}? ?-LEQCheck {true|false}? ?-modifyOnlyLayers <bottom_layer>:<top_layer>? ?-prefixName <prefix>? ?-preserveModuleFunction {true|false}? ?-refinePlace {true|false}? ?-spreadInverter {true|false}?e ?-updateTiming {true|false}? ?-delayCalcEffort <effort_level>?",
        ),
        # man1/setEditMode.1
        #   WARNING: unclosed bracket '[' at position 156
        _syn(
            "setEditMode",
            "Updates the Edit Route and Edit Via forms, the design display area, and vias that are subsequently created with the editAddVia command, with the information specified by the parameters",
            "setEditMode ?-help? ?-align {true|false}? ?-allow_45_degree {true|false}? ?-arrow_increment <value>? ?-assign_multi_pattern_color {auto|mask1|mask2|mask3}? ?-auto_distribute_bus {true|false} ?-auto_split_bus {true|false}? ?-bus_honor_start_params {true|false}? ?-bus_honor_width_setting {true|false}? ?-bus_total_width_horizontal <value>? ?-bus_total_width_vertical <value>? ?-change_order_at_turn {Reverse Order | Keep Order}? ?-check_design_boundary {true|false}? ?-circle_NDR_vias_only {true|false}? ?-close_polygons {true|false}? ?-color_align_with_track {true|false}? ?-connect_pin {in|out|inout|nodir}? ?-connect_with_specified_layer {true|false}? ?-create_crossover_vias {true|false}? ?-create_is_edit_flag {true|false}? ?-create_via_on_pin {true|false}? ?-cut_class <class_name>? ?-cut_wire_overlap {regular|special}? ?-debug_file <output_file>? ?-delete_pin_with_wire {true|false}? ?-delete_tsv {true|false}? ?-delete_wire_via_deep_through {true|false}? ?-display_wire_length_with_cursor {true|false}? ?-draw_shield {true|false}? ?-draw_with_group_centerline {true|false}? ?-drawing_wire <value>? ?-drc_aware_cross_metal {true|false}? ?-drc_on {true|false}? ?-drc_use_non_default_spacing {true|false}? ?-extend_wires {start|end|start_cell_boundary|end_cell_boundary}? ?-final_check_with_verify {true|false}? ?-ignore_drc {conn_antenna|max_via_stack|min_cut|min_enclosed_area|min_step|protrusion}? ?-jog_connect_layer <value>? ?-keep_floating_via {true|false}? ?-keep_status {true|false}? ?-keep_via {true|false}? ?-lateral_movement_range <value>? ?-layer <name>? ?-layer_horizontal <name>? ?-layer_maximum <layerName>? ?-layer_minimum <layerName>? ?-layer_vertical <name>? ?-look_down_layers <integer>? ?-look_up_layers <integer>? ?-max_pointer_number <integer>? ?-mirror_bus_route {true|false}? ?-nets <nets>? ?-no_merge_special_wire {true|false}? ?-only_show_edit_layer {true|false}? ?-orthogonal_connection_only {true|false}? ?-outer_shield_spacing <value>? ?-outer_shield_width <value>? ?-override {true|false}? ?-partial_overlap_threshold <value>? ?-pull_back_distance <string>? ?-reset? ?-reshape {true|false}? ?-return_object_pointer {true|false}? ?-rule <rule>? ?-shape {RING|STRIPE|FOLLOWPIN|IOWIRE|COREWIRE|BLOCKWIRE|PADRING|BLOCKRING|FILLWIRE|FILLWIREOPC|DRCFILL|None}? ?-shield {high|low|adjacent}? ?-shield_look_down_layers <integer>? ?-shield_look_up_layers <integer>? ?-shield_shape {RING|STRIPE|FOLLOWPIN|IOWIRE|COREWIRE|BLOCKWIRE |PADRING|BLOCKRING|FILLWIRE|DRCFILL|None}? ?-shielding_nets <nets>? ?-show_drc_info_for_edit_shape {true|false}? ?-sibling_look_down_layers <integer>? ?-sibling_look_up_layers <integer>? ?-snap {true|false}? ?-snap_align_to {center|low|high|auto}? ?-snap_bus_to_pin {true|false}? ?-snap_end_to {track_regular|track_special|manufacturing_grid}? ?-snap_objects_to_track {special|regular|patch|pin}? ?-snap_to {special|pg|pin|row}? ?-snap_to_track_honor_color {true|false}? ?-snap_trim_metal_to_trim_grid {true|false}? ?-spacing <value>? ?-spacing_horizontal <value>? ?-spacing_vertical <value>? ?-status {cover|fixed|noshield|routed|shield|auto}? ?-stop_at_drc {true|false}? ?-stretch_end {high | low}? ?-stretch_with_intersect {true|false}? ?-subclass {<subclass>}? ?-turn_at {center_line|wire_edge}? ?-type {regular|special|patch}? ?-unrestricted_regular_wire_width {true|false}? ?-update_shield_net {true|false}? ?-use_fixVia {true|false}? ?-use_interleaving_wire_group {true|false}? ?-use_wire_group {true|false}? ?-use_wire_group_bits <number_of_bits>? ?-use_wire_group_reinforcement {true|false}? ?-use_wire_group_reinforcement_group_via {true|false}? ?-use_wire_group_reinforcement_spacing <spacing>? ?-use_wire_group_reinforcement_width <width>? ?-verbose {true|false}? ?-via_allow_geom_drc {true|false}? ?-via_auto_replace {true|false}? ?-via_auto_snap {true|false}? ?-via_cell_name <cellname>? ?-via_columns <value>? ?-via_create_by {viacell|parameters}? ?-via_cut_layer <cut_layer>? ?-via_exclude_spec <value>? ?-via_override_spec <value>? ?-via_rows <value>? ?-via_scale_height <value>? ?-via_scale_width <value>? ?-via_snap_honor_color {true|false}? ?-via_snap_to_intersection {true|false}? ?-via_type {auto|regular|special}? ?-width <value>? ?-width_horizontal <value>? ?-width_vertical <value>? ?-wire_override_spec <specification>?",
        ),
        # man1/setEndCapMode.1
        _syn(
            "setEndCapMode",
            "",
            "setEndCapMode ?-help? ?-antenna_tap_fill_wall_cells {listOfCellNames}? ?-avoidTwoSitesCellAbut {true|false}? ?-barrier_border_cell_bottom_y <cellNames>? ?-barrier_border_cell_top_y <cellNames>? ?-barrier_cell_x <cellNames>? ?-barrier_cell_xy <cellNames>? ?-barrier_cell_y <cellNames>? ?-barrier_keepout_from_boundary {value_x value_y}? ?-barrier_pitch {x_pitch y_pitch}?|?-barrier_termination_bottom_y <cellNames>? ?-barrier_termination_top_y <cellNames>? ?-barrier_termination_x <cellNames>? ?-barrier_y_mode {1|2}? ?-bottomEdge <ListOfCellNames>? ?-boundary_tap {true|false}? ?-boundary_tap_swap_flow {true|false}? ?-cells <ListOfCellNames>? ?-create_rows {true|false}? ?-DoubleHeightIncornerProtrusion {true|false}? ?-enable_shrink_physical_cell_flow {true|false}? ?-flipY {true|false}? ?-incrementalLeftEdge <ListOfCellNames>? ?-incrementalRightEdge <ListOfCellNames>? ?-insert_nppp_wall {{Wall_Cell} {Wall_Pad}}? ?-leftBottomCorner <ListOfCellNames>? ?-leftBottomCornerEven <cellName>? ?-leftBottomCornerNeighbor <cellName>? ?-leftBottomCornerOdd <cellName>? ?-leftBottomEdge <cellName>? ?-leftBottomEdgeEven <cellName>? ?-leftBottomEdgeNeighbor <site1_cell site2_cell...>? ?-leftBottomEdgeOdd <cellName>? ?-leftCornerBottomBorder <ListOfCellNames>? ?-leftCornerTopBorder <ListOfCellNames>? ?-leftEdge <cellName>? ?-leftEdgeBottomBorder <cellName>? ?-leftEdgeEven <cellName>? ?-leftEdgeOdd <cellName>? ?-leftEdgeTopBorder <cellName>? ?-leftTopCorner <ListOfCellNames>? ?-leftTopCornerEven <cellName>? ?-leftTopCornerNeighbor <cellName>? ?-leftTopCornerOdd <cellName>? ?-leftTopEdge <cellName>? ?-leftTopEdgeEven <cellName>? ?-leftTopEdgeNeighbor <site1_cell site2_cell...>? ?-leftTopEdgeOdd <cellName>? ?-min_horizontal_channel_width <channelWidth>? ?-min_jog_height <jogHeight>? ?-min_jog_width <jogWidth>? ?-min_vertical_channel_width <channelWidth>? ?-nppp_wall_pitch <spacingValue>? ?-nppp_wall_to_FILLWALL_spacing <spacingValue>? ?-nppp_wall_to_incorner_spacing <spacingValue>? ?-prefix endcaprefix? ?-reset? ?-rightBottomCorner <ListOfCellNames>? ?-rightBottomCornerEven <cellName>? ?-rightBottomCornerNeighbor <cellName>? ?-rightBottomCornerOdd <cellName>? ?-rightBottomEdge <cellName>? ?-rightBottomEdgeEven <cellName>? ?-rightBottomEdgeNeighbor <site1_cell site2_cell...>? ?-rightBottomEdgeOdd <cellName>? ?-rightCornerBottomBorder <ListOfCellNames>? ?-rightCornerTopBorder <ListOfCellNames>? ?-rightEdge <cellName>? ?-rightEdgeBottomBorder <cellName>? ?-rightEdgeEven <cellName>? ?-rightEdgeOdd <cellName>? ?-rightEdgeTopBorder <cellName>? ?-rightTopCorner <ListOfCellNames>? ?-rightTopCornerEven <cellName>? ?-rightTopCornerNeighbor <cellName>? ?-rightTopCornerOdd <cellName>? ?-rightTopEdge <cellName>? ?-rightTopEdgeEven <cellName>? ?-rightTopEdgeNeighbor <site1_cell site2_cell...>? ?-rightTopEdgeOdd <cellName>? ?-topBottomEdge <ListOfCellNames>? ?-topEdge <ListOfCellNames>? ?-useEvenOddSite {none|even|odd}? ?-wall_keepout_from_vertical_boundary <macro>? ?-wall_offset <macro>? ?-wall_pitch <macro>? ?-wall_shift_step <macro>? ?-wall_to_convex_corner_spacing <macro>?",
        ),
        # man1/setExportMode.1
        _syn(
            "setExportMode",
            "Controls certain aspects of how the software writes out a Verilog netlist",
            "setExportMode ?-help? ?-reset? ?-fullPinout {true | false}? ?-implicitPortMapping {true | false}?",
        ),
        # man1/setExtractRCMode.1
        _syn(
            "setExtractRCMode",
            "Sets the native RC extraction mode",
            "setExtractRCMode ?-help? ?-reset? ?-assumeMetFill <scalevalue>? ?-capFilterMode {relOnly | relAndCoup | relOrCoup}? ?-cerebrus_license_only {true | false}? ?-compressOptMemRCDB {true | false}? ?-coupled {true | false}? ?-coupling_c_th <value_in_fF>? ?-defViaCap {true | false}? ?-effortLevel {low | medium | high | signoff}? ?-engine {preRoute | postRoute}? ?-extraCmdFile fileName? ?-extractionFillStreamMapFile <fileName>? ?-extract_rc_quantus_executable <path_to_Quantus_executable>? ?-hardBlockObs {true | false}? ?-incremental {true | false}? ?-layerIndependent {0 | 1}? ?-lefTechFileMap <fileName>? ?-localCpu number_of_cpu? ?-pvs_fill {true | false}? ?-qrcCmdFile <fileName>? ?-qrcCmdType {auto | partial | custom}? ?-qrcOutputMode {rcdb | spef}? ?-qrcRunMode {concurrent | sequential}? ?-relative_c_th <value>? ?-signoff_stream_layer_map <fileName>? ?-total_c_th <value_in_fF>? ?-tQuantusModelFile <fileName>? ?-tsvSubcktFile <file_name>? ?-turboReduce {true | false | auto}? ?-useQrcOAInterface {true | false}? ?-useShieldingInDetailMode {true | false}? ?-viaCap {true | false}? ?-writeDefOptionsForSignoffExtract list_of_def_options?",
        ),
        # man1/setFillerMode.1
        #   WARNING: bracket mismatch: '[' at position 815 closed by '}' at position 864
        #   WARNING: unmatched closing bracket ']' at position 865
        _syn(
            "setFillerMode",
            "Controls certain aspects of how the software adds filler cells",
            "setFillerMode ?-help? ?-reset? ?-add_fillers_with_drc {true|false}? ?-avoid_abutment_patterns { 1:1 1:2 ...}? ?-check_signal_drc {true | false}? ?-check_trim_rule {true|false}? ?-core {{list_of_cells1} {list_of_cells2} ...}? ?-corePrefix <prefix>? ?-createRows {true | false}? ?-keepFixed {true | false}? ?-diffCellViol {true | false}? ?-distribute_implant_evenly {true|false}? ?-double_height_filler_insertion {true|false}? ?-ecoMode {true | false}? ?-enable_restore_filler_flow {true|false}? ?-fitGap {true | false}? ?-honorPrerouteAsObs {true | false}? ?-horizontal_exception_cell {fillerCell ...}? ?-horizontal_max_length <instance_length>? ?-horizontal_repair_cell {fillCell ...}? ?-preserveUserOrder {true | false}? ?-scheme {locationFirst | cellFirst}? ?-swap_cell {{cell swap pair1} {cell swap pair2} ...}? ?-vertical_stack_exception_cell <ListOfCellNames>}? ?-vertical_stack_left_edge_exception_cell <ListOfCellNames>? ?-vertical_stack_max_length <instance_length>? ?-vertical_stack_repair_cell {fillerCell ...}? ?-vertical_stack_repair_edge {left|right}? ?-vertical_stack_right_edge_exception_cell <ListOfCellNames>? ?-y_flip_type { integer : { first | last } ... }?",
        ),
        # man1/setFinishFPlanMode.1
        _syn(
            "setFinishFPlanMode",
            "Set the active objects and specifies the channel direction for the finishFloorplan command to use whenever you perform advanced placement-related refinements to a floorplan",
            "setFinishFPlanMode ?-help? ?-reset? ?-abuttedEdgeAsNonRowArea {true|false}? ?-activeObj {macro|macroHalo|core|iopad|iocell|fence|hardblkg|softblkg|partialblkg|routeblkg|routingblkg|row}? ?-direction {<x>|<y>|<xy>}? ?-drcRegionObj {macro|macroHalo|hardBlkg|minGap|coreSpacing|nonRowArea|row}? ?-override {true|false}?",
        ),
        # man1/setFixedBlockSize.1
        _syn(
            "setFixedBlockSize",
            "Specifies that during floorplan resizing, the size of the specified modules and/or blackboxes should not change",
            "setFixedBlockSize ?-help? <name_list>",
        ),
        # man1/setFixedBudget.1
        _syn(
            "setFixedBudget",
            "This command fixes the budget for a particular path segment between partitions and start/end points and helps in reducing the distribution budget delay in the path segments",
            "setFixedBudget ?-help? {?{?{-from {list_of_pins} | -fromFlopsOf {hinst}} {-to {list_of_pins} | -toFlopsOf {hinst}}? | ?-through {list_of_hinst}?} {-slack | -delay } ?-add? <value>? | ?-reset?}",
        ),
        # man1/setFlipChipMode.1
        _syn(
            "setFlipChipMode",
            "Loads data for placePIO and fcroute commands",
            "setFlipChipMode ?-help? ?-reset? ?-allow_layer_change {true | false}? ?-auto_pairing_file <fileName>? ?-bump_use_oct_shape {true | false}? ?-check_bump_access_directions {true|false}? ?-compaction {true | false}? ?-connectPowerCellToBump {true | false}? ?-constraintFile <fileName>? ?-drop_via_on_all_geometries {true | false}? ?-drop_via_on_power_mesh <layerName>? ?-extraConfig <fileName>? ?-finger_direction {N|E|S|W}? ?-finger_max_width <real_value>? ?-finger_min_width <real_value>? ?-finger_target_mesh_layer_range {<topLayer> ?<bottomLayer>?}? ?-honor_bump_connect_target_constraint {true | false}? ?-ignore_pad_type_check {true | false}? ?-layerChangeBotLayer <layerName>? ?-layerChangeTopLayer <layerName>? ?-lower_layer_prevent_45_routing {true | false}? ?-lower_layer_route_width <value>? ?-merge_nearby_pin {true | false}? ?-multi_pad_routing_style {default|serial|star}? ?-multipleConnection {multiPadsToBump | multiBumpsToPad | default}? ?-pg_mesh_direction {default | horizontal | vertical}? ?-pg_mesh_main_width <real_value>? ?-pg_mesh_max_width <real_value>? ?-pg_mesh_width <value>? ?-prevent_diagonal_wire_access_bumps {true | false}? ?-prevent_via_under_bump {true | false}? ?-prevent_via_under_bump_extension <real_value>? ?-route_bump_cluster {true|false}? ?-route_pg_style {none | finger | mesh}? ?-route_style {manhattan | 45DegreeRoute}? ?-routeWidth <real_value>? ?-via_abut_bump {true | false}? ?-wire_to_pad_honor_min_spacing <float_value>?",
        ),
        # man1/setFlipping.1
        _syn(
            "setFlipping",
            "Specifies the orientation of the bottom row in the core area",
            "setFlipping ?-help?",
        ),
        # man1/setFPlanMode.1
        _syn(
            "setFPlanMode",
            "Sets the global parameters of the check floorplan feature",
            "setFPlanMode ?-help? ?-reset? ?-autoSyncMasterClone {busGuides|constraints|stdcells|macros|routeBlockages|placeBlockages}? ?-cellsForExtraSites <cell_name>? ?-checkTypes {basic|fence|oddEvenSiteRow|macroPin|color|alignmentFollowingPin|alignmentPartitionClone| busGuideConnectivity|feedThrough|partitionInPartition|multiLayerPin|powerDomain| partition|place|sameLengthSite|narrowChannel|blockOnly|unifiedVddOnBottom|tsv|all}? ?-cutOffPlaceBlockageOutsideDie {true|false}? ?-cutOffRouteBlockageOutsideDie {true|false}? ?-defaultBlockageNamePrefix <string>? ?-defaultPowerDomainSite {true|false}? ?-defaultRowPatternSite <string>? ?-defaultTechSite <string>? ?-enableRectilinearDesign {true|false}? ?-extraRowPattern <rowPatternName>? ?-extraSites <site_name>? ?-firstRowSiteIndex <int>? ?-includeIoWhenInitArea {true|false}? ?-initAllCompatibleCoreSiteRows {true|false}? ?-keepRowsWhenMovingPowerDomain {true|false}? ?-lastRowSiteIndex <int>? ?-maxIoHeight {true|false}? ?-minimumSites <value>? ?-move_child_constraint_with_constraint {true|false}? ?-move_macros_with_constraint {guide|region|fence|none|all}? ?-move_preplaced_std_cell_only {true|false}? ?-move_std_cell_with_constraint {guide|region|fence|none|all}? ?-narrowChannelThreshold <value>? ?-no_cut_row {true|false}? ?-powerRailLayer <string>? ?-rowHeightIncrementCornerToCorner <value>? ?-rowHeightIncrementIncornerToCorner <value>? ?-rowHeightIncrementIncornerToIncorner <value>? ?-rowHeightMultiple <value>? ?-rowSiteHeight {any|odd|even|computed}? ?-rowSiteWidth {any|odd|even}? ?-skipViolations <string>? ?-snap_all_corners_to_grid {true|false}? ?-snapBlockGrid {manufacturing|inst|placement|userDefine|LayerTrack|finfetInst|finfetManufacturing|finfetPlacement}? ?-snapConstraintGrid {manufacturing|inst|placement|userDefine|LayerTrack|finfetInst|finfetManufacturing|finfetPlacement}? ?-snapCoreGrid {manufacturing|inst|placement|userDefine|LayerTrack|finfetInst|finfetManufacturing|finfetPlacement}? ?-snapDieGrid {manufacturing|inst|placement|userDefine|LayerTrack|finfetInst|finfetManufacturing|finfetPlacement}? ?-snapIoGrid {manufacturing|inst|placement|userDefine|LayerTrack|finfetInst|finfetManufacturing|finfetPlacement}? ?-snapPlaceBlockageGrid {manufacturing|inst|finfetInst|finfetManufacturing|userDefine}? ?-snapPlaceBlockageType {closest|upsize|sequential}? ?-user_define_grid {<x_offset y_offset x_pitch y_pitch>}?",
        ),
        # man1/setFPlanRowSpacingAndType.1
        _syn(
            "setFPlanRowSpacingAndType",
            "Specifies the standard row spacing values and row pattern type",
            "setFPlanRowSpacingAndType ?-help?",
        ),
        # man1/setGenerateViaMode.1
        _syn(
            "setGenerateViaMode",
            "Auto-generates vias required by nanoroute for the default and non-default rules (NDRs)",
            "setGenerateViaMode ?-help? ?-reset? ?-auto {true|false}? ?-ndr_only {true|false}?",
        ),
        # man1/setHierMode.1
        _syn(
            "setHierMode",
            "Sets global parameters for hierarchy aware optimization",
            "setHierMode ?-help? ?-reset? ?-addAntennaCell {true | false}? ?-optStage {preCTS | postCTS | unset}?",
        ),
        # man1/setHInstColorId.1
        _syn(
            "setHInstColorId",
            "Specifies the color ID for a hierarchical instance",
            "setHInstColorId ?-help? <hInstName> <colorID> ?-descendant?",
        ),
        # man1/setIlmMode.1
        _syn(
            "setIlmMode",
            "Controls certain behaviors of ILM commands",
            "setIlmMode ?-help? ?-reset? ?-filterInternalPath {true|false}? ?-keepAsync {true|false}? ?-keepHighFanoutPorts {true|false}? ?-keepInstInSdc {true|false}? ?-ilm <ilmName>? ?-ilmCell <ilmCellName>? ?-keepFlatten {true|false}? ?-keepLoopBack {true|false}? ?-map {view|corner}? ?-maxNumInsts <maxInstances>? ?-maxNumRegisters <maxRegisters>? ?-resetMap {view|corner}? ?-slackDriven {true|false}? ?-top <topViewName>?",
        ),
        # man1/setIlmType.1
        _syn(
            "setIlmType",
            "Controls the behavior of commands in the presence of ILMs",
            "setIlmType ?-help? ?-model {timing | si}?",
        ),
        # man1/setImportMode.1
        _syn(
            "setImportMode",
            "Controls aspects of how the software reads in the Verilog netlist and other design files",
            "setImportMode ?-help? ?-reset? ?-discardFloatingVNets {true|false}? ?-keepEmptyModule {true| false}? ?-minDBUPerMicron <DBUPerMicron>? ?-syncRelativePath {true | false}? ?-timerMode {true|false}?",
        ),
        # man1/setInstancePlacementStatus.1
        _syn(
            "setInstancePlacementStatus",
            "Changes the placement attributes status for all hard macros, all partition blocks, all black‐ boxes, or selected instances",
            "setInstancePlacementStatus ?-help? {-allHardMacros | -allPtnBlks |-allBlackBoxes | -name <instName(s)>} ?-status {unplaced | fixed | placed | cover | softFixed}?",
        ),
        # man1/setInstGroupPhyHier.1
        _syn(
            "setInstGroupPhyHier",
            "Sets a pre-existing instance group into a physical hierarchy where you can generate a corresponding netlist",
            "setInstGroupPhyHier ?-help? <groupName>",
        ),
        # man1/setIntegRouteConstraint.1
        #   WARNING: unclosed bracket '[' at position 32
        #   WARNING: unclosed bracket '[' at position 52
        #   WARNING: unclosed bracket '[' at position 1095
        #   WARNING: unclosed bracket '{' at position 1108
        _syn(
            "setIntegRouteConstraint",
            "Applies specialty routing constraints in the database for nets in the designs",
            "setIntegRouteConstraint ?-help? ??-file <string>? | ??-accessStyle {none | straight | clustered}? ?-bottomLayer <layerNum>? ?-bus_bit_order? ?-busGroupWidth <integer>? ?-connectSupply {<float> anyPoint}? ?-cornerStyle {none | crossover | river}? ?-crossTieShieldInterval <string>? ?-crossTieShieldLayerLimit <string>? ?-crossTieShieldedLayers <string>? ?-groupToOutsideSpacing {<layer1 spacing1> <layer2>?<:layerN>? <spacing2>...}? ?-hard? ?-hierarchicalScope {local local_below local_above local_above_below}? ?-intergroupGap {<layer1> <spacing1> <layer2>?:layerN? <spacing2>...}? ?-layerGap {<layer1> <gap1> <layer2>?:layerN? <gap2>...}? ?-layerMatch? ?-matchGap {<layer1> <gap1> <layer2>?:layerN? <gap2>...}? ?-matchStyle {accordion | trombone | coil}? ?-matchType {length resistance maxResistance}? ?-maxLength <value>? ?-maxRes <value>? ?-minBusBit <integer>? ?-minLength <value>? ?-minRes <value>? ?-name <string>? ?-noshareshield? ?-rule <NDR_name>? ?-shieldGap {<layer1> <gap1> <layer2>?:layerN? <gap2> ...}? ?-shieldNet {<net1 net2>}? ?-shieldTolerance {<net1 value1 net2 value2> ...}? ?-shieldType {unspecified side bottom bottomSide top topSide topBottom",
        ),
        # man1/setInvFootPrint.1
        _syn(
            "setInvFootPrint",
            "Specifies the inverter cell footprints",
            "setInvFootPrint ?-help? ?-library <libName>? <invCellOrFootprintNames>",
        ),
        # man1/setIoFlowFlag.1
        _syn(
            "setIoFlowFlag",
            "Sets the flag to use I/O row flow for pad placement",
            "setIoFlowFlag ?-help? {0 | 1}",
        ),
        # man1/setIoRowMargin.1
        _syn(
            "setIoRowMargin",
            "Sets the distance from the die boundary edge to the I/O row starting edge location",
            "setIoRowMargin ?-help?",
        ),
        # man1/setIsolatedCutRule.1
        _syn(
            "setIsolatedCutRule",
            "Specifies spacing rules for isolated cut layers",
            "setIsolatedCutRule ?-help? -spacing <spacing1> ?-cornerSpacing <spacing2>? ?-layer {<cutLayer_list>}?",
        ),
        # man1/setLatencyFile.1
        _syn(
            "setLatencyFile",
            "Specifies the latency file that the timing engine must load when the timing analysis mode is set to -use‐ fulSkew",
            "setLatencyFile ?-help? <latencyFileName>",
        ),
        # man1/setLayerPreference.1
        _syn(
            "setLayerPreference",
            "Sets a new preference for the specified object or layer",
            'setLayerPreference ?-help? <layer_name> ?-isVisible {1 | 0}? ?-isSelectable {1 | 0}? ?-color {<color_name> | <color_value>}? ?-lineWidth {<lw>}? ?-stipple <stipple_name> | -stippleData <width><height><"stipple_data">?',
        ),
        # man1/setLibraryUnit.1
        _syn(
            "setLibraryUnit",
            "Sets the time and capacitance unit values for constraints and report generation",
            "setLibraryUnit ?-help? ?-cap <capUnit>? ?-time <timeUnit>?",
        ),
        # man1/setLicenseCheck.1
        _syn(
            "setLicenseCheck",
            "Manages licenses for product options",
            'setLicenseCheck ?-help? ?-checkout <lic>? ?-default? ?-existOnServer? ?-optionList "<lic1 lic2> ..."? ?-status? ?-wait <time_in_minutes>?',
        ),
        # man1/setLimitedAccessFeature.1
        _syn(
            "setLimitedAccessFeature",
            "Enables or disables a limited access feature",
            "setLimitedAccessFeature ?-help? <variableName> <1> | <0>",
        ),
        # man1/setMaxCapPerFreq.1
        _syn(
            "setMaxCapPerFreq",
            "Adds a maximum capacitance per frequency table to the existing max_capacitance statement in the timing library",
            "setMaxCapPerFreq ?-help? ?-lib libName? ?-force? -freq {<freq1 ><freq2 >…} -cap {<cap1 ><cap2 >…} -pins {cell pin}",
        ),
        # man1/setMaxCapPerFreqTran.1
        _syn(
            "setMaxCapPerFreqTran",
            "Sets the maximum capacitance of a pin in the design",
            "setMaxCapPerFreqTran ?-help? -freq {<freq1><freq2 freq3>…} -tran {<tran1><tran2 tran3>…} -cap {{<cap11 ><cap12 cap13>…} {{<cap21 ><cap22 cap23>…}} {{<cap31 ><cap32 cap33>…}}} -pins {cell <outputpin>} ?-lib <libName>? ?-force? ?-inputpin <inputpin>?",
        ),
        # man1/setMaxTranPerFreq.1
        _syn(
            "setMaxTranPerFreq",
            "Adds a maximum transition per frequency table to the existing max_transition statement in the timing library",
            "setMaxTranPerFreq ?-help? ?-lib libName? ?-force? -freq {<freq1 ><freq2 freq3>…} -tran {<tran1 ><tran2 tran3>…} -pins {cell pin}",
        ),
        # man1/setMessageLimit.1
        _syn(
            "setMessageLimit",
            "Limits error and warning messages to a specified number per unique ID",
            "setMessageLimit ?-help? <numberToLimit> ?<prefix> ?<ID1>, <ID2>, ...??",
        ),
        # man1/setModuleView.1
        _syn(
            "setModuleView",
            "Specifies the FlexView (readOnly|interface|all) for the top level and each of the partitions",
            "setModuleView ?-help? ?-topReadOnly {true | false}? ?-hinst {<list_of_partition_hinsts>}? ?-partition {<list_of_paritions>}? ?-type {readOnly|interface|all}? Specifies the FlexView (readOnly|interface|all) for the top level and each of the partitions. This way optimization can be limited to the selected sections of the partitions and the top-level logic.",
        ),
        # man1/setMsvMode.1
        _syn(
            "setMsvMode",
            "Sets the special handling for inter-domain nets and to use effective power domains for ISO/LS insertion",
            "setMsvMode ?-help? ?-allowNestedDefaultDomain {true | false}? ?-allowPowerDomainMinGapZero {true | false}? ?-checkAllNetsForDomainCrossing {true | false}? ?-handleBackToBackIsolation {true | false}? ?-handlePD {true|false}? ?-handlePDComplex {true|false}? ?-honorCpfGlobalConnectionSpecForAoBuffer {true | false}? ?-honorCpfGlobalConnectionSpecForShifter {true | false}? ?-honorDotLibRelatedPGPin {true | false}? ?-honorEffectiveDomainForIsoLsInsertion {true | false}? ?-markIsoEnablePinAsAlwaysOn {true | false}? ?-notUseTopFTermDomainForVoltage {true|false}? ?-reset? ?-shareWellAOBufferingSupport {true|false}? ?-upf_allow_shifter_voltage_mismatch {true|false}? ?-upf_insert_on_floating_pins {true|false}?",
        ),
        # man1/setMultiColorsHier.1
        _syn(
            "setMultiColorsHier",
            "Specifies the color assignment for hierarchical instances based on the color Id from the Module Color Preference form (accessed by clicking Floorplan - Edit Floorplan - Color Module)",
            "setMultiColorsHier ?-help? ?<colorID> ?<hInstName>??",
        ),
        # man1/setMultiCpuUsage.1
        _syn(
            "setMultiCpuUsage",
            "Specifies the number of threads to use for multi-threading, or the maximum number of computers to use for distributed processing, or the maximum number of computers and the number of threads to use for Superthreading",
            "setMultiCpuUsage ?-help? ?-acquireLicense <integer>? ?-autoPageFaultMonitor {0 1 2 3}? ?-cpuPerRemoteHost <integer>? ?-keepLicense {true false}? ?-licenseList <string>? ?-localCpu <string>? ?-releaseLicense? ?-remoteHost <integer>? ?-reset? ?-threadInfo {0 1 2}? ?-verbose?",
        ),
        # man1/setNanoRouteMode.1
        #   WARNING: unclosed bracket '[' at position 4788
        _syn(
            "setNanoRouteMode",
            "Controls certain aspects of how the NanoRoute router routes the design",
            'setNanoRouteMode ?-help? ?-extract_keep_fill_wires {true|false}? ?-reset? ?-route_adjust_auto_via_weight {true|false}? ?-route_allow_inst_overlaps {true|false}? ?-route_ignore_follow_pin_shapes {true|false}? ?-route_process_node <value>? ?-route_rc_extraction_corner <value>? ?-route_skip_analog {true|false}? ?-route_via_weight{<via_name> <via_weight ...>}? ?-route_detail_add_passive_fill_only_on_layers <layers>? ?-route_detail_allow_passive_fill_only_in_layers <layers>? ?-route_detail_antenna_eco_list_file <file_name>? ?-route_detail_auto_stop {true|false}? ?-route_detail_check_mar_on_cell_pin {true|false}? ?-route_detail_end_iteration <pass_number>? ?-route_detail_fix_antenna {true|false}? ?-route_detail_fix_antenna_on_secondary_pg_nets {true|false}? ?-route_detail_fix_antenna_with_gate_array_filler_mode {true|false}? ?-route_detail_merge_abutting_cut {true|false}? ?-route_detail_min_length_for_spread_wire {<layer_1 length_1 ... layer_n length_n>}? ?-route_detail_min_length_for_widen_wire <value>? ?-route_detail_min_slack_for_opt_wire <value>? ?-route_detail_no_taper_in_layers "<bottom_layer_number>:<top_layer_number>"? ?-route_detail_no_taper_on_output_pin {true|false|auto}? ?-route_detail_on_grid_only none | false | true | all | {?wire ?ml:mh?? | ?via ?ml:mh??}? ?-route_detail_post_route_litho_repair {true|false}? ?-route_detail_post_route_spread_wire {auto| true | false | 0 | 0.25 | 0.5 | 1 }? ?-route_detail_post_route_swap_via {true | multiCut | false | none}? ?-route_detail_postroute_via_priority {auto | allNets | criticalNetsfirst | nonCriticalNetOnly}? ?-route_detail_post_route_via_pillar_effort {none | low | medium | high}? ?-route_detail_post_route_wire_widen {widen | shrink | none}? ?-route_detail_post_route_wire_widen_rule <rule_name>? ?-route_detail_search_and_repair {true|false}? ?-route_detail_signoff_effort {high | medium | low | auto | n}? ?-route_detail_stub_routing_in_first_layer {true|false}? ?-route_detail_use_multi_cut_via_effort {low | medium | high}? ?-route_number_fail_limit <integer>? ?-route_number_thread <number_processors>? ?-route_number_warning_limit <integer>? ?-route_third_party_data {true|false}? ?-route_high_freq_constraint_groups {order net match bus pair shield}? ?-route_high_freq_match_report_file <file_name>? ?-route_high_freq_num_reserved_layers <value>? ?-route_high_freq_remove_floating_shield {true|false}? ?-route_high_freq_search_repair {auto | false | true | only}? ?-route_high_freq_shield_trim_length <value>? ?-route_interposer_allow_diagonal_trunk {auto | true | false}? ?-route_interposer_control_options <value>? ?-route_interposer_interlayer_shielding_layers <value>? ?-route_interposer_interlayer_shielding_nets <value>? ?-route_interposer_interlayer_shielding_offsets <value>? ?-route_interposer_interlayer_shielding_widths <value>? ?-route_interposer_same_layer_shielding_net <net_name>? ?-route_interposer_same_layer_shielding_width_spacing {<width> <spacing>}? ?-route_interposer_trunk_routing_layers <value>? ?-route_interposer_trunk_routing_width_spacing {<width> <spacing>}? ?-route_add_antenna_inst_prefix <value>? ?-route_allow_pin_as_feedthru {true|TRUE|false|FALSE|none|NONE|output|input|inout, <bottomLayerNum>:<topLayerNum>}? ?-route_antenna_cell_name {"<cell_name>" | "<list_of_cell_names>"}? ?-route_concurrent_minimize_via_count_effort <value>? ?-route_connect_to_bumps {true | false}? ?-route_fix_clock_nets {true|false}? ?-route_route_clock_nets_first {true|false}? ?-route_disable_route_rule_on_via_pillar_to_special_net_wire <value>? ?-route_eco_ignore_existing_route <value>? ?-route_enable_route_rule_si_limit_length <value>? ?-route_enforce_route_rule_on_special_net_wire {false | true | <special_net_name_list>}? ?-route_extra_via_enclosure <distance>? ?-route_honor_exclusive_region {true|false}? ?-route_honor_power_domain {true|false}? ?-route_ignore_antenna_top_cell_pin {true|false}? ?-route_antenna_diode_insertion {true|false}? ?-route_diode_insertion_for_clock_nets {true|false}? ?-route_shield_tap_cell_insertion {true|false}? ?-route_relaxed_route_rule_spacing_to_power_ground_nets {<layer>:<spacing layer>:<spacing>}? ?-route_reserve_space_for_multi_cut {true|false}? ?-route_reverse_direction {(<lx ly ux u>y <bottom_layer>:<top_layer>)}? ?-route_selected_net_only {true|false}? ?-route_shield_crosstie_offset {<layerName>:<numTrack1> <layerName2>:<numTrack2>...}? ?-route_shield_length_threshold <value>? ?-route_shield_report_skip_status {true|false}? ?-route_shield_stripe_layer_range <value>? ?-route_shield_tap_cell_name <string>? ?-route_strictly_honor_1d_routing <value>? ?-route_strict_honor_route_rule {true | false | <bottomLayerNum>:<topLayerNum>| wire <bottomLayerNum>:<topLayerNum>}? ?-route_stripe_layer_range "<bottomLayerNum>:<topLayerNum>"? ?-route_tieoff_to_shapes "auto |"-route_tieoff_to_shapes ""auto | stripe | ring | followpin | powergroundpin""" ?-route_trim_pull_back_distance_from_boundary {<layer>:<value ...>}? ?-route_trunk_with_cluster_target_size <integer>? ?-route_use_auto_via <value>? ?-route_with_eco {true|false}? ?-route_with_litho_driven {true|false}? ?-route_with_si_driven {true|false}? ?-route_with_timing_driven {true|false}? ?-route_with_trim_metal <value>? ?-route_with_via_in_pin {true| false | <bottomLayerNum>:<topLayerNum>}? ?-route_with_via_only_for_block_cell_pin <value>? ?-route_with_via_only_for_stdcell_pin {true| false | <bottomLayerNum>:<topLayerNum>}?',
        ),
        # man1/setNet.1
        _syn(
            "setNet",
            "Marks the specified nets and their related pins as either special nets and pins, or regular nets and pins",
            "setNet ?-help? {-net <netName> | -file <fileName>} ?-setTermSpecial? -type {regular | special}",
        ),
        # man1/setOaxMode.1
        #   WARNING: unclosed bracket '[' at position 1069
        _syn(
            "setOaxMode",
            "Controls aspects of how the Innovus™ Implementation System software reads OpenAccess technology, and creates OpenAccess libraries",
            "setOaxMode ?-help? ?-reset? ?-allowAnalysisOnly {true|false}? ?-allowBitConnection {true | false}? ?-allowTechUpdate {true | false}? ?-bindkeyFile <fileName>? ?-compressLevel <value>? ?-convertTo {polygon|defaultStyle}? ?-cutRows {true | false}? ?-displayDrfFile <pathName>? ?-displayDrfInLibrary {true|false}? ?-drcFillPurpose {gap_fill|drawing}? ?-encloseQuickAbstractPins {true | false}? ?-fullLayerList {true | false}? ?-fullPath {true | false}? ?-hybridRows {true|false}? ?-instPlacedIfUnknown {true | false}? ?-libCreateMode {none | attach | copy | reference}? ?-locking {true | false | errorIfLocked}? ?-logicOnlyImport {true | false}? ?-merge_trim {true | false}? ?-nonRectilinearShapes {bbox|approximate}? ?-pinPurpose {true | false}? ?-pushPinConstraint {true | false}? ?-quickAbstractForCustomCells {pcells |stdcells |all | off}? ?-readSystemReservedLayers {all | text | off}? ?-saveCdsFixedVias {new_vias_only | off}? ?-saveMaskDataLocked {true | false}? ?-saveNetVoltage {true | false}? ?-saveRelativePath {true | false}? ?-saveRestoreFile {true | false}? ?-silently_ignore_unsupported_vias {true | false} ?-textPurpose <purpose_name>? ?-tieNet {<tieHighNetName><tieLowNetName>}? ?-updateMode {true | false | auto}? ?-useVirtuosoBindkey {true | false}? ?-useVirtuosoColor {true | false}? ?-viewSubType {VCE | VXL | none}?",
        ),
        # man1/setObjFPlanBox.1
        _syn(
            "setObjFPlanBox",
            "Defines the bounding box of a specified object, even outside the core boundary",
            "setObjFPlanBox ?-help?",
        ),
        # man1/setObjFPlanBoxList.1
        _syn(
            "setObjFPlanBoxList",
            "Defines the rectilinear shape of an object even if the object lies outside the core area",
            "setObjFPlanBoxList ?-help? {Cell | Group | Instance | Layershape | Module}",
        ),
        # man1/setObjFPlanPolygon.1
        _syn(
            "setObjFPlanPolygon",
            "Specifies a rectilinear object with polygon coordinates",
            "setObjFPlanPolygon ?-help? {Cell | Group | Instance | Layershape | Module }",
        ),
        # man1/setOptMode.1
        _syn(
            "setOptMode",
            "Sets global parameters for timing optimization",
            'setOptMode ?-help? ?-opt_activity_refresh_args "<list_of_arguments">? ?-opt_add_always_on_feed_through_buffers {true | false}? ?-opt_add_insts {true | false}? ?-opt_add_ports {true | false}? ?-opt_add_repeater_report_failure_reason {true | false}? ?-opt_all_end_points {true | false}? ?-opt_allow_only_cell_swapping {true | false}? ?-opt_allow_multi_bit_on_flop_with_sdc {true | false | mergeOnly | splitOnly}? ?-opt_area_recovery {true |false | default}? ?-opt_area_recovery_setup_target_slack <slack>? ?-opt_clone_insts_list { {…} … }? ?-opt_consider_routing_congestion {auto | false | true}? ?-opt_constant_inputs {true | false}? ?-opt_constant_nets {true | false}? ?-opt_concatenate_default_and_user_prefixes {true | false}? ?-opt_delete_insts {true | false}? ?-opt_detail_drv_failure_reason {true | false}? ?-opt_detail_drv_failure_reason_max_num_nets <value>? ?-opt_down_size_insts {true | false}? ?-opt_drv {true | false}? ?-opt_drv_margin <margin>? ?-opt_drv_with_miller_cap {true | false}? ?-opt_duplicate_cte_constrained_hport {true | false}? ?-opt_early_hold_fixing {ideal | propagated}? ?-opt_enable_clock_pulse_width_checks {true | false}? ?-opt_enable_data_to_data_checks {true | false}? ?-opt_enable_podv2_clock_opt_flow {true | false}? ?-opt_enable_restructure {true | false}? ?-opt_enable_targeted_synthesis {true | false}? ?-opt_fix_fanout_load {true | false}? ?-opt_flop_pins_report {false | true}? ?-opt_flops_report {false | true}? ?-opt_high_effort_cells <list_of_cells>? ?-opt_hold_allow_overlap {auto | true | false}? ?-opt_hold_allow_resize {true | false}? ?-opt_hold_allow_setup_tns_degradation {true | false}? ?-opt_hold_cells <list_of_buffers>? ?-opt_hold_on_excluded_clock_nets {true | false}? ?-opt_hold_slack_threshold <slack>? ?-opt_hold_target_slack <holdTargetslack>? ?-opt_honor_density_screen {true | false}? ?-opt_honor_fences {true | false}? ?-opt_hold_ignore_path_groups {<groupA groupB> ...}? ?-opt_icg_enable_pin_rebuffering {true | auto | false}? ?-opt_leakage_to_dynamic_ratio <ratio>? ?-opt_max_density <density>? ?-opt_max_length <length>? ?-opt_move_insts {true | false}? ?-opt_multi_bit_combinational_mode {auto | power | area}? ?-opt_multi_bit_combinational_opt {false | true | mergeOnly | splitOnly}? ?-opt_multi_bit_combinational_merge_timing_effort {none | low | medium | high}? ?-opt_multi_bit_combinational_split_timing_effort {none | low | medium | high}? ?-opt_multi_bit_flop_merge_bank_label_inference {true | false}? ?-opt_multi_bit_flop_merge_timing_effort {low | medium | high}? ?-opt_multi_bit_flop_name_prefix <prefix_name>? ?-opt_multi_bit_flop_name_separator <separator_name>? ?-opt_multi_bit_flop_name_suffix _<user_suffix>? ?-opt_multi_bit_flop_opt {true | false | mergeOnly | splitOnly}? ?-opt_multi_bit_flop_reorder_bits {false | true | timing | power}? ?-opt_multi_bit_flop_split_report_failure_reason {true|false}? ?-opt_multi_bit_flop_split_timing_effort {low | medium | high}? ?-opt_multi_bit_unused_bit_count <integer>? ?-opt_multi_bit_unused_bits {false | true | prePlace | preCTS}? ?-opt_new_inst_prefix <prefix>? ?-opt_new_net_prefix <prefix>? ?-opt_one_pass_lec {true | false}? ?-opt_podv2_flow_effort {auto | standard | extreme}? ?-opt_pin_swapping {true | false}? ?-opt_post_route_allow_overlap {true | false}? ?-opt_post_route_area_reclaim {none | setupAware | holdAndSetupAware}? ?-opt_post_route_art_flow {true | false}? ?-opt_post_route_check_antenna_rules {true | false}? ?-opt_post_route_drv_recovery {false | auto | true}? ?-opt_post_route_fix_clock_drv {true | false}? ?-opt_post_route_fix_glitch {true | false}? ?-opt_post_route_fix_si_transitions {true | false}? ?-opt_post_route_hold_recovery {false | auto | true}? ?-opt_post_route_setup_recovery {false | auto | true}? ?-opt_power_effort {none | low | high}? ?-opt_pre_route_ndr_aware <list>? ?-opt_preserve_all_sequential {true | false}? ?-opt_preserve_hpin_function {true | false}? ?-opt_remove_redundant_insts {true | false}? ?-opt_report_multi_bit_unmerged_reasons {true | false}? ?-opt_resize_flip_flops {true | false}? ?-opt_resize_level_shifter_and_iso_insts {true | false}? ?-opt_resize_power_switch_insts {true | false}? ?-opt_route_opt_recovery {true | false | auto}? ?-opt_sequential_genus_restructure_report_failure_reason {true | false}? ?-opt_setup_target_slack <setupTargetSlack>? ?-opt_skew {true | false}? ?-opt_skew_ccopt {none | standard | extreme}? ?-opt_skew_post_route {true|false}? ?-opt_skew_pre_cts {true|false}? ?-opt_target_based_opt_file <filename>? ?-opt_target_based_opt_file_only {true | false}? ?-opt_target_based_opt_hold_file <hold_file_name>? ?-opt_tied_inputs {true | false}? ?-opt_time_design_compress_reports {true | false}? ?-opt_time_design_expanded_view {true | false}? ?-opt_time_design_num_paths <number>? ?-opt_time_design_report_net {true | false}? ?-opt_time_design_vertical_timing_summary {true|false}? ?-opt_unfix_clock_insts {true | false}? ?-opt_verbose {true | false}? ?-reset?',
        ),
        # man1/setOutboundReport.1
        _syn(
            "setOutboundReport",
            "Controls what extrapolation information is to be saved in the log file(s)",
            "setOutboundReport ?-help? -delay {early | late | both} ?-filename_prefix <string>? ?-report_constant_nets {true | false}? ?-type {lower | upper | both}?",
        ),
        # man1/setPathGroupOptions.1
        _syn(
            "setPathGroupOptions",
            "Specifies options to guide timing optimization and timing analysis when path groups are used",
            "setPathGroupOptions ?-help? <pathgroupName>?-early? ?-effortLevel {low | high}? ?-late? ?-skewingSlackConstraint <value_in_ns>? ?-slackAdjustment <float>? ?-slackAdjustmentPriority <integer>? ?-targetSlack <float>? ?-view <view_names>? ?-weight <integer>?",
        ),
        # man1/setPGPinUseSignalRoute.1
        _syn(
            "setPGPinUseSignalRoute",
            "Sets the internal bit for a given cell/pin pair to be routed by the signal router",
            "setPGPinUseSignalRoute ?-off? ?-all?",
        ),
        # man1/setPinAssignMode.1
        _syn(
            "setPinAssignMode",
            "Sets the global parameters of the partition or block pin assignment feature",
            "setPinAssignMode ?-help? ?-reset? ?-advanced_node_rule_support {true | false}? ?-allow_unconnected_in_abutted_edge {true | false}? ?-allowNonNdrNetPinsOnNdrTracks {true | false}? ?-block_boundary_macro_distance<distance>? ?-force_abutment_with_fixed {true | false}? ?-insidePinSearchDistance {<nrTracks>}? ?-max_distance_pairing <distance>? ?-maxChannelWidthAsAbutted <channelWidthInMicrons>? ?-pinEditInBatch {true | false}? ?-pinOffStripe {below | all | none}? ?-pinToStripeDistance {<listOfLayerDistanceValuePair>}? ?-pinToViaDistanceNonPrefDirection {<listOfLayerDistanceValuePair>}? ?-pinToViaDistancePrefDirection {<listOfLayerDistanceValuePair>}? ?-promotedMacroMaxLayer <layerName>? ?-promotedMacroMinLayer <layerName>? ?-restrict_boundary_macro_distance <distance>? ?-strict_abutment {true | false}? ?-useCommonColorEngineForIO {true|false}?",
        ),
        # man1/setPinConstraint.1
        _syn(
            "setPinConstraint",
            "Sets the constraints for partition pins or an I/O pins",
            "setPinConstraint ?-help? {?-global | -cell <cell_name> | -matchEarlyGlobalRoute? ?-global | -pin <pin_name_list>| -area {<x1 y1 x2 y2>} | -side <side> <_name> | -matchEarlyGlobalRoute? ?-global | -layer {<layer_id_or_name_list>} | -loc {<x> <y> z}? ?-global | -loc {<x> <y> z} | -edge <edge_numbers> | -corner <corner_number>? ??-pin <pin_name_list> ?-loc {<x > <y> z}? ?-edge <edge_numbers>?? | ??-loc {<x> <y> z}? ?-edge <edge_numbers>?? | ?-corner_to_pin_distance <pin_distance> ?-corner <corner_number>??? ?{-pin <pin_name_list> | -pinTemplate {<layer_id_or_name_list>}} ?-use_min_width_as_depth | -depth <depth>? ?-width <width>?? ??-layer {<layer_id_or_name_list>} ?-side <side_names>?? | ?-pinTemplate {<layer_id_or_name_list>} ?-use_min_width_as_depth??? ?-spacing <spacing> ?-area {<x1 y1 x2 y2>}? ?-side <side_names>??} ?-depth <depth> ?-special_wire??",
        ),
        # man1/setPinDensityMapMode.1
        _syn(
            "setPinDensityMapMode",
            "Sets global parameters for the reportPinDensityMap command",
            "setPinDensityMapMode ?-help? ?-reset? ?-displayStep <step_value>? ?-gridInMicron <micron>? ?-gridInRow <numberRow>? ?-threshold <density>?",
        ),
        # man1/setPlaceMode.1
        _syn(
            "setPlaceMode",
            "Controls certain aspects of how the software places cells",
            "setPlaceMode ?-help? ?-reset? ?-place_design_enable_3d {true|false}? ?-place_design_floorplan_mode {true|false}? ?-place_design_integrity_ir_fix_effort {low|medium|high}? ?-place_design_refine_macro {true|false}? ?-place_design_refine_place {true|false}? ?-place_detail_activity_power_driven {true|false}? ?-place_detail_allow_border_pin_abut {true | false}? ?-place_detail_allow_single_height_row_symmetry_x <siteName>? ?-place_detail_check_cut_spacing {true|false}? ?-place_detail_check_inst_space_group {true|false}? ?-place_detail_check_route {true | false}? ?-place_detail_color_aware_legal {true|false}? ?-place_detail_context_aware_legal {none|all|optional|required|user}? ?-place_detail_eco_max_distance <maxDistance>? ?-place_detail_eco_priority_insts {placed|fixed|eco}? ?-place_detail_fixed_shifter {true|false}? ?-place_detail_honor_inst_pad {true|false}? ?-place_detail_io_pin_blockage {true|false}? ?-place_detail_iraware_max_drive_strength <maxDriveStrength>? ?-place_detail_irdrop_aware_effort {none|low|medium|high}? ?-place_detail_irdrop_aware_timing_effort {none|standard|high}? ?-place_detail_irdrop_region_number <valueOfDebugIrdrop>? ?-place_detail_legalization_inst_gap <numberOfSites>? ?-place_detail_max_shifter_column_depth <value>? ?-place_detail_max_shifter_depth <value>? ?-place_detail_max_shifter_row_depth <value>? ?-place_detail_no_filler_without_implant {true|false}? ?-place_detail_pad_fixed_insts {true|false}? ?-place_detail_pad_physical_cells {true|false}? ?-place_detail_preroute_as_obs {<layerNum> ...}? ?-place_detail_PGFTV_insertion_cell_list <listOfCells>? ?-place_detail_preserve_routing {true|false}? ?-place_detail_remove_affected_routing {true|false}? ?-place_detail_swap_eeq_cells {true|false}? ?-place_detail_use_check_drc {true|false}? ?-place_detail_use_diffusion_transition_fill {true|false}? ?-place_detail_use_GA_filler_groups {true|false}? ?-place_detail_use_no_diffusion_one_site_filler {true|false}? ?-place_detail_wire_length_opt_effort {none|medium|high}? ?-place_global_activity_power_driven {false|true}? ?-place_global_activity_power_driven_effort {none|standard|high}? ?-place_global_align_macro {true|false}? ?-place_global_allow_3d_stack {true|false}? ?-place_global_auto_blockage_in_channel {none | soft | partial}? ?-place_global_clock_gate_aware {true|false}? ?-place_global_clock_power_driven {true|false}? ?-place_global_clock_power_driven_effort {low|standard|high}? ?-place_global_cong_effort {low|medium|high|auto}? ?-place_global_cpg_effort {low|medium|high}? ?-place_global_cpg_file <macro_loc_ori_file_name>? ?-place_global_enable_advanced_pipeline {true|false}? ?-place_global_enable_distributed_place {true|false}? ?-place_global_ignore_scan {true|1|false|0|auto}? ?-place_global_ignore_spare {true|false}? ?-place_global_max_density <value>? ?-place_global_module_aware_spare {true|false}? ?-place_global_module_padding <module factor>? ?-place_global_place_io_pins {true|false}? ?-place_global_reorder_scan {true|false}? ?-place_global_soft_guide_strength {low|medium|high}? ?-place_global_timing_effort {medium|high}? ?-place_global_uniform_density {false|true}? ?-place_hard_fence {true|false}? ?-place_hierarchical_flow {true|false}? ?-place_opt_post_place_tcl <tcl_file>? ?-place_opt_run_global_place {none|seed|full}? ?-place_spare_update_timing_graph {true|false}?",
        ),
        # man1/setPreference.1
        _syn(
            "setPreference",
            "Defines preferences, such as, commands issued during a session can be logged to a log or the screen",
            "setPreference ?-help? <preference_name>",
        ),
        # man1/setProbePin.1
        #   WARNING: unmatched closing bracket '}' at position 82
        _syn(
            "setProbePin",
            "Sets a pad or bump as a probe point",
            "setProbePin ?-help? {{-instName <instName> -pinName <pinName>} | -bump <bumpName>}}",
        ),
        # man1/setPromotedMacroPin.1
        _syn(
            "setPromotedMacroPin",
            "Selects or marks signal and/or PG pin shapes to be promoted later on",
            "setPromotedMacroPin ?-help? {-reset | -reportOnlyFile <fileName.tcl> | {?-insts {<instName> | <instNameList>}? ?-pins {<pinName> | <pinNameList>}? ?-layers {<layerId> | <layerIdList>}? ?-override? ?-abuttedToBoundaryOnly?}}",
        ),
        # man1/setPtnPinStatus.1
        _syn(
            "setPtnPinStatus",
            "Sets the pin status for a pin of a partition as fixed, placed, cover, or unplaced",
            "setPtnPinStatus ?-help? ?-selectedPinStatus {fixed | placed | cover}? ?-pin {<pinName >| <pinNameList>}? ?-status {fixed | placed | unplaced | cover}? {?-pin {<pinName >| <pinNameList>} -status{fixed | placed | unplaced | cover} ?-cell <partitionName>?? }",
        ),
        # man1/setPtnPinUSE.1
        _syn(
            "setPtnPinUSE",
            "Allows you to change the USE property of a partition pin",
            "setPtnPinUSE ?-help? <ptnName> <pinName> <pinUse>",
        ),
        # man1/setPtnUserCnsFile.1
        _syn(
            "setPtnUserCnsFile",
            "Specifies the constraints file for a specific partition",
            "setPtnUserCnsFile -fileName <name> -ptnName <partitionName> ?-view?",
        ),
        # man1/setRailPrototypeMode.1
        _syn(
            "setRailPrototypeMode",
            "Sets the mode for Power Aware Congestion Estimation (PACE)",
            "setRailPrototypeMode ?-help? ?-reset? ?-domain {{<PD1 float net1>} {<PD2 float net2>}..}? ?-railModel {virtual | existing}? ?-totalPower <float>?",
        ),
        # man1/setResizeEdge.1
        _syn(
            "setResizeEdge",
            "Sets the edges that will be resized for doing edge-based floorplan resize",
            "setResizeEdge ?-help? {-edges <edge_list>}",
        ),
        # man1/setResizeFPlanMode.1
        _syn(
            "setResizeFPlanMode",
            "Controls certain aspects of how floorplan resizes the design",
            "setResizeFPlanMode ?-help? ?-reset? ?-honorHalo {true | false}? ?-maintainResourceRatioAfterResize {true | false}? ?-shrinkFence {true | false}? ?-snapToTrack {true | false}? ?-shiftBased {true | false} | -proportional {true | false} | -congAware {true | false}? ?-ioProportional {true | false} | -ioMoveWithEdge {true | false} | -ioFix {true | false}?",
        ),
        # man1/setResizeLine.1
        _syn(
            "setResizeLine",
            "Sets the resize lines for shift-based floorplan resize option of the resizeFloorplan command",
            "setResizeLine ?-help?",
        ),
        # man1/setRouteBlkDefaultLayer.1
        _syn(
            "setRouteBlkDefaultLayer",
            "Specifies the default layers for routing blockages, for both metal layers and cut layers",
            "setRouteBlkDefaultLayer ?-help? {{?-layer <layerName> | {<layerNameList>} | all? ?-cutLayer <layerName> | {<layerNameList>} | all? ?-drcRegionLayer <layerName> | {<layerNameList>} | all? ?-trimMetalLayer <layerName> | {<layerNameList>} | all? } | {-allMetalCut }}",
        ),
        # man1/setRouteMode.1
        _syn(
            "setRouteMode",
            "Sets global parameters for the Early Global Route or earlyGlobalRoute",
            'setRouteMode ?-help? ?-reset? ?-earlyGlobalEffortLevel {standard | medium | low }? ?-earlyGlobalHonorMsvRouteConstraint {true|false}? ?-earlyGlobalNumTracksPerClockWire <value>? ?-earlyGlobalReverseDirection "( <x1 y1 x2 y2> ) <Metal2:Metal2> ( <x3 y3 x4 y4> ) <Metal3:Metal3 ...> "? ?-earlyGlobalRouteBumpNets {true|false}? ?-earlyGlobalRoutePartitionAllowFeedthru <list_of_ptn_cell_names>? ?-earlyGlobalRoutePartitionHonorFence <list_of_ptn_cell_names>? ?-earlyGlobalRoutePartitionHonorPin <list_of_ptn_cell_names>? ?-earlyGlobalRoutePartitionPinGuide {true|false}? ?-earlyGlobalRouteSecondPG {true|false}? ?-earlyGlobalRouteSelectedNetsOnly {true|false}? ?-earlyGlobalRouteStripeLayerRange {<layerIdx1>:<layerIdx2>}? ?-earlyGlobalSecondPGMaxFanout< integer>?',
        ),
        # man1/setScanReorderMode.1
        _syn(
            "setScanReorderMode",
            "Controls certain aspects of how the software reorders scan chains",
            "setScanReorderMode ?-help? ?-reset? ?-addScanPortPrefix <prefix>? ?-clkAware {true | false}? ?-compLogic {true | false}? ?-enable_for_partition {true|false}? ?-keepPDPorts {true | false}? ?-keepPort <fileName>? ?-preferH {true | false}? ?-preferV {true | false}? ?-scanEffort {low | medium | high | auto}? ?-skipMode {skipNone | skipBuffer | skipFloatingBuffer}? ?-swapEffort {low|medium|high}?",
        ),
        # man1/setSchedulingFile.1
        _syn(
            "setSchedulingFile",
            "Specifies the name of the scheduling file",
            "setSchedulingFile ?-help? <schedulingFileName>",
        ),
        # man1/setSdpGroupAttribute.1
        _syn(
            "setSdpGroupAttribute",
            "Sets or modifies the specified attributes of an existing SDP group",
            "setSdpGroupAttribute ?-help? ?-flip {X Y XY NONE}? ?-justifyBy {SW SE NW NE MID}? -name <sdp_name> ?-orient {R0 MX MY R180 NONE}? ?-origin {x y}? ?-padding {x y}? ?-skipSpace <spacing_pattern>?",
        ),
        # man1/setSdpMode.1
        _syn(
            "setSdpMode",
            "Sets SDP-related sticky options before using commands like placeSdpGroup and place_design",
            "setSdpMode ?-help? ?-clock_location {bottom|center}? ?-disable_extended_core {true|false}? ?-honor_dont_use {true|false}? ?-honor_orient {true|false}? ?-legalization {NONE|SW|SE|NW|NE|AUTO}? ?-legalization_effort {low|medium|high}? ?-max_move_distance <value>? ?-num_column <numberOfCol>? ?-place_report <file_name>? ?-pre_fixed_cells_blockage_direction {NONE|X|Y}? ?-reset?",
        ),
        # man1/setSdpObjectStatus.1
        _syn(
            "setSdpObjectStatus",
            "Sets the placement status of all or specified SDP group/instances",
            "setSdpObjectStatus ?-help? -status {unplaced|placed|fixed|cover} ?-name object_name_list | -all?",
        ),
        # man1/setSdpTopGroup.1
        _syn(
            "setSdpTopGroup",
            "Specifies the location or the hierarchical path of a data path",
            "setSdpTopGroup ?-help? -group <group_name> ?-force? {-location <llx><lly> | -hierPath <path>}",
        ),
        # man1/setSelectedDensityArea.1
        _syn(
            "setSelectedDensityArea",
            "Specifies the attributes for the selected density screen area(s)",
            "setSelectedDensityArea ?-help? <x1 y1 x2 y2>",
        ),
        # man1/setSelectedObstruct.1
        _syn(
            "setSelectedObstruct",
            "Sets the placement blockage attributes, like the area, name, and type, for the selected placement blockage (only)",
            "setSelectedObstruct ?-help?",
        ),
        # man1/setSelectedPtnCut.1
        _syn(
            "setSelectedPtnCut",
            "Sets the area and the name for the selected partition cut area",
            "setSelectedPtnCut ?-help? <X1><Y1><X2><Y2> <PartitionName>",
        ),
        # man1/setSelectedPtnFeedthrough.1
        _syn(
            "setSelectedPtnFeedthrough",
            "Sets the area, name, and layer ID for the selected partition routing feedthrough object",
            "setSelectedPtnFeedthrough ?-help? <x1><y1><x2><y2> <PtnFeedthroughName> { <layerID> | <layerIDList> }",
        ),
        # man1/setSelectedPtnPinBlk.1
        _syn(
            "setSelectedPtnPinBlk",
            "Sets the area, name, and layer ID for the selected partition pin blockage",
            "setSelectedPtnPinBlk ?-help? <x1><y1><x2><y2> <PtnPinBlkName> {<layerID>}",
        ),
        # man1/setSelectedPtnPinGuide.1
        _syn(
            "setSelectedPtnPinGuide",
            "Sets area, name, and layer Id for the selected pin guide object",
            "setSelectedPtnPinGuide ?-help? <x1><y1><x2><y2> <ptnPinObj> <layerID><space> ?<cellName>?",
        ),
        # man1/setSelectedRouteBlk.1
        _syn(
            "setSelectedRouteBlk",
            "Sets a routing blockage for an attribute of the selected routing blockage",
            "setSelectedRouteBlk ?-help?",
        ),
        # man1/setSelectedStripBoxShape.1
        _syn(
            "setSelectedStripBoxShape",
            "Sets the shape of the selected strip box",
            "setSelectedStripBoxShape ?-help?",
        ),
        # man1/setSelectedStripBoxState.1
        _syn(
            "setSelectedStripBoxState",
            "Sets the state of the selected strip box",
            "setSelectedStripBoxState ?-help? <index> {ROUTED FIXED COVER SHIELD} ?<shield_net>?",
        ),
        # man1/setSelectedWireState.1
        _syn(
            "setSelectedWireState",
            "Sets the state of the selected wire",
            "setSelectedWireState ?-help? <index> <value>",
        ),
        # man1/setSelHInstColor.1
        _syn(
            "setSelHInstColor",
            "Specifies the color Id for the selected hierarchical instances",
            "setSelHInstColor ?-help? ?<colorID>?",
        ),
        # man1/setShrinkFactor.1
        _syn(
            "setShrinkFactor",
            "Sets the value by which the software shrinks the design before extraction",
            "setShrinkFactor ?-help? <shrinkFactor>",
        ),
        # man1/setSignoffOptMode.1
        _syn(
            "setSignoffOptMode",
            "Applies non-default settings for signoffTimeDesign and signoffOptDesign super commands",
            "setSignoffOptMode ?-help? ?-reset? ?-addInst {true | false}? ?-addLoad {true | false}? ?-allowSkewing {true | false}? ?-alongRouteBuffering {true | false}? ?-bufferCellList <cell_list>? ?-checkType {early | late | both}? ?-clockCellList <cell_list>?selectDrv ?-clockMaxLevel <INT>? ?-deleteInst {true | false}? ?-disableGeometryChecks {true | false}? ?-drvMargin <float>? ?-ecoFilePrefix <string>? ?-emType {all | avg | rms | peak}? ?-fixCellEm {true | false}? ?-fixClockDrv {true | false}? ?-fixDataDrv {true | false}? ?-fixGlitch {true | false}? ?-fixHoldAllowSetupDegrade {none | low | medium}? ?-fixHoldAllowSetupOptimization {true | false}? ?-fixHoldAllowSetupTnsDegrade {true | false}? ?-fixHoldVariationAware {true | false}? ?-fixHoldWithMargin <float>? ?-fixIrDrop {true|false}? ?-fixMaxCap {true | false}? ?-fixMaxTran {true | false}? ?-fixOsusGlitch {true | false}? ?-fixSlackInRangeLowerLimit <value_in_ns>? ?-fixSlackInRangeUpperLimit <value_in_ns>? ?-fixSiSlew {true | false}? ?-fixXtalk {true | false}? ?-fixXtalkPreserveHold {true | false}? ?-fixXtalkPreserveSetup {true | false}? ?-holdTargetSlack <float>? ?-holdTargetSlackPerView {viewName1 slack1 viewName2 slack2 …}? ?-holdXtalkDeltaThreshold <value_in_ns>? ?-holdXtalkSlackThreshold <value_in_ns>? ?–ignoreDrvChecks {true | false}? ?-keepTempFiles {true | false}? ?-legalOnly {true | false}? ?-loadCellList <cell_list>? ?-loadEcoOptDb <dir_name>? ?-loadIrdropDb <dir_name>? ?-maxCapMargin <cap_margin_value>? ?-maxLocalDensity <threshold_value>? ?-maxOptRunTime <INT>? ?-maxPaths <INT>? ?-maxRunTime <INT>? ?-maxSlack <float>? ?-maxTranMargin <tran_margin_value>? ?-numReportPaths <INT>? ?-nworst <INT>? ?-optimizeCoreOnly {true | false}? ?-optimizeReplicatedModules {true | false}? ?-optimizeSequentialCells {true | false}? ?-partitionListFile <string>? ?-pbaEcoRoute {true|false}? ?-pbaEffort {medium | high}? ?-postMask {true | false}? ?-postStaTcl <FILE>? ?-powerAware {true | false}? ?-powerOptFocus total | leakage | dynamic | leakageOnly | dynamicOnly? ?-prefixName <string>? ?-preserveFiller {true | false}? ?-preStaTcl <FILE>? ?-resizeInst {true | false}? ?-retime {none |aocv | path_slew_propagation | aocv_path_slew_propagation}? ?-retimeDepth {default | infinite}? ?-retimeDepthEarly {default | infinite}? ?-retimeMode {none | path | exhaustive}? ?-routingCongestionAware {true | false}? ?-routeCongestionThreshold <threshold_value>? ?-saveEcoOptDb <dir_name>? ?-selectHoldEndpoints <file_name>? ?-selectDrvNetFile <file_name>? ?-selectDrvPinFile <file_name>? ?-selectSetupEndpoints <file_name>? ?-setupRecovery {true | false}? ?-setupTargetSlack <float>? ?-setupTargetSlackPerView {viewName1 slack1 viewName2 slack2 …}? ?-setupXtalkDeltaThreshold <value_in_ns>? ?-setupXtalkSlackThreshold <value_in_ns>? ?-skewCoreOnly {true | false}? ?-skipDrvNetfile <file_name>? ?-specifyHoldEndpointsMargin <string>? ?-specifySetupEndpointsMargin <string>? ?-swapInst {true | false}? ?-upsizeInPowerOpt {true | false}? ?-useGaFillerList <list_of_Gate_Array_filler_cells_name>? ?-usePfcDecapList list_of_decap_cells? ?-usePfcFillerList list_of_filler_cells? ?-usePfcRegularList list_of_regular_cells? ?-verbose {true | false}?",
        ),
        # man1/setSIMode.1
        _syn(
            "setSIMode",
            "Sets signal integrity configuration parameters used for crosstalk analysis and repair",
            "setSIMode ?-help? ?-reset? ?-accumulated_small_attacker_factor <double>? ?-accumulated_small_attacker_mode {cap | current | zero_mean}? ?-accumulated_small_attacker_threshold <double>? ?-attacker_alignment {path | path_overlap | timing_aware_edge | input_arrival}? ?-clock_delta_delay_threshold <double>? ?-clocks {asynchronous|synchronous}? ?-constrained_input_threshold_failure_point {input | both}? ?-delta_delay_annotation_mode {lumpedOnNet | arc}? ?-delta_delay_threshold <double>? ?-double_switching {none | clock | data_sequential | all}? ?-enable_bus_attacker_correlation {true | false}? ?-enable_delay_report {true | false}? ?-enable_drv_with_delta_slew {true | false}? ?-enable_dynamic_receiver_peak_limits {true | false}? ?-enable_double_clocking_check {true | false}? ?-enable_glitch_propagation {true | false}? ?-enable_glitch_propagation_spice_deck {true | false}? ?-enable_glitch_report {true | false}? ?-enable_logical_correlation {true | false}? ?-enable_overshoot_undershoot_glitch {true | false}? ?-enable_two_stage_driver_weakening {true | false}? ?-enable_virtual_attacker_constituent_report {true | false}? ?-glitch_accuracy_level <int>? ?-glitch_analysis_type {source | full_propagation}? ?-hold_slack <double>? ?-individual_attacker_clock_threshold <float>? ?-individual_attacker_simulation_filtering {true | false}? ?-individual_attacker_threshold <double>? ?-input_glitch_full_propagation_threshold <double>? ?-input_glitch_full_propagation_vh_threshold <double>? ?-input_glitch_full_propagation_vl_threshold <double>? ?-input_glitch_threshold <double>? ?-input_glitch_vh_threshold <double>? ?-input_glitch_vl_threshold <double>? ?-nonlinear_attacker_slew {true | false}? ?-num_si_iteration <int>? ?-pessimistic_mode {advanced | advanced_node | reduced_pessimism | increased_pessimism | high_pessimism}? ?-receiver_clk_peak_limit <double>? ?-receiver_latch_peak_limit <double>? ?-receiver_peak_limit <double>? ?-report_max_virtual_attacker_constituents <int>? ?-report_si_slew_max_transition {true | false}? ?-secondary_attacker_decoupling_factor <double>? ?-separate_delta_delay_on_data {true | false}? ?-setup_slack <double>? ?-si_reselection {delta_delay | slack}? ?-si_reselection_delay_threshold <double>? ?-skip_noise_model_check <pins>? ?-skip_tw <nets>? ?-switch_prob <double>? ?-unconstrained_net_use_inf_tw {true | false}? ?-use_infinite_TW {true | false}?",
        ),
        # man1/setSnapGrid.1
        _syn(
            "setSnapGrid",
            "Creates a global snapping grid for wiring (including metal fill shapes and via cuts)",
            "setSnapGrid ?-help? -layer {<layer_list>} ?-pitch <x><y>?",
        ),
        # man1/setSpecialRouteType.1
        _syn(
            "setSpecialRouteType",
            "Sets special routing wires to a particular shape type so that they can be written out into a DEF file using the -specialShape parameter of the defOutBySection command",
            "setSpecialRouteType ?-help? -stopTypeList <swire_type_list> ?-stopLayer <Metal_layer>? -setType {BLOCKRING|BLOCKAGEWIRE|BLOCKWIRE|COREWIRE|DRCFILL|FILLWIREOPC|FILLWIRE|FOLLOWPIN|IOWIRE|NO‐ TYPE|PADRING|RING|STRIPE} {-bumpCell<bumpCellList> | -instPin {{<inst1><pin1>} {<inst2><pin2>}...}}",
        ),
        # man1/setSrouteMode.1
        _syn(
            "setSrouteMode",
            "Comprises some of the sroute -extraConfig options",
            "setSrouteMode ?-help? ?-allowWrongWayRoute {true | false}? ?-avoidOverCoreRowLayer <layerName>? ?-blockPinConnectRingPinCorners {true | false}? ?-blockPinRouteWithPinWidth {true | false}? ?-connectBrokenCorePin {true | false}? ?-corePinIgnoreObs {none | placement_blockage | overlap_obs | block_halo}? ?-corePinJoinLimit <value>? ?-corePinLength <value>? ?-corePinMaxViaScale <widthPct heightPct>? ?-corePinSiteRailWidth {{<site1 layer11 Width11 layer12 Width12> …} {<site2 layer21 Width21 layer22 Width22> …} …}? ?-corePinSnapTo {M1_pin | opt_routing_track | grid | half_grid}? ?-corePinStopRoute {RowEnd | CellPinEnd}? ?-corePinReferenceMacro {<macro1 macro2> ...}? ?-corePinReferToFollowPin {true | false}? ?-extendNearestTarget {true | false}? ?-jogThresholdRatio <value>? ?-layerNormalCost layer1 cost1 layer2 cost2 ...? ?-layerWrongWayCost layer1 cost1 layer2 cost2 ...? ?-padPinMinViaSize <viaSizePercent>? ?-padRingLefConvention {true | false}? ?-secondaryPinMaxGap <value>? ?-secondaryPinRailWidth <value>? ?-signalPinAsPG {true | false}? ?-splitLongVia {<threshold_value step_value offset_value height_value>}? ?-targetNumber <value>? ?-targetSearchDistance dist? ?-timeLimit <value>? ?-treatEndcapAsCore {true | false}? ?-treatWelltapAsEndcap <cell_name_list>? ?-viaConnectToShape {padring | ring | stripe | blockring | blockpin | coverpin | noshape | blockwire | corewire | follow‐ pin | iowire}? ?-viaThruToClosestRing {true | false}? ?-corePinLengthAsInstance {true | false}? ?-padPinSplit {<width spacing> | <width1 spacing1 width2 spacing2 width3 spacing3 …>}? ?-srpgAonCellPin {cellName:pinName}? ?-reset?",
        ),
        # man1/setStreamOutMode.1
        _syn(
            "setStreamOutMode",
            "Controls certain aspects of GDSII Stream files generated by the Innovus software",
            "setStreamOutMode ?-help? ?-cellInstanceColor {true|false}? ?-cellMasterColor {true|false}? ?-cellNameUserPrefix {prefix}? ?-cellNameUserSuffix {suffix}? ?-check_map_file {true|false}? ?-ignoreFixedMask {true|false}? ?-labelAllPinShape {true | false}? ?-mergeAppend {true|false}? ?-noPinLabelOnNets {<list_of_net_names>}? ?-oasisCompression {true|false}? ?-oasisLayerName {true|false}? ?-oasisSCellOffset {true|false}? ?-pinTextOrientation {default | automatic}? ?-remove_short_metal_within_cell_boundary {FTV_cell_list}? ?-reset? ?-removeNets {<list_of_nets>}? ?-SEcompatible {true | false}? ?-SEvianames {true | false}? ?-snapToMGrid {true | false}? ?-specifyViaName {default | <format_string>}? ?-streamConvertRectToPath {true|false}? ?-streamVersion <version_number>? ?-supportPathType4 {true | false}? ?-textSize value? ?-uniquifyCellNamesPrefix {true | false}? ?-virtualConnection {true | false}?",
        ),
        # man1/setTieHiLoMode.1
        _syn(
            "setTieHiLoMode",
            "Controls certain aspects of how the software adds or deletes tie-high and tie-low cells",
            "setTieHiLoMode ?-help? ?-reset? ?-cell {{tieHi1 tieLo1} {tieHi2 tieLo2} ...}? ?-createHierPort {true | false}? ?-honorDontTouch {true | false}? ?-honorDontUse {true|false}? ?-maxDistance <distanceValue>? ?-maxFanout <fanOutValue>? ?-modulePrevention {true | false}? ?-prefix <prefixName>? ?-reportHierPort {true | false}?",
        ),
        # man1/setTopCell.1
        _syn(
            "setTopCell",
            "Switches the design to the partition specified by the <cellName>",
            "setTopCell <cellName> Switches the design to the partition specified by the <cellName>.",
        ),
        # man1/setUsefulSkewMode.1
        _syn(
            "setUsefulSkewMode",
            "Sets global parameters for the skewClock command",
            "setUsefulSkewMode ?-help? ?-opt_skew_apply_delay_limits_to_full_flow {true|false}? ?-opt_skew_delay_pre_cts {true|false}? ?-opt_skew_macro_only {true | false}? ?-opt_skew_max_allowed_delay <delay>? ?-opt_skew_min_allowed_delay <delay>? ?-opt_skew_no_boundary {true | false}? ?-reset?",
        ),
        # man1/setViaGenMode.1
        _syn(
            "setViaGenMode",
            "Sets global variables for vias that connect rings and stripes when you use the addRing, addStripe, edit‐ PowerVia, sroute, addSplitPowerVia or editAddRoute commands",
            "setViaGenMode ?-help? ?-reset? ?-accuracy_effort {low | medium | high}? ?-add_pin_to_pin_via {true | false}? ?-align_merged_stack_via_metals {true | false}? ?-allow_via_expansion {true | false}? ?-allow_wire_shape_change {true | false}? ?-area_only {true | false}? ?-bot_enclosure {<overhang1 overhang2>}? ?-create_double_row_cut_via {0 | 1 | 2}? ?-create_max_row_cut_via {true | false}? ?-cut_spacing {<x_spacing y_spacing>}? ?-cutclass_preference {default | {?square? ?bar? ?large?} | cutclass_name_list} | file_name? ?-disable_via_merging {true | false}? ?-extend_out_wire_end {true | false}? ?-full_cut_via_only {true | false}? ?-genvia_naming_prefix <viaNamePrefix>? ?-hookup_contact_max {<distance1_max distance2_max>}? ?-hookup_contact_pg_track {<start_value pitch_value>}? ?-hookup_preplace_fix {0 | 1}? ?-hookup_rail_pair {0 | 1}? ?-hookup_via_distance {<distance_value1> ?<distance_value2> ?<boundary_spacing>??}? ?-hookup_via_fixed_grid {true | false}? ?-hookup_via_min_distance <distance>? ?-hookup_via_style {none | loose | compact | moderate}? ?-hookup_via_viarule {<filler> {<default> |{<list_of_via> <rule>/<cell_names> }} ...}? ?-hookup_virtual_trim_grid {default |{-layer -mask1 {-pitch -core_offset...}}}? ?-ignore_design_boundary {true | false}? ?-ignore_DRC {true | false}? ?-ignore_viarule_enclosure {true | false}? ?-inherit_wire_status {true | false}? ?-invoke_verifyGeometry {true | false}? ?-keep_existing_via {0 | 1 | 2}? ?-keep_fixed_via {true | false}? ?-mincut_preference <value>? ?-optimize_cross_via {true | false}? ?-optimize_via_on_routing_track {true | false}? ?-parameterized_via_only {true | false | auto}? ?-partial_overlap_threshold <float>? ?-preferred_vias_only {use_lef | open | keep}? ?-reference_boundary {design|core}? ?-respect_signal_routes {0 | 1 | 2}? ?-respect_stdcell_geometry {true | false}? ?-respect_wire_ndr {true | false}? ?-set_via_expansion_dir {auto | horizontal | vertical}? ?-snap_via_center_to_grid {{ layer1 {none | grid | half_grid | either } ?hard?} layer2 {{none | grid | half_grid | either } ?hard?} … }? ?-split_long_via_global_grid {x_offset x_pitch x_length_threshold x_length_multiplier y_offset y_pitch y_length_threshold y_length_multiplier}? ?-symmetrical_via_only {true | false | auto}? ?-top_enclosure {<overhang1 overhang2>}? ?-use_track_offset {true | false}? ?-use_trim_metal_enclosure {true | false}? ?-viarule_preference {default | predefined | generated | <list of via rule/cell names> | <file_name>}?",
        ),
        # man1/setWhatIfClockLatency.1
        _syn(
            "setWhatIfClockLatency",
            "Specifies the clock insertion delay from a clock input port to register clock input pins within a blackbox or blackblob",
            "setWhatIfClockLatency <blackBoxCellName> ?-clockFrom <clockPortName>? ?-init <value>? ?-new <value>? ?-genConstr <value>?",
        ),
        # man1/setWhatIfClockPort.1
        _syn(
            "setWhatIfClockPort",
            "Defines a port as a clock port",
            "setWhatIfClockPort <blackBoxCellName> -port <portName>",
        ),
        # man1/setWhatIfDriveType.1
        _syn(
            "setWhatIfDriveType",
            "Sets the output and bidirectional ports that have the specified type of cell within the blackbox or blackblob as drivers on the interface nets",
            "setWhatIfDriveType <blackBoxCellName> ?-port <outputPortName>? ?-lib <libName>? -cell <cellName> ?-slew <value> ?-outputCap <value>?? ?-inputPin <libraryInputPin>? ?-outputPin <libraryOutputPin>?",
        ),
        # man1/setWhatIfLoadType.1
        _syn(
            "setWhatIfLoadType",
            "",
            "setWhatIfLoadType <blackBoxCellName> ?-port <inputPortName>? ?-lib <libName>? -cell <libraryCellName> ?-inputPin <libraryInputPin>? ?-multiply_by <value>?",
        ),
        # man1/setWhatIfPortParameters.1
        _syn(
            "setWhatIfPortParameters",
            "",
            "setWhatIfPortParameters <blackBoxCellName> ?-port <portName>? ?-cap <capacitanceValue>? ?-cell <cell name>? ?-max_cap <maxCapacitanceValue>? ?-max_trans <maxTransitionValue>? ?-max_fanout <maxFanoutValue>? ?-pin <pin name>?",
        ),
        # man1/setWhatIfPortPriority.1
        _syn(
            "setWhatIfPortPriority",
            "Command setWhatIfPortPriority is obsolete and has been replaced by setWhatIfTimingMode",
            "setWhatIfPortPriority ?-driveCell | -portParam?",
        ),
        # man1/setWhatIfTimingMode.1
        _syn(
            "setWhatIfTimingMode",
            "Sets the timing model mode for all blackboxes or blackblobs of the design",
            "setWhatIfTimingMode ?-help? ?-reset? ?-context {in | out}? ?-defaultOutputCap <value>? ?-model {intrinsic | normalized}? ?-portPriority {cellType | portParam}?",
        ),
        # man1/setWindowPreference.1
        _syn(
            "setWindowPreference",
            "Enables or disables windows (panels) from the Innovus main display",
            "setWindowPreference ?-help? <window_name> {on | off}",
        ),
        # man1/shiftOrigin.1
        _syn(
            "shiftOrigin",
            "Shifts the entire design to a new location",
            "shiftOrigin ?-help? {-center | -lowerLeft | -location <x y> | -delta <x y>}",
        ),
        # man1/show_ccopt_cell_name_info.1
        _syn(
            "show_ccopt_cell_name_info",
            "Returns the list of cell name codes",
            "show_ccopt_cell_name_info ?-help?",
        ),
        # man1/showPtnWireX.1
        _syn(
            "showPtnWireX",
            "Displays and writes a file of wires that physically cross over partitions",
            "showPtnWireX ?-help? ?ptnName? ?-outfile <fileName>? ?-excludeNet <exNetFileName>? ?-excludeClock? ?-excludeTri? ?-excludeHighFan <nrFan>? ?-allNets? ?-delta?",
        ),
        # man1/signoff_verify_design.1
        _syn(
            "signoff_verify_design",
            "Enables configurable signoff checking at every design stage",
            "signoff_verify_design ?-help? ?-abort_on_layout_error {yes | no}? ?-abort_on_missing_rulecheck {yes | no}? ?-area {<x1 y1 x2 y2>}? ?-attach_instance_name <attribute_number>? ?-attach_net_name <attribute_number>? ?-attach_net_prop {{<prop_name> <attr_num>} ... }? ?-auto_merge_base_class <string>? ?-beol <string> | -feol <string> | -light? ?-bg? ?-config_file <file_name>? ?-control_file <file_name>? ?-core_license <license_combination>? ?-die_area_as_boundary? ?-dp <n>? ?-dp_timeout <seconds>? ?-drc | -merge_library | -generate_context | -smartconnect | -smart_verify_lvs | -smart_verify_drc | -load_results <path_to_rundir>? ?-erc_checks? ?-error_limit <n>? ?-extra_options <string>? ?-format {stream | oasis}? ?-ignore_blockage? ?-ignore_fill? ?-layer_map_file <streamOut_map_file>? ?-layers <layer_names> | -layer_range {top_layer | bottom_layer}? ?-layout_path <string>? ?-lib_name <library name>? ?-license_dp_continue? ?-license_stacking {larger_license | same_license}? ?-license_timeout <number_of_seconds>? ?-lsf? ?-merge <string>? ?-merge_path <string>? ?-mode {ALL FILLONLY NOFILL NOINSTANCES}? ?-mp <n>? ?-mt <n>? ?-net_map_file <string>? ?-nets <string>? ?-no_query? ?-no_structure_name? ?-offset {<x y>}? ?-output_macros? ?-process_node <foundary_node>? ?-pvs_fill? ?-report_file? ?-rule_file_drc <file_name>? ?-rule_file_smart_verify_lvs <file_name>? ?-run_name <directory_name>? ?-selected_inst? ?-skip_auto_load_results? ?-stripes <number>? ?-structure_name <structure_name>? ?-transform_to_inst_master? ?-ui_data? ?-uniquify_cell_names? ?-units {100 | 200 | 400 | 800 | 1000 | 2000 | 4000 | 8000 | 10000 | 20000}? ?-working_dir <working_directory>?",
        ),
        # man1/signoffOptDesign.1
        _syn(
            "signoffOptDesign",
            "Runs timing, area, DRV, dynamic or leakage optimization on signoff timing",
            "signoffOptDesign ?-help? ?-all? ?-area? ?–drv? ?-dynamic? ?-hold? ?-leakage? ?-noEcoRoute? ?-outDir <dir_name>? ?-reportFullClockPath? ?-power? ?-prefix <prefix_name>? ?-setup?",
        ),
        # man1/signoffTimeDesign.1
        _syn(
            "signoffTimeDesign",
            "Runs signoff timing analysis using extraction (Quantus) and Tempus in batch mode, and generates timing reports and ECO DB for each view",
            "signoffTimeDesign ?-help? ?-noEcoDB? ?-noExpandedViews? ?-outDir <string>? ?-prefix <string>? ?-reportFullClockPath? ?-reportOnly?",
        ),
        # man1/sizeof_collection.1
        _syn(
            "sizeof_collection",
            "Returns the total number of objects contained in the specified collection",
            "sizeof_collection ?-help? <collection>",
        ),
        # man1/skewClock.1
        _syn(
            "skewClock",
            "Modifies the clock arrival time on sequential elements in order to improve the data path timing between two sequential elements",
            "skewClock ?-help? ?-hold? ?-postCTS? ?-postRoute?",
        ),
        # man1/snapFPlan.1
        _syn(
            "snapFPlan",
            "Snaps floorplan objects to the grid",
            "snapFPlan ?-help? {{-all} | {-selected} | {?-guide??-block??-stdCell??-ioPad??-areaIo??-ptnCore??-pinGuide??-routeBlk??-placeBlk??-macroPin??-pin??-pinBlk?}}",
        ),
        # man1/snapFPlanIO.1
        _syn(
            "snapFPlanIO",
            "Snaps I/O cells to a user-defined grid",
            "snapFPlanIO ?-help? ?-selected? ?-userGrid | -toIoRow ?-overlapRowOnly??",
        ),
        # man1/soft_stack_size_limit.1
        _syn(
            "soft_stack_size_limit",
            "",
            "soft_stack_size_limit",
        ),
        # man1/sort_collection.1
        _syn(
            "sort_collection",
            "Returns a sorted collection of objects based on the property",
            "sort_collection ?-help? <collection>?-dictionary? {<property_or_><list_of_properties>} ?-descending?",
        ),
        # man1/source.1
        _syn(
            "source",
            "",
            "source ?-help?",
        ),
        # man1/spaceBondPad.1
        _syn(
            "spaceBondPad",
            "Spaces bond pads and the corresponding area I/O instances based on the constraints returned by the get‐ CellDist()Tcl script",
            "spaceBondPad ?-help? ?-spread?",
        ),
        # man1/spaceIoInst.1
        _syn(
            "spaceIoInst",
            "Spaces the selected I/O cells horizontally or vertically by a specified distance value, and can evenly dis‐ tribute the spacing horizontally or vertically between two or more I/O cells",
            "spaceIoInst ?-help? ?-fixSide {left | right | top | bottom | horDistribute | vertDistribute}? ?-space <value>?",
        ),
        # man1/spaceObject.1
        _syn(
            "spaceObject",
            "Spaces objects (instances, modules, or blockages) horizontally or vertically by a specified distance value, and can evenly distribute the spacing horizontally or vertically between three or more objects",
            "spaceObject ?-help? -fixSide {left | right | center | top | bottom | middle | distHorizontal | distVertical} ?-honorHalo? ?-space <value >?-isSpaceMeanLLtoLL?< >?",
        ),
        # man1/specify_cell_stack_area.1
        _syn(
            "specify_cell_stack_area",
            "Defines the cell area that needs to be involved while calculating stack rule of the correspond‐ ing group",
            "specify_cell_stack_area ?-help? -cell <cell_name> -group <group_name> -rect {x1 y1 x2 y2}",
        ),
        # man1/specify_cell_stack_group.1
        _syn(
            "specify_cell_stack_group",
            "Defines the stack rule of a cell group",
            "specify_cell_stack_group ?-help? -name <group_name> {-max_horizontal_length <max_continuous_length> }",
        ),
        # man1/specify_cell_virtual_align.1
        _syn(
            "specify_cell_virtual_align",
            "Aligns a filler cell that does not have any pin or obs geometries to align, but the cell still needs to be aligned",
            "specify_cell_virtual_align ?-help? ?-cell <cells>? ?-mask <id>? ?-pin_x_loc <microns>?",
        ),
        # man1/specify_lib.1
        _syn(
            "specify_lib",
            "Specify the name of the timing library file(s) for dynamic power analysis",
            "specify_lib ?-help? ?<<in_file> <<file1>?<file2>? ...>>? ?-reset?",
        ),
        # man1/specify_pg_keepout.1
        _syn(
            "specify_pg_keepout",
            "Defines the PG keepout box for a cell or a pin",
            "specify_pg_keepout ?-help? ?-bottom <value>? ?-left <value>? ?-pin <string>? ?-right <value>? ?-top <value>? {-cell <lib_cell_name> | -inst <instance_name>} {-layer <layer_name> | -layerId <layer_id>}",
        ),
        # man1/specifyBlackBox.1
        _syn(
            "specifyBlackBox",
            "Converts a hard macro into a blackbox",
            "specifyBlackBox ?-help? ?-coreSpacing {<left right top bottom>}? ?-minPitchLeft <integer>? ?-minPitchRight <integer>? ?-minPitchTop <integer>? ?-minPitchBottom <integer>? ?-pinLayerLeft {<list_of_layers>}? ?-pinLayerRight {l<ist_of_layers>}? ?-pinLayerTop {<list_of_layers>}? ?-pinLayerBottom {<list_of_layers>}? ?-reservedLayer {<list_of_layers>}? ?-placementHalo {<left right top bottom>}? ?-routingHalo <float>? ?-routingHaloTopLayer <integer>? ?-routingHaloBottomLayer <integer>? ?-noRebuildTiming? ?-cell <string>| -masterInst <string>? {-size {<x y>} | -area <float> | -gateCount <string> | {-gateArea <float >?-cellUtil <float>? ?-includeMacroArea {0 | 1} {-macroArea <float >| -macroList {<macroName> ?<count>?}}?}} ?{-area <float >| -gateCount <string>} ?-minWidth <float> | -minHeight <float> | -fixedWidth <float> | -fixedHeight <float>?? ?-minWidth <float> | -minHeight <float> | -fixedWidth <float> | -fixedHeight <float> |-aspectRatioRange {<min max>}? ?-aspectRatio <float >|-aspectRatioRange {<min max>}?",
        ),
        # man1/specifyCellEdgeSpacing.1
        _syn(
            "specifyCellEdgeSpacing",
            "",
            "specifyCellEdgeSpacing ?-help? {<<edgeType1>> <<edgeType2>> <spacing> ?-exceptExactSpacing <distance>??-exceptAbutted | -forbiddenSpacing??-exceptNonFillerInBetween?} | ?-reset?",
        ),
        # man1/specifyCellEdgeType.1
        _syn(
            "specifyCellEdgeType",
            "Specifies edge type for cell edges as EDGETYPE in macro LEF",
            "specifyCellEdgeType ?-help? {-left <edgeType> | -right <edgeType> | -top <edgeType> | -bottom <edgeType> | -reset } ?{-left <edgeType> | -right <edgeType>} ?-cellRow <rowNumber>?? ?{-left <edgeType> | -right <edgeType>} ?-half {top | bottom}?? ?{-top <edgeType> | -bottom <edgeType>} ?-range {x y}?? ?{-cell <cellName>} ?-reset??",
        ),
        # man1/specifyCellPad.1
        _syn(
            "specifyCellPad",
            "Specifies leaf cells to which padding (placement clearance) is to be added in the left, right, top, or bottom directions and a factor to use to calculate the padding dimension",
            "specifyCellPad <leaf_cellName> {<padding> | ??-right <padding>? ?-left <padding>? ?-top <padding>? ?-bottom <padding>??}",
        ),
        # man1/specifyClockToDataSpacing.1
        _syn(
            "specifyClockToDataSpacing",
            "",
            "specifyClockToDataSpacing ?-help? {{-cell <clockCell> {?-x <leftRightSpacing>? ?-y <topBottomSpacing>?}} | -reset }",
        ),
        # man1/specifyIlm.1
        _syn(
            "specifyIlm",
            "Specifies ILM data directory for the specified block",
            "specifyIlm ?-help? {?-cell <cellName> ?-dir <dirName>?? | -cellview <lib cell view>}",
        ),
        # man1/specifyInstPad.1
        _syn(
            "specifyInstPad",
            "Specifies a value (number of sites) for padding for an instance",
            "specifyInstPad <instName> {<padding> | ??-right <padding>? ?-left <padding>? ?-top <padding>? ?-bottom <padding>??}",
        ),
        # man1/specifyJtag.1
        _syn(
            "specifyJtag",
            "Specifies instances to place with the placeJtag command",
            "specifyJtag {-help} {-cell <leafCellName> | -inst <instName> | -instGroup | -hinst <hInstName> | -group {<hInstName> | <cellName>} | -groupWArea {<hInstName> | <cellNam>e <width> <height>} }",
        ),
        # man1/specifyLockupElement.1
        _syn(
            "specifyLockupElement",
            "Specifies a cell or instance as a lockup element",
            "specifyLockupElement {-cell <leafCellName> | -inst <instName>} -in <ftname> -out <ftname>",
        ),
        # man1/specifyNetWeight.1
        _syn(
            "specifyNetWeight",
            "Specifies the priority weighting of a net",
            "specifyNetWeight ?-help?",
        ),
        # man1/specifyPartition.1
        _syn(
            "specifyPartition",
            "Loads the partition specification file",
            "specifyPartition ?-help? <partitionSpecFileName> ?-noEqualizePtnHInst?",
        ),
        # man1/specifyScanCell.1
        _syn(
            "specifyScanCell",
            "Specifies scan cells that are not listed in the timing library",
            "specifyScanCell ?-help? <?><cellName>? ?-in <ftname>? ?-out <ftname>? ?-scanClock <ftname>? ?-scanEnable <ftname>?",
        ),
        # man1/specifyScanChain.1
        _syn(
            "specifyScanChain",
            "Specifies a scan chain or group in a design",
            "specifyScanChain ?-help? ?<scanChainName>? ?-start {<ftname> | <instPinName>}? ?-stop {<ftname >| <instPinName>}?",
        ),
        # man1/specifyScanChainPartition.1
        _syn(
            "specifyScanChainPartition",
            "Defines a group (a partition) of compatible scan chains for the scan reordering flow",
            "specifyScanChainPartition -partition <partitionName> {-all | <chainName1 chainName2 ...>}",
        ),
        # man1/specifySelectiveBlkgGate.1
        _syn(
            "specifySelectiveBlkgGate",
            "Specifies cells and instances that are allowed to be placed inside the soft blockage during le‐ galization",
            "specifySelectiveBlkgGate ?-help? ?-cell <cellName>? ?-inst <instName>?",
        ),
        # man1/specifySpareGate.1
        _syn(
            "specifySpareGate",
            "Specifies spare gates to place",
            "specifySpareGate {-help} {-cell <leafCellName> |-inst <instanceName> | -hinst {<hierarchicalInstanceName>}}",
        ),
        # man1/spefIn.1
        _syn(
            "spefIn",
            "Loads resistors and capacitors for the interconnects in SPEF into the Innovus database to calculate delays or build a timing graph",
            "spefIn ?-help? <fileNameList> ?-extended? ?-idx? ?-scaleNets <netFileName>? ?-scaleRC? ?-starN | -noStarN? ?{-rc_corner <list_of_rc_corners> ?-spef_field {1 2 3 … N}?}? ?-via_variation_file <viaVariationFileName>?",
        ),
        # man1/spgM3StripePushDown.1
        _syn(
            "spgM3StripePushDown",
            "",
            "spgM3StripePushDown",
        ),
        # man1/spgM3StripeShrink.1
        _syn(
            "spgM3StripeShrink",
            "",
            "spgM3StripeShrink",
        ),
        # man1/sroute.1
        #   WARNING: unclosed bracket '[' at position 1198
        _syn(
            "sroute",
            "Routes power structures",
            "sroute ?-help? ?-allowJogging {0 | 1}? ?-allowLayerChange {0 | 1}? ?-area {x1 y1 x2 y2}? ?-blockPin {<useLef all onBoundary leftBoundary rightBoundary topBoundary bottomBoundary abutPins>}? ?-blockPinLayerRange {<minLayerName maxLayerName>}? ?-blockPinTarget {nearestTarget | boundaryWithPin | farthestPadRing} | {?blockring? ?padring? ?ring? ?stripe? ?ringpin? ?blockpin?}? ?-blockPinWidthRange {<min max>}? ?-connect {?blockPin? ?corePin? ?padPin? ?padRing? ?floatingStripe? ?secondaryPowerPin?}? ?-connectAlignedBlockAndPadPin {blockPinAsTarget | padPinAsTarget}? ?-connectInsideArea? ?-corePinCheckStdcellGeoms? ?-corePinLayer <layerNumList>? ?-corePinTarget {{?blockring? ?ring? ?stripe? ?padring? ?ringpin? ?blockpin?}|{ firstAfterRowEnd | boundaryWithPin | far‐ thestPadRing | none }}? ?-corePinWidth <real>? ?-crossoverViaLayerRange {<bot top>}? ?-deleteExistingRoutes? ?-detailed_log? ?-floatingStripeTarget {?blockring? ?ring? ?stripe? ?padring? ?ringpin? ?blockpin? ?followpin?}? ?-inst {<names_of_blocks>}? ?-layerChangeRange {<bottomLayerName topLayerName>}? ?-nets {<names>}? ?-noBlockPinOneAmongOverlappedPins? ?-padPinLayerRange {<minLayerName maxLayerName>}? ?-padPinWidth <real>? ?-padPinPortConnect {?onePort | allPort??oneGeom |allGeom? | preferLayer} ?-padRingWidth <real>? ?-padRingLayer {<layerNumList>}? ?-powerDomains ?<powerDomainName1 powerDomainName2> …?? ?-secondaryPinNet {<list_of_nets>}? ?-secondaryPinRailVerticalStripeGrid {<topLayerNum width pitch>}? ?-stripeLayerRange {<minLayerName maxLayerName>}? ?-targetObjListFile <filename>? ?-targetViaLayerRange {<bot top>}? ?-uda <subclass_string>? ?-padCellSkipRoutingOnPadSide {<top bottom left right>}? ?-padPinTarget {nearestTarget | {?blockring? ?ring? ?stripe? ?ringpin? ?blockpin? ?followpin?}}? ?-secondaryPinRailLayer?",
        ),
        # man1/staggerBondPad.1
        _syn(
            "staggerBondPad",
            "Generates a staggered wirebond pad pattern on top of an existing I/O ring",
            "staggerBondPad ?-help? {-startIoInstName <instName> ?-endIoInstName <instName>? | -ring <number> | -side {e | w | n | s} ?-ring <number>? | -all} {-pattern <pattern_string> | -startStaggerPosition {i | m | o}} ?-pad <position><padName position padName...>? ?-pinName <pinName>?",
        ),
        # man1/start_parallel_edit.1
        _syn(
            "start_parallel_edit",
            "Initializes parallel editing by drawing a yellow square on the main window to indicate the edit area and saving the physical data, net attributes, via cell names and Non-Default Rules (NDRs) to a multiple binary files",
            "start_parallel_edit ?-help? ?-area_restricted? -region {<x1 y1 x2 y2>}",
        ),
        # man1/streamOut.1
        _syn(
            "streamOut",
            "Creates a GDSII Stream file of the current database",
            "streamOut <gdsFileName> ?-attachInstanceName <attributeNumber>? ?-attachNetName <attributeNumber>? ?-attachNetProp {{<prop_name1> <attr_num1>} {<prop_name2> <attr_num2>........}}? ?-area {<x1 y1 x2 y2>} ?-strict??-enclosed_instances_only?? ?-dieAreaAsBoundary? ?-extraMapFile <mapFile>? ?-format {stream oasis}?-outputInstanceName <instName>? ?-outputNetName <netName>?? ?-help? ?-ignoreSubtype {NETTYPE SHAPE}? ?-libName <libraryName>? ?-mapFile <mapFile>? ?-mergeViaCellMapFile <cell_list>? ?-merge {<listOfExternalGDSOASISFiles>} ?-noTSV <tsv_name_list>??-uniquifyCellNames?? ?-reportFile <file_name>? ?-mode {ALL | FILLONLY | NOFILL | NOINSTANCES}? ?-offset <x><y>? ?-outputCriticalNetColorFromFileOnly <sideFile>? ?-outputMacros? ?-probe_pin_label <probeLabel>? ?-signoff_fill? ?-structureName <structureName> | -noStructureName? ?-units {100 | 200 | 1000 | 2000 | 10000 | 20000}?",
        ),
        # man1/stretchRows.1
        _syn(
            "stretchRows",
            "Stretches selected rows",
            "stretchRows ?-help? {-left | -right | -left -right} ?-toCoreEdge?",
        ),
        # man1/summaryReport.1
        _syn(
            "summaryReport",
            "Reports statistics for the entire design, or a selected object in the design",
            "summaryReport ?-help? ?-outdir <directoryName>? ?-noText | -noHtml? ?-outfile <fileName> | -noText? ?-noHtml | -browser? ?-exclude_base_cell_for_density <cell_name_list> | -exclude_inst_prefix <list_of_prefixes>?",
        ),
        # man1/suppressMessage.1
        _syn(
            "suppressMessage",
            "Suppresses error or warning messages identified by a unique ID",
            "suppressMessage ?-help? <prefix numId> ?<numId2 … numIdn>?",
        ),
        # man1/suspend.1
        _syn(
            "suspend",
            "Suspends your script and returns to the Innovus prompt",
            "suspend ?-help?",
        ),
        # man1/swap_well_taps.1
        _syn(
            "swap_well_taps",
            "Swaps to custom tap cell to avoid OD spacing rule",
            "swap_well_taps ?-help? ?-both_violation <cellName>? -cells <cellName> ?-check_only? ?-default_cell <defaultCellName>? -diffusion_forbidden_spacing <float> ?-left_violation <cellName>? ?-right_violation <cellName>? ?-skip_cells <cellNameList>? ?-swap_report <reportName>? ?-violation_report <reportName>?",
        ),
        # man1/swapPins.1
        _syn(
            "swapPins",
            "Switches the locations of two pins",
            "swapPins ?-help?",
        ),
        # man1/swapRegularCellWithAlwaysOnCell.1
        _syn(
            "swapRegularCellWithAlwaysOnCell",
            "Identifies the regular buffer/inverter and swaps it with always-on buffer/inverter",
            "swapRegularCellWithAlwaysOnCell ?-help? ?-cellMapFile <filename>? ?-defaultAlwaysOnCell <AoCellNames>? ?-nets <LPErrorNetList>? ?-verbose?",
        ),
        # man1/swapSignal.1
        _syn(
            "swapSignal",
            "Swaps signal between selected instances (I/O pads or bumps)",
            "swapSignal ?-help? ??-from {<nameList>} -to {<nameList>}? | -circle_offset <value>?",
        ),
        # man1/synthesize_ccopt_flexible_htrees.1
        _syn(
            "synthesize_ccopt_flexible_htrees",
            "This command is used to synthesize all flexible H-trees that have been created but not previously synthesized, in one go",
            "synthesize_ccopt_flexible_htrees ?-help? ?-block_master_clone? ?-dry_run? ?-report_out_file <filename>? ?-spec_file <filename>? ?-use_estimated_routes | -trial_mode {true | false | placement_only | routing_only}?",
        ),
        # man1/time_info.1
        _syn(
            "time_info",
            "Reports and tracks runtime and memory performance",
            "time_info ?-help? ?<stage_name>? ?-current? ?-report? ?-stamp? ?-table <metric_table_id>?",
        ),
        # man1/timeDesign.1
        _syn(
            "timeDesign",
            "Runs Early Global Route, extraction, and timing analysis, and generates detailed timing reports",
            "timeDesign ?-help? ?-drvReports? ?-expandReg2Reg? ?-expandedViews? ?-hold? ?-idealClock? ?-numPaths <integer>? ?-outDir <string>? ?-pathreports? ?-prefix <string>? ?-proto? ?-reportOnly? ?-slackReports? ?-timingDebugReport? ?-useTransitionFiles? ?-prePlace | -preCTS | -postCTS | -postRoute?",
        ),
        # man1/timing_all_registers_filter_clock_pins_by_clock.1
        _syn(
            "timing_all_registers_filter_clock_pins_by_clock",
            "",
            "timing_all_registers_filter_clock_pins_by_clock {true | false}",
        ),
        # man1/timing_all_registers_identify_macros_include_is_macro_cell.1
        _syn(
            "timing_all_registers_identify_macros_include_is_macro_cell",
            "",
            "timing_all_registers_identify_macros_include_is_macro_cell {true | false}",
        ),
        # man1/timing_all_registers_include_icg_cells.1
        _syn(
            "timing_all_registers_include_icg_cells",
            "",
            "timing_all_registers_include_icg_cells {true | false}",
        ),
        # man1/timing_allow_input_delay_on_clock_source.1
        _syn(
            "timing_allow_input_delay_on_clock_source",
            "",
            "timing_allow_input_delay_on_clock_source {true | false}",
        ),
        # man1/timing_analysis_precision_ps.1
        _syn(
            "timing_analysis_precision_ps",
            "",
            "timing_analysis_precision_ps {0.1 | 0.01}",
        ),
        # man1/timing_aocv_analysis_mode.1
        _syn(
            "timing_aocv_analysis_mode",
            "",
            "timing_aocv_analysis_mode {launch_capture | clock_only | separate_data_clock | combine_launch_capture}",
        ),
        # man1/timing_aocv_derate_mode.1
        _syn(
            "timing_aocv_derate_mode",
            "",
            "timing_aocv_derate_mode {aocv_multiplicative | aocv_additive}",
        ),
        # man1/timing_aocv_slack_threshold.1
        _syn(
            "timing_aocv_slack_threshold",
            "",
            "timing_aocv_slack_threshold integer",
        ),
        # man1/timing_aocv_stage_count_recalculate_on_timing_reset.1
        _syn(
            "timing_aocv_stage_count_recalculate_on_timing_reset",
            "",
            "timing_aocv_stage_count_recalculate_on_timing_reset {true | false}",
        ),
        # man1/timing_apply_check_derate_to_external_output_delay.1
        _syn(
            "timing_apply_check_derate_to_external_output_delay",
            "",
            "timing_apply_check_derate_to_external_output_delay {true | false}",
        ),
        # man1/timing_apply_default_primary_input_assertion.1
        _syn(
            "timing_apply_default_primary_input_assertion",
            "",
            "timing_apply_default_primary_input_assertion {true | false}",
        ),
        # man1/timing_apply_exceptions_to_data_check_related_pin.1
        _syn(
            "timing_apply_exceptions_to_data_check_related_pin",
            "",
            "timing_apply_exceptions_to_data_check_related_pin {true | false}",
        ),
        # man1/timing_apply_setup_hold_exceptions_to_data_check_related_pin.1
        _syn(
            "timing_apply_setup_hold_exceptions_to_data_check_related_pin",
            "",
            "timing_apply_setup_hold_exceptions_to_data_check_related_pin {true | false}",
        ),
        # man1/timing_cap_unit.1
        _syn(
            "timing_cap_unit",
            "",
            "timing_cap_unit <string>",
        ),
        # man1/timing_case_analysis_for_icg_propagation.1
        _syn(
            "timing_case_analysis_for_icg_propagation",
            "",
            "timing_case_analysis_for_icg_propagation {false | require_seq_prop | always}",
        ),
        # man1/timing_case_analysis_for_sequential_propagation.1
        _syn(
            "timing_case_analysis_for_sequential_propagation",
            "",
            "timing_case_analysis_for_sequential_propagation {true | false}",
        ),
        # man1/timing_case_analysis_propagation.1
        _syn(
            "timing_case_analysis_propagation",
            "",
            "timing_case_analysis_propagation {true | false}",
        ),
        # man1/timing_check_timing_report_all_checks.1
        _syn(
            "timing_check_timing_report_all_checks",
            "",
            "timing_check_timing_report_all_checks {true | false}",
        ),
        # man1/timing_check_timing_signal_level_high_to_low_threshold.1
        _syn(
            "timing_check_timing_signal_level_high_to_low_threshold",
            "",
            "timing_check_timing_signal_level_high_to_low_threshold double",
        ),
        # man1/timing_check_timing_signal_level_low_to_high_threshold.1
        _syn(
            "timing_check_timing_signal_level_low_to_high_threshold",
            "",
            "timing_check_timing_signal_level_low_to_high_threshold double",
        ),
        # man1/timing_clock_phase_propagation.1
        _syn(
            "timing_clock_phase_propagation",
            "",
            "timing_clock_phase_propagation {positive | negative | both}",
        ),
        # man1/timing_clock_source_use_driving_cell.1
        _syn(
            "timing_clock_source_use_driving_cell",
            "",
            "timing_clock_source_use_driving_cell {true | false}",
        ),
        # man1/timing_clock_uncertainty_from_to_precedence.1
        _syn(
            "timing_clock_uncertainty_from_to_precedence",
            "",
            "timing_clock_uncertainty_from_to_precedence {true | false}",
        ),
        # man1/timing_collection_all_fanin_fanout_traversal_mode.1
        _syn(
            "timing_collection_all_fanin_fanout_traversal_mode",
            "",
            "timing_collection_all_fanin_fanout_traversal_mode {true | false}",
        ),
        # man1/timing_collection_result_display_limit.1
        _syn(
            "timing_collection_result_display_limit",
            "",
            "timing_collection_result_display_limit <integer>",
        ),
        # man1/timing_collection_variable_assignment_compatibility.1
        _syn(
            "timing_collection_variable_assignment_compatibility",
            "",
            "timing_collection_variable_assignment_compatibility {true | false}",
        ),
        # man1/timing_constraint_disable_min_max_input_delay_worst_casing.1
        _syn(
            "timing_constraint_disable_min_max_input_delay_worst_casing",
            "",
            "timing_constraint_disable_min_max_input_delay_worst_casing {true | false}",
        ),
        # man1/timing_constraint_enable_detailed_report_invalid_begin_end_points.1
        _syn(
            "timing_constraint_enable_detailed_report_invalid_begin_end_points",
            "",
            "timing_constraint_enable_detailed_report_invalid_begin_end_points {true | false}",
        ),
        # man1/timing_constraint_enable_drv_limit_override.1
        _syn(
            "timing_constraint_enable_drv_limit_override",
            "",
            "timing_constraint_enable_drv_limit_override {true | false}",
        ),
        # man1/timing_constraint_enable_logging.1
        _syn(
            "timing_constraint_enable_logging",
            "",
            "timing_constraint_enable_logging {true | false}",
        ),
        # man1/timing_constraint_enable_report_invalid_begin_end_points.1
        _syn(
            "timing_constraint_enable_report_invalid_begin_end_points",
            "",
            "timing_constraint_enable_report_invalid_begin_end_points {true | false}",
        ),
        # man1/timing_constraint_enable_search_path.1
        _syn(
            "timing_constraint_enable_search_path",
            "",
            "timing_constraint_enable_search_path {true | false}",
        ),
        # man1/timing_constraint_enable_separate_multicycle_data_checks.1
        _syn(
            "timing_constraint_enable_separate_multicycle_data_checks",
            "",
            "timing_constraint_enable_separate_multicycle_data_checks {true | false}",
        ),
        # man1/timing_constraint_load_minimal_set_for_automated_eco.1
        _syn(
            "timing_constraint_load_minimal_set_for_automated_eco",
            "",
            "timing_constraint_load_minimal_set_for_automated_eco {true | false}",
        ),
        # man1/timing_constraint_path_delay_exclude_check_delay_from_ignore_clock_latency.1
        _syn(
            "timing_constraint_path_delay_exclude_check_delay_from_ignore_clock_latency",
            "",
            "timing_constraint_path_delay_exclude_check_delay_from_ignore_clock_latency {true | false}",
        ),
        # man1/timing_constraint_path_delay_exclude_io_delay_from_ignore_clock_latency.1
        _syn(
            "timing_constraint_path_delay_exclude_io_delay_from_ignore_clock_latency",
            "",
            "timing_constraint_path_delay_exclude_io_delay_from_ignore_clock_latency {true | false}",
        ),
        # man1/timing_constraint_path_delay_exclude_unconstrained_endpoints.1
        _syn(
            "timing_constraint_path_delay_exclude_unconstrained_endpoints",
            "",
            "timing_constraint_path_delay_exclude_unconstrained_endpoints {true | false}",
        ),
        # man1/timing_constraint_path_delay_include_clock_pin_endpoints.1
        _syn(
            "timing_constraint_path_delay_include_clock_pin_endpoints",
            "",
            "timing_constraint_path_delay_include_clock_pin_endpoints {true | false}",
        ),
        # man1/timing_constraint_update_io_latency_averaging_mode.1
        _syn(
            "timing_constraint_update_io_latency_averaging_mode",
            "",
            "timing_constraint_update_io_latency_averaging_mode {rise_fall | rise_only}",
        ),
        # man1/timing_constraint_warn_for_timing_derate_exceeding_max_limit.1
        _syn(
            "timing_constraint_warn_for_timing_derate_exceeding_max_limit",
            "",
            "timing_constraint_warn_for_timing_derate_exceeding_max_limit <double>",
        ),
        # man1/timing_context_apply_default_primary_input_assertion.1
        _syn(
            "timing_context_apply_default_primary_input_assertion",
            "",
            "timing_context_apply_default_primary_input_assertion {true | false}",
        ),
        # man1/timing_context_apply_port_sdc_exceptions.1
        _syn(
            "timing_context_apply_port_sdc_exceptions",
            "",
            "timing_context_apply_port_sdc_exceptions {true | false}",
        ),
        # man1/timing_context_clock_mapping_check_waveform.1
        _syn(
            "timing_context_clock_mapping_check_waveform",
            "",
            "timing_context_clock_mapping_check_waveform {true | false}",
        ),
        # man1/timing_context_clock_mapping_percentage_tolerance.1
        _syn(
            "timing_context_clock_mapping_percentage_tolerance",
            "",
            "timing_context_clock_mapping_percentage_tolerance {true | false}",
        ),
        # man1/timing_context_clock_phase_based_clock_mapping.1
        _syn(
            "timing_context_clock_phase_based_clock_mapping",
            "",
            "timing_context_clock_phase_based_clock_mapping {true | false}",
        ),
        # man1/timing_context_continue_on_invalid_module_list.1
        _syn(
            "timing_context_continue_on_invalid_module_list",
            "",
            "timing_context_continue_on_invalid_module_list {true | false}",
        ),
        # man1/timing_context_data_phase_based_clock_mapping.1
        _syn(
            "timing_context_data_phase_based_clock_mapping",
            "",
            "timing_context_data_phase_based_clock_mapping {true | false}",
        ),
        # man1/timing_context_port_based_clock_mapping.1
        _syn(
            "timing_context_port_based_clock_mapping",
            "",
            "timing_context_port_based_clock_mapping {true | false}",
        ),
        # man1/timing_continue_on_error.1
        _syn(
            "timing_continue_on_error",
            "",
            "timing_continue_on_error {true | false}",
        ),
        # man1/timing_cppr_enable_mismatch_transition_mode.1
        _syn(
            "timing_cppr_enable_mismatch_transition_mode",
            "",
            "timing_cppr_enable_mismatch_transition_mode {true | false}",
        ),
        # man1/timing_cppr_opposite_edge_mean_scale_factor.1
        _syn(
            "timing_cppr_opposite_edge_mean_scale_factor",
            "",
            "timing_cppr_opposite_edge_mean_scale_factor {0.0 | 1.0}",
        ),
        # man1/timing_cppr_opposite_edge_sigma_scale_factor.1
        _syn(
            "timing_cppr_opposite_edge_sigma_scale_factor",
            "",
            "timing_cppr_opposite_edge_sigma_scale_factor {0.0 | 1.0}",
        ),
        # man1/timing_cppr_opposite_edge_sigma_scale_factor_cell.1
        _syn(
            "timing_cppr_opposite_edge_sigma_scale_factor_cell",
            "",
            "timing_cppr_opposite_edge_sigma_scale_factor_cell <double >",
        ),
        # man1/timing_cppr_opposite_edge_sigma_scale_factor_net.1
        _syn(
            "timing_cppr_opposite_edge_sigma_scale_factor_net",
            "",
            "timing_cppr_opposite_edge_sigma_scale_factor_net <double>",
        ),
        # man1/timing_cppr_propagate_thru_latches.1
        _syn(
            "timing_cppr_propagate_thru_latches",
            "",
            "timing_cppr_propagate_thru_latches {true | false}",
        ),
        # man1/timing_cppr_remove_clock_to_data_crp.1
        _syn(
            "timing_cppr_remove_clock_to_data_crp",
            "",
            "timing_cppr_remove_clock_to_data_crp {true | false}",
        ),
        # man1/timing_cppr_self_loop_mode.1
        _syn(
            "timing_cppr_self_loop_mode",
            "",
            "timing_cppr_self_loop_mode {true | false}",
        ),
        # man1/timing_cppr_skip_clock_reconvergence.1
        _syn(
            "timing_cppr_skip_clock_reconvergence",
            "",
            "timing_cppr_skip_clock_reconvergence {true | false}",
        ),
        # man1/timing_cppr_skip_clock_reconvergence_for_unmatched_clocks.1
        _syn(
            "timing_cppr_skip_clock_reconvergence_for_unmatched_clocks",
            "",
            "timing_cppr_skip_clock_reconvergence_for_unmatched_clocks {true | false}",
        ),
        # man1/timing_cppr_threshold_ps.1
        _syn(
            "timing_cppr_threshold_ps",
            "",
            "timing_cppr_threshold_ps <float>",
        ),
        # man1/timing_cppr_transition_sense.1
        _syn(
            "timing_cppr_transition_sense",
            "",
            "timing_cppr_transition_sense {normal | same_transition | same_transition_expanded}",
        ),
        # man1/timing_create_clock_default_propagated.1
        _syn(
            "timing_create_clock_default_propagated",
            "",
            "timing_create_clock_default_propagated {true | false}",
        ),
        # man1/timing_create_clock_use_ideal_slew.1
        _syn(
            "timing_create_clock_use_ideal_slew",
            "",
            "timing_create_clock_use_ideal_slew {true | false}",
        ),
        # man1/timing_default_opcond_per_lib.1
        _syn(
            "timing_default_opcond_per_lib",
            "",
            "timing_default_opcond_per_lib {true | false}",
        ),
        # man1/timing_defer_mmmc_object_updates.1
        _syn(
            "timing_defer_mmmc_object_updates",
            "",
            "timing_defer_mmmc_object_updates {true | false}",
        ),
        # man1/timing_derate_aocv_dynamic_delays.1
        _syn(
            "timing_derate_aocv_dynamic_delays",
            "",
            "timing_derate_aocv_dynamic_delays {true | false}",
        ),
        # man1/timing_derate_aocv_reference_point.1
        _syn(
            "timing_derate_aocv_reference_point",
            "",
            "timing_derate_aocv_reference_point {1 | 0}",
        ),
        # man1/timing_derate_dynamic_compatibility.1
        _syn(
            "timing_derate_dynamic_compatibility",
            "",
            "timing_derate_dynamic_compatibility {1 | 0}",
        ),
        # man1/timing_derate_incremental_adjust_additive_mode.1
        _syn(
            "timing_derate_incremental_adjust_additive_mode",
            "",
            "timing_derate_incremental_adjust_additive_mode {true | false}",
        ),
        # man1/timing_derate_incremental_multiply_accumulative_mode.1
        _syn(
            "timing_derate_incremental_multiply_accumulative_mode",
            "",
            "timing_derate_incremental_multiply_accumulative_mode {true | false}",
        ),
        # man1/timing_derate_negative_delay_backward_compatibility.1
        _syn(
            "timing_derate_negative_delay_backward_compatibility",
            "",
            "timing_derate_negative_delay_backward_compatibility {true | false}",
        ),
        # man1/timing_derate_ocv_reference_point.1
        _syn(
            "timing_derate_ocv_reference_point",
            "",
            "timing_derate_ocv_reference_point {1 | 0}",
        ),
        # man1/timing_derate_spatial_distance_unit.1
        _syn(
            "timing_derate_spatial_distance_unit",
            "",
            "timing_derate_spatial_distance_unit {default | 1um | 1nm}",
        ),
        # man1/timing_derate_voltage_scaling_mode.1
        _syn(
            "timing_derate_voltage_scaling_mode",
            "",
            "timing_derate_voltage_scaling_mode {first_library | snap_to_nearest | interpolate}",
        ),
        # man1/timing_disable_bidi_output_timing_checks.1
        _syn(
            "timing_disable_bidi_output_timing_checks",
            "",
            "timing_disable_bidi_output_timing_checks {true | false}",
        ),
        # man1/timing_disable_black_box_endpoints.1
        _syn(
            "timing_disable_black_box_endpoints",
            "",
            "timing_disable_black_box_endpoints {true | false}",
        ),
        # man1/timing_disable_bus_contention_check.1
        _syn(
            "timing_disable_bus_contention_check",
            "",
            "timing_disable_bus_contention_check {true | false}",
        ),
        # man1/timing_disable_clock_gating_checks.1
        _syn(
            "timing_disable_clock_gating_checks",
            "",
            "timing_disable_clock_gating_checks {true | false}",
        ),
        # man1/timing_disable_clockperiod_checks.1
        _syn(
            "timing_disable_clockperiod_checks",
            "",
            "timing_disable_clockperiod_checks {true | false}",
        ),
        # man1/timing_disable_constant_propagation_for_sequential_cells.1
        _syn(
            "timing_disable_constant_propagation_for_sequential_cells",
            "",
            "timing_disable_constant_propagation_for_sequential_cells {true | false}",
        ),
        # man1/timing_disable_drv_reports_on_constant_nets.1
        _syn(
            "timing_disable_drv_reports_on_constant_nets",
            "",
            "timing_disable_drv_reports_on_constant_nets {true | false}",
        ),
        # man1/timing_disable_floating_bus_check.1
        _syn(
            "timing_disable_floating_bus_check",
            "",
            "timing_disable_floating_bus_check {true | false}",
        ),
        # man1/timing_disable_genclk_combinational_blocking.1
        _syn(
            "timing_disable_genclk_combinational_blocking",
            "",
            "timing_disable_genclk_combinational_blocking {true | false}",
        ),
        # man1/timing_disable_inferred_clock_gating_checks.1
        _syn(
            "timing_disable_inferred_clock_gating_checks",
            "",
            "timing_disable_inferred_clock_gating_checks {true | false}",
        ),
        # man1/timing_disable_internal_inout_cell_paths.1
        _syn(
            "timing_disable_internal_inout_cell_paths",
            "",
            "timing_disable_internal_inout_cell_paths {true | false}",
        ),
        # man1/timing_disable_internal_inout_net_arcs.1
        _syn(
            "timing_disable_internal_inout_net_arcs",
            "",
            "timing_disable_internal_inout_net_arcs {true | false}",
        ),
        # man1/timing_disable_lib_pulsewidth_checks.1
        _syn(
            "timing_disable_lib_pulsewidth_checks",
            "",
            "timing_disable_lib_pulsewidth_checks {true | false}",
        ),
        # man1/timing_disable_library_data_to_data_checks.1
        _syn(
            "timing_disable_library_data_to_data_checks",
            "",
            "timing_disable_library_data_to_data_checks {true | false}",
        ),
        # man1/timing_disable_library_tiehi_tielo.1
        _syn(
            "timing_disable_library_tiehi_tielo",
            "",
            "timing_disable_library_tiehi_tielo {true | false}",
        ),
        # man1/timing_disable_netlist_constants.1
        _syn(
            "timing_disable_netlist_constants",
            "",
            "timing_disable_netlist_constants {true | false}",
        ),
        # man1/timing_disable_nochange_checks.1
        _syn(
            "timing_disable_nochange_checks",
            "",
            "timing_disable_nochange_checks {true | false}",
        ),
        # man1/timing_disable_non_sequential_checks.1
        _syn(
            "timing_disable_non_sequential_checks",
            "",
            "timing_disable_non_sequential_checks {true | false}",
        ),
        # man1/timing_disable_output_as_clock_port.1
        _syn(
            "timing_disable_output_as_clock_port",
            "",
            "timing_disable_output_as_clock_port {true | false}",
        ),
        # man1/timing_disable_parallel_arcs.1
        _syn(
            "timing_disable_parallel_arcs",
            "",
            "timing_disable_parallel_arcs {true | false}",
        ),
        # man1/timing_disable_pulsewidth_same_edge_si_cppr_mode.1
        _syn(
            "timing_disable_pulsewidth_same_edge_si_cppr_mode",
            "",
            "timing_disable_pulsewidth_same_edge_si_cppr_mode {true | false}",
        ),
        # man1/timing_disable_recovery_removal_checks.1
        _syn(
            "timing_disable_recovery_removal_checks",
            "",
            "timing_disable_recovery_removal_checks {true | false}",
        ),
        # man1/timing_disable_report_header_info.1
        _syn(
            "timing_disable_report_header_info",
            "",
            "timing_disable_report_header_info {true | false}",
        ),
        # man1/timing_disable_retime_clock_path_slew_propagation.1
        _syn(
            "timing_disable_retime_clock_path_slew_propagation",
            "",
            "timing_disable_retime_clock_path_slew_propagation {true | false}",
        ),
        # man1/timing_disable_sdf_retain_arc_merging.1
        _syn(
            "timing_disable_sdf_retain_arc_merging",
            "",
            "timing_disable_sdf_retain_arc_merging {true | false}",
        ),
        # man1/timing_disable_skew_checks.1
        _syn(
            "timing_disable_skew_checks",
            "",
            "timing_disable_skew_checks {true | false}",
        ),
        # man1/timing_disable_test_signal_arc.1
        _syn(
            "timing_disable_test_signal_arc",
            "",
            "timing_disable_test_signal_arc {true | false}",
        ),
        # man1/timing_disable_timing_model_latch_inferencing.1
        _syn(
            "timing_disable_timing_model_latch_inferencing",
            "",
            "timing_disable_timing_model_latch_inferencing {true | false}",
        ),
        # man1/timing_disable_tristate_disable_arcs.1
        _syn(
            "timing_disable_tristate_disable_arcs",
            "",
            "timing_disable_tristate_disable_arcs {true | false}",
        ),
        # man1/timing_disable_user_data_to_data_checks.1
        _syn(
            "timing_disable_user_data_to_data_checks",
            "",
            "timing_disable_user_data_to_data_checks {true | false}",
        ),
        # man1/timing_driving_cell_override_library.1
        _syn(
            "timing_driving_cell_override_library",
            "",
            "timing_driving_cell_override_library {true | false}",
        ),
        # man1/timing_dynamic_loop_breaking.1
        _syn(
            "timing_dynamic_loop_breaking",
            "",
            "timing_dynamic_loop_breaking {true | false}",
        ),
        # man1/timing_enable_all_fanin_fanout_levels_compatibility.1
        _syn(
            "timing_enable_all_fanin_fanout_levels_compatibility",
            "",
            "timing_enable_all_fanin_fanout_levels_compatibility {true | false}",
        ),
        # man1/timing_enable_aocv_slack_based.1
        _syn(
            "timing_enable_aocv_slack_based",
            "",
            "timing_enable_aocv_slack_based {0 | 1}",
        ),
        # man1/timing_enable_case_analysis_conflict_warning.1
        _syn(
            "timing_enable_case_analysis_conflict_warning",
            "",
            "timing_enable_case_analysis_conflict_warning {true | false}",
        ),
        # man1/timing_enable_clock2clock_clockgating_check.1
        _syn(
            "timing_enable_clock2clock_clockgating_check",
            "",
            "timing_enable_clock2clock_clockgating_check {true | false}",
        ),
        # man1/timing_enable_clock_phase_based_rise_fall_derating.1
        _syn(
            "timing_enable_clock_phase_based_rise_fall_derating",
            "",
            "timing_enable_clock_phase_based_rise_fall_derating {true | false}",
        ),
        # man1/timing_enable_data_through_clock_gating.1
        _syn(
            "timing_enable_data_through_clock_gating",
            "",
            "timing_enable_data_through_clock_gating {true | false}",
        ),
        # man1/timing_enable_derating_for_pulsewidth_checks.1
        _syn(
            "timing_enable_derating_for_pulsewidth_checks",
            "",
            "timing_enable_derating_for_pulsewidth_checks {true | false}",
        ),
        # man1/timing_enable_early_late_data_slews_for_setuphold_mode_checks.1
        _syn(
            "timing_enable_early_late_data_slews_for_setuphold_mode_checks",
            "",
            "timing_enable_early_late_data_slews_for_setuphold_mode_checks {true | false}",
        ),
        # man1/timing_enable_genclk_divide_by_inherit_parent_duty_cycle.1
        _syn(
            "timing_enable_genclk_divide_by_inherit_parent_duty_cycle",
            "",
            "timing_enable_genclk_divide_by_inherit_parent_duty_cycle {true | false}",
        ),
        # man1/timing_enable_genclk_edge_based_source_latency.1
        _syn(
            "timing_enable_genclk_edge_based_source_latency",
            "",
            "timing_enable_genclk_edge_based_source_latency {true | false}",
        ),
        # man1/timing_enable_genclk_source_path_register_limit.1
        _syn(
            "timing_enable_genclk_source_path_register_limit",
            "",
            "timing_enable_genclk_source_path_register_limit {true | false}",
        ),
        # man1/timing_enable_get_object_escaped_name_backward_compatible.1
        _syn(
            "timing_enable_get_object_escaped_name_backward_compatible",
            "",
            "timing_enable_get_object_escaped_name_backward_compatible {true | false}",
        ),
        # man1/timing_enable_get_objects_regexp_compatibility.1
        _syn(
            "timing_enable_get_objects_regexp_compatibility",
            "",
            "timing_enable_get_objects_regexp_compatibility {true | false}",
        ),
        # man1/timing_enable_hier_context_unmapped_clock_analysis.1
        _syn(
            "timing_enable_hier_context_unmapped_clock_analysis",
            "",
            "timing_enable_hier_context_unmapped_clock_analysis {true | false}",
        ),
        # man1/timing_enable_hierarchical_get_nets_support.1
        _syn(
            "timing_enable_hierarchical_get_nets_support",
            "",
            "timing_enable_hierarchical_get_nets_support {true | false}",
        ),
        # man1/timing_enable_latch_thru_mode.1
        _syn(
            "timing_enable_latch_thru_mode",
            "",
            "timing_enable_latch_thru_mode {true | false}",
        ),
        # man1/timing_enable_latency_through_clock_gating.1
        _syn(
            "timing_enable_latency_through_clock_gating",
            "",
            "timing_enable_latency_through_clock_gating {true | false}",
        ),
        # man1/timing_enable_mmmc_loop_handling.1
        _syn(
            "timing_enable_mmmc_loop_handling",
            "",
            "timing_enable_mmmc_loop_handling {true | false}",
        ),
        # man1/timing_enable_multi_drive_net_reduction_with_assertions.1
        _syn(
            "timing_enable_multi_drive_net_reduction_with_assertions",
            "",
            "timing_enable_multi_drive_net_reduction_with_assertions {none | delay | all}",
        ),
        # man1/timing_enable_multifrequency_latch_analysis.1
        _syn(
            "timing_enable_multifrequency_latch_analysis",
            "",
            "timing_enable_multifrequency_latch_analysis {true | false}",
        ),
        # man1/timing_enable_path_delay_to_unconstrained_endpoints_compatibility.1
        _syn(
            "timing_enable_path_delay_to_unconstrained_endpoints_compatibility",
            "",
            "timing_enable_path_delay_to_unconstrained_endpoints_compatibility {true | false}",
        ),
        # man1/timing_enable_pessimistic_cppr_for_reconvergent_clock_paths.1
        _syn(
            "timing_enable_pessimistic_cppr_for_reconvergent_clock_paths",
            "",
            "timing_enable_pessimistic_cppr_for_reconvergent_clock_paths {true | false}",
        ),
        # man1/timing_enable_power_ground_constants.1
        _syn(
            "timing_enable_power_ground_constants",
            "",
            "timing_enable_power_ground_constants {true | false}",
        ),
        # man1/timing_enable_preset_clear_arcs.1
        _syn(
            "timing_enable_preset_clear_arcs",
            "",
            "timing_enable_preset_clear_arcs {true | false}",
        ),
        # man1/timing_enable_pulsed_latch.1
        _syn(
            "timing_enable_pulsed_latch",
            "",
            "timing_enable_pulsed_latch {true | false}",
        ),
        # man1/timing_enable_sdc_compatible_data_check_mcp.1
        _syn(
            "timing_enable_sdc_compatible_data_check_mcp",
            "",
            "timing_enable_sdc_compatible_data_check_mcp {true | false}",
        ),
        # man1/timing_enable_si_cppr.1
        _syn(
            "timing_enable_si_cppr",
            "",
            "timing_enable_si_cppr {true | false}",
        ),
        # man1/timing_enable_simultaneous_setup_hold_mode.1
        _syn(
            "timing_enable_simultaneous_setup_hold_mode",
            "",
            "timing_enable_simultaneous_setup_hold_mode {true | false}",
        ),
        # man1/timing_enable_spatial_derate_mode.1
        _syn(
            "timing_enable_spatial_derate_mode",
            "",
            "timing_enable_spatial_derate_mode {true | false}",
        ),
        # man1/timing_enable_tristate_clock_gating.1
        _syn(
            "timing_enable_tristate_clock_gating",
            "",
            "timing_enable_tristate_clock_gating {true | false}",
        ),
        # man1/timing_enable_uncertainty_for_clock_checks.1
        _syn(
            "timing_enable_uncertainty_for_clock_checks",
            "",
            "timing_enable_uncertainty_for_clock_checks {true | false}",
        ),
        # man1/timing_enable_uncertainty_for_pulsewidth_checks.1
        _syn(
            "timing_enable_uncertainty_for_pulsewidth_checks",
            "",
            "timing_enable_uncertainty_for_pulsewidth_checks {true | false}",
        ),
        # man1/timing_enable_vtskew_derate_mode.1
        _syn(
            "timing_enable_vtskew_derate_mode",
            "",
            "timing_enable_vtskew_derate_mode {true | false}",
        ),
        # man1/timing_enable_zero_delay_analysis_mode.1
        _syn(
            "timing_enable_zero_delay_analysis_mode",
            "",
            "timing_enable_zero_delay_analysis_mode {true | false}",
        ),
        # man1/timing_extract_model_aocv_mode.1
        _syn(
            "timing_extract_model_aocv_mode",
            "",
            "timing_extract_model_aocv_mode {graph_based | path_based | none}",
        ),
        # man1/timing_extract_model_case_analysis_in_library.1
        _syn(
            "timing_extract_model_case_analysis_in_library",
            "",
            "timing_extract_model_case_analysis_in_library {true | false}",
        ),
        # man1/timing_extract_model_check_arcs_as_lvf.1
        _syn(
            "timing_extract_model_check_arcs_as_lvf",
            "",
            "timing_extract_model_check_arcs_as_lvf {true | false}",
        ),
        # man1/timing_extract_model_consider_design_level_drv.1
        _syn(
            "timing_extract_model_consider_design_level_drv",
            "",
            "timing_extract_model_consider_design_level_drv {true | false}",
        ),
        # man1/timing_extract_model_disable_cycle_adjustment.1
        _syn(
            "timing_extract_model_disable_cycle_adjustment",
            "",
            "timing_extract_model_disable_cycle_adjustment {true | false}",
        ),
        # man1/timing_extract_model_enable_combinational_arc_to_clock_source_on_output_ports.1
        _syn(
            "timing_extract_model_enable_combinational_arc_to_clock_source_on_output_ports",
            "",
            "timing_extract_model_enable_combinational_arc_to_clock_source_on_output_ports {true | false}",
        ),
        # man1/timing_extract_model_exhaustive_validation_dir.1
        _syn(
            "timing_extract_model_exhaustive_validation_dir",
            "",
            "timing_extract_model_exhaustive_validation_dir <string>",
        ),
        # man1/timing_extract_model_exhaustive_validation_mode.1
        _syn(
            "timing_extract_model_exhaustive_validation_mode",
            "",
            "timing_extract_model_exhaustive_validation_mode {true | false}",
        ),
        # man1/timing_extract_model_gating_as_nochange_arc.1
        _syn(
            "timing_extract_model_gating_as_nochange_arc",
            "",
            "timing_extract_model_gating_as_nochange_arc {true | false}",
        ),
        # man1/timing_extract_model_ideal_clock_latency_arc.1
        _syn(
            "timing_extract_model_ideal_clock_latency_arc",
            "",
            "timing_extract_model_ideal_clock_latency_arc {true | false}",
        ),
        # man1/timing_extract_model_include_applied_load_in_characterization_range.1
        _syn(
            "timing_extract_model_include_applied_load_in_characterization_range",
            "",
            "timing_extract_model_include_applied_load_in_characterization_range {true | false}",
        ),
        # man1/timing_extract_model_include_applied_slew_in_characterization_range.1
        _syn(
            "timing_extract_model_include_applied_slew_in_characterization_range",
            "",
            "timing_extract_model_include_applied_slew_in_characterization_range {true | false}",
        ),
        # man1/timing_extract_model_max_feedthrough_characterization_load.1
        _syn(
            "timing_extract_model_max_feedthrough_characterization_load",
            "",
            "timing_extract_model_max_feedthrough_characterization_load {true | false}",
        ),
        # man1/timing_extract_model_non_borrowing_latch_path_as_setup.1
        _syn(
            "timing_extract_model_non_borrowing_latch_path_as_setup",
            "",
            "timing_extract_model_non_borrowing_latch_path_as_setup {true | false}",
        ),
        # man1/timing_extract_model_slew_propagation_mode.1
        _syn(
            "timing_extract_model_slew_propagation_mode",
            "",
            "timing_extract_model_slew_propagation_mode {worst_slew | path_based_slew}",
        ),
        # man1/timing_extract_model_write_clock_checks_as_arc.1
        _syn(
            "timing_extract_model_write_clock_checks_as_arc",
            "",
            "timing_extract_model_write_clock_checks_as_arc {true | false}",
        ),
        # man1/timing_extract_model_write_clock_checks_as_scalar_tables.1
        _syn(
            "timing_extract_model_write_clock_checks_as_scalar_tables",
            "",
            "timing_extract_model_write_clock_checks_as_scalar_tables {true | false}",
        ),
        # man1/timing_extract_model_write_lvf.1
        _syn(
            "timing_extract_model_write_lvf",
            "",
            "timing_extract_model_write_lvf {true | false}",
        ),
        # man1/timing_extract_model_write_min_max_clock_tree_path.1
        _syn(
            "timing_extract_model_write_min_max_clock_tree_path",
            "",
            "timing_extract_model_write_min_max_clock_tree_path {true | false}",
        ),
        # man1/timing_generate_normalized_driver_waveform.1
        _syn(
            "timing_generate_normalized_driver_waveform",
            "",
            "timing_generate_normalized_driver_waveform {0 | 1}",
        ),
        # man1/timing_generated_clocks_allow_nested_assertions.1
        _syn(
            "timing_generated_clocks_allow_nested_assertions",
            "",
            "timing_generated_clocks_allow_nested_assertions {true | false}",
        ),
        # man1/timing_generated_clocks_inherit_ideal_latency.1
        _syn(
            "timing_generated_clocks_inherit_ideal_latency",
            "",
            "timing_generated_clocks_inherit_ideal_latency {true | false}",
        ),
        # man1/timing_get_of_objects_hier_compatibility.1
        _syn(
            "timing_get_of_objects_hier_compatibility",
            "",
            "timing_get_of_objects_hier_compatibility {true | false}",
        ),
        # man1/timing_hier_object_name_compatibility.1
        _syn(
            "timing_hier_object_name_compatibility",
            "",
            "timing_hier_object_name_compatibility {true | false}",
        ),
        # man1/timing_hierarchical_context_continue_on_top_block_clock_mismatch.1
        _syn(
            "timing_hierarchical_context_continue_on_top_block_clock_mismatch",
            "",
            "timing_hierarchical_context_continue_on_top_block_clock_mismatch {true | false}",
        ),
        # man1/timing_ignore_clock_based_path_delay_on_data_checks.1
        _syn(
            "timing_ignore_clock_based_path_delay_on_data_checks",
            "",
            "timing_ignore_clock_based_path_delay_on_data_checks {true | false}",
        ),
        # man1/timing_ignore_lumped_rc_assertions.1
        _syn(
            "timing_ignore_lumped_rc_assertions",
            "",
            "timing_ignore_lumped_rc_assertions {true | false}",
        ),
        # man1/timing_io_use_clock_network_latency.1
        _syn(
            "timing_io_use_clock_network_latency",
            "",
            "timing_io_use_clock_network_latency ?always | ideal?",
        ),
        # man1/timing_library_convert_async_setuphold_to_recrem.1
        _syn(
            "timing_library_convert_async_setuphold_to_recrem",
            "",
            "timing_library_convert_async_setuphold_to_recrem ?1 | 0?",
        ),
        # man1/timing_library_genclk_use_group_name.1
        _syn(
            "timing_library_genclk_use_group_name",
            "",
            "timing_library_genclk_use_group_name {true | false}",
        ),
        # man1/timing_library_hold_constraint_corner_sigma_multiplier.1
        _syn(
            "timing_library_hold_constraint_corner_sigma_multiplier",
            "",
            "timing_library_hold_constraint_corner_sigma_multiplier <double >",
        ),
        # man1/timing_library_hold_sigma_multiplier.1
        _syn(
            "timing_library_hold_sigma_multiplier",
            "",
            "timing_library_hold_sigma_multiplier <double >",
        ),
        # man1/timing_library_infer_async_pins_from_timing_arcs.1
        _syn(
            "timing_library_infer_async_pins_from_timing_arcs",
            "",
            "timing_library_infer_async_pins_from_timing_arcs {true | false}",
        ),
        # man1/timing_library_infer_cap_range_from_ccs_receiver_model.1
        _syn(
            "timing_library_infer_cap_range_from_ccs_receiver_model",
            "",
            "timing_library_infer_cap_range_from_ccs_receiver_model {true | false}",
        ),
        # man1/timing_library_infer_cap_range_from_ecsm_receiver_model.1
        _syn(
            "timing_library_infer_cap_range_from_ecsm_receiver_model",
            "",
            "timing_library_infer_cap_range_from_ecsm_receiver_model {true | false} <Default>: false",
        ),
        # man1/timing_library_infer_socv_from_aocv.1
        _syn(
            "timing_library_infer_socv_from_aocv",
            "",
            "timing_library_infer_socv_from_aocv {true | false}",
        ),
        # man1/timing_library_read_ccs_noise_data.1
        _syn(
            "timing_library_read_ccs_noise_data",
            "",
            "timing_library_read_ccs_noise_data {true | false}",
        ),
        # man1/timing_library_read_without_power.1
        _syn(
            "timing_library_read_without_power",
            "",
            "timing_library_read_without_power {true | false}",
        ),
        # man1/timing_library_scale_aocv_to_socv_to_n_sigma.1
        _syn(
            "timing_library_scale_aocv_to_socv_to_n_sigma",
            "",
            "timing_library_scale_aocv_to_socv_to_n_sigma <<n_sigma value>>",
        ),
        # man1/timing_library_setup_constraint_corner_sigma_multiplier.1
        _syn(
            "timing_library_setup_constraint_corner_sigma_multiplier",
            "",
            "timing_library_setup_constraint_corner_sigma_multiplier <double >",
        ),
        # man1/timing_library_setup_sigma_multiplier.1
        _syn(
            "timing_library_setup_sigma_multiplier",
            "",
            "timing_library_setup_sigma_multiplier <double >",
        ),
        # man1/timing_library_use_trilib_drv_values.1
        _syn(
            "timing_library_use_trilib_drv_values",
            "",
            "timing_library_use_trilib_drv_values {true | false}",
        ),
        # man1/timing_library_use_two_piece_receiver_cap.1
        _syn(
            "timing_library_use_two_piece_receiver_cap",
            "",
            "timing_library_use_two_piece_receiver_cap {true | false}",
        ),
        # man1/timing_library_zero_negative_timing_check_arcs.1
        _syn(
            "timing_library_zero_negative_timing_check_arcs",
            "",
            "timing_library_zero_negative_timing_check_arcs {true | false}",
        ),
        # man1/timing_max_transition_use_si_transition.1
        _syn(
            "timing_max_transition_use_si_transition",
            "",
            "timing_max_transition_use_si_transition {true | false}",
        ),
        # man1/timing_multifrequency_clock_rounding_factor.1
        _syn(
            "timing_multifrequency_clock_rounding_factor",
            "",
            "timing_multifrequency_clock_rounding_factor {1e-04 | 1e-05}",
        ),
        # man1/timing_normalized_driver_waveform_clip_linear_part.1
        _syn(
            "timing_normalized_driver_waveform_clip_linear_part",
            "",
            "timing_normalized_driver_waveform_clip_linear_part {0 | 1}",
        ),
        # man1/timing_normalized_driver_waveform_weight_factor.1
        _syn(
            "timing_normalized_driver_waveform_weight_factor",
            "",
            "timing_normalized_driver_waveform_weight_factor <<float value>>",
        ),
        # man1/timing_null_collection_return_compatibility.1
        _syn(
            "timing_null_collection_return_compatibility",
            "",
            "timing_null_collection_return_compatibility {true | false}",
        ),
        # man1/timing_path_based_enable_bounding_box_for_io_paths.1
        _syn(
            "timing_path_based_enable_bounding_box_for_io_paths",
            "",
            "timing_path_based_enable_bounding_box_for_io_paths {true | false}",
        ),
        # man1/timing_path_based_enable_closest_common_pin_driver_for_bounding_box.1
        _syn(
            "timing_path_based_enable_closest_common_pin_driver_for_bounding_box",
            "",
            "timing_path_based_enable_closest_common_pin_driver_for_bounding_box {true | false}",
        ),
        # man1/timing_path_based_enable_exhaustive_depth_bounded_by_gba.1
        _syn(
            "timing_path_based_enable_exhaustive_depth_bounded_by_gba",
            "",
            "timing_path_based_enable_exhaustive_depth_bounded_by_gba {true | false}",
        ),
        # man1/timing_path_based_enable_report_launch_clock_path.1
        _syn(
            "timing_path_based_enable_report_launch_clock_path",
            "",
            "timing_path_based_enable_report_launch_clock_path {true | false}",
        ),
        # man1/timing_path_based_enable_verbose_mode.1
        _syn(
            "timing_path_based_enable_verbose_mode",
            "",
            "timing_path_based_enable_verbose_mode <value >",
        ),
        # man1/timing_path_based_exhaustive_enable_design_coverage.1
        _syn(
            "timing_path_based_exhaustive_enable_design_coverage",
            "",
            "timing_path_based_exhaustive_enable_design_coverage {true | false}",
        ),
        # man1/timing_path_based_exhaustive_max_paths_limit.1
        _syn(
            "timing_path_based_exhaustive_max_paths_limit",
            "",
            "timing_path_based_exhaustive_max_paths_limit <integer>",
        ),
        # man1/timing_path_based_ipba_endpoints_max_limit.1
        _syn(
            "timing_path_based_ipba_endpoints_max_limit",
            "",
            "timing_path_based_ipba_endpoints_max_limit <integer> < >",
        ),
        # man1/timing_path_based_report_analysis_summary_max_paths_limit.1
        _syn(
            "timing_path_based_report_analysis_summary_max_paths_limit",
            "",
            "timing_path_based_report_analysis_summary_max_paths_limit <integer >",
        ),
        # man1/timing_pba_exhaustive_path_nworst_limit.1
        _syn(
            "timing_pba_exhaustive_path_nworst_limit",
            "",
            "timing_pba_exhaustive_path_nworst_limit <value>",
        ),
        # man1/timing_pll_clock_use_driving_cell.1
        _syn(
            "timing_pll_clock_use_driving_cell",
            "",
            "timing_pll_clock_use_driving_cell {true | false}",
        ),
        # man1/timing_prefix_module_name_with_library_genclk.1
        _syn(
            "timing_prefix_module_name_with_library_genclk",
            "",
            "timing_prefix_module_name_with_library_genclk {true | false}",
        ),
        # man1/timing_propagate_latch_data_uncertainty.1
        _syn(
            "timing_propagate_latch_data_uncertainty",
            "",
            "timing_propagate_latch_data_uncertainty {true | false}",
        ),
        # man1/timing_property_arrival_clocks_consider_clock_source_data_phase.1
        _syn(
            "timing_property_arrival_clocks_consider_clock_source_data_phase",
            "",
            "timing_property_arrival_clocks_consider_clock_source_data_phase {true | false}",
        ),
        # man1/timing_property_arrival_clocks_consider_data_phase.1
        _syn(
            "timing_property_arrival_clocks_consider_data_phase",
            "",
            "timing_property_arrival_clocks_consider_data_phase {true | false}",
        ),
        # man1/timing_property_arrival_clocks_consider_latency_phase.1
        _syn(
            "timing_property_arrival_clocks_consider_latency_phase",
            "",
            "timing_property_arrival_clocks_consider_latency_phase {true | false}",
        ),
        # man1/timing_property_arrival_window_enable_tcl_dict_format.1
        _syn(
            "timing_property_arrival_window_enable_tcl_dict_format",
            "",
            "timing_property_arrival_window_enable_tcl_dict_format {true | false}",
        ),
        # man1/timing_property_clock_used_as_data_unconstrained_clock_source_paths.1
        _syn(
            "timing_property_clock_used_as_data_unconstrained_clock_source_paths",
            "",
            "timing_property_clock_used_as_data_unconstrained_clock_source_paths {true | false}",
        ),
        # man1/timing_property_return_null_collection_with_quiet.1
        _syn(
            "timing_property_return_null_collection_with_quiet",
            "",
            "timing_property_return_null_collection_with_quiet {true | false}",
        ),
        # man1/timing_rail_swing_checks_high_voltage_threshold.1
        _syn(
            "timing_rail_swing_checks_high_voltage_threshold",
            "",
            "timing_rail_swing_checks_high_voltage_threshold double",
        ),
        # man1/timing_rail_swing_checks_low_voltage_threshold.1
        _syn(
            "timing_rail_swing_checks_low_voltage_threshold",
            "",
            "timing_rail_swing_checks_low_voltage_threshold double",
        ),
        # man1/timing_rcdb_allow_mismatch_option.1
        _syn(
            "timing_rcdb_allow_mismatch_option",
            "",
            "timing_rcdb_allow_mismatch_option {true | false}",
        ),
        # man1/timing_read_library_without_ecsm.1
        _syn(
            "timing_read_library_without_ecsm",
            "",
            "timing_read_library_without_ecsm {true | false}",
        ),
        # man1/timing_read_library_without_sensitivity.1
        _syn(
            "timing_read_library_without_sensitivity",
            "",
            "timing_read_library_without_sensitivity {1 | 0}",
        ),
        # man1/timing_recompute_sdf_in_setuphold_mode.1
        _syn(
            "timing_recompute_sdf_in_setuphold_mode",
            "",
            "timing_recompute_sdf_in_setuphold_mode {true | false}",
        ),
        # man1/timing_reduce_multi_drive_net_arcs.1
        _syn(
            "timing_reduce_multi_drive_net_arcs",
            "",
            "timing_reduce_multi_drive_net_arcs {true | false}",
        ),
        # man1/timing_reduce_multi_drive_net_arcs_threshold.1
        _syn(
            "timing_reduce_multi_drive_net_arcs_threshold",
            "",
            "timing_reduce_multi_drive_net_arcs_threshold <int>",
        ),
        # man1/timing_remove_clock_reconvergence_pessimism.1
        _syn(
            "timing_remove_clock_reconvergence_pessimism",
            "",
            "timing_remove_clock_reconvergence_pessimism {true | false}",
        ),
        # man1/timing_report_analysis_summary_csv_extended_new_format.1
        _syn(
            "timing_report_analysis_summary_csv_extended_new_format",
            "",
            "timing_report_analysis_summary_csv_extended_new_format {true | false}",
        ),
        # man1/timing_report_arrival_property_worstcase_mode.1
        _syn(
            "timing_report_arrival_property_worstcase_mode",
            "",
            "timing_report_arrival_property_worstcase_mode <integer>",
        ),
        # man1/timing_report_begin_end_pair_max_path_limit.1
        _syn(
            "timing_report_begin_end_pair_max_path_limit",
            "",
            "timing_report_begin_end_pair_max_path_limit <integer>",
        ),
        # man1/timing_report_check_timing_unconstrained_endpoints_due_to_constants.1
        _syn(
            "timing_report_check_timing_unconstrained_endpoints_due_to_constants",
            "",
            "timing_report_check_timing_unconstrained_endpoints_due_to_constants {true | false}",
        ),
        # man1/timing_report_clock_pin_as_begin_point.1
        _syn(
            "timing_report_clock_pin_as_begin_point",
            "",
            "timing_report_clock_pin_as_begin_point {true | false}",
        ),
        # man1/timing_report_constraint_enable_extended_drv_format.1
        _syn(
            "timing_report_constraint_enable_extended_drv_format",
            "",
            "timing_report_constraint_enable_extended_drv_format {true | false}",
        ),
        # man1/timing_report_constraint_extended_cell_em_flow.1
        _syn(
            "timing_report_constraint_extended_cell_em_flow",
            "",
            "timing_report_constraint_extended_cell_em_flow {true | false}",
        ),
        # man1/timing_report_constraint_format.1
        _syn(
            "timing_report_constraint_format",
            "",
            "timing_report_constraint_format <string >",
        ),
        # man1/timing_report_constraint_report_all_drv_violation.1
        _syn(
            "timing_report_constraint_report_all_drv_violation",
            "",
            "timing_report_constraint_report_all_drv_violation {true | false}",
        ),
        # man1/timing_report_constraint_rise_fall_clock_period_check.1
        _syn(
            "timing_report_constraint_rise_fall_clock_period_check",
            "",
            "timing_report_constraint_rise_fall_clock_period_check {true | false}",
        ),
        # man1/timing_report_constraint_use_infinity_slack_for_unconstrained.1
        _syn(
            "timing_report_constraint_use_infinity_slack_for_unconstrained",
            "",
            "timing_report_constraint_use_infinity_slack_for_unconstrained {true | false}",
        ),
        # man1/timing_report_default_frequency_for_unconstrained_nets.1
        _syn(
            "timing_report_default_frequency_for_unconstrained_nets",
            "",
            "timing_report_default_frequency_for_unconstrained_nets <value>",
        ),
        # man1/timing_report_disable_max_paths_per_group.1
        _syn(
            "timing_report_disable_max_paths_per_group",
            "",
            "timing_report_disable_max_paths_per_group {true | false}",
        ),
        # man1/timing_report_drv_enable_clock_source_as_clock.1
        _syn(
            "timing_report_drv_enable_clock_source_as_clock",
            "",
            "timing_report_drv_enable_clock_source_as_clock {true | false}",
        ),
        # man1/timing_report_drv_enable_frequency_per_view.1
        _syn(
            "timing_report_drv_enable_frequency_per_view",
            "",
            "timing_report_drv_enable_frequency_per_view {true | false}",
        ),
        # man1/timing_report_drv_enable_ghz_notation_for_drv_fields.1
        _syn(
            "timing_report_drv_enable_ghz_notation_for_drv_fields",
            "",
            "timing_report_drv_enable_ghz_notation_for_drv_fields {true | false}",
        ),
        # man1/timing_report_drv_enable_slew_threshold_scaling.1
        _syn(
            "timing_report_drv_enable_slew_threshold_scaling",
            "",
            "timing_report_drv_enable_slew_threshold_scaling {true | false}",
        ),
        # man1/timing_report_drv_per_frequency.1
        _syn(
            "timing_report_drv_per_frequency",
            "",
            "timing_report_drv_per_frequency {true | false}",
        ),
        # man1/timing_report_drv_per_frequency_per_input_slew.1
        _syn(
            "timing_report_drv_per_frequency_per_input_slew",
            "",
            "timing_report_drv_per_frequency_per_input_slew {true | false}",
        ),
        # man1/timing_report_drv_use_worst_timing_slack.1
        _syn(
            "timing_report_drv_use_worst_timing_slack",
            "",
            "timing_report_drv_use_worst_timing_slack {true | false}",
        ),
        # man1/timing_report_enable_clock_to_for_unconstrained_paths.1
        _syn(
            "timing_report_enable_clock_to_for_unconstrained_paths",
            "",
            "timing_report_enable_clock_to_for_unconstrained_paths {true | false}",
        ),
        # man1/timing_report_enable_clock_unrolling.1
        _syn(
            "timing_report_enable_clock_unrolling",
            "",
            "timing_report_enable_clock_unrolling {true | false}",
        ),
        # man1/timing_report_enable_cppr_point.1
        _syn(
            "timing_report_enable_cppr_point",
            "",
            "timing_report_enable_cppr_point { true | false}",
        ),
        # man1/timing_report_enable_em_index_clipping_report.1
        _syn(
            "timing_report_enable_em_index_clipping_report",
            "",
            "timing_report_enable_em_index_clipping_report {true | false}",
        ),
        # man1/timing_report_enable_lead_trail_to_rise_fall_map.1
        _syn(
            "timing_report_enable_lead_trail_to_rise_fall_map",
            "",
            "timing_report_enable_lead_trail_to_rise_fall_map {true | false}",
        ),
        # man1/timing_report_enable_markers.1
        _syn(
            "timing_report_enable_markers",
            "",
            "timing_report_enable_markers {true | false}",
        ),
        # man1/timing_report_enable_max_capacitance_drv_for_constants.1
        _syn(
            "timing_report_enable_max_capacitance_drv_for_constants",
            "",
            "timing_report_enable_max_capacitance_drv_for_constants {true | false}",
        ),
        # man1/timing_report_enable_max_path_limit_crossed.1
        _syn(
            "timing_report_enable_max_path_limit_crossed",
            "",
            "timing_report_enable_max_path_limit_crossed {true | false}",
        ),
        # man1/timing_report_enable_report_clock_timing_across_clock_pin.1
        _syn(
            "timing_report_enable_report_clock_timing_across_clock_pin",
            "",
            "timing_report_enable_report_clock_timing_across_clock_pin {true | false}",
        ),
        # man1/timing_report_enable_si_debug.1
        _syn(
            "timing_report_enable_si_debug",
            "",
            "timing_report_enable_si_debug {true | false}",
        ),
        # man1/timing_report_enable_slack_summary_at_bottom.1
        _syn(
            "timing_report_enable_slack_summary_at_bottom",
            "",
            "timing_report_enable_slack_summary_at_bottom {true | false}",
        ),
        # man1/timing_report_enable_unique_pins_multiple_capture_clock_paths.1
        _syn(
            "timing_report_enable_unique_pins_multiple_capture_clock_paths",
            "",
            "timing_report_enable_unique_pins_multiple_capture_clock_paths",
        ),
        # man1/timing_report_enable_use_valid_start_end_points.1
        _syn(
            "timing_report_enable_use_valid_start_end_points",
            "",
            "timing_report_enable_use_valid_start_end_points {true | false}",
        ),
        # man1/timing_report_generated_clock_info.1
        _syn(
            "timing_report_generated_clock_info",
            "",
            "timing_report_generated_clock_info {true | false}",
        ),
        # man1/timing_report_group_based_mode.1
        _syn(
            "timing_report_group_based_mode",
            "",
            "timing_report_group_based_mode {true | false}",
        ),
        # man1/timing_report_max_transition_check_using_nsigma_slew.1
        _syn(
            "timing_report_max_transition_check_using_nsigma_slew",
            "",
            "timing_report_max_transition_check_using_nsigma_slew {true | false}",
        ),
        # man1/timing_report_property_fastest_clock_consider_data_phase.1
        _syn(
            "timing_report_property_fastest_clock_consider_data_phase",
            "",
            "timing_report_property_fastest_clock_consider_data_phase {true | false}",
        ),
        # man1/timing_report_pulse_width_matching_launch_capture_paths.1
        _syn(
            "timing_report_pulse_width_matching_launch_capture_paths",
            "",
            "timing_report_pulse_width_matching_launch_capture_paths {true | false}",
        ),
        # man1/timing_report_redirect_message_types.1
        _syn(
            "timing_report_redirect_message_types",
            "",
            "timing_report_redirect_message_types {none | info}",
        ),
        # man1/timing_report_retime_formatting_mode.1
        _syn(
            "timing_report_retime_formatting_mode",
            "",
            "timing_report_retime_formatting_mode {manual | retime_compare | retime_replace}",
        ),
        # man1/timing_report_skip_constraint_loop_check.1
        _syn(
            "timing_report_skip_constraint_loop_check",
            "",
            "timing_report_skip_constraint_loop_check {true | false}",
        ),
        # man1/timing_report_socv_summary_mean_sigma.1
        _syn(
            "timing_report_socv_summary_mean_sigma",
            "",
            "timing_report_socv_summary_mean_sigma {true | false}",
        ),
        # man1/timing_report_timing_header_detail_info.1
        _syn(
            "timing_report_timing_header_detail_info",
            "",
            "timing_report_timing_header_detail_info {default | extended}",
        ),
        # man1/timing_report_unconstrained_path_early_late_header.1
        _syn(
            "timing_report_unconstrained_path_early_late_header",
            "",
            "timing_report_unconstrained_path_early_late_header {true | false}",
        ),
        # man1/timing_report_unconstrained_paths.1
        _syn(
            "timing_report_unconstrained_paths",
            "",
            "timing_report_unconstrained_paths {true | false}",
        ),
        # man1/timing_report_use_receiver_model_capacitance.1
        _syn(
            "timing_report_use_receiver_model_capacitance",
            "",
            "timing_report_use_receiver_model_capacitance {true | false}",
        ),
        # man1/timing_report_use_worst_parallel_cell_arc.1
        _syn(
            "timing_report_use_worst_parallel_cell_arc",
            "",
            "timing_report_use_worst_parallel_cell_arc {true | false}",
        ),
        # man1/timing_resolve_driver_conflicts.1
        _syn(
            "timing_resolve_driver_conflicts",
            "",
            "timing_resolve_driver_conflicts {conservative | aggressive}",
        ),
        # man1/timing_sdf_adjust_negative_setuphold.1
        _syn(
            "timing_sdf_adjust_negative_setuphold",
            "",
            "timing_sdf_adjust_negative_setuphold {true | false}",
        ),
        # man1/timing_sdf_enable_setuphold_scond_ccond.1
        _syn(
            "timing_sdf_enable_setuphold_scond_ccond",
            "",
            "timing_sdf_enable_setuphold_scond_ccond {true | false}",
        ),
        # man1/timing_self_loop_paths_no_skew.1
        _syn(
            "timing_self_loop_paths_no_skew",
            "",
            "timing_self_loop_paths_no_skew {true | false}",
        ),
        # man1/timing_self_loop_paths_no_skew_max_depth.1
        _syn(
            "timing_self_loop_paths_no_skew_max_depth",
            "",
            "timing_self_loop_paths_no_skew_max_depth <value>",
        ),
        # man1/timing_self_loop_paths_no_skew_max_slack.1
        _syn(
            "timing_self_loop_paths_no_skew_max_slack",
            "",
            "timing_self_loop_paths_no_skew_max_slack <value>",
        ),
        # man1/timing_set_clock_source_to_output_as_data.1
        _syn(
            "timing_set_clock_source_to_output_as_data",
            "",
            "timing_set_clock_source_to_output_as_data {true | false}",
        ),
        # man1/timing_set_nsigma_multiplier.1
        _syn(
            "timing_set_nsigma_multiplier",
            "",
            "timing_set_nsigma_multiplier <value>",
        ),
        # man1/timing_set_scaling_for_negative_checks.1
        _syn(
            "timing_set_scaling_for_negative_checks",
            "",
            "timing_set_scaling_for_negative_checks {default | divider | multiplier}",
        ),
        # man1/timing_set_scaling_for_negative_delays.1
        _syn(
            "timing_set_scaling_for_negative_delays",
            "",
            "timing_set_scaling_for_negative_delays {default | divider | multiplier}",
        ),
        # man1/timing_socv_preserve_variation_with_annotations.1
        _syn(
            "timing_socv_preserve_variation_with_annotations",
            "",
            "timing_socv_preserve_variation_with_annotations {true | false}",
        ),
        # man1/timing_socv_rc_variation_mode.1
        _syn(
            "timing_socv_rc_variation_mode",
            "",
            "timing_socv_rc_variation_mode {true | false}",
        ),
        # man1/timing_socv_statistical_min_max_mode.1
        _syn(
            "timing_socv_statistical_min_max_mode",
            "",
            "timing_socv_statistical_min_max_mode {statistical | mean_and_three_sigma_bounded}",
        ),
        # man1/timing_socv_view_based_nsigma_multiplier_mode.1
        _syn(
            "timing_socv_view_based_nsigma_multiplier_mode",
            "",
            "timing_socv_view_based_nsigma_multiplier_mode {true | false}",
        ),
        # man1/timing_spatial_derate_chip_size.1
        _syn(
            "timing_spatial_derate_chip_size",
            "",
            "timing_spatial_derate_chip_size <value_in_microns>",
        ),
        # man1/timing_spatial_derate_distance_mode.1
        _syn(
            "timing_spatial_derate_distance_mode",
            "",
            "timing_spatial_derate_distance_mode {bounding_box | chip_size}",
        ),
        # man1/timing_suppress_escape_characters.1
        _syn(
            "timing_suppress_escape_characters",
            "",
            "timing_suppress_escape_characters {true | false}",
        ),
        # man1/timing_suppress_ilm_constraint_mismatches.1
        _syn(
            "timing_suppress_ilm_constraint_mismatches",
            "",
            "timing_suppress_ilm_constraint_mismatches {true | false}",
        ),
        # man1/timing_time_unit.1
        _syn(
            "timing_time_unit",
            "",
            "timing_time_unit <string>",
        ),
        # man1/timing_timing_window_pessimism_removal_include_si_delay.1
        _syn(
            "timing_timing_window_pessimism_removal_include_si_delay",
            "",
            "timing_timing_window_pessimism_removal_include_si_delay {true | false}",
        ),
        # man1/timing_use_clock_pin_attribute_for_clock_net_marking.1
        _syn(
            "timing_use_clock_pin_attribute_for_clock_net_marking",
            "",
            "timing_use_clock_pin_attribute_for_clock_net_marking {true | false}",
        ),
        # man1/timing_use_incremental_si_transition.1
        _syn(
            "timing_use_incremental_si_transition",
            "",
            "timing_use_incremental_si_transition {true | false}",
        ),
        # man1/timing_use_latch_early_launch_edge.1
        _syn(
            "timing_use_latch_early_launch_edge",
            "",
            "timing_use_latch_early_launch_edge {true | false}",
        ),
        # man1/timing_use_latch_time_borrow.1
        _syn(
            "timing_use_latch_time_borrow",
            "",
            "timing_use_latch_time_borrow {true | false}",
        ),
        # man1/timing_use_verilog_for_model_netlist.1
        _syn(
            "timing_use_verilog_for_model_netlist",
            "",
            "timing_use_verilog_for_model_netlist {true | false}",
        ),
        # man1/timing_waveform_aware_pulse_width_checks_high_voltage_level.1
        _syn(
            "timing_waveform_aware_pulse_width_checks_high_voltage_level",
            "",
            "timing_waveform_aware_pulse_width_checks_high_voltage_level <double>",
        ),
        # man1/timing_waveform_aware_pulse_width_checks_low_voltage_level.1
        _syn(
            "timing_waveform_aware_pulse_width_checks_low_voltage_level",
            "",
            "timing_waveform_aware_pulse_width_checks_low_voltage_level <double>",
        ),
        # man1/timing_write_sdf_no_escape_backslash_control.1
        _syn(
            "timing_write_sdf_no_escape_backslash_control",
            "",
            "sdf_no_escape_backslash_control {true | false}",
        ),
        # man1/trace_obj_connectivity.1
        _syn(
            "trace_obj_connectivity",
            "Traces the connections of specified macros, selected macros, or specified ports",
            "trace_obj_connectivity ?-help? ?-clear_trace? ?-level <level>? ?-mode {netlist_based timing_based}? ?-out_file <file_name>? ?-insts <string>? | ?-ports <string>? | ?-selected? | ?-in_files <file_name>?",
        ),
        # man1/traceJtag.1
        _syn(
            "traceJtag",
            "Traces JTAG logic between the I/O pins and the pins of given leaf instances",
            "traceJtag -infile <jtagPinFile> -outfile <jtagInstanceFile>",
        ),
        # man1/translateSNDCSetupFile.1
        _syn(
            "translateSNDCSetupFile",
            "",
            "translateSNDCSetupFile ?-help? <sndcSetupFile> <outputFile>",
        ),
        # man1/trim_pg.1
        _syn(
            "trim_pg",
            "This command offers a semi-automated mechanism that helps in trimming the redundant PG stripes and vias using an existing power grid pattern based on IR drop analysis reports",
            "trim_pg ?-help? ?-area {<x1, y1, x2, y2>} | -candidate_file <file_name>? -net {<list_of_nets>} {{-layer {<layer_name1> ?<layer_name2>?} -pattern {<str1> ?<str2> … <strN>?} -type {stripe | via}} | -candidate_file <file_name>} ?-exclude_local_grid {{<lx1 ly1 ux1 uy1>} {<lx2 ly2 ux2 uy2>}...} | -candidate_file <file_name>? ?-exclude {{<lx1 ly1 ux1 uy1>} {<lx2 ly2 ux2 uy2>}...} | -candidate_file <file_name>? ?-keep_dangling_via? ?-threshold <threshold_value> | -candidate_file <file_name>?",
        ),
        # man1/trim_pg_library.1
        _syn(
            "trim_pg_library",
            "Specifies to remove a list of cells from the specified PGV",
            "trim_pg_library ?-help? ?-delete_cells <cell1> <cell2> ...? ?-delete_cells_file <file_name>? -library_list_file <file_name> ?-output <directory><_name>? -output_library <library><_name>",
        ),
        # man1/trimDesign.1
        _syn(
            "trimDesign",
            "Allows you to specify the coordinates of a box to create a small portion of the design as an independent de‐ sign",
            "trimDesign ?-help? ?-coreToBoundary <distance>? ?-dir <output_dir_to_save_trimmed_design>? ?-encryptName <proc_name_to_encrypt>? ?-name <trim_design_name>? ?-nets <list_of_net_names>? ?-placeOnly? ?-area {<x1 y1 x2 y2>} | -polygon< list_of_points >| -selectedRouteBlk?",
        ),
        # man1/trimMetalFillNearNet.1
        _syn(
            "trimMetalFillNearNet",
            "Trims any metal fill around critical nets",
            "trimMetalFillNearNet ?-help? ?-area {x1 y1 x2 y2}? ?-clock? ?-createFillBlockage <blockage_name>? ?-layer <layer_name_list>? ?-minTrimDensity {<percent1><layer_list1> ?{<percent2><layer_list2>}?}? ?-minTrimUnionDensityToAboveLayer {<percent1 layer_list1> ?{<percent2 layer_list2>}?..}? ?-net {<net_name_list> | <net_object_pointer_list>}? ?-recomputeDensity? ?-remove? ?-slackThreshold <slack_in_ns>? ?-spacing <dist_in_um>? ?-spacingAbove <dist_in_um>? ?-spacingBelow <dist_in_um>?",
        ),
        # man1/trPrintIgnoredPadNets.1
        _syn(
            "trPrintIgnoredPadNets",
            "",
            "trPrintIgnoredPadNets <value>",
        ),
        # man1/ui_view_box.1
        _syn(
            "ui_view_box",
            "Reports the coordinates of the current area being viewed in the GUI",
            "ui_view_box ?-help?",
        ),
        # man1/uiAdd.1
        _syn(
            "uiAdd",
            "Adds a new interface element with the specified name of the specified type",
            "uiAdd ?-help? <name> ?-before <name>? ?-checked {true | false}? ?-command <string>? ?-disabled {true | false}? ?-enablevar <string>? ?-foreground <string>? ?-icon <filename>? ?-in <name>? ?-label <string>? ?-movable {true | false}? ?-newline {true | false}? ?-shortcut <string>? ?-tooltip <string>? -type {menu | toolbar | submenu | command | check | radio | separator | toolbutton} ?-underline <integer>? ?-value <string>? ?-variable <string>? ?-visiblevar <string>?",
        ),
        # man1/uiDelete.1
        _syn(
            "uiDelete",
            "Deletes an existing interface element with the specified name",
            "uiDelete ?-help? <name>",
        ),
        # man1/uiFind.1
        _syn(
            "uiFind",
            "Enables you to retrieve an element's name by specifying a property-value combination",
            "uiFind ?-help? ?<name>? ?<property> {<value>}?",
        ),
        # man1/uiGet.1
        _syn(
            "uiGet",
            "Retrieves the current value of the specified property of the element that is being queried",
            "uiGet ?-help? ?<name>? ?-quiet? ?-before | -checked | -children | -command | -disabled | -dockwin | -enablevar | -foreground | -geometry | -icon | -in | -label | -menu | -message | -movable | -newline | -shortcut | -statusbar | -title | -toolbar | -tooltip | -type | -underline | -value | -variable | -visible | -visiblevar | -windowstatus?",
        ),
        # man1/uiGetRecordObjByInfo.1
        _syn(
            "uiGetRecordObjByInfo",
            "Returns the point of an object based on specific layer/name/area",
            "uiGetRecordObjByInfo ?-help? ?-layer <layer_value>? ?-name <object_name>? -objType {viaInst sViaInst sWire wire pWire pBlkg} -rect {x1 y1 x2 y2}",
        ),
        # man1/uiSet.1
        _syn(
            "uiSet",
            "For elements of type menu, submenu, command, check, radio, separator, toolbar, and toolbutton, the uiSet command works like the tk command <widget>configure",
            "uiSet ?-help? <name> ?-before <name>? ?-checked {true | false}? ?-command <string>? ?-disabled {true | false}? ?-enablevar <string>? ?-foreground <string>? ?-geometry <string >| -fullscreen {true | false}? ?-icon <filename>? ?-in <name>? ?-label <string>? ?-message <string>? ?-movable {true | false}? ?-newline {true | false}? ?-shortcut <string>? ?-statusbar <string>? ?-title <string>? ?-tooltip <string>? ?-underline <integer>? ?-value <string >? ?-variable <string>? ?-visible {true | false}? ?-visiblevar <string>?",
        ),
        # man1/uiSetTool.1
        _syn(
            "uiSetTool",
            "Selects specified tool widget in the main window and enters interactive mode",
            "uiSetTool ?-help? <mode>",
        ),
        # man1/unassignBump.1
        _syn(
            "unassignBump",
            "Removes the Verilog signal names from bumps, which removes the connection between bumps and I/O pins",
            "unassignBump ?-help? {-allBumps | -byBumpName {<list>} | -byBumpSite {<list>} | -selected}",
        ),
        # man1/unassignTSV.1
        _syn(
            "unassignTSV",
            "Unassigns the specified TSV",
            "unassignTSV {-netName <netname>| -all |-signal | -power | -ground | -selected}",
        ),
        # man1/undo.1
        _syn(
            "undo",
            "Undoes the previous edit made with any bump placement, floorplanning, power planning, or wire edit commands listed below",
            "undo ?-help?",
        ),
        # man1/undo_uniquify_partition.1
        _syn(
            "undo_uniquify_partition",
            "Brings back the recursion of cells in a netlist and restores the master and clone association",
            "undo_uniquify_partition ?-help? -hinst <hierarchical_instance_name>?-preserve_routes?",
        ),
        # man1/unfixAllIos.1
        _syn(
            "unfixAllIos",
            "Changes the status of all I/Os from FIXED to PLACED",
            "unfixAllIos ?-help? ?-incAreaIo?",
        ),
        # man1/unfixBondPad.1
        _syn(
            "unfixBondPad",
            "Unassigns the fixed status of a specified bond pad",
            "unfixBondPad ?-help? {-ioInstName <InstName>?-pinName <pinName>? | -selected}",
        ),
        # man1/unfixBump.1
        _syn(
            "unfixBump",
            "Removes the bump assignment status from a specified list of assigned bumps that were set with the setBumpFixed command",
            "unfixBump ?-help? {-allBumps | -byBumpName {<list>}}",
        ),
        # man1/unflattenIlm.1
        _syn(
            "unflattenIlm",
            "Reverts the ILM back to its original hard macro view",
            "unflattenIlm ?-help?",
        ),
        # man1/ungroup.1
        _syn(
            "ungroup",
            "Ungroups the specified hinsts",
            "ungroup ?-help? <hInst>+ ?-check_only? ?-exclude <hinst>+? ?-flatten? ?-honor_dont_touch? ?-threshold <instance_count>? ?-verbose? ?-simple | -prefix <prefix> | -escaped? ?-force | -only_user_hierarchy?",
        ),
        # man1/uniquify.1
        _syn(
            "uniquify",
            "Supports regrouping of master-clone partitions inside the non-unique modules",
            "uniquify ?-help? {?<design> | <module>? | -new_master <hinsts>} ?-exclude <modules>? ?-verbose?",
        ),
        # man1/uniquify_partition.1
        _syn(
            "uniquify_partition",
            "Removes the master and clone association by uniquifying the cells (module) in the netlist",
            "uniquify_partition ?-help? -hinst <hierarchical_instance_name>",
        ),
        # man1/unloadPtnPin.1
        _syn(
            "unloadPtnPin",
            "Removes the loading of partition pins by the loadPtnPin command",
            "unloadPtnPin ?-help? -ptnName <partitionName> {-file <floorplanFileName> }",
        ),
        # man1/unlockOaDesign.1
        _syn(
            "unlockOaDesign",
            "Unlocks the specified OpenAccess design",
            "unlockOaDesign ?-help? <lib> <cell> <view>",
        ),
        # man1/unplaceAllBlocks.1
        _syn(
            "unplaceAllBlocks",
            "Unplaces all blocks in the floorplan",
            "unplaceAllBlocks ?-help?",
        ),
        # man1/unplaceAllGuides.1
        _syn(
            "unplaceAllGuides",
            "Clears all constraints (guides, regions, and fences) from the floorplan",
            "unplaceAllGuides ?-help?",
        ),
        # man1/unplaceAllInsts.1
        _syn(
            "unplaceAllInsts",
            "Unplaces all instances from the floorplan including blobs and std cells whose status is PLACED",
            "unplaceAllInsts ?-help?",
        ),
        # man1/unplaceGuide.1
        _syn(
            "unplaceGuide",
            "Unplaces hierarchical instances and instance groups from the floorplan",
            "unplaceGuide ?-help?",
        ),
        # man1/unplaceGuideConstraints.1
        _syn(
            "unplaceGuideConstraints",
            "Clears only the guide constraints from the floorplan",
            "unplaceGuideConstraints ?-help?",
        ),
        # man1/unplaceJtag.1
        _syn(
            "unplaceJtag",
            "Changes the placement status of JTAG inst from FIXED to PLACED",
            "unplaceJtag",
        ),
        # man1/unregister_gui_edit_callback.1
        _syn(
            "unregister_gui_edit_callback",
            "Removes the callback function from the specified move action",
            "unregister_gui_edit_callback ?-help? -command <string> -edit_type {selection pre-move post-move}",
        ),
        # man1/unset_ccopt_property.1
        _syn(
            "unset_ccopt_property",
            "This command is used to reset the CCOpt object properties to their default values",
            "unset_ccopt_property ?-help?",
        ),
        # man1/unsetFixedBlockSize.1
        _syn(
            "unsetFixedBlockSize",
            "Specifies that during floorplan resizing, the size of the specified modules and/or blackboxes can change",
            "unsetFixedBlockSize ?-help?",
        ),
        # man1/unsetMessageLimit.1
        _syn(
            "unsetMessageLimit",
            "Removes the default or user-specified limit on error and warning messages",
            "unsetMessageLimit ?-help? ?<prefix> ?<ID1>, <ID2>, ...??",
        ),
        # man1/unsetPinConstraint.1
        _syn(
            "unsetPinConstraint",
            "Removes the constraints for a partition pin",
            "unsetPinConstraint ?-help? {?-global | -cell <cell_name> | -all_user? ?-global | -pin <pin_name_list> | -area {<x1 y1 x2 y2>} | -all_area | -side <side_names>? ?-global | -layer? ?-global | -loc | -edge | -corner <corner_number>? ??-pin <pin_name_list> ?-loc? ?-edge?? | ?-corner_to_pin_distance ?-corner <corner_number>??? ?{-pin <pin_name_list> | -pinTemplate {<layer_id_or_name_list>}} -width? ?{-pin <pin_name_list> | -pinTemplate {<layer_id_or_name_list>}} -depth? ??-layer ?-side <side_names>?? | -pinTemplate {<layer_id_or_name_list>}? ?-spacing ?-area {x1 y1 x2 y2}? ?-all_area? ?-side <side_names>?? } ?-depth ?-special_wire?? ?-all_user?",
        ),
        # man1/unsetProbePin.1
        _syn(
            "unsetProbePin",
            "Unsets a pad or bump as a probe point",
            "unsetProbePin ?-help? {-instName <InstName> -pinName <pinName>} | <-bump bumpName>",
        ),
        # man1/unspecifyBlackBox.1
        _syn(
            "unspecifyBlackBox",
            "Unspecifies or deletes a blackbox and converts it to a module if the blackbox was originally defined as a module, or a block if the blackbox has a cdump or LEF macro definition",
            "unspecifyBlackBox ?-help? {-cell <cellName> | -all} ?-keepPtn?",
        ),
        # man1/unspecifyIlm.1
        _syn(
            "unspecifyIlm",
            "Unspecifies the ILM cell",
            "unspecifyIlm ?-help? -cell <cellName>",
        ),
        # man1/unspecifyJtag.1
        _syn(
            "unspecifyJtag",
            "Unspecifies instances that were specified by the specifyJtag command",
            "unspecifyJtag {-cell <leaf_cellName> | -inst <instanceName> | -hinst <hierarchicalInstanceName> | -group <hierarchicalInstanceName> | <cellName>}",
        ),
        # man1/unspecifySelectiveBlkgGate.1
        _syn(
            "unspecifySelectiveBlkgGate",
            "Specifies cells and instances that are forbidden to be placed inside the soft blockage during legalization",
            "unspecifySelectiveBlkgGate ?-help? ?-cell <cellName>? ?-inst <instName>?",
        ),
        # man1/unsuppressMessage.1
        _syn(
            "unsuppressMessage",
            "Reverses the effect of the suppressMessage command",
            "unsuppressMessage <prefix> <numId >?<numId2> … <numIdn>?",
        ),
        # man1/update_analysis_view.1
        _syn(
            "update_analysis_view",
            "Changes attribute values for the specified existing analysis view",
            "update_analysis_view ?-help? -name <<existingAnalysisViewName>> {?-constraint_mode <<newModeName>>? ?-delay_corner <<newDelayCornerObj>>? ?-latency_file <<string>>?}",
        ),
        # man1/update_bus_guide.1
        _syn(
            "update_bus_guide",
            "Updates the selected bus guide as specified",
            "update_bus_guide ?-help? ?-avoidObstacles? ?-layer_horizontal {<id> | <id1:id2>}? ?-layer_vertical {<id> | <id1:id2>}? ?-no_snap? ?-resize_direction {low high}? ?-type {hard | soft}? ?-width <value> | -net_group <name> | {{-rule <rulename> | {-wire_width <value> -wire_spacing <value>}} ?-with_shield?}?",
        ),
        # man1/update_ccopt_clock_tree.1
        _syn(
            "update_ccopt_clock_tree",
            "Updates the specified clock tree",
            "update_ccopt_clock_tree ?-help?",
        ),
        # man1/update_clock_latencies.1
        _syn(
            "update_clock_latencies",
            "Updates the IO latencies for clock sinks specified using the consider_during_latency_update prop‐ erty",
            "update_clock_latencies ?-help?",
        ),
        # man1/update_clock_tree_source_latency.1
        _syn(
            "update_clock_tree_source_latency",
            "Stores clock arrival and transition times at the clock tree source group roots in preparation for multi-tap CTS",
            "update_clock_tree_source_latency ?-help? -clock_tree_source_groups <source_group_list>",
        ),
        # man1/update_clock_tree_spec_annotations.1
        _syn(
            "update_clock_tree_spec_annotations",
            "Updates all ideal nets, transition and delay annotations to match active timing con‐ straints and removes all prior annotations from the clock tree specification",
            "update_clock_tree_spec_annotations ?-help? ?-file <file_name>?",
        ),
        # man1/update_constraint_mode.1
        _syn(
            "update_constraint_mode",
            "Updates the SDC constraint file information for the specified existing constraint mode object",
            "update_constraint_mode ?-help? ?-ilm_sdc_files {file1.sdc file2.sdc ...}? ?-name <modeName>? {??-sdc_files {file1.sdc file2.sdc ...}? ?-tcl_vars {{<var_name1> <value1>} {<var_name2> <value2>} {<var_name3> <value3>} ...}? ?-reset_latency_files??}",
        ),
        # man1/update_delay_corner.1
        _syn(
            "update_delay_corner",
            "Modifies the parameters of an existing delay calculation corner object",
            "update_delay_corner ?-help? ?-early_estimated_worst_irDrop_factor <percent>? ?-early_irdrop_data <files_or_directories>? ?-early_irdrop_file <list_of_files>? ?-early_library_set <libSetName>? ?-early_opcond <opcondName>? ?-early_opcond_library <libName>? ?-early_rc_corner rcCornerObj? ?-early_temp_file <tempName>? ?-irdrop_data <files_or_directories>? ?-irdrop_file <list_of_files>? ?-late_estimated_worst_irDrop_factor <percent>? ?-late_irdrop_data <files_or_directories>? ?-late_irdrop_file <list_of_files>? ?-late_library_set <libSetName>? ?-late_opcond <opcondName>? ?-late_opcond_library <libName>? ?-late_rc_corner <rcCornerObj>? ?-late_temp_file <tempName>? ?-library_set <libSetObj>? -name <delayCornerObj> ?-opcond <opcondName>? ?-opcond_library <libName>? ?-pg_net_voltages <voltage_pairs>? ?-power_domain <powerDomainName>? ?-rc_corner <rcCornerObj>? ?-si_enabled {true | false}? ?-supply_set <supplySetName>? ?-temp_file <tempName>?",
        ),
        # man1/update_floorplan_for_macro_place.1
        _syn(
            "update_floorplan_for_macro_place",
            "Enables you to update the floorplan before defining constraints for macros with the set_macro_place_constraint command",
            "update_floorplan_for_macro_place ?-help? ?-init_rows? ?-keep_fixed_insts {<inst1 inst2 ...>}? ?-remove {all route_blockage place_blockage relative_floorplan power_domain insts_place wire boundary_constraint physi‐ cal_inst drc PG_pin}?",
        ),
        # man1/update_glitch.1
        _syn(
            "update_glitch",
            "Allows you to run glitch analysis without running SI delay analysis",
            "update_glitch ?-help? ?-effort {medium | high}?",
        ),
        # man1/update_io_latency.1
        _syn(
            "update_io_latency",
            "Provides an automated means of balancing IO and Core clock latencies after the clock network has been added to the design so that pre and post clock tree skew between the clocks is maintained as closely as possible",
            "update_io_latency ?-source?",
        ),
        # man1/update_library_set.1
        _syn(
            "update_library_set",
            "Updates an existing specified library set",
            "update_library_set ?-help? ?-aocv <string>? ?-library_side_file <string>? -name <libSetName> ?-si <string>? ?-socv <string>? ?-timing <string>?",
        ),
        # man1/update_module_model.1
        _syn(
            "update_module_model",
            "Invokes an independent session in interactive or batch mode at top-level design",
            "update_module_model ?-help? ?-cpu <number_of_cpus>? ?-distribute_job? ?-eco_report? ?-log_dir <dir_name>? ?-return_tag <tag_name>? ?-return_type {lef flexIlm ilm pnr}? ?-tag <tag_name>? {?-distribute_run | -cell <cell_name>? ?-interactive | -plugin_tcl <tcl_commands> | -gen_eco_only?}",
        ),
        # man1/update_names.1
        _syn(
            "update_names",
            "Updates the inst, net, phys_insts, port, module, and design names at each level of hierarchy",
            "update_names ?-help? ?-allowed <chars>? ?-change_modules <hinsts_modules> ?-local?? ?-design? ?-first_restricted <chars>? ?-honor_dont_touch? ?-hport? ?-inst? ?-last_restricted <chars>? ?-log_file <string> ?-append_log?? ?-map {{<from to>}...}? ?-max_length <integer>? ?-module? ?-net? ?-nocase? ?-phys_inst? ?-port? ?-prefix <string >?-name_collision?? ?-quiet? ?-random ?-random_map_dir <out_dir>?? ?-regexp? ?-replace_string <string>? ?-reserved_words <string>? ?-restricted <string>? ?-suffix <string> ?-name_collision?? ?-system_verilog? ?-verilog? ?-vhdl?",
        ),
        # man1/update_oa_lib.1
        _syn(
            "update_oa_lib",
            "Updates the specified OpenAccess library from within Innovus",
            "update_oa_lib ?-help? <lib_name> ?-compress_level <value>? ?-create_cdsinfo_tag? ?-tech_attach_to_reference?",
        ),
        # man1/update_partition.1
        _syn(
            "update_partition",
            "Creates a new partitioned output that contains the optimised blocks and top",
            "update_partition ?-pinLocation? ?-postECOSuffix <postECOSuffix>? {-flexIlmECO} {-goldenBlockDir <directory>} -flexIlmDir <directory>?-ecoDir <directory>? ?-fullNetlistWithECODir <directory> -flexILMECODir <directory>?",
        ),
        # man1/update_rc_corner.1
        _syn(
            "update_rc_corner",
            "Adds or changes attribute values for the specified existing RC corner object",
            "update_rc_corner ?-T <temperatureValue>? ?-cap_table <newcapTableFile>? -name <existingRcCornerName> ?-postRoute_res {<resFactor1><resFactor2><resFactor3>}? ?-postRoute_cap {<capFactor1><capFactor2><capFactor3>}? ?-postRoute_xcap {<xcapFactor1><xcapFactor2><xcapFactor3>}? ?-postRoute_clkres {<resFactor1> <resFactor2> <resFactor3>}? ?-postRoute_clkcap {<capFactor1> <capFactor2> <capFactor3>}? ?-preRoute_clkres <resFactor>? ?-preRoute_clkcap <capFactor>? ?-preRoute_res <resFactor>? ?-preRoute_cap <capFactor>? ?-qx_tech_file <newFileName>? ?-via_variation_file <viaVariationFile>?",
        ),
        # man1/usf_version.1
        _syn(
            "usf_version",
            "Retrieves the version of the USF Physical being used to interpret the USF commands",
            "usf_version ?-help?",
        ),
        # man1/uu2dbu.1
        _syn(
            "uu2dbu",
            "Takes an arbitrary list of values and returns it in the same form, with each user unit floating point value con‐ verted to its database integer value equivalent",
            "uu2dbu ?help? <value> ?-unit {100 | 200 | 1000 | 2000 | 10000 | 20000}? ?-unit <number>? {<value> | {<value_list>}}",
        ),
        # man1/validate_pg_library.1
        _syn(
            "validate_pg_library",
            "Specifies to validate a macro PGV",
            "validate_pg_library ?-help? ?-activity <value>? -cell<cell_name>?-clock {<clk1> <clk2> ...}? ?-disable_rail_analysis {true | false}? ?-dynamic_analysis_duration <value>? ?-enable_xp {true | false}? ?-extraction_include_file <filename>? -extraction_tech_file <tech_file_path> ?-frequency <value>? ?-input_pin_set_case_analysis_low {<pin1> <pin2> ...}? ?-input_pin_set_case_analysis_high {<pin1> <pin2> ...}? ?-liberty <liberty_file>? ?-max_ir_drop <value>? ?-net_capacitance <value>? ?-output <output_dir>? ?-pin_capacitance <value>? -power_grid_library_path <pgv_path> ?-power_grid_library_view <view_name>? ?-power_pad_size <value>? ?-rail_analysis_type {static | dynamic}? ?-sdc_file <filename>? ?-set_power_switching_pattern <trigger_file>? ?-set_total_power <value>? ?-step_size <value>? ?-supply_voltage <value>? -tech_lef_file <tech_lef_file_path> ?-transition_time <time>? ?-power_include_file <filename>? ?-rail_include_file_begin <filename>? ?-rail_include_file_end <filename>? ?-rail_trigger_switching_pattern <pattern>? ?-temperature <value>? ?-twf_path <twf_location>? ?-user_defined_ploc_file<filename>? ?-pgv_mode_dynamic_switch_pattern <pattern?>",
        ),
        # man1/verify_antenna.1
        _syn(
            "verify_antenna",
            "Verifies the process antenna effect (PAE) in multi-thread mode with geometry-based check through the ad‐ vanced NanoRoute antenna checker feature",
            "verify_antenna ?-help? ?-detailed? ?-limit <integer>? ?-no_max_float_area? ?-nets {<netNames>} | -selected? ?-report <filename>? ?-use {all | signal | power | clock}?",
        ),
        # man1/verify_drc.1
        _syn(
            "verify_drc",
            "Checks for DRC violations and creates violation markers in the design database that can be seen on the GUI and browsed with the Violation Browser",
            "verify_drc ?-help? ?-area {{<lx1 ly1 ux1 uy1>} {<lx2 ly2 ux2 uy2>}...}? ?-check_illegal_trim_shapes? ?-check_ndr_spacing? ?-check_only {all | regular | special | selected_net | selected | cell | default}? ?-check_reverse? ?-check_routing_halo? ?-check_same_via_cell? ?-check_short_only? ?-check_trim_length? ?-check_uncolored? ?-enable_post_passive_fill_check? ?-exclude_pg_net? ?-ignore_fill_wire? ?-ignore_trial_route? ?-layer_range {layer1 ?layer2?}? ?-limit <max_error>? ?-report <filename>? ?-view_window?",
        ),
        # man1/verify_stacked_die.1
        _syn(
            "verify_stacked_die",
            "Checks die edge violation between adjacent dies",
            "verify_stacked_die ?-help? ?-check_type <type_name>? ?-chip_name {<chip1> <chip2> ...}?",
        ),
        # man1/verifyACLimit.1
        _syn(
            "verifyACLimit",
            "Checks for the following types of AC current violations on signal nets",
            "verifyACLimit ?-help?",
        ),
        # man1/verifyCMP.1
        _syn(
            "verifyCMP",
            "Runs Chemical and Mechanical Polishing (CMP) analysis at block level or chip level during the Sign-Off phase",
            "verifyCMP ?-help? ?-ccp_setup_file <string>? ?-cpu <integer>? ?-end_level <string>? ?-gdsList <string>? ?-mapFile <string>? ?-output_dir <string>? ?-pvs_fill? ?-runMode <string>? ?-start_level <string>? ?-tsmc_vcmp <string>? ?-tsmc_proc <string>? ?-vmp_files <string>? ?-vmp_name <string>?",
        ),
        # man1/verifyConnectivity.1
        _syn(
            "verifyConnectivity",
            "Detects conditions such as opens, unconnected wires (geometric antennas), unconnected pins, loops, partial routing, and unrouted nets; generates violation markers in the design window; reports violations",
            "verifyConnectivity ?-help? ?-allPGPinPort? ?-append? ?-connLoop | -geomLoop | -geomConnect? ?-dividePowerNet? ?-error <integer>? ?-ignorePGPin <cell_name>:<pin_name>? ?-markerOnHighestLayer? ?-net <netNames> | -selected? ?-noAntenna? ?-noFill? ?-noFloatingMetal? ?-noOpen? ?-noSoftPGConnect? ?-noUnConnPin? ?-noUnroutedNet? ?-noWeakConnect? ?-preferredTopLayer <integer> | -honorGroundLayerRange? ?-rawViolsMark? ?-removeOldOpenVio? ?-report <filename>? ?-tsv <abstractdiefilenames>? ?-type {all | special | regular}? ?-useNewOpenVio? ?-useVirtualConnection? ?-warning <value>?",
        ),
        # man1/verifyCutDensity.1
        _syn(
            "verifyCutDensity",
            "Checks the density of specified cut layers or areas of cut layers, or the cut density of the whole chip",
            "verifyCutDensity ?-area {<x1 y1 x2 y2>}? ?-detailed? ?-globalDensity? ?-ignoreCellBlock? ?-layer <layer_name_list>? ?-oversize <value>? ?-report <fileName>?",
        ),
        # man1/verifyEndCap.1
        _syn(
            "verifyEndCap",
            "Checks whether pre/post cap cells have been inserted correctly based on setEndCapMode settings",
            "verifyEndCap ?-help? ?-area {<x1 y1 x2 y2>}? ?-coreBoundaryOnly? ?-error <integer>? ?-ignore_macro <SCLA,...>? ?-powerDomain <string>? ?-report <filename>? ?-row <string>? ?-tripleWell? ?-wrongLocation?",
        ),
        # man1/verifyFlipChipRoutingConstraints.1
        _syn(
            "verifyFlipChipRoutingConstraints",
            "Reports the status of bump placement and routing contsraints",
            "verifyFlipChipRoutingConstraints ?-help? ?-routeStyle {manhattan | 45DegreeRoute}?",
        ),
        # man1/verifyIO2BumpConnectivity.1
        _syn(
            "verifyIO2BumpConnectivity",
            "Verifies multiBump multiPad connectivity",
            "verifyIO2BumpConnectivity ?-help? ?-error <integer>? ?-report <string>? ?-subclass <string>? ?-warning <integer>? ?-bump_connect_target | -class_bump? ?-bumps <string> | -class_bump? ?-bumps <string> | -nets <string>?",
        ),
        # man1/verifyIsolatedCut.1
        _syn(
            "verifyIsolatedCut",
            "Checks cuts in all or specified cut layers against the spacing rules set by setIsolatedCutRule",
            "verifyIsolatedCut ?-help? ?-area {<x1 y1 x2 y2>}? ?-error <integer>? ?-layer {<cutLayer_list>}? ?-maxXY? ?-report <filename>?",
        ),
        # man1/verifyLitho.1
        _syn(
            "verifyLitho",
            "Runs LPA on the selected design to flag litho hotspots",
            "verifyLitho ?-help? -apply {hotspot | ripandreroute | squishHints} ?-check_locally? ?-config <string>? ?-cpu <integer>? -dir <string> ?-gdsList <string>? ?-guideline? ?-hints_to_apply <string>? ?-incrCheck <string>? ?-layerMapFile <string>? ?-mapFile <string>? ?-noCompress? ?-oasis? ?-oasisList <string>? ?-optionFile string? ?-previousDir <string>? ?-reportFile <string>? {-routingLayersOnly | -signOff | -reportOnly | -loadBlockage} ?-runMode <string>? ?-streamOutOptions <string>? -techFile <string> ?-verify_function <string>?",
        ),
        # man1/verifyMetalDensity.1
        _syn(
            "verifyMetalDensity",
            "Checks the metal density of each routing layer and of macros against values specified by LEF file, or against its own internal default values",
            "verifyMetalDensity ?-help? ?-report filename? ?-detailed? ?-ignoreLEFDensity? ?-layer <layer_name_list>? ?-area {x1 y1 x2 y2}? ?-oversize value?",
        ),
        # man1/verifyPowerDomain.1
        #   WARNING: unclosed bracket '[' at position 156
        _syn(
            "verifyPowerDomain",
            "Verifies whether the power domains are set up correctly in terms of timing library binding and PG con‐ nection",
            "verifyPowerDomain ?-help? ?-allInstInPD? ?-aobBiasConn? ?-aoBufferType? ?-bind? ?-cell_bind {<cell ...>}? ?-drcFile <string>? ?-gconn ?<module_name_list>?? ?-isoNetPD ?<fileName>? ?-libBindingVoltage? ?-noFTermIsoC? ?-noFTermShifter? ?-place ?-place_rpt <report_name>?? ?-powerSwitch? ?-pwrWithinMinGap? ?-retention {<fileName ...>}? ?-xNetPD {<fileName>}?",
        ),
        # man1/verifyPowerSwitch.1
        _syn(
            "verifyPowerSwitch",
            "Verifies power switch placement and enable connections, including the row coverage for column inser‐ tion",
            "verifyPowerSwitch ?-help? ?-powerDomain <powerDomain>? ?-checkFloatingInput? ?-checkFloatingOutput? ?-checkFloating? ?-checkOverlap? ?-checkPlace? ?-checkLoop? ?-checkRowCoverage? ?-checkAll? ?-hilite? ?-reportFile? ?-reportLongestChain? ?-startingNet?",
        ),
        # man1/verifyPowerVia.1
        _syn(
            "verifyPowerVia",
            "This command provides a variety of power-rail overlap checks to look for missing power-grid vias",
            "verifyPowerVia ?-help? ?-append? ?-area {<x1> <y1> <x2> <y2>}? ?-checkWirePinOverlap? ?-edgeToEdge? ?-error <integer>? ?-exclude_region_file <check_file>? ?-fill? ?-hookup_pitch <pitch_value>? ?-ignore_objects {drc_fill | io_wire}? ?-ignore_partial_overlap {true | false | <value>}? ?-layerRange {<bottomLayer> <topLayer>}? ?-layer_rail <layer_name?> ?-layer_stripe <layer_list>? ?-net {<netNames>} | -selected? ?-nonOrthogonalCheck ?-distance {x y}?? ?-pitch <pitch_value>? ?-report <file>? ?-search_range {x y}? ?-shielding? ?-stackedVia? ?-stripe_rule <value>? ?-viaUtil <value>? ?-what_if_report <filename>? ?-widthRange<string>?",
        ),
        # man1/verifyTieCell.1
        _syn(
            "verifyTieCell",
            "Checks tie cell connections",
            "verifyTieCell ?-help? ?-noTieCell <filename>? ?-powerDomain <string>? ?-report <filename>?",
        ),
        # man1/verifyWellAntenna.1
        _syn(
            "verifyWellAntenna",
            "Checks for any CORE rows that have well-process-antenna violations",
            "verifyWellAntenna ?-help? ?-needToProtect {<cell_list>}? ?-changeToProtect {<cell_list>}? ?-changeToNotProtect {<cell_list>}? ?-report <filename> ?-detailed??",
        ),
        # man1/verifyWellTap.1
        _syn(
            "verifyWellTap",
            "Generates violation markers for missing well-tap cells and for well-tap cells that do not meet the rule specified for the distance between well-tap cells",
            "verifyWellTap ?-help? ?-area <x1 y1 x2 y2>? ?-avoidAbutment? ?-check <string>? ?-cell <list_of_well_tap_cells>? ?-fromEdge? ?-layer <layer_name>? ?-powerDomain <powerDomainName>? ?-report <filename>? ?-rule <distance>? ?-siteOffset <number_of_sites>? ?-wellCutCell <list_of_well_cut_cells>?",
        ),
        # man1/verifyWireGap.1
        _syn(
            "verifyWireGap",
            "Verifies the continuity of follow pin and stripes",
            "verifyWireGap ?-help? ?-append? ?-area {<x1 y1 x2 y2>}? ?-layers <layer_names>? ?-net <power_nets>? ?-report <filename>? ?-wireToBoundary ?-chip {<v1 v2>}? ?-core {<v1 v2>}? ?-block {<v1 v2>}? ?-powerdomain {<v1> <v2>}?? ?-wireToShape ?-ring <value>?? ?-wireToWire <value>?",
        ),
        # man1/view_dynamic_movie.1
        _syn(
            "view_dynamic_movie",
            "Provides the ability to view movies created during dynamic analysis",
            "view_dynamic_movie ?-help? ?-type ?ir|tc?? ?-movies_directory <dir>?",
        ),
        # man1/view_dynamic_waveform.1
        #   WARNING: unclosed bracket '[' at position 148
        _syn(
            "view_dynamic_waveform",
            "Provides the ability to view dynamic current or voltage waveforms generated during analysis",
            "view_dynamic_waveform ?-help? ?-type ?current | voltage | profile?? ?-waveform_files {<file1><file2> ... <fileN>}? ?-instance_name <instance_name>? ?-composite_waveform_type ?hierarchy | clock | clock_with_seq | total_current? ?-composite_waveform_name ?<hierarchy_name>| <clock_name>?? ?-power_db ?<powermeter>.db?? ?-effective_voltage_waveform? ?-free_data? ?-state_directory <directory_name>? ?-hier_block_file<filename>? ?-clear_hier?",
        ),
        # man1/view_package_results.1
        _syn(
            "view_package_results",
            "",
            "view_package_results ?-help? ?-result_file <<filename>>? -type <<package_analysis_type>> ?-workspace <<workspacename>>?",
        ),
        # man1/viewBumpConnection.1
        _syn(
            "viewBumpConnection",
            "Displays the connection as a flightline between a power/ground (PG) bump and a PG I/O pad, during signal bump assignment",
            "viewBumpConnection ?-help? ?-honor_color? ?-multiBumpsToPad? ?-multiPadsToBump? ?-remove? ???-net <net_list>? ?-bump <bump_list>? ?-io_inst <io_inst_list>? ?-selected??|??-bumpType {all | power | signal}? ?-tar‐ get {pad | ring}???",
        ),
        # man1/viewLast.1
        _syn(
            "viewLast",
            "Displays the last view window or the previous view",
            "viewLast ?-help?",
        ),
        # man1/viewLog.1
        _syn(
            "viewLog",
            "Opens up a log file in a separate console window for viewing within the Innovus",
            "viewLog ?-help? ?-file <logFileName>?",
        ),
        # man1/viewNext.1
        _syn(
            "viewNext",
            "Displays the next view window",
            "viewNext ?-help?",
        ),
        # man1/viewSnapshot.1
        _syn(
            "viewSnapshot",
            "Opens a window SnapShot Result for viewing saved snapshots",
            "viewSnapshot ?-help? -dir <string> ?-name <string>? ?-view <string>?",
        ),
        # man1/violationBrowser.1
        _syn(
            "violationBrowser",
            "Displays a list of violations in the design database",
            "violationBrowser ?-help? ?-aclimit? ?-all? ?-area {<x1 y1 x2 y2>}? ?-connectivity? ?-density? ?-displayByLayer? ?-geometry? ?-max_error_per_type <value>? ?-no_display_false? ?-overlap? ?-process_antenna? ?-search_desc? ?-short? ?-filter_query <LO_formula> | {-filter <filterString> -filter_mode {AND | OR | NOT}}?",
        ),
        # man1/violationBrowserDeleteByArea.1
        _syn(
            "violationBrowserDeleteByArea",
            "Deletes markers from a specified area or the entire design area",
            "violationBrowserDeleteByArea ?-help? ?-all? ?-area {<x1 y1 x2 y2}>?",
        ),
        # man1/violationBrowserReport.1
        _syn(
            "violationBrowserReport",
            "Reports violations flagged by the verification commands",
            "violationBrowserReport ?-help? ?-all? ?-aclimit? ?-connectivity? ?-density? ?-geometry? ?-max_error_per_type <integer?> ?-no_display_false? ?-overlap? ?-process_antenna? ?-short? ?-area {<x1 y1 x2 y2>}? ?-report <filename>? ?-filter <filterString>? ?-filter_mode {AND | OR | NOT}? ?-search_desc?",
        ),
        # man1/vPuts.1
        _syn(
            "vPuts",
            "Outputs information to the verbose log file (innovus.logv) and the standard output",
            "vPuts ?-help? ?<string>? ?-nonewline?",
        ),
        # man1/win.1
        _syn(
            "win",
            "Opens the Innovus main window",
            "win ?-help? ?on | off? Opens the Innovus main window. This is usually done after executing the command innovus -init <tclCommandFile>.",
        ),
        # man1/windowDeselect.1
        _syn(
            "windowDeselect",
            "Deselects all objects within the specified area",
            "windowDeselect ?-help? ?<ux1>? ?<uy1>? ?<ux2>? ?<uy2>?",
        ),
        # man1/windowSelect.1
        _syn(
            "windowSelect",
            "Selects all objects within the specified area",
            "windowSelect ?-help? <area>",
        ),
        # man1/windowToggleSelect.1
        _syn(
            "windowToggleSelect",
            "Toggles between selecting or deselecting objects that are enclosed by the area defined by the coordi‐ nates",
            "windowToggleSelect ?-help? <x1><y1><x2><y2>",
        ),
        # man1/wireload.1
        _syn(
            "wireload",
            "Generates the wireload models and outputs the models in hierarchical and flat formats",
            "wireload ?-help? ?-outfile <fileNamePrefix>? ?-scale <factor>? ?-percent <samplingRate>? ?-cell <cellName> | -inst <instanceName> ?-name <modelName>?? ?-instanceBased? ?-cellLimit <moduleSize>? ?-custom? ?-noSmooth? ?-netCoverRatio? ?-logarithmic? ?-peakCap? ?-view <viewName>?",
        ),
        # man1/write_category_summary.1
        _syn(
            "write_category_summary",
            "Writes a text file containing the following information",
            "write_category_summary ?-help? -report <string> ??-ascend | -descend? ?-byTNS | -byWNS?? ?-csv | {-no_frame_fix_width ?-no_split?}?",
        ),
        # man1/write_codesign_die_abstract.1
        _syn(
            "write_codesign_die_abstract",
            "Writes the abstract of current die to a file",
            "write_codesign_die_abstract ?-help?",
        ),
        # man1/write_design_stack_config.1
        _syn(
            "write_design_stack_config",
            "",
            "write_design_stack_config ?-help? {?-xml <StackedDieFileName>? ?-power_config_file <PowerConnectionFile>?}",
        ),
        # man1/write_do_lec.1
        _syn(
            "write_do_lec",
            "Writes out the dofile for the Conformal® Logical Equivalence Checker tool",
            "write_do_lec ?-help? ?-1801_golden <fileName>? ?-1801_revised <fileName>? ?-checkpoint <fileName>? ?-cpf_golden <fileName>? ?-cpf_revised <fileName>? ?-cw_sim <simulationLanguage>? ?-dft_constraint_file <fileName>? ?-env_var <envVariables>? ?-fastelab2gen? ?-fastgen2fvmap? ?-fastrtl2elab? ?-golden_design {rtl|fv_map|<file>}? ?-gzip_fv_json? ?-log_file <fileName>? ?-low_power_analysis? ?-no_dft? ?-no_exit? ?-no_insert_iso_in_dof? ?-no_lp? ?-pre_compare <fileName>? ?-pre_exit <fileName>? ?-pre_read <fileName>? ?-revised_design {fv_map|<file>}? ?-rtl_revised? ?-sim_lib <simulationLibrary>? ?-sim_plus_liberty? ?-smart? ?-tmp_dir <directoryName>? ?-top <designName>? ?-verbose? ?-write_session <fileName>? ?-hier | -flat? ?<output_filename> | >?",
        ),
        # man1/write_do_lec_innovus.1
        _syn(
            "write_do_lec_innovus",
            "Writes out the dofile for the Conformal® Logical Equivalence Checker tool",
            "write_do_lec_innovus ?-help? <output_filename> ?-checkpoint <lec_checkpoint_file>? ?-golden_design <filename>? ?-log_file <filename>? ?-no_exit? ?-pre_compare <filename>? ?-pre_exit <filename>? ?-pre_read <filename>? ?-revised_design <filename>? ?-verbose? ?-write_session <lec_session_name>? {-hier | -flat } > <output_filename>",
        ),
        # man1/write_extraction_spec.1
        _syn(
            "write_extraction_spec",
            "Creates the Quantus command file or the Common Command Language (CCL) file in the current working directory and saves the design data for running standalone Quantus",
            "write_extraction_spec ?-help? ?-no_design_data? ?-out_dir {dir_name}? ?-rc_corners {<list_of_rc_corners>}?",
        ),
        # man1/write_generalized_feedthru_paths.1
        _syn(
            "write_generalized_feedthru_paths",
            "Automatically derives feedthrough topological paths from the user specified paths to cover all the chain connectivity probabilities in a master and clone hinst scenario",
            "write_generalized_feedthru_paths ?-help? ?-dont_generalize_reverse_paths? ?-dont_generalize_sub_paths? ?-topological_out_file <file_name>? -use_topological_file <file_name>",
        ),
        # man1/write_global_slack_report.1
        _syn(
            "write_global_slack_report",
            "Reports early and late slacks on every instance pin in the design",
            "write_global_slack_report ?-early? ?-late? ?-rise? ?-fall? ?-include_ports? ?-max_slack <val>? ?-min_slack <val>? ?-view <view_name>? ?> | >> <file_name>? ?<pin_port_list>?",
        ),
        # man1/write_global_slack_worst_trigger_path_on_clocks.1
        _syn(
            "write_global_slack_worst_trigger_path_on_clocks",
            "",
            "write_global_slack_worst_trigger_path_on_clocks {true | false}",
        ),
        # man1/write_ilm_eco_db.1
        #   WARNING: unmatched closing bracket ']' at position 40
        _syn(
            "write_ilm_eco_db",
            "",
            "write_ilm_eco_db ?-help? -cell <tcl_obj>? {-dir <directoryName> | -module_model_tag <tagName>}",
        ),
        # man1/write_instance_obs.1
        _syn(
            "write_instance_obs",
            "Saves all the instance obstruction shapes of the specified layer in an output file",
            "write_instance_obs ?-help? <output_file>?-layer <layer_name>? ?-with_outer_shape?",
        ),
        # man1/write_ldb.1
        _syn(
            "write_ldb",
            "Converts text library to Cadence binary format library called LDB",
            "write_ldb -library <string >< > -outfile <string >< >",
        ),
        # man1/write_lec_dft_constraints.1
        _syn(
            "write_lec_dft_constraints",
            "",
            "write_lec_dft_constraints <dictionary>",
        ),
        # man1/write_lec_directory_naming_style.1
        _syn(
            "write_lec_directory_naming_style",
            "",
            "write_lec_directory_naming_style <directory_name>",
        ),
        # man1/write_lec_files.1
        _syn(
            "write_lec_files",
            "",
            "write_lec_files {true | false}",
        ),
        # man1/write_lef_abstract.1
        _syn(
            "write_lef_abstract",
            "Generates design abstract (LEF) information for the current routed block-level design",
            "write_lef_abstract ?-help? <fileName> ?-add_obs_layers <layer_list>? ?-cutObsMinSpacing? ?-cutObsToExposeRouting <distance_in_microns>? ?-excludeObsLayers <layer_list>? ?-excludePinLayers <layer_list>? ?-design_boundary <point_list>? ?-extractBlockObs? ?-extractBlockPGPinLayers <layer_number_list>? ?-extractBlockSignalPinLayers <layer_list>? ?-extractWellLayerObs <well_layer_list >?-extractWellObsByRow <margin>?? ?-ignoreBumpOnPin {all pg signal}? ?-ioPadPin? ?-noCutObs? ?-property? ?-extractWellLayerObs <well_layer_list> ?-mergeConnectedWellOnly?? ?-obsSpacing {<val> <layers> ?<val2> <layers> ...?}< >?-obsSpacingPerLayer?? ?-specifyTopLayer <layer_number >?-obs_above_top_layer <layer>+?? ?-stripePin ?-selected?? ?-stripePin ?-portForEachStripePin?? ?-stripePin ?-PGPinLayers <layer_number_list>?? ?-stripePin ?-PGNets <net>+?? ?-5.6 | -5.7 | -5.8?",
        ),
        # man1/write_lef_library.1
        _syn(
            "write_lef_library",
            "The write_lef_library command facilitates comparisons between LEF-based input and OpenAccess-based in‐ put",
            "write_lef_library ?-help? ?<filename>? ?-all_auto_generated_via | -macro_only? ?-lef_layer_order? ?-macro_only ?-no_property?? ?-tech_only | -macro_only? ?-tech_only | -macro_list <string>? ?-use_spacing_table_default?",
        ),
        # man1/write_macro_place_constraint.1
        _syn(
            "write_macro_place_constraint",
            "Enables you to write constraints into a TCL format file from the database",
            "write_macro_place_constraint ?-help? ?-cpg_scope {selected macro_only all}? -out_file <string> ?-sections {array basic cpg pg_model_over_macros pg_resource_model}?",
        ),
        # man1/write_ml_design.1
        _syn(
            "write_ml_design",
            "Writes design-related data for JedAI to csv files with specified prefix",
            "write_ml_design ?-help? ?-no_power? ?-objects <object_list>? -prefix <string> ?-verbose? ?-views <view_list>?",
        ),
        # man1/write_ml_library.1
        _syn(
            "write_ml_library",
            "Writes library-related data for JedAI to csv files with the specified prefix",
            "write_ml_library ?-help? ?-objects <object_list>? -prefix <string>",
        ),
        # man1/write_ml_timing_graph.1
        _syn(
            "write_ml_timing_graph",
            "Writes timing-related data for JedAI to csv files",
            "write_ml_timing_graph ?-help? ?-noedge? -prefix <string> ?-register_only? ?-views <view_list>?",
        ),
        # man1/write_ml_timing_path.1
        _syn(
            "write_ml_timing_path",
            "Writes timing-related data for JedAI to csv files",
            "write_ml_timing_path ?-help? ?-anchor_file <string>? ?-begin_end_pair? ?-chain_levels <int>? ?-chain_path? ?-each_endpoint? ?-from <pin_list>? ?-gen_anchor? ?-hpin? ?-io_only? ?-max_paths <int>? ?-max_slack <float>? ?-nworst <int>? ?-partitions <partition_list>? ?-path_group <string>? ?-per_partition? -prefix <string> ?-retime {aocv ssta path_slew_propagation aocv_path_slew_propagation}? ?-retime_mode {path exhaustive}? ?-start_pathid <int>? ?-to <pin_list>? ?-verbose? ?-views <view_list>?",
        ),
        # man1/write_model_timing.1
        _syn(
            "write_model_timing",
            "Writes the interface timing characteristics of the design in the specified timing model report file",
            "write_model_timing ?-help? ?<model_timing_report_file>? ?-inputs <string>? ?-nworst <integer>? ?-outputs <string>? ?-slew_propagation {worst | path_based}? ?-type {arc | slack}? ?-verbose? ?-view <string>? -setup <string> | -hold <string>",
        ),
        # man1/write_module_model_context.1
        _syn(
            "write_module_model_context",
            "Creates a context model for a specific cell or a master/clone instance",
            "write_module_model_context ?-help? {-cell <cellName> | -master_clone_inst <master_clone_inst>} ?–tag t<ag_name>? ?-type {extraction_context timing_context}? ?-type_specific_options <type_specific_options>?",
        ),
        # man1/write_name_mapping.1
        _syn(
            "write_name_mapping",
            "Writes or updates the initial netlist key point names and corresponding current netlist key point names to a file",
            "write_name_mapping ?-help? ?-bbox_pins? ?-hierarchical? ?-map_pins {input output all}? ?-pin_polarity? ?-enable_one_to_one_mapping |-report_power_format? ?-skip_clock_gate? ?-updated_only? {<output_filename> | ??-output <output_directory>? -prefix <filename_prefix>?} ?-hdl | -initial | ?-input_mapping_file <mapping_file >?-print_deleted??-include_new_iterms???",
        ),
        # man1/write_net_groups_topo.1
        _syn(
            "write_net_groups_topo",
            "Creates a topological file (used by the insertPtnFeedthrough command) for nets of the net group associated with a bus guide",
            "write_net_groups_topo ?-help? ?-net_groups <list_of_net_groups>? ?-outFile <file_name>?",
        ),
        # man1/write_oa_techfile.1
        _syn(
            "write_oa_techfile",
            "",
            "write_oa_techfile ?-help? ?<fileName>? ?-include_rules? ?-process_node <coord>?",
        ),
        # man1/write_path_descriptions.1
        _syn(
            "write_path_descriptions",
            "Writes out the path descriptions of all the timing paths specified in the variable (path collec‐ tion) to an ASCII file",
            "write_path_descriptions ?-help?",
        ),
        # man1/write_path_list_summary.1
        _syn(
            "write_path_list_summary",
            "Writes the Path List categorized summary into a text and/or CSV file",
            "write_path_list_summary ?-help? ?-category <string>? ?-compress? ?-csv? -report <fileName>",
        ),
        # man1/write_physical_context_data.1
        _syn(
            "write_physical_context_data",
            "Writes the physical context data needed for timing analysis",
            "write_physical_context_data ?-help? <fileName> ?-designation <name>? ?-type <technologyName>?",
        ),
        # man1/write_power_constraints.1
        _syn(
            "write_power_constraints",
            "Writes out all the power constraints such as the power analysis mode, activity file specifica‐ tions, simulation period specifications, and so on, into a file",
            "write_power_constraints ?-help? ?-outfile <filename>?",
        ),
        # man1/write_power_intent.1
        _syn(
            "write_power_intent",
            "Writes the CPF/IEEE1801 file",
            "write_power_intent ?-help? <fileName>{-cpf ??-hierInst –topHier? | ?-inst?? | -1801 | -incremental_1801} ?-no_extra_connects?",
        ),
        # man1/write_sdf.1
        _syn(
            "write_sdf",
            "Writes delays to a Standard Delay Format (SDF) file",
            "write_sdf ?-help? <file_name> ?-abstracted_model? ?-adjust_setuphold_for_zero_hold_slack? ?-base_delay? ?-celltiming {all | none | nochecks}? ?-collapse_internal_pins? ?-condelse? ?-delimiter <char>? ?-delta_delay? ?-edges {edged | library | noedge | check_edge}? ?-exclude_cells <cell_list>? ?-exclude_cells_keep_io_nets? ?-exclude_cells_keep_top_level_nets? ?-exclude_disabled_arcs? ?-exclude_disabled_modes? ?-exclude_whatif_arcs? ?-filter? ?-ideal_clock_network? ?-include_variation? ?-interconn {all | none | noport | noinport | nooutport}? ?-map_file {file1 file2 ...}? ?-max_view <viewName>? ?-merge_arcs? ?-min_period_edges {posedge | negedge | both | none}? ?-min_view <viewName>? ?-no_condition? ?-no_derate? ?-no_escape? ?-nonegchecks? ?-precision <non_neg_integer>? ?-process <string>? ?-recompute_delay_calc? ?-recompute_parallel_arcs? ?-recrem {merge_always | split | merge_when_paired}? ?-remashold? ?-resort_values_min_to_max? ?-scale <float>? ?-setuphold {merge_always | split | merge_when_paired}? ?-splitrecrem? ?-splitsetuphold? ?-target_application {sta | verilog}? ?-temperature <string>? ?-timingcheck {order}? ?-transform_out_to_out_arcs? ?-typ_view <viewName>? ?-version {2.1 3.0}? ?-view <viewName>? ?-voltage <string>?",
        ),
        # man1/write_spd.1
        _syn(
            "write_spd",
            "Dumps the SPD file based on the user-selected signals with corresponding shielding and PG shapes directly",
            "write_spd ?-help? -file <spdFileName> ?{-nets <netName(s)> | -selected } ?-cut_margin <cutMargin>? ?-with_shield??",
        ),
        # man1/write_tcf.1
        _syn(
            "write_tcf",
            "Writes out the propagated switching activity information to a toggle count format (TCF) file",
            "write_tcf <file> ?-block <block_name>? ?-exclude_hier_insts <list_of_instances>? ?-primary_input? ?-seq_output? ?-pin? ?-macro_output?",
        ),
        # man1/write_text_timing_report.1
        _syn(
            "write_text_timing_report",
            "Writes a text file containing information about paths that have been loaded from a .mtarpt file from Timing Debug, either with the load_timing_debug_report command or in the Display/Generate Timing Report form in the GUI",
            "write_text_timing_report ?-help? ?-mtarpt file.mtarpt | -category category_name? ?-format{{<column1 width1>} {<column2 width2>} ...}? ?-path_specification <path_specification>? ?-summary? -report <file.tarpt>",
        ),
        # man1/write_timing_windows.1
        _syn(
            "write_timing_windows",
            "Generates a timing window file (TWF)",
            "write_timing_windows ?-help? ?-pin? ?-power_compatible? ?-view <string>? ?-ssta_sigma_multiplier <float>? ?-voltage_threshold <string>? <output_file>",
        ),
        # man1/write_usf.1
        _syn(
            "write_usf",
            "Writes the safety intent of your design to the specified Unified Safety Format (USF) file",
            "write_usf ?-help? <USF_file>",
        ),
        # man1/writeAnnotatedTransition.1
        _syn(
            "writeAnnotatedTransition",
            "Writes the value of transitions on each pin to an output file",
            "writeAnnotatedTransition ?-help? -file <out_file> ?-min | -max? ?-writeOutput? ?-direct? ?-noPort? ?-view <view_name>?",
        ),
        # man1/writeBumpLocation.1
        _syn(
            "writeBumpLocation",
            "Writes the bump information to a file",
            "writeBumpLocation <fileName> ?-selected?",
        ),
        # man1/writeDesignTiming.1
        _syn(
            "writeDesignTiming",
            "Writes out the timing information of the design",
            "writeDesignTiming <filename>",
        ),
        # man1/writeDieAbstract.1
        _syn(
            "writeDieAbstract",
            "Writes the abstract of current die to a file",
            "writeDieAbstract <DIEABSTRACTFILE> ?-noFilter?",
        ),
        # man1/writeFlipChipProperty.1
        _syn(
            "writeFlipChipProperty",
            "Saves the bump and pad properties in the bump and IO pad property file",
            "writeFlipChipProperty ?-help? <fileName>",
        ),
        # man1/writeFlowTemplate.1
        _syn(
            "writeFlowTemplate",
            "Copies the Innovus Foundation flows templates into the directory you specify, or to the current direc‐ tory if you do not specify one with the -directory parameter",
            "writeFlowTemplate",
        ),
        # man1/writeFPlanScript.1
        _syn(
            "writeFPlanScript",
            "Allows you to write out the specified floorplan sections and source the output file after init_design",
            "writeFPlanScript ?-help? ?-appendToFile? ?-compactRow? -fileName <fileName> ?-no_snap_to_grid? ?-selected | -sections {boundary row placeBlockages routeBlockages pinBlockages groups constraints pins ioPad areaIO bump partitions blocks globalNetConnect busSinkGroups blackboxes netGroupAndBusGuide relativefplan pinGroups pinGuides cus‐ tomShape coverCell}?",
        ),
        # man1/writeHif.1
        _syn(
            "writeHif",
            "Writes out a HIF file after the NanoRoute router fixes lithography problems",
            "writeHif ?-help? -file <filename>",
        ),
        # man1/writeIntegRouteConstraint.1
        _syn(
            "writeIntegRouteConstraint",
            "Writes the constraints to an output file in the following order: diffPair, matchLength, bus, netClass, NDR, shield, and additional",
            "writeIntegRouteConstraint ?-help? -file <output_file> ?-net <net_name> | -name <string> | -additional?",
        ),
        # man1/writeLefAbstractCustomerHeader.1
        _syn(
            "writeLefAbstractCustomerHeader",
            "",
            "writeLefAbstractCustomerHeader <header_information>",
        ),
        # man1/writeMicroBumpMappingFile.1
        _syn(
            "writeMicroBumpMappingFile",
            "Writes the micro bump mapping file for Quantus and Voltus use",
            "writeMicroBumpMappingFile ?-help? <fileName>?-mergeWith {<filename1 filename2 ...>}?",
        ),
        # man1/writeSdpFile.1
        _syn(
            "writeSdpFile",
            "Saves the current SDP relative placement information into a file",
            "writeSdpFile ?-help? -file <file_name> ?-template | -topGroup <group_name>? ?-template | -command? ?-template | ?-updateRelativePlaceConstraint | -updateOrientation??",
        ),
        # man1/writeSetLoad.1
        _syn(
            "writeSetLoad",
            "Writes the capacitive loading on each net to an output file",
            "writeSetLoad ?-help? ?-direct? ?-excludeZeroCap? ?-includePinCap? ?-wire_load? ?-view <viewName>? -file <outFile>",
        ),
        # man1/writeTimingCon.1
        _syn(
            "writeTimingCon",
            "Generates the timing constraints file in Design Compiler format",
            "writeTimingCon ?-help? ?<<filename>>? ?-clocks <<string>>? ?-commands <<string>>? ?-exclude_annotated {delays | checks | transitions}? ?-pins <<string>>? ?-view <<viewName>>?",
        ),
        # man1/writeVSMappingFile.1
        _syn(
            "writeVSMappingFile",
            "Writes out a bump mapping file for Voltage Storm use",
            "writeVSMappingFile <fileName>",
        ),
        # man1/zoomBox.1
        _syn(
            "zoomBox",
            "Zooms in the viewable window to the area that encloses the specified coordinates",
            "zoomBox ?-help? <area>",
        ),
        # man1/zoomIn.1
        _syn(
            "zoomIn",
            "Zooms in the viewable window",
            "zoomIn ?-help?",
        ),
        # man1/zoomOut.1
        _syn(
            "zoomOut",
            "Zooms out from the viewable window by two times",
            "zoomOut ?-help?",
        ),
        # man1/zoomSelected.1
        _syn(
            "zoomSelected",
            "Zooms in the viewable window to the area that encloses the selected objects",
            "zoomSelected ?-help? ?-margin <value>?",
        ),
        # man1/zoomTo.1
        _syn(
            "zoomTo",
            "Zooms in the viewable window to the point defined by the coordinates with a default radius of 150 microns",
            "zoomTo ?-help?",
        ),
    )
