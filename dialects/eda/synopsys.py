"""Synopsys EDA Tcl commands — Design Compiler, PrimeTime, ICC2, Formality.

Vendor-specific commands for the ``synopsys-eda-tcl`` dialect.
SDC base commands are provided separately by ``eda_sdc_base``.
"""

from __future__ import annotations

from compiler.registry.models import CommandSpec, FormKind, FormSpec, HoverSnippet, ValidationSpec
from compiler.registry.signatures import Arity

_SOURCE = "Synopsys Design Compiler / PrimeTime / ICC2"
_DIALECT = frozenset({"synopsys-eda-tcl"})


def _syn(    name: str,
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


def synopsys_command_specs() -> tuple[CommandSpec, ...]:
    """Return Synopsys-specific command specs."""
    return (
        # cat2/acs_get_parent_partition.2
        _syn(            "acs_get_parent_partition",
            "Creates a collection of designs that are compiled partitions containing the specified subdesign.",
            "acs_get_parent_partition design_name ?-hierarchy? ?-list?",
        ),
        # cat2/acs_read_hdl.2
        _syn(            "acs_read_hdl",
            "Reads in the HDL source code of a design and generates the GTECH representation.",
            "acs_read_hdl ?design_name? ?-hdl_source file_or_dir_list? ?-exclude_list file_or_dir_list? ?-format {verilog | vhdl}? ?-recurse? ?-no_dependency_check? ?-no_elaborate? ?-library design_lib_name? ?-verbose? ?-auto_update | -update file_list? ?-destination destination_dir? ?-sv_package_files file_list?",
        ),
        # cat2/acs_report_user_messages.2
        _syn(            "acs_report_user_messages",
            "Reports the number of error, warning, and information messages.",
            "acs_report_user_messages ?-total? ?-errors? ?-warnings? ?-infos? ?-reset?",
        ),
        # cat2/add_command_hook.2
        _syn(            "add_command_hook",
            "Add hook into command execution",
            "add_command_hook -before script -after script -replace script ?-name name? commandName",
        ),
        # cat2/add_module.2
        _syn(            "add_module",
            "Reads in a specified library file containing module functional information and uses it to update an existing technology library.",
            "add_module ?-overwrite? ?-force? ?-permanent? file_name library_name ?-no_warnings?",
        ),
        # cat2/add_parameter.2
        _syn(            "add_parameter",
            "Define parameters that can be overridden by apply_power_model.",
            "add_parameter parameter_name ?-default default_value? ?-type type_name? ?-description description text?",
        ),
        # cat2/add_pg_pin_to_db.2
        _syn(            "add_pg_pin_to_db",
            "Converts a non-PG-pin-based logic library in compiled format (.db file) into a PG-pin-based logic library in .db format.",
            "add_pg_pin_to_db input_db_filename -output pg_db_filename ?-mw_library_name mw_lib_name? ?-pg_map_file map_file? ?-pg_map_template template_filename? ?-expanded? ?-fast? ?-force_update? ?-verbose?",
        ),
        # cat2/add_pg_pin_to_lib.2
        _syn(            "add_pg_pin_to_lib",
            "Converts a non-PG-pin based logic library in Liberty format (.lib file) into a PG-pin-based logic library in .lib format.",
            "add_pg_pin_to_lib input_lib_filename -output pg_lib_filename ?-mw_library_name mw_lib_name? ?-pg_map_file map_file? ?-pg_map_template template_filename? ?-common_shell_path common_shell_path? ?-expanded? ?-fast? ?-force_update? ?-verbose?",
        ),
        # cat2/add_port_state.2
        _syn(            "add_port_state",
            "Adds state information to a supply port.",
            "add_port_state supply_port_name -state {state_name state_value}",
        ),
        # cat2/add_power_state.2
        _syn(            "add_power_state",
            "Adds state information to a supply set or a group or a domain.",
            "add_power_state ?-supply | -group | -domain? object_name ?-simstate {simstate}? ?-update? ?-state state_name {?-supply_expr {supply_expression}? ?-logic_expr {logic_expression}? ?-simstate {simstate}? ?-illegal?}?*",
        ),
        # cat2/add_pst_state.2
        _syn(            "add_pst_state",
            "Defines the states of each of the supply nets for one possible state of the design.",
            "add_pst_state state_name -pst table_name -state supply_states",
        ),
        # cat2/add_row.2
        _syn(            "add_row",
            "Creates a list of rows in the design.",
            "add_row -within {coordinates} ?-direction horizontal | vertical? ?-flip_first_row? ?-no_double_back? ?-minimal_channel_height channel_height? ?-no_start_from_first_row? ?-tile_name tile_name? ?-snap_to_row_direction {wire_track | tile_width | none}? ?-snap_to_orthogonal_row_direction {existing_row | wire_track | none}? ?-left_offset left_offset? ?-right_offset right_offset? ?-top_offset top_offset? ?-bottom_offset bottom_offset? ?-allow_overlap?",
        ),
        # cat2/add_state_transition.2
        #   WARNING: unmatched closing bracket '}' at position 115
        #   WARNING: unmatched closing bracket ']' at position 116
        _syn(            "add_state_transition",
            "Adds state transitions to an existing UPF object.",
            "add_state_transition ?-supply | -domain | -group?object_name ?-update? ?-transition transition_name {through_list}?}?* ?-complete?",
        ),
        # cat2/add_supply_state.2
        _syn(            "add_supply_state",
            "Adds state information to a supply object.",
            "add_supply_state supply_name -state {state_name state_value}",
        ),
        # cat2/add_to_collection.2
        _syn(            "add_to_collection",
            "Adds objects to a collection, resulting in a new collection. The base collection remains unchanged.",
            "add_to_collection ?-unique? collection1 object_spec",
        ),
        # cat2/add_to_rp_group.2
        _syn(            "add_to_rp_group",
            "Adds a cell, hierarchical group, or keepout to an existing relative placement group.",
            "add_to_rp_group rp_groups -leaf cell_names ?-column integer? ?-row integer? ?-pin_align_name pin_name? ?-orientation direction? ?-alignment bottom-left | bottom-right? ?-num_rows integer? ?-num_columns integer? ?-free_placement?",
        ),
        # cat2/alias.2
        _syn(            "alias",
            "Creates a pseudo-command that expands to one or more words, or lists current alias definitions.",
            "alias ?name? ?def?",
        ),
        # cat2/alib_analyze_libs.2
        _syn(            "alib_analyze_libs",
            "Reads in the target library files, analyzes each of them separately, and creates the corresponding alib files.",
            "alib_analyze_libs",
        ),
        # cat2/all_active_scenarios.2
        _syn(            "all_active_scenarios",
            "Lists the active scenarios available in memory.",
            "all_active_scenarios",
        ),
        # cat2/all_clock_gates.2
        _syn(            "all_clock_gates",
            "Returns a collection of clock-gating cells or pins in the current design.",
            "all_clock_gates ?-no_hierarchy? ?-clock clock_name? ?-cells? ?-enable_pins? ?-clock_pins? ?-output_pins? ?-test_pins? ?-observation_pins? ?-origin origin?",
        ),
        # cat2/all_connected.2
        _syn(            "all_connected",
            "Returns the objects connected to a net, port, pin, net instance, or pin instance.",
            "all_connected ?-leaf? object",
        ),
        # cat2/all_critical_cells.2
        _syn(            "all_critical_cells",
            "Returns a collection of critical leaf cells in the top hierarchy of the current design.",
            "all_critical_cells ?-slack_range range_value?",
        ),
        # cat2/all_critical_pins.2
        _syn(            "all_critical_pins",
            "Returns a collection of critical endpoints or startpoints in the current design.",
            "all_critical_pins ?-type endpoint | startpoint? ?-slack_range range_value?",
        ),
        # cat2/all_designs.2
        _syn(            "all_designs",
            "Returns a collection containing all designs in the current design.",
            "all_designs",
        ),
        # cat2/all_dont_touch.2
        _syn(            "all_dont_touch",
            "Returns a collection of dont_touch cells or nets from the current design or from the specified input collection.",
            "all_dont_touch -cells | -nets ?input_coll?",
        ),
        # cat2/all_drc_violated_nets.2
        _syn(            "all_drc_violated_nets",
            "Returns a collection of DRC-violated nets from the current design or from the specified input collection.",
            "all_drc_violated_nets -max_capacitance | -max_transition | -max_fanout ?input_coll? ?-bound upper? ?-threshold threshold?",
        ),
        # cat2/all_high_fanout.2
        _syn(            "all_high_fanout",
            "Returns a collection of high-fanout nets from the current design or from the specified input collection. Constant high fanout nets, i.e., logic 1 and logic 0, are excluded from the returned collection.",
            "all_high_fanout -nets ?-threshold value? ?input_coll? ?-through_buf_inv?",
        ),
        # cat2/all_ideal_nets.2
        _syn(            "all_ideal_nets",
            "Returns a collection of ideal nets from the current design or from the specified input collection.",
            "all_ideal_nets ?input_coll?",
        ),
        # cat2/all_isolation_cells.2
        _syn(            "all_isolation_cells",
            "Returns a collection of isolation cells available in the design.",
            "all_isolation_cells",
        ),
        # cat2/all_level_shifters.2
        _syn(            "all_level_shifters",
            "Returns a collection of level-shifter cells available in the design.",
            "all_level_shifters ?-type els | simple?",
        ),
        # cat2/all_macro_cells.2
        _syn(            "all_macro_cells",
            "Returns a collection of all macro cells in the design or from a list of objects in the input collection.",
            "all_macro_cells ?input_coll?",
        ),
        # cat2/all_physical_only_cells.2
        _syn(            "all_physical_only_cells",
            "Returns a collection of all the physical-only cells from a design or from a list of objects in an input collection.",
            "all_physical_only_cells ?-lib_cells lib_list | -cell_name list? ?-coordinates {llx lly urx ury}? ?input_coll_handle?",
        ),
        # cat2/all_rp_groups.2
        _syn(            "all_rp_groups",
            "Returns a collection of specified relative placement groups and all groups in their hierarchy.",
            "all_rp_groups ?rp_groups?",
        ),
        # cat2/all_rp_hierarchicals.2
        _syn(            "all_rp_hierarchicals",
            "Returns a collection of hierarchical relative placement groups that contain the specified groups in their hierarchy. The specified groups can be either included or instantiated in their parent group.",
            "all_rp_hierarchicals ?rp_groups?",
        ),
        # cat2/all_rp_inclusions.2
        _syn(            "all_rp_inclusions",
            "Returns a collection that contains the hierarchical relative placement groups that include the specified groups.",
            "all_rp_inclusions ?rp_groups?",
        ),
        # cat2/all_rp_instantiations.2
        _syn(            "all_rp_instantiations",
            "Returns a collection of hierarchical relative placement groups that instantiate the specified groups.",
            "all_rp_instantiations ?rp_groups?",
        ),
        # cat2/all_rp_references.2
        _syn(            "all_rp_references",
            "Returns a collection of relative placement groups that directly contain the specified cells, which are either leaf cells or hierarchical cells that contain instantiated relative placement groups.",
            "all_rp_references ?cell_list? ?-design design_name?",
        ),
        # cat2/all_scenarios.2
        _syn(            "all_scenarios",
            "Lists all defined scenarios available in memory.",
            "all_scenarios",
        ),
        # cat2/all_self_gates.2
        _syn(            "all_self_gates",
            "Returns a collection of self-gating cells or pins in the current design. This command is supported only in topographical mode.",
            "all_self_gates ?-no_hierarchy? ?-clock clock_name? ?-cells? ?-enable_pins? ?-clock_pins? ?-output_pins? ?-test_pins?",
        ),
        # cat2/all_test_modes.2
        _syn(            "all_test_modes",
            "Displays all of the test modes that are defined for the current design.",
            "all_test_modes",
        ),
        # cat2/all_threestate.2
        _syn(            "all_threestate",
            "Returns a collection of three-state cells or nets.",
            "all_threestate -nets ?input_coll?",
        ),
        # cat2/all_tieoff_cells.2
        _syn(            "all_tieoff_cells",
            "Returns a collection of all tie-off cells in the current design or in the input collection.",
            "all_tieoff_cells ?input_coll?",
        ),
        # cat2/all_upf_repeater_cells.2
        _syn(            "all_upf_repeater_cells",
            "Returns a collection of repeater cells available in the design by virtue of the UPF repeater-supply port attribute.",
            "all_upf_repeater_cells",
        ),
        # cat2/analyze.2
        _syn(            "analyze",
            "Analyzes the specified HDL source files and stores the resulting templates into the specified library in a format ready to specialize and elaborate to form linkable cells of a full design.",
            "analyze ?-format verilog | sverilog | vhdl? ?-define define_list? ?-library library_name | -work library_name? ?-uses design_libs_list? ?-vcs vcs_opts? ?-create_update? ?-update? ?-recursive? ?-autoread? ?-rebuild? ?-output_script output_string? ?-exclude exclude_list? ?-verbose? ?-top top_design_name? file_list",
        ),
        # cat2/analyze_datapath.2
        _syn(            "analyze_datapath",
            "Provides a datapath analysis report that lists the resources and datapath blocks used in the current design.",
            "analyze_datapath ?-file file_name?",
        ),
        # cat2/analyze_datapath_extraction.2
        _syn(            "analyze_datapath_extraction",
            "Analyzes DesignWare datapath extraction.",
            "analyze_datapath_extraction ?-no_autoungroup? ?-no_report? ?-filter_msg none | low | medium? ?-sort_msg? ?-max_msgs max_num_msgs? ?-html_file_name html_file? ?design_list?",
        ),
        # cat2/analyze_dw_power.2
        _syn(            "analyze_dw_power",
            "Reports the DesignWare delay and power contribution.",
            "analyze_dw_power ?-nosplit? ?-hierarchy? ?-sort slack | dyn_pwr | lkg_pwr? ?-sort_ascending?",
        ),
        # cat2/analyze_minpwr_library.2
        _syn(            "analyze_minpwr_library",
            "Displays function, drive strength, area and power characteristics of cells from a target library used in datapath generation.",
            "analyze_minpwr_library ?-legend? ?library_list?",
        ),
        # cat2/analyze_mv_design.2
        _syn(            "analyze_mv_design",
            "Analyzes multivoltage design connections.",
            "analyze_mv_design ?-level_shifter | -always_on | -lib_cells? ?-from_pin from_pin_list? ?-to_pin to_pin_list? ?-net target_net? ?-isolation? ?-enable_level_shifter? ?-retention? ?-verbose? ?-voltage_type all | nominal?",
        ),
        # cat2/analyze_mv_feasibility.2
        _syn(            "analyze_mv_feasibility",
            "Analyzes multivoltage feasibility of current design.",
            "analyze_mv_feasibility ?-lib_cells? ?-resolved_strategy? ?-isolation? ?-enable_level_shifter? ?-level_shifter? ?-repeater? ?-retention? ?-format output_format? ?-domain domain_name? ?-strategy strategy_name? ?-elements objects? ?-disable_clubbing?",
        ),
        # cat2/analyze_rtl_congestion.2
        _syn(            "analyze_rtl_congestion",
            "Reports pre-synthesis congestion analysis.",
            "analyze_rtl_congestion ?-nosplit?",
        ),
        # cat2/annotate_trace.2
        _syn(            "annotate_trace",
            "Control annotation of traced command execution to the shell output.",
            "annotate_trace ?-start | -stop? ?-profile profile_annotation_type? ?-log log_string? ?-quiet?",
        ),
        # cat2/apply_clock_gate_latency.2
        _syn(            "apply_clock_gate_latency",
            "Annotates the clock latencies on the existing clock-gating cells based on the settings previously specified using the set_clock_gate_latency command.",
            "apply_clock_gate_latency",
        ),
        # cat2/apply_power_model.2
        _syn(            "apply_power_model",
            "Apply a power model which describes the power intent of a reference library cell to instances.",
            "apply_power_model power_model_name ?-elements instance_names? ?-supply_map supply_map_list? ?-port_map port_map_list? ?-parameters param_map_list? ?-all_hard_macros?",
        ),
        # cat2/apropos.2
        _syn(            "apropos",
            "Searches the command database for a pattern.",
            "apropos ?-symbols_only? pattern",
        ),
        # cat2/as_collection.2
        _syn(            "as_collection",
            "Find a collection by name",
            "as_collection ?-check? collection1",
        ),
        # cat2/associate_supply_set.2
        _syn(            "associate_supply_set",
            "Associates a supply set handle to another supply set handle or supply set reference, or associates a list of supply sets.",
            "associate_supply_set supply_set_names -handle supply_set_handle",
        ),
        # cat2/balance_buffer.2
        _syn(            "balance_buffer",
            "Builds a balanced buffer tree on user-specified nets and drivers.",
            "balance_buffer ?-from start_point_list? ?-to end_point_list? ?-net net_list? ?-force? ?-library library_name? ?-prefer buffer | inverter | lib_cell_name?",
        ),
        # cat2/balance_registers.2
        _syn(            "balance_registers",
            "Moves the registers of the current design to achieve a minimum cycle time.",
            "balance_registers",
        ),
        # cat2/break.2
        _syn(            "break",
            "Immediately exits a loop structure.",
            "break",
        ),
        # cat2/capture_detailed_script_runtime.2
        _syn(            "capture_detailed_script_runtime",
            "Enable detailed capture of runtime script report to a file.",
            "capture_detailed_script_runtime ?-start? ?-stop? ?-output output?",
        ),
        # cat2/capture_qor_data.2
        _syn(            "capture_qor_data",
            "Captures custom QoR data into a QORsum panel",
            "capture_qor_data -panel panel_name ?-label label_name? ?-output output_dir? ?-columns columns? ?-data data? ?-gui_setup tcl_code? ?-gui_cleanup tcl_code? ?-use_default_panel?",
        ),
        # cat2/cd.2
        _syn(            "cd",
            "Changes the current directory.",
            "cd ?directory?",
        ),
        # cat2/cell_of.2
        _syn(            "cell_of",
            "Returns the cell objects for the specified pins in the current design.",
            "cell_of ?object_list?",
        ),
        # cat2/change_link.2
        _syn(            "change_link",
            "Changes the design to which a cell is linked.",
            "change_link object_list design_name ?-all_instances? ?-force? ?-pin_map pin_map_list?",
        ),
        # cat2/change_names.2
        _syn(            "change_names",
            "Changes the names of ports, cells, and nets in a design.",
            "change_names ?-rules name_rules? ?-hierarchy? ?-verbose? ?-names_file names_file? ?-log_changes log_file? ?-restore? ?-dont_touch object_list? ?-instance instance? ?-new_name new_name? ?-skip_inactive_constraints? ?-dont_touch_collection object_list?",
        ),
        # cat2/change_selection.2
        _syn(            "change_selection",
            "Changes the selection in the GUI, taking a collection of objects and changing the selection according to the type of change specified.",
            "change_selection ?-name slct_bus? ?-replace? ?-add? ?-remove? ?-toggle? ?-type object_type? collection ?-push? ?-undo?",
        ),
        # cat2/characterize.2
        _syn(            "characterize",
            "Captures information about the environment of specific cell instances and assigns the information as attributes on the design to which the cells are linked.",
            "characterize cell_list ?-no_timing? ?-constraints? ?-connections? ?-power? ?-verbose?",
        ),
        # cat2/check_bindings.2
        _syn(            "check_bindings",
            "Checks the bindings in a synthetic library module definition.",
            "check_bindings ?-bindings binding_list? ?-pin_widths pin_width_list? module_name",
        ),
        # cat2/check_block_abstraction.2
        _syn(            "check_block_abstraction",
            "Checks the readiness of a block abstraction for usage in a toplevel design at various stages of the flow.",
            "check_block_abstraction",
        ),
        # cat2/check_bsd.2
        _syn(            "check_bsd",
            "Checks whether a design's boundary-scan implementation is compliant with IEEE Std 1149.1.",
            "check_bsd ?-verbose true | false? ?-infer_instructions true | false? ?-effort low | medium | high?",
        ),
        # cat2/check_budget.2
        _syn(            "check_budget",
            "Checks that user-specified budgets and fixed delays are consistent with path constraints.",
            "check_budget ?-verbose? ?-tolerance tolerance? ?-from object_list? ?-to object_list? ?-no_interblock_logic? ?cell_list?",
        ),
        # cat2/check_design.2
        _syn(            "check_design",
            "Checks the current design for consistency.",
            "check_design ?-summary? ?-no_warnings? ?-one_level? ?-multiple_designs? ?-no_connection_class? ?-nosplit? ?-unmapped? ?-cells? ?-ports? ?-designs? ?-nets? ?-tristates? ?error-ids? ?-html_file_name html_file?",
        ),
        # cat2/check_error.2
        _syn(            "check_error",
            "Reports extended information on message IDs from the last command.",
            "check_error ?-verbose? ?-reset?",
        ),
        # cat2/check_implementations.2
        _syn(            "check_implementations",
            "Checks the implementations in a synthetic library module definition.",
            "check_implementations ?-implementations implementation_list? ?-parameters parameter_list? module_name",
        ),
        # cat2/check_library.2
        _syn(            "check_library",
            "Performs consistency checks between logic and physical libraries, across logic libraries, and within physical libraries.",
            "check_library ?-logic_library_name logic_library_name_list? ?-mw_library_name phys_library_name_list? ?-physical_library_name phys_library_name_list? ?-cells cell_list?",
        ),
        # cat2/check_license.2
        _syn(            "check_license",
            "Checks the availability of a license for a feature.",
            "check_license feature_list",
        ),
        # cat2/check_mv_design.2
        _syn(            "check_mv_design",
            "Checks for violations in a multivoltage design.",
            "check_mv_design ?-verbose? ?-isolation? ?-target_library_subset? ?-opcond_mismatches? ?-connection_rules? ?-level_shifters? ?-power_nets? ?-clock_gating_style? ?-objects object_name_list? ?-models? ?-max_messages message_count? ?-output output_file_name?",
        ),
        # cat2/check_rp_groups.2
        _syn(            "check_rp_groups",
            "Checks the relative placement constraints and reports any failures.",
            "check_rp_groups {rp_groups | -all} ?-output filename? ?-verbose? ?-critical?",
        ),
        # cat2/check_scan_def.2
        _syn(            "check_scan_def",
            "Performs scan chain structural consistency checking based either on the scan chain information stored as an attribute in the current .ddc file, or an ASCII SCANDEF file.",
            "check_scan_def ?-file file_name?",
        ),
        # cat2/check_scenarios.2
        _syn(            "check_scenarios",
            "Performs consistency checks between the scenarios, for scenario specific information such as TLUplus files, operating conditions on the libraries, clocks and so on.",
            "check_scenarios ?-output? ?-display?",
        ),
        # cat2/check_synlib.2
        _syn(            "check_synlib",
            "Performs semantic checks on synthetic libraries.",
            "check_synlib",
        ),
        # cat2/check_target_library_subset.2
        _syn(            "check_target_library_subset",
            "Checks and prints out the inconsistent settings among target library, target library subset, and operating conditions.",
            "check_target_library_subset ?-verbose? ?-max_messages int?",
        ),
        # cat2/check_tlu_plus_files.2
        _syn(            "check_tlu_plus_files",
            "Checks the files used for TLUPlus extraction.",
            "check_tlu_plus_files",
        ),
        # cat2/check_upf.2
        _syn(            "check_upf",
            "Checks the UPF loaded on a hierarchical design for validity of references across the abstract boundary between the top level and the block level.",
            "check_upf",
        ),
        # cat2/clean_buffer_tree.2
        _syn(            "clean_buffer_tree",
            "Removes the buffer tree at the specified driver pin, load pin, or driver net on a mapped design.",
            "clean_buffer_tree ?-from start_point_list? ?-to object_list? ?-net net_list? ?-source_of object_list? ?-hierarchy? ?-global? ?-threshold integer_in_1?",
        ),
        # cat2/close_lib.2
        _syn(            "close_lib",
            "Decrements the open count of a library. A library is removed from memory when its open count is zero.",
            "close_lib ?-save_designs? ?-force? ?-purge? ?-all? ?-compress? ?library?",
        ),
        # cat2/close_mw_lib.2
        _syn(            "close_mw_lib",
            "Closes the current Milkyway library.",
            "close_mw_lib",
        ),
        # cat2/compare_collections.2
        _syn(            "compare_collections",
            "Compares the contents of two collections. If the same objects are in both collections, the result is \"0\" (like string compare). If they are different, the result is nonzero. The order of the objects can optionally be considered.",
            "compare_collections ?-order_dependent? collection1 collection2",
        ),
        # cat2/compare_delay_calculation.2
        _syn(            "compare_delay_calculation",
            "Compares the Arnoldi-based delays with the Elmore delays in the current design.",
            "compare_delay_calculation ?-verbose? ?-ccs?",
        ),
        # cat2/compare_lib.2
        _syn(            "compare_lib",
            "Performs a cross-reference check between a technology library and a symbol library or between a technology library and a physical library.",
            "compare_lib library1 library2",
        ),
        # cat2/compare_qor_data.2
        _syn(            "compare_qor_data",
            "Generates the QoRsum web application and report for viewing or comparing QoR results.",
            "compare_qor_data -run_locations run_location_list ?-run_names run_name_list? ?-output output_dir? ?-force?",
        ),
        # cat2/compare_supplies.2
        _syn(            "compare_supplies",
            "compares voltage levels or relative ON-ness between two given supplies.",
            "compare_supplies supply_list ?-on_status? ?-voltage_level?",
        ),
        # cat2/compile.2
        _syn(            "compile",
            "Performs logic-level and gate-level synthesis and optimization on the current design.",
            "compile ?-no_map? ?-map_effort medium | high? ?-area_effort none | low | medium | high? ?-incremental_mapping? ?-exact_map? ?-ungroup_all? ?-boundary_optimization? ?-auto_ungroup area | delay? ?-no_design_rule | -only_design_rule | -only_hold_time? ?-scan? ?-top? ?-power_effort none | low | medium | high? ?-gate_clock?",
        ),
        # cat2/compile_exploration.2
        _syn(            "compile_exploration",
            "Performs a fast mapping of gates with limited timing and area optimization.",
            "compile_exploration ?-check_only? ?-exact_map? ?-gate_clock? ?-no_autoungroup? ?-no_boundary_optimization? ?-no_seq_output_inversion? ?-scan?",
        ),
        # cat2/compile_prefer_runtime.2
        _syn(            "compile_prefer_runtime",
            "Overrides runtime-intensive user settings with settings designed to improve runtime. The compile_prefer_runtime command settings take effect when you run the compile_ultra, compile_ultra -incremental, or the optimize_netlist -area command.",
            "compile_prefer_runtime",
        ),
        # cat2/compile_ultra.2
        _syn(            "compile_ultra",
            "Performs a high-effort compile on the current design for better quality of results (QoR).",
            "compile_ultra ?-incremental? ?-scan? ?-exact_map? ?-no_autoungroup? ?-no_seq_output_inversion? ?-no_boundary_optimization? ?-no_design_rule | -only_design_rule? ?-timing_high_effort_script | -area_high_effort_script? ?-top? ?-retime? ?-gate_clock? ?-self_gating? ?-check_only? ?-congestion? ?-spg? ?-no_auto_layer_optimization? ?-only_map?",
        ),
        # cat2/compute_polygons.2
        _syn(            "compute_polygons",
            "Returns a list or collection of polygons that exactly cover the region computed by performing a Boolean operation on the input polygons.",
            "compute_polygons -boolean and | or | not | xor poly_list1 poly_list2",
        ),
        # cat2/connect_logic_net.2
        _syn(            "connect_logic_net",
            "Connects a logic net to logic ports in a UPF description.",
            "connect_logic_net net_name -ports port_list ?-reconnect?",
        ),
        # cat2/connect_net.2
        _syn(            "connect_net",
            "Connects the specified net to the specified pins or ports.",
            "connect_net net object_list",
        ),
        # cat2/connect_pin.2
        _syn(            "connect_pin",
            "Connects pins or ports at any level of hierarchy.",
            "connect_pin -from from_object -to to_list ?-port_name port_name? ?-verbose?",
        ),
        # cat2/connect_supply_net.2
        _syn(            "connect_supply_net",
            "Connects the supply net to specified supply ports and pins.",
            "connect_supply_net supply_net_name -ports list ?-vct vct_name?",
        ),
        # cat2/continue.2
        _syn(            "continue",
            "Begins the next loop iteration.",
            "continue",
        ),
        # cat2/convert_from_polygon.2
        _syn(            "convert_from_polygon",
            "Converts each polygon into a list or collection of mutually exclusive rectangles.",
            "convert_from_polygon polygons ?-format polygon | rectangle?",
        ),
        # cat2/convert_pg.2
        _syn(            "convert_pg",
            "Converts RTL PG information extracted from RTL into UPF. This command is supported only in UPF mode.",
            "convert_pg ?-net_creation_style style?",
        ),
        # cat2/convert_to_polygon.2
        _syn(            "convert_to_polygon",
            "Returns a polygon list for the specified objects.",
            "convert_to_polygon ?-quiet? ?-collection? object_spec",
        ),
        # cat2/copy_collection.2
        _syn(            "copy_collection",
            "Duplicates the contents of a collection, resulting in a new collection. The base collection remains unchanged.",
            "copy_collection collection1",
        ),
        # cat2/copy_design.2
        _syn(            "copy_design",
            "Copies a design to a new design, or copies a list of designs to a new file in dc_shell memory.",
            "copy_design design_list target_name",
        ),
        # cat2/copy_lib.2
        _syn(            "copy_lib",
            "Copies one or more design libraries from one location to another.",
            "copy_lib ?-force? ?-merge | -no_designs? ?-from_lib source_name? -to_lib destination_name",
        ),
        # cat2/copy_mw_lib.2
        _syn(            "copy_mw_lib",
            "Copies a Milkyway library to another location.",
            "copy_mw_lib ?-from mw_lib? -to lib_name",
        ),
        # cat2/cputime.2
        _syn(            "cputime",
            "Reports the CPU time in seconds.",
            "cputime ?-all? ?-verbose?",
        ),
        # cat2/create_auto_path_groups.2
        _syn(            "create_auto_path_groups",
            "Creates path groups for the current design.",
            "create_auto_path_groups -mode rtl | mapped ?-exclude IO | macro | ICG? ?-slack slack? ?-max max? ?-min_regs_per_hierarchy min_regs? ?-prefix prefix? ?-file file_name? ?-verbose? ?-user_path_groups_file user_file_name? ?-skip?",
        ),
        # cat2/create_block_abstraction.2
        _syn(            "create_block_abstraction",
            "Generates a block abstraction for the current design. The command identifies the interface logic of the current design and annotates the design in memory with the interface logic.",
            "create_block_abstraction ?-include objects?",
        ),
        # cat2/create_bounds.2
        _syn(            "create_bounds",
            "Creates a fixed move bound or floating group bound in the design.",
            "create_bounds ?-name bound_name? ?-coordinate {llx1 lly1 urx1 ury1 ...}? ?-dimension bound_dimension? ?-diamond central_object? ?-effort low | medium | high | ultra? ?-type soft | hard? ?-exclusive? ?-color color? ?-cycle_color? ?-repelling diamond | rect? ?-groups list? object_list",
        ),
        # cat2/create_bsd_patterns.2
        _syn(            "create_bsd_patterns",
            "Generates a set of functional patterns for a boundary-scan design.",
            "create_bsd_patterns -output test_program_name ?-effort low | medium | high? ?-type pattern_type? ?-setup_instructions instruction_list? ?-bsd_test_setup enable | disable? ?-jtag_reset enable | disable?",
        ),
        # cat2/create_buffer_tree.2
        _syn(            "create_buffer_tree",
            "Creates a buffer tree for the specified driver pins and nets.",
            "create_buffer_tree ?-from pin_net_list? ?-incremental? ?-no_legalize? ?-on_route ?-skip_detail_route?? ?-align_hierarchy_for_long_nets?",
        ),
        # cat2/create_bus.2
        _syn(            "create_bus",
            "Creates a port bus or a net bus.",
            "create_bus object_list bus_name ?-type type_name? ?-sort? ?-no_sort? ?-start start_bit? ?-end end_bit?",
        ),
        # cat2/create_cell.2
        _syn(            "create_cell",
            "Creates leaf or hierarchical cells in the current design or its subdesigns.",
            "create_cell cell_list ?reference_name? ?-hierarchical? ?-logic 0 | 1? ?-only_physical?",
        ),
        # cat2/create_command_group.2
        _syn(            "create_command_group",
            "Creates a new command group.",
            "create_command_group ?-info info_text? group_name",
        ),
        # cat2/create_core_area.2
        _syn(            "create_core_area",
            "Defines the core area for the current design.",
            "create_core_area -coordinate {{llx lly} {urx ury}} ?-tile_name tile_name? ?-direction horizontal | vertical? ?-name core_name?",
        ),
        # cat2/create_design.2
        _syn(            "create_design",
            "Creates a design in dc_shell memory.",
            "create_design design_name ?file_name?",
        ),
        # cat2/create_dft_netlist.2
        _syn(            "create_dft_netlist",
            "Creates a DFT netlist from the current design.",
            "create_dft_netlist -type extest",
        ),
        # cat2/create_die_area.2
        _syn(            "create_die_area",
            "Creates the die area for the current design.",
            "create_die_area -coordinate list -polygon list",
        ),
        # cat2/create_failsafe_fsm_group.2
        _syn(            "create_failsafe_fsm_group",
            "Creates one failsafe_fsm_group",
            "create_failsafe_fsm_group -rule failsafe_fsm_rule ?-name group_name? ?-registers registers? ?-parity par_registers? ?-synchronizer sync_register? ?-error_signal signal? ?-update?",
        ),
        # cat2/create_failsafe_fsm_rule.2
        _syn(            "create_failsafe_fsm_rule",
            "Creates one failsafe_fsm_rule",
            "create_failsafe_fsm_rule ?-name rule_name? ?-encoding_style encoding_style? ?-error_detection_synchronizer? ?-distance values? ?-register_mapping lib_cell_list? ?-fit_rate_threshold fit_rate_threshold?",
        ),
        # cat2/create_lib.2
        _syn(            "create_lib",
            "Creates a design library.",
            "create_lib ?-technology tech_path | -use_technology_lib tech_lib_name? ?-scale_factor scale_factor? ?-ref_libs ref_libs? ?-convert_sites site_name_pairs_list? ?-base_lib base_library_path? library_name",
        ),
        # cat2/create_link_block_abstraction.2
        _syn(            "create_link_block_abstraction",
            "Generates IC Compiler II abstract NDM references for the current design and all the DCNXT block abstractions in the current design via link feature.",
            "create_link_block_abstraction ?-top_block? ?-output_ddc_file output_file_name? ?-output_ndm_dir ndm_cache_dir? ?-overwrite?",
        ),
        # cat2/create_logic_net.2
        _syn(            "create_logic_net",
            "Defines a logic net.",
            "create_logic_net net_name",
        ),
        # cat2/create_logic_port.2
        _syn(            "create_logic_port",
            "Defines a logic port.",
            "create_logic_port port_name ?-direction in | out | inout?",
        ),
        # cat2/create_missing_constraints.2
        _syn(            "create_missing_constraints",
            "Generates missing path constraints in the current design based on user-specified default settings.",
            "create_missing_constraints ?-period period_value? ?-waveform edge_list? ?-input_delay delay_value? ?-output_delay delay_value? ?-pin_load load_value? ?-driving_lib_cell lib_cell_name? ?-driving_lib_pin lib_pin_name? ?-exclude object_list? ?-clock_tracing_mode tracing_mode? ?-output file? ?-no_apply?",
        ),
        # cat2/create_multibit.2
        _syn(            "create_multibit",
            "Creates a multibit component for the specified list of cells or cell instances in the current design.",
            "create_multibit object_list ?-name multibit_name? ?-sort? ?-no_sort?",
        ),
        # cat2/create_mw_lib.2
        _syn(            "create_mw_lib",
            "Creates a Milkyway library.",
            "create_mw_lib ?-technology technology_file_name? ?-bus_naming_style style? ?-mw_reference_library lib_list? ?-reference_control_file rc_file_name? ?-open? libName",
        ),
        # cat2/create_net.2
        _syn(            "create_net",
            "Creates nets in the current design or its subdesign.",
            "create_net ?-power | -ground? net_list",
        ),
        # cat2/create_net_search_pattern.2
        _syn(            "create_net_search_pattern",
            "Defines a net pattern.",
            "create_net_search_pattern ?-fanout_upper_limit number? ?-fanout_lower_limit number? ?-bbox_half_perimeter_upper_limit length? ?-bbox_half_perimeter_lower_limit length? ?-net_length_upper_limit length? ?-net_length_lower_limit length? ?-blocked_area_ratio_upper_limit percentage? ?-blocked_area_ratio_lower_limit percentage? ?-aspect_ratio_upper_limit ratio? ?-aspect_ratio_lower_limit ratio? ?-centered_within {llx lly urx ury}? ?-connect_to_port? ?-connect_to_macro? ?-setup_slack_lower_limit number? ?-setup_slack_upper_limit number?",
        ),
        # cat2/create_net_shape.2
        _syn(            "create_net_shape",
            "Creates a new net shape.",
            "create_net_shape ?-type wire | path | rect? -origin point | -bbox rect | -points list_of_points ?-length length? ?-width width? ?-path_type square | round | extend_half_width | octagon? -layer layer ?-mask_constraint constraint? -net net_name ?-vertical? ?-route_type route_type? ?-net_type ground | power | clock | signal? ?-datatype int? ?-avoid_short_segment?",
        ),
        # cat2/create_operating_conditions.2
        _syn(            "create_operating_conditions",
            "Creates a new set of operating conditions in a library.",
            "create_operating_conditions -name name -library library_name -process process_value -temperature temperature_value -voltage voltage_value ?-tree_type tree_type? ?-calc_mode calc_mode? ?-rail_voltages rail_value_pairs?",
        ),
        # cat2/create_pin_guide.2
        _syn(            "create_pin_guide",
            "Creates a pin guide for top-level ports to contrain the terminals to a specified bounding box.",
            "create_pin_guide -bbox bounding_box_rect | -boundary rectilinear_boundary ?-parents soft_macro_or_plan_group? ?-name pin_guide_name? ?-exclusive? objects",
        ),
        # cat2/create_placement_blockage.2
        _syn(            "create_placement_blockage",
            "Creates a new placement blockage.",
            "create_placement_blockage -bbox {llx1 lly1 urx1 ury1} ?-type hard | soft | partial? ?-blocked_percentage percentage? ?-no_register? ?-buffer_only? ?-category attribute_name? ?-no_rp_group? ?-no_pin? ?-blocked_layers layers? ?-no_hard_macro? ?-name blockage_name?",
        ),
        # cat2/create_port.2
        _syn(            "create_port",
            "Creates ports in the current design or its subdesign.",
            "create_port port_list ?-direction dir?",
        ),
        # cat2/create_power_domain.2
        _syn(            "create_power_domain",
            "Creates a power domain, which provides a power supply distribution network.",
            "create_power_domain domain_name ?-elements cells? ?-exclude_elements cells? ?-include_scope? ?-scope instance_name? ?-supply {supply_set_handle_name ?supply_set_name?}?* ?-available_supplies {supply_set_name_list}? ?-atomic? ?-update?",
        ),
        # cat2/create_power_state_group.2
        _syn(            "create_power_state_group",
            "Defines a group name to be used in the add_power_state command.",
            "create_power_state_group group_name",
        ),
        # cat2/create_power_switch.2
        _syn(            "create_power_switch",
            "Creates a power switch in the specified power domain.",
            "create_power_switch switch_name -domain domain_name -output_supply_port {port_name supply_net_name} -input_supply_port {port_name supply_net_name} -control_port {port_name net_name} -supply_set supply_set_name ?-ack_port {port_name net_name ?{boolean_function}?}? ?-ack_delay {port_name delay}? -on_state {state_name input_supply_port {boolean_function}} ?-off_state {state_name {boolean_function}}? ?-on_partial_state {state_name {boolean_function}}? ?-error_state {state_name {boolean_function}}?",
        ),
        # cat2/create_pst.2
        _syn(            "create_pst",
            "Creates a power state table (PST), using a specific order of supply nets.",
            "create_pst table_name -supplies list",
        ),
        # cat2/create_qor_snapshot.2
        _syn(            "create_qor_snapshot",
            "Generates a quality-of-results report for active scenarios of the current design and stores the report into a set of files.",
            "create_qor_snapshot -name name ?-power? ?-clock_tree? ?-show_all? ?-route? ?-save_mw? ?-significant_digits digits? ?-zero_wire_load? ?-max_paths number? ?-nworst number? ?-scenarios list_of_scenarios? ?-infeasible_paths? ?-nosplit?",
        ),
        # cat2/create_qtm_constraint_arc.2
        _syn(            "create_qtm_constraint_arc",
            "Creates a constraint arc for a quick timing model (QTM).",
            "create_qtm_constraint_arc ?-name arc_name? -setup | -hold -from port_name -to port_spec -edge rise | fall ?-signal_edge rise | fall? ?-input_transition_rise rise_time? ?-input_transition_fall fall_time? -path_type name ?-path_factor factor? | -value constraint_value",
        ),
        # cat2/create_qtm_delay_arc.2
        _syn(            "create_qtm_delay_arc",
            "Creates a delay arc for a quick timing model (QTM).",
            "create_qtm_delay_arc ?-name arc_name? -from ports -to ports ?-from_edge rise | fall? ?-to_edge rise | fall? ?-input_transition_rise rise_time? ?-input_transition_fall fall_time? -path_type name ?-path_factor factor? | -value delay_value | -total_value total_value ?-max_insertion_delay? ?-min_insertion_delay?",
        ),
        # cat2/create_qtm_drive_type.2
        _syn(            "create_qtm_drive_type",
            "Creates a drive type in a quick timing model (QTM).",
            "create_qtm_drive_type -lib_cell lib_cell_name ?-input_pin pin_name? ?-output_pin pin_name? ?-input_transition_rise rtrans? ?-input_transition_fall ftrans? drive_type_name",
        ),
        # cat2/create_qtm_generated_clock.2
        _syn(            "create_qtm_generated_clock",
            "Creates a generated clock for a quick timing model (QTM).",
            "create_qtm_generated_clock -source master_clock_name ?-divide_by divide_factor | -multiply_by multiply_factor? ?-invert? generated_clock_name",
        ),
        # cat2/create_qtm_insertion_delay.2
        _syn(            "create_qtm_insertion_delay",
            "Specifies the insertion delay on the clock port of a quick timing model (QTM).",
            "create_qtm_insertion_delay ?-max? ?-min? ?-value insertion_delay? port_list",
        ),
        # cat2/create_qtm_load_type.2
        _syn(            "create_qtm_load_type",
            "Creates a load type for a quick timing model (QTM) description.",
            "create_qtm_load_type -lib_cell lib_cell_name ?-input_pin pin_name? load_type_name",
        ),
        # cat2/create_qtm_model.2
        _syn(            "create_qtm_model",
            "Begins the definition of a quick timing model (QTM) description.",
            "create_qtm_model model_name",
        ),
        # cat2/create_qtm_path_type.2
        _syn(            "create_qtm_path_type",
            "Creates a path type in a quick timing model (QTM) description.",
            "create_qtm_path_type -lib_cell lib_cell_name ?-input_pin input_pin_name? ?-output_pin output_pin_name? ?-fanout count? path_type_name",
        ),
        # cat2/create_qtm_port.2
        _syn(            "create_qtm_port",
            "Creates a quick timing model (QTM) port.",
            "create_qtm_port -type port_type port_list",
        ),
        # cat2/create_register_bank.2
        _syn(            "create_register_bank",
            "Creates a multibit register bank from a list of single-bit registers.",
            "create_register_bank object_list ?-name bank_name? -lib_cell library_name/lib_cell_name",
        ),
        # cat2/create_route_guide.2
        _syn(            "create_route_guide",
            "Creates a new route guide.",
            "create_route_guide -coordinate rectangle ?-no_signal_layers layers? ?-no_preroute_layers layers? ?-standard_cell_region? ?-zero_min_spacing? ?-preferred_direction_only_layers layers? ?-switch_preferred_direction_layers layers? ?-repair_as_single_sbox? ?-horizontal_track_utilization percentage? ?-vertical_track_utilization percentage? ?-track_utilization_layers layers? ?-name guide_name? ?-single_layer_routing layers? ?-access_preference {access_preference_spec}?",
        ),
        # cat2/create_rp_group.2
        _syn(            "create_rp_group",
            "Creates relative placement groups.",
            "create_rp_group group_list ?-design design_name? ?-columns num_cols? ?-rows num_rows? ?-alignment bottom-left | bottom-pin | bottom-right? ?-pin_align_name pin_name? ?-utilization percentage? ?-ignore? ?-x_offset float? ?-y_offset float? ?-cts_option fixed_placement | size_only? ?-route_opt_option fixed_placement | in_place_size_only? ?-psynopt_option fixed_placement | size_only | all_optimization? ?-move_effort low | medium | high? ?-allow_keepout_over_tapcell false | true? ?-allow_non_rp_cells? ?-place_around_fixed_cells standard | physical_only | none | all? ?-anchor_corner bottom-left | bottom-right | top-left | top-right | rp-location ?-anchor_row integer? ?-anchor_column integer?? ?-placement_type bit_slice | compression | vertical_compression? ?-group_orient default | N | FN | S | FS? ?-cell_orient_opt? ?-auto_blockage? ?-disable_buffering? ?-ignore_rows ignore_row_names_list? ?-max_rp_width float? ?-max_rp_height float?",
        ),
        # cat2/create_safety_core_group.2
        _syn(            "create_safety_core_group",
            "Creates one safety_core_group",
            "create_safety_core_group -rule safety_core_rule -cores objects ?-name group_name? ?-logic cells? -error_signal pin or port ?-split_pins pins? ?-update?",
        ),
        # cat2/create_safety_core_rule.2
        _syn(            "create_safety_core_rule",
            "Creates one safety_core_rule",
            "create_safety_core_rule ?-name rule_name? ?-update? ?-num_cores count? ?-distance values? ?-routing_separation? ?-routing_guardband distance? ?-logic_module reference? ?-logic_mapping lib_cell_list?",
        ),
        # cat2/create_safety_error_code_group.2
        _syn(            "create_safety_error_code_group",
            "Creates one safety_error_code_group.",
            "create_safety_error_code_group -rule safety_error_code_rule ?-name group_name? -data pins_or_ports -checkbits pins_or_ports ?-error_signal pin_or_port? ?-update? ?-requirement_id requirement_id_string?",
        ),
        # cat2/create_safety_error_code_rule.2
        _syn(            "create_safety_error_code_rule",
            "Creates one safety_error_code_rule object",
            "create_safety_error_code_rule -type type ?-name rule_name? ?-slice_size size? ?-mode mode? ?-sequential? ?-update?",
        ),
        # cat2/create_safety_register_group.2
        _syn(            "create_safety_register_group",
            "Creates one safety_register_group",
            "create_safety_register_group -rule safety_register_rule ?-name group_name? ?-registers registers? ?-logic cells? ?-split_pins pins? ?-error_signal pin_or_port? ?-update?",
        ),
        # cat2/create_safety_register_rule.2
        _syn(            "create_safety_register_rule",
            "Creates one safety_register_rule",
            "create_safety_register_rule -type rule_type ?-name rule_name? ?-distance values? ?-register_mapping lib_cell_list? ?-logic_module lib_cell? ?-tap_mapping lib_cell_name_list? ?-split_pin_types pin_type_list? ?-update?",
        ),
        # cat2/create_scenario.2
        _syn(            "create_scenario",
            "Creates a scenario in memory.",
            "create_scenario scenario_name",
        ),
        # cat2/create_site_row.2
        _syn(            "create_site_row",
            "Creates a row of sites.",
            "create_site_row -coordinate {X Y} -name row_name -kind site_type -space space -count site_count ?-orient orientation? ?-dir direction?",
        ),
        # cat2/create_supply_net.2
        _syn(            "create_supply_net",
            "Creates a supply net for the specified power domain. The supply net is created in the logic hierarchy at the same scope as the specified power domain.",
            "create_supply_net supply_net_name ?-domain domain_name? ?-reuse? ?-resolve unresolved | parallel | one_hot | parallel_one_hot | resolution_function_name?",
        ),
        # cat2/create_supply_port.2
        _syn(            "create_supply_port",
            "Creates a supply port in the specified power domain. If a power domain is not specified, creates the port in the current scope.",
            "create_supply_port supply_port_name ?-domain domain_name? ?-direction in | out | inout | internal?",
        ),
        # cat2/create_supply_set.2
        _syn(            "create_supply_set",
            "Creates a set of supplies that can be used to define the power network. A supply set is created in the current logic hierarchy.",
            "create_supply_set ?-function {function_name supply_net_name}? ?-update? supply_set_name",
        ),
        # cat2/create_terminal.2
        _syn(            "create_terminal",
            "Creates a new terminal for a logical port.",
            "create_terminal -bbox rect | -bounding_box rect -layer layer ?-mask_constraint constraint? -port port_name ?-direction {pin_directions}? ?-name terminal_name?",
        ),
        # cat2/create_test_protocol.2
        _syn(            "create_test_protocol",
            "Creates a test protocol based on user specifications.",
            "create_test_protocol ?-infer_asynch? ?-infer_clock? ?-capture_procedure single_clock | multi_clock?",
        ),
        # cat2/create_track.2
        _syn(            "create_track",
            "Creates tracks for a routing layer or poly layer.",
            "create_track -layer layer ?-space track_pitch? ?-count number_of_tracks? ?-coord start_x_or_y? ?-dir X | Y? ?-bounding_box track_boundary_box? ?-mask_constraint constraint?",
        ),
        # cat2/create_user_shape.2
        _syn(            "create_user_shape",
            "Creates a new user shape. A user shape is a metal shape that is not associated with a net.",
            "create_user_shape ?-type wire | path | trap | rect | poly? -origin point | -points list_of_points | -bbox rect | -boundary boundary ?-length length? ?-width width? ?-path_type square | round | extend_half_width | octagon? -layer layer ?-mask_constraint constraint? ?-vertical? ?-route_type route_type? ?-datatype int? ?-avoid_short_segment?",
        ),
        # cat2/create_via.2
        _syn(            "create_via",
            "Creates a new via at a specified location.",
            "create_via -at point ?-name name? -master via_master | -auto ?-net net_name | -no_net? ?-allow_multiple? ?-route_type route_type? ?-orient orientation? ?-type via | via_array? ?-row num_rows? ?-col num_columns? ?-x_pitch x_distance? ?-y_pitch y_distance?",
        ),
        # cat2/create_via_master.2
        _syn(            "create_via_master",
            "Creates a design via master using parameters or a geometry list.",
            "create_via_master -name via_master_name -cut_layer_name cut_layer_name -lower_layer_name low_layer_name -upper_layer_name up_layer_name ?-rectangles {{layer_name {llx lly urx ury}} ...}? ?-cut_width cut_width? ?-cut_height cut_height? ?-lower_layer_enc_width low_enc_width? ?-lower_layer_enc_height lo_enc_height? ?-upper_layer_enc_width up_enc_width? ?-upper_layer_enc_height up_enc_height? ?-min_cut_spacing min_cut_spacing? ?-quiet?",
        ),
        # cat2/create_via_rule.2
        _syn(            "create_via_rule",
            "Creates a via_rule.",
            "create_via_rule -name via_rule_name ?-cut_layer_names {name_list}? ?-cut_names {name_list}? ?-cut_rows {int_list}? ?-cuts_per_row {int_list}?",
        ),
        # cat2/create_voltage_area.2
        _syn(            "create_voltage_area",
            "Creates a voltage area at a specified region that constrains the placement of specified hierarchical cells. This command is supported only in topographical mode.",
            "create_voltage_area modules -name voltage_area_name | -power_domain {power_domain_name} -coordinate {llx1 lly1 urx1 ury1 ...} ?-guard_band_x guard_band_width? ?-guard_band_y guard_band_width? ?-is_fixed? ?-color color | -cycle_color? ?-target_utilization float?",
        ),
        # cat2/create_wiring_keepouts.2
        _syn(            "create_wiring_keepouts",
            "Creates a wiring keepout.",
            "create_wiring_keepouts -name name -layer layer -coordinate list_of_float_values",
        ),
        # cat2/cross_probing_filter.2
        _syn(            "cross_probing_filter",
            "Filters a collection based on file name and line number criteria.",
            "cross_probing_filter -source source_patterns objects",
        ),
        # cat2/current_design_name.2
        _syn(            "current_design_name",
            "Returns the current design name.",
            "current_design_name",
        ),
        # cat2/current_dft_partition.2
        _syn(            "current_dft_partition",
            "Sets or gets the design partition for the current specification.",
            "current_dft_partition ?design_partition_label?",
        ),
        # cat2/current_instance.2
        _syn(            "current_instance",
            "Sets the working instance object and enables other commands to be used on a specific cell in the design hierarchy.",
            "current_instance ?instance?",
        ),
        # cat2/current_lib.2
        _syn(            "current_lib",
            "Sets or returns the current library.",
            "current_lib ?-quiet? ?library_name?",
        ),
        # cat2/current_mw_lib.2
        _syn(            "current_mw_lib",
            "Gets the current Milkyway library.",
            "current_mw_lib",
        ),
        # cat2/current_scenario.2
        _syn(            "current_scenario",
            "Sets the current scenario.",
            "current_scenario ?scenario_name?",
        ),
        # cat2/current_test_mode.2
        _syn(            "current_test_mode",
            "Sets or gets the current working test mode for the current design.",
            "current_test_mode ?test_mode_label?",
        ),
        # cat2/cut_row.2
        #   WARNING: unclosed bracket '[' at position 8
        _syn(            "cut_row",
            "Removes rows from the current design.",
            "cut_row ?-all | -within {coordinates}",
        ),
        # cat2/date.2
        _syn(            "date",
            "Returns a string containing the current date and time.",
            "date",
        ),
        # cat2/dc_allocate_budgets.2
        _syn(            "dc_allocate_budgets",
            "Allocates budgets to specified cells.",
            "dc_allocate_budgets ?cell_list? ?-write_script? ?-file_format_spec format_spec? ?-format dctcl | dcsh? ?-separator hierarchy_separator? ?-mode rtl | gate | mixed? ?-budget_design_ware? ?-levels budget_levels? ?-no_interblock_logic? ?-min_register_to_output minimum_budget? ?-min_input_to_output minimum_budget? ?-min_input_to_register minimum_budget?",
        ),
        # cat2/dcnxt_use_icc2_link.2
        _syn(            "dcnxt_use_icc2_link",
            "Specifies the features for which the IC Compiler II tool is launched from within Design Compiler.",
            "dcnxt_use_icc2_link ?-placement {true | false}? ?-auto_floorplan {true | false}? ?-congestion_use_global_route {true | false}? ?-report_only?",
        ),
        # cat2/decrypt_lib.2
        _syn(            "decrypt_lib",
            "Decrypts a Milkyway library containing locked technology information.",
            "decrypt_lib ?-format {mwlib}? -key key_string lib_name",
        ),
        # cat2/define_design_lib.2
        _syn(            "define_design_lib",
            "Maps a design library to a UNIX directory.",
            "define_design_lib library_name -path directory",
        ),
        # cat2/define_dft_design.2
        _syn(            "define_dft_design",
            "Characterizes a design as a DFT design to be used for DFT insertion.",
            "define_dft_design -design_name design_name ?-type design_type? ?-interface access_list? ?-test_model model_path_name? ?-params param_list? ?-validate true | false?",
        ),
        # cat2/define_dft_partition.2
        _syn(            "define_dft_partition",
            "Defines a design DFT partition to be created during DFT synthesis.",
            "define_dft_partition design_partition_label ?-default false | true? ?-include list_of_design_objects? ?-clocks list_of_clocks? ?-rising_edge_clocks list_of_clocks? ?-falling_edge_clocks list_of_clocks? ?-extest_cells list_of_wrapped_cores? ?-wrapper enable | disable?",
        ),
        # cat2/define_libcell_subset.2
        _syn(            "define_libcell_subset",
            "Defines a subset of library cells to restrict the optimization of sequential and instantiated combinational cells.",
            "define_libcell_subset ?-libcell_list lib_cells? ?-family_name name?",
        ),
        # cat2/define_name_maps.2
        _syn(            "define_name_maps",
            "Defines object name mapping for an application and design.",
            "define_name_maps -application application_name -design_name design_name -columns column_list entries",
        ),
        # cat2/define_name_rules.2
        _syn(            "define_name_rules",
            "Defines a set of name rules for designs.",
            "define_name_rules name_rules ?-max_length length? ?-target_bus_naming_style bus_naming_style? ?-allowed allowed_chars? ?-restricted restricted_chars? ?-first_restricted first_chars? ?-last_restricted last_chars? ?-reserved_words reserves? ?-replacement_char char? ?-remove_chars? ?-equal_ports_nets? ?-inout_ports_equal_nets? ?-collapse_name_space? ?-case_insensitive? ?-special output_format? ?-prefix prefix_name? ?-map map_string? ?-type object_type? ?-reset? ?-remove_internal_net_bus? ?-remove_port_bus? ?-check_bus_indexing? ?-check_bus_indexing_use_type_info? ?-rename_three_state_port_net? ?-check_internal_net_name? ?-remove_irregular_port_bus? ?-remove_irregular_net_bus? ?-flatten_multi_dimension_busses? ?-preserve_struct_ports? ?-dont_change_bus_members? ?-dont_change_ports? ?-add_dummy_nets? ?-dummy_net_prefix dummy_nets_format? ?-dir_inout_as_in?",
        ),
        # cat2/define_power_model.2
        _syn(            "define_power_model",
            "Defines a power model which describes the power intent of a reference library cell.",
            "define_power_model power_model_name ?-for library_cells? {UPF_commands}",
        ),
        # cat2/define_preserve_user_attribute.2
        _syn(            "define_preserve_user_attribute",
            "Use the define_preserve_user_attribute command to specify which user-defined attributes to preserve on sequential cells in synthesis flows.",
            "define_preserve_user_attribute ?attribute_preservation_list? | ?-reset?",
        ),
        # cat2/define_qor_data_panel.2
        _syn(            "define_qor_data_panel",
            "Defines a new panel in the QORsum report where custom data can be captured",
            "define_qor_data_panel -name panel_name -type panel_type ?-group panel_group? ?-key_columns list_of_metrics? ?-hierarchical?",
        ),
        # cat2/define_routing_rule.2
        _syn(            "define_routing_rule",
            "Defines design-specific, nondefault routing rules that are stored in the design database.",
            "define_routing_rule rule_name ?-reference_rule_name ref_rule_name | -default_reference_rule? ?-widths {layer_name_and_width_pairs}? ?-spacings {layer_name_and_spacing_pairs}? ?-spacing_weights {layer_name_and_weight_pairs}? ?-spacing_weight_levels {layer_name_and_weight_level_pairs}? ?-spacing_length_thresholds {layer_name_and_length_threshold_pairs}? ?-shield? ?-shield_widths {layer_name_and_shield_width_pairs}? ?-shield_spacings {layer_name_and_shield_spacing_pairs}? ?-snap_to_track? ?-via_cuts {via_definition_list} | -cuts {cut_definition_list}? ?-taper_level tapering_level? ?-taper_distance tapering_distance? ?-driver_taper_distance driver_tapering_distance? ?-multiplier_width layer_width? ?-multiplier_spacing layer_spacing? ?-double_pattern_mask_constraints layer_and_constraint_pairs? ?-via_spacings via_layer_name_pairs_and_spacing? ?-rdl_taper_distance rdl_tapering_distance? ?-rdl_taper_widths {layer_name_and_rdl_tapering_width_pairs}? ?-taper_over_pin_layers number_of_layers? ?-taper_under_pin_layers number_of_layers? ?-single_side_spacing?",
        ),
        # cat2/define_scaling_lib_group.2
        _syn(            "define_scaling_lib_group",
            "Defines a scaling library group to support voltage and/or temperature scaling.",
            "define_scaling_lib_group ?-name name? ?lib_file_names?",
        ),
        # cat2/define_test_mode.2
        _syn(            "define_test_mode",
            "Defines a test mode to be created during DFT synthesis.",
            "define_test_mode test_mode_label ?-encoding {port_name 0 | 1, ...}? ?-usage mode_purpose? ?-target core_mode_pair_list? ?-transparent_mode_of parent_mode_name?",
        ),
        # cat2/define_user_attribute.2
        _syn(            "define_user_attribute",
            "Defines a new user-defined attribute.",
            "define_user_attribute -type string | int | float | double | boolean -classes class_list ?-range_min min? ?-range_max max? ?-one_of values? ?-quiet? attr_name ?-import?",
        ),
        # cat2/delete_operating_conditions.2
        _syn(            "delete_operating_conditions",
            "Deletes a specific set of operating conditions from a library.",
            "delete_operating_conditions -library library_name -name op_cond_name",
        ),
        # cat2/derive_constraints.2
        _syn(            "derive_constraints",
            "Propagates design environment, constraints, and attribute settings from the top-level design to the specified subdesigns.",
            "derive_constraints ?-attributes_only? ?-verbose? ?-budget? cell_list",
        ),
        # cat2/describe_state_transition.2
        _syn(            "describe_state_transition",
            "Defines named state transitions for an object.",
            "describe_state_transition transition_name ?-object object? ?-from from_list? ?-to to_list? ?-paired {{from_state to_state}*}? ?-through through_list? ?-legal | illegal? ?-illegal?",
        ),
        # cat2/dft_drc.2
        _syn(            "dft_drc",
            "Checks the current design against test design rules.",
            "dft_drc ?-pre_dft? ?-verbose? ?-coverage_estimate? ?-sample percentage?",
        ),
        # cat2/disconnect_net.2
        _syn(            "disconnect_net",
            "Disconnects a net from pins or ports.",
            "disconnect_net net object_list | -all",
        ),
        # cat2/distance.2
        _syn(            "distance",
            "Describes basic command types for describing mask geometry.",
            "distance",
        ),
        # cat2/drive_of.2
        #   WARNING: unclosed bracket '[' at position 42
        _syn(            "drive_of",
            "Returns the drive resistance value of the specified library cell pin.",
            "drive_of library_cell_pin ?-rise | -fall? ?-piece best | worst | average | ?-min?",
        ),
        # cat2/duplicate_logic.2
        _syn(            "duplicate_logic",
            "Duplicates combinational logic paths, given a startpoint pin, an endpoint pin, and, optionally, a list of intermediate (through) pins.",
            "duplicate_logic -from start_points ?-through mid_points? -to end_points ?-location location? ?-sufix suffix? ?-report_only?",
        ),
        # cat2/echo.2
        _syn(            "echo",
            "Echos arguments to standard output.",
            "echo ?-n? ?arguments?",
        ),
        # cat2/elaborate.2
        _syn(            "elaborate",
            "Builds a design from the intermediate format of a Verilog module, a VHDL entity and architecture, or a VHDL configuration.",
            "elaborate design_name ?-library library_name | -work library_name? ?-architecture arch_name? ?-parameters param_list? ?-file_parameters file_list? ?-update? ?-ref?",
        ),
        # cat2/enable_redirect_bg_commands.2
        _syn(            "enable_redirect_bg_commands",
            "Specify the allowed command type for redirect background executable.",
            "enable_redirect_bg_commands ?-all? ?-read_only?",
        ),
        # cat2/enable_write_lib_mode.2
        _syn(            "enable_write_lib_mode",
            "Enables usage of the write_lib command in the tool session.",
            "enable_write_lib_mode",
        ),
        # cat2/encrypt_lib.2
        _syn(            "encrypt_lib",
            "Encrypts a VHDL source library file.",
            "encrypt_lib file_name ?-output encrypted_file? ?-format {vhdl | tf | mwlib}? ?-key string?",
        ),
        # cat2/error_info.2
        _syn(            "error_info",
            "Prints extended information on errors from the last command.",
            "error_info",
        ),
        # cat2/estimate_fp_black_boxes.2
        #   WARNING: bracket mismatch: '[' at position 24 closed by '}' at position 109
        #   WARNING: unmatched closing bracket ']' at position 110
        _syn(            "estimate_fp_black_boxes",
            "Sets the size of a black box based on an estimation of the objects that it will contain when replaced with real logic.",
            "estimate_fp_black_boxes ?-sm_size {width height} | -polygon {{x1 y1} {x2 y2} ...} | -sm_gate_equiv gate_count}? ?-sm_util util? ?-hard_macros names? ?-fixed_shape? ?-reset_shape? black_boxes",
        ),
        # cat2/exit.2
        _syn(            "exit",
            "Terminates the application.",
            "exit ?exit_code?",
        ),
        # cat2/extend_mw_layers.2
        _syn(            "extend_mw_layers",
            "Extends Milkyway database layer number support to 4095 layers, using layers 4001 through 4095 as the system-reserved layers.",
            "extend_mw_layers",
        ),
        # cat2/extract_physical_constraints.2
        _syn(            "extract_physical_constraints",
            "Extracts physical constraint information from one or more Design Exchange Format (DEF) files. This command is supported only in Design Compiler in topographical mode.",
            "extract_physical_constraints def_files ?-verbose? ?-no_incremental? ?-exact? ?-allow_physical_cells? ?-standard_cell topo | spg? ?-ignore_undefined_site_rows?",
        ),
        # cat2/extract_rc.2
        _syn(            "extract_rc",
            "Executes virtual routing for nets in a design.",
            "extract_rc -estimate",
        ),
        # cat2/filter.2
        _syn(            "filter",
            "Returns a list of design objects that satisfy a conditional attribute expression.",
            "filter object_list expression ?-regexp? ?-nocase?",
        ),
        # cat2/find.2
        _syn(            "find",
            "Finds a design or library object.",
            "find type ?name_list? ?-hierarchy? ?-flat?",
        ),
        # cat2/find_objects.2
        _syn(            "find_objects",
            "Finds logical hierarchy objects within a scope. This is a UPF query command.",
            "find_objects scope -pattern pattern_string -object_type inst | port | net | model | supply_port | process ?-direction in | out | inout? ?-transitive true | false? ?-non_leaf? ?-leaf_only? ?-traverse_macros? ?-ignore_case? ?-regexp | -exact?",
        ),
        # cat2/fix_mv_design.2
        _syn(            "fix_mv_design",
            "Fixes multivoltage and PVT violations of buffers in a design.",
            "fix_mv_design ?-buffer? ?-from objects? ?-lib_cells lib_cells? ?-verbose?",
        ),
        # cat2/foreach.2
        _syn(            "foreach",
            "Specifies the control structure for list traversal loop execution.",
            "foreach",
        ),
        # cat2/generate_mv_constraints.2
        _syn(            "generate_mv_constraints",
            "Generates new isolation strategies for design elements.",
            "generate_mv_constraints ?-align_isolation_clamp_value? ?-no_isolation? ?-output output_file_name? ?-include_elements? ?-apply? ?-elements element_list? ?-dft_level_shifter? ?-dft_isolation?",
        ),
        # cat2/generate_rtl_upf.2
        _syn(            "generate_rtl_upf",
            "Writes out the design's UPF power intent as a UPF command script in DC Explorer.",
            "generate_rtl_upf -path path_name",
        ),
        # cat2/get_alternative_lib_cells.2
        _syn(            "get_alternative_lib_cells",
            "Creates a collection of equivalent library cells for a specified cell or library cell.",
            "get_alternative_lib_cells ?-quiet? ?-regexp | -exact? ?-nocase? ?-filter expression? ?-libraries libraries? pattern_or_objects",
        ),
        # cat2/get_always_on_logic.2
        _syn(            "get_always_on_logic",
            "Returns a collection of cells and nets on the always-on paths in the design.",
            "get_always_on_logic ?-cells? ?-nets? ?-all? ?-boundary?",
        ),
        # cat2/get_app_var.2
        _syn(            "get_app_var",
            "Gets the value of an application variable.",
            "get_app_var ?-default | -details | -list? ?-only_changed_vars? var",
        ),
        # cat2/get_attribute.2
        _syn(            "get_attribute",
            "Returns the value of an attribute on a list of design or library objects.",
            "get_attribute object_list attribute_name ?-bus? ?-quiet? ?-return_null_values?",
        ),
        # cat2/get_bounds.2
        _syn(            "get_bounds",
            "Creates a collection of bounds from the current design.",
            "get_bounds ?-quiet? ?-regexp | -exact? ?-nocase? ?-filter expression? ?patterns | -of_objects objects?",
        ),
        # cat2/get_buffers.2
        _syn(            "get_buffers",
            "Creates a collection of buffer cells.",
            "get_buffers ?-quiet? ?-regexp | -exact? ?-nocase? ?-filter expression? ?-inverter? ?-inverting_buffers? ?-library lib_spec? ?patterns?",
        ),
        # cat2/get_clusters.2
        _syn(            "get_clusters",
            "Creates a collection of one or more clusters.",
            "get_clusters ?-quiet? ?-regexp ?-nocase?? ?-exact? ?-filter expression? ?-hier? ?-flat? patterns | -of_objects objects",
        ),
        # cat2/get_command_hooks.2
        _syn(            "get_command_hooks",
            "Get registered hooks for this command",
            "get_command_hooks commandName",
        ),
        # cat2/get_command_option_values.2
        _syn(            "get_command_option_values",
            "Queries current or default option values.",
            "get_command_option_values ?-default | -current? -command command_name",
        ),
        # cat2/get_core_area.2
        _syn(            "get_core_area",
            "Creates a collection containing the core area of the current design.",
            "get_core_area",
        ),
        # cat2/get_cross_probing_info.2
        _syn(            "get_cross_probing_info",
            "Gets cross-probing information about cells and ports and returns the results as a string.",
            "get_cross_probing_info ?-unique_source? objects",
        ),
        # cat2/get_current_hook_command.2
        _syn(            "get_current_hook_command",
            "Get the currently running command string",
            "get_current_hook_command",
        ),
        # cat2/get_defined_commands.2
        _syn(            "get_defined_commands",
            "Get information on defined commands and groups.",
            "get_defined_commands ?-details? ?-groups? ?pattern?",
        ),
        # cat2/get_design_lib_path.2
        _syn(            "get_design_lib_path",
            "Returns the directory to which the specified library is mapped.",
            "get_design_lib_path library_name",
        ),
        # cat2/get_designs.2
        _syn(            "get_designs",
            "Creates a collection of one or more designs loaded into the tool.",
            "get_designs ?-hierarchical? ?-quiet? ?-regexp? ?-nocase? ?-exact? ?-filter expression? patterns",
        ),
        # cat2/get_dft_hierarchical_pins.2
        _syn(            "get_dft_hierarchical_pins",
            "Returns a collection of ports and hierarchical pins created during DFT insertion.",
            "get_dft_hierarchical_pins",
        ),
        # cat2/get_die_area.2
        _syn(            "get_die_area",
            "Returns a collection containing the die area of the current design.",
            "get_die_area",
        ),
        # cat2/get_domain_elements.2
        _syn(            "get_domain_elements",
            "Creates a collection of elements of power domains..",
            "get_domain_elements ?power_domains?",
        ),
        # cat2/get_dont_touch_cells.2
        _syn(            "get_dont_touch_cells",
            "Creates a collection of dont_touch cells that meet the specified criteria.",
            "get_dont_touch_cells ?-type type? ?-hierarchical? patterns",
        ),
        # cat2/get_dont_touch_nets.2
        _syn(            "get_dont_touch_nets",
            "Creates a collection of dont_touch nets that meet the specified criteria.",
            "get_dont_touch_nets ?-type type? ?-hierarchical? patterns",
        ),
        # cat2/get_early_data_check_records.2
        #   WARNING: unclosed bracket '[' at position 174
        _syn(            "get_early_data_check_records",
            "Creates a collection of check records. You can assign these records to a variable or pass them to another command.",
            "get_early_data_check_records ?-filter expression? ?-quiet? ?-regexp? ?-nocase? ?-exact? ?-expect exact_count? ?-expect_at_least minimum_count? ?-expect_each_pattern_matches? ?patterns",
        ),
        # cat2/get_failsafe_fsm_groups.2
        _syn(            "t_failsafe_fsm_groups",
            "Gets a collection of failsafe FSM groups.",
            "get_failsafe_fsm_groups ?-of_objects cells? ?-quiet?",
        ),
        # cat2/get_failsafe_fsm_rules.2
        _syn(            "get_failsafe_fsm_rules",
            "return the names of failsafe FSM rules.",
            "get_failsafe_fsm_rules ?-of_objects cells? ?-quiet?",
        ),
        # cat2/get_flat_cells.2
        _syn(            "get_flat_cells",
            "Creates a collection of leaf cells that match certain criteria in the current design.",
            "get_flat_cells ?-quiet? ?-regexp | -exact? ?-nocase? ?-filter expression? ?patterns | -of_objects objects? ?-all?",
        ),
        # cat2/get_flat_nets.2
        _syn(            "get_flat_nets",
            "Creates a collection of top-level nets of hierarchical net groups in the current design that match the specified criteria.",
            "get_flat_nets ?-quiet? ?-regexp | -exact? ?-nocase? ?-filter expression? ?patterns | -of_objects objects? ?-all?",
        ),
        # cat2/get_flat_pins.2
        _syn(            "get_flat_pins",
            "Creates a collection of leaf-cell pins in the current design that match the specified criteria.",
            "get_flat_pins ?-quiet? ?-regexp | -exact? ?-nocase? ?-filter expression? ?patterns | -of_objects objects? ?-all?",
        ),
        # cat2/get_generated_clocks.2
        _syn(            "get_generated_clocks",
            "Creates a collection of generated clocks.",
            "get_generated_clocks ?-quiet? ?-regexp | -exact? ?-nocase? ?-filter expression? ?patterns?",
        ),
        # cat2/get_gui_stroke_bindings.2
        _syn(            "get_gui_stroke_bindings",
            "Queries the data for stroke bindings.",
            "get_gui_stroke_bindings ?-dictionary dict_name? ?-builtin?",
        ),
        # cat2/get_latch_loop_groups.2
        _syn(            "get_latch_loop_groups",
            "Returns a list of collections of pins, each collection containing the transparent latch data pins in one latch loop group.",
            "get_latch_loop_groups ?-of_objects pin_list? ?-loop_breakers_only?",
        ),
        # cat2/get_layers.2
        _syn(            "get_layers",
            "Creates a collection of one or more layers.",
            "get_layers ?-quiet? ?-regexp | -exact? ?-nocase? ?-filter expression? ?patterns | -of_objects objects?",
        ),
        # cat2/get_lib_attribute.2
        _syn(            "get_lib_attribute",
            "Returns the value of an attribute on a list of library objects.",
            "get_lib_attribute object_list attribute_name",
        ),
        # cat2/get_license.2
        _syn(            "get_license",
            "Obtains a license for a feature.",
            "get_license feature_list ?-quantity num_licenses?",
        ),
        # cat2/get_magnet_cells.2
        _syn(            "get_magnet_cells",
            "Returns a collection of magnet cells that can be pulled closer to the specified magnet objects.",
            "get_magnet_cells magnet_objects ?-stop_by_sequential_cells? ?-exclude_buffers? ?-exclude_cells object_list? ?-logical_level level | -stop_points object_list?",
        ),
        # cat2/get_matching_nets_for_pattern.2
        _syn(            "get_matching_nets_for_pattern",
            "Gets all matching nets for a defined search pattern. The time units for the -setup_*, -hold_*, and -transition_* options should always be the same as the time unit returned by the report_units command.",
            "get_matching_nets_for_pattern -pattern id ?-setup_slack_lower_limit number? ?-setup_slack_upper_limit number? ?-hold_slack_lower_limit number? ?-hold_slack_upper_limit number? ?-transition_lower_limit number? ?-transition_upper_limit number? ?-optimizable?",
        ),
        # cat2/get_message_ids.2
        _syn(            "get_message_ids",
            "Get application message ids",
            "get_message_ids ?-type severity? ?pattern?",
        ),
        # cat2/get_message_info.2
        _syn(            "get_message_info",
            "Returns information about diagnostic messages.",
            "get_message_info ?-error_count | -warning_count | -info_count | -limit l_id | -occurrences o_id | -suppressed s_id | -id i_id?",
        ),
        # cat2/get_multibits.2
        _syn(            "get_multibits",
            "Creates a collection of one or more multibits loaded into dc_shell. You can assign these multibits to a variable or pass them into another command.",
            "get_multibits ?-quiet? ?-regexp? ?-nocase? ?-filter expression? ?patterns?",
        ),
        # cat2/get_path_groups.2
        _syn(            "get_path_groups",
            "Creates a collection of path groups that match the specified criteria.",
            "get_path_groups ?-quiet? ?-regexp? ?-nocase? ?-filter expression? patterns",
        ),
        # cat2/get_physical_hierarchy.2
        _syn(            "get_physical_hierarchy",
            "Returns a list of hierarchical cells that are physical hierarchies in the current design.",
            "get_physical_hierarchy",
        ),
        # cat2/get_placement_area.2
        _syn(            "get_placement_area",
            "Returns a list of coordinates for the current core placement area.",
            "get_placement_area",
        ),
        # cat2/get_placement_blockages.2
        _syn(            "get_placement_blockages",
            "Creates a collection of placement blockages that match the specified criteria.",
            "get_placement_blockages ?-quiet? ?-within region | -touching region | -intersect region? ?-filter expression? ?-type hard | soft | pin | hard_macro | partial? ?patterns?",
        ),
        # cat2/get_polygon_area.2
        _syn(            "get_polygon_area",
            "Calculate the area of the input polygon.",
            "get_polygon_area polygon",
        ),
        # cat2/get_power_derate.2
        _syn(            "get_power_derate",
            "Returns the power derating factors for either the current design, a list of cells or library cells.",
            "get_power_derate ?-scenarios scenario_list? ?-leakage? ?-switching? ?-internal? ?-user? ?object_list?",
        ),
        # cat2/get_power_domains.2
        _syn(            "get_power_domains",
            "Creates a collection of power domains that match the specified criteria.",
            "get_power_domains ?-quiet? ?-regexp? ?-nocase? ?-filter expression? ?-hierarchical? ?patterns | -of_objects objects?",
        ),
        # cat2/get_power_switches.2
        _syn(            "get_power_switches",
            "Creates a collection of power switches that match the specified criteria.",
            "get_power_switches ?-quiet? ?-regexp? ?-nocase? ?-filter expression? ?-hierarchical? ?patterns?",
        ),
        # cat2/get_references.2
        _syn(            "get_references",
            "Creates a collection of one or more references loaded into memory.",
            "get_references ?-hierarchical? ?-quiet? ?-regexp? ?-nocase? ?-exact? ?-filter expression? patterns",
        ),
        # cat2/get_related_supply_net.2
        _syn(            "get_related_supply_net",
            "Creates a collection of related supply nets of pins.",
            "get_related_supply_net ?pins? ?-ground?",
        ),
        # cat2/get_related_supply_set.2
        _syn(            "get_related_supply_set",
            "Creates a collection of related supply sets of signal pins or ports.",
            "get_related_supply_set ?-quiet? objects",
        ),
        # cat2/get_route_zrt_common_options.2
        _syn(            "get_route_zrt_common_options",
            "Gets the value of the specified common route option.",
            "get_route_zrt_common_options -name name_of_option",
        ),
        # cat2/get_route_zrt_global_options.2
        _syn(            "get_route_zrt_global_options",
            "Gets the value of the specified global route option.",
            "get_route_zrt_global_options -name name_of_option",
        ),
        # cat2/get_rp_groups.2
        _syn(            "get_rp_groups",
            "Creates a collection of relative placement groups that match the specified criteria.",
            "get_rp_groups ?patterns | -of_objects objects? ?-quiet? ?-nocase? ?-exact? ?-regexp? ?-ignored? ?-top?",
        ),
        # cat2/get_safety_core_groups.2
        _syn(            "get_safety_core_groups",
            "Returns a collection of safety core group names from the current design.",
            "get_safety_core_groups ?-of_objects of_objects? ?-quiet?",
        ),
        # cat2/get_safety_core_rules.2
        _syn(            "get_safety_core_rules",
            "return the names of safety core rules.",
            "get_safety_core_rules ?-of_objects of_object? ?-quiet?",
        ),
        # cat2/get_safety_error_code_groups.2
        _syn(            "get_safety_error_code_groups",
            "Returns a collection of safety error code group names from the current design.",
            "get_safety_error_code_groups ?-of_objects of_objects? ?-quiet?",
        ),
        # cat2/get_safety_error_code_rules.2
        _syn(            "get_safety_error_code_rules",
            "return the names of safety error code rules.",
            "get_safety_error_code_rules ?-of_objects of_object? ?-quiet?",
        ),
        # cat2/get_safety_register_groups.2
        _syn(            "get_safety_register_groups",
            "Gets a collection of safety register groups.",
            "get_safety_register_groups ?-of_objects cells? ?-quiet?",
        ),
        # cat2/get_safety_register_rules.2
        _syn(            "get_safety_register_rules",
            "return the names of safety register rules.",
            "get_safety_register_rules ?-of_objects registers? ?-quiet?",
        ),
        # cat2/get_scan_cell_names.2
        _syn(            "get_scan_cell_names",
            "Returns a list containing the names of scan cells for the specified option filters.",
            "get_scan_cell_names ?-view spec | existing_dft? ?-chain chain_name_list | all? ?-test_mode mode_name_list | all?",
        ),
        # cat2/get_scan_cells_of_chain.2
        _syn(            "get_scan_cells_of_chain",
            "Returns a collection containing all scan cells of the specified scan chain.",
            "get_scan_cells_of_chain -chain chain_name ?-test_mode test_mode?",
        ),
        # cat2/get_scan_chain_names.2
        _syn(            "get_scan_chain_names",
            "Returns a list containing the names of scan chains for the specified option filters.",
            "get_scan_chain_names ?-view spec | existing_dft? ?-test_mode mode_name_list | all?",
        ),
        # cat2/get_scan_chains.2
        _syn(            "get_scan_chains",
            "Returns the number of scan chains in the current design.",
            "get_scan_chains ?-test_mode test_mode?",
        ),
        # cat2/get_scenarios.2
        _syn(            "get_scenarios",
            "Returns a list of scenarios that match all of the specified criteria.",
            "get_scenarios ?-setup true | false? ?-hold true | false? ?-leakage_power true | false? ?-dynamic_power true | false? ?-active true | false? ?pattern? ?-cts_mode true | false? ?-cts_corner min | max | min_max?",
        ),
        # cat2/get_selection.2
        _syn(            "get_selection",
            "Returns a collection that contains the objects in the current selection.",
            "get_selection ?-slct_targets target_selection_bus ?-slct_targets_operation operation?? ?-create_slct_buses? ?-name selection_bus? ?-type object_type? ?-design design? ?-more_than more? ?-fewer_than fewer? ?-count? ?-num max_objects? ?-type_list?",
        ),
        # cat2/get_shift_register_chains.2
        _syn(            "get_shift_register_chains",
            "Creates a list of collections of shift-register cells in the current design, where each collection is an ordered set of shift-register chain cells.",
            "of collection get_shift_register_chains ?-quiet? ?-power_domain ignore | skip | split? ?patterns?",
        ),
        # cat2/get_site_rows.2
        _syn(            "get_site_rows",
            "Returns a collection of site rows from the current design that match the specified criteria.",
            "get_site_rows ?-quiet? ?-regexp | -exact? ?-nocase? ?-filter expression? ?-within region | -touching region | -intersect region? ?patterns?",
        ),
        # cat2/get_supply_nets.2
        _syn(            "get_supply_nets",
            "Creates a collection of supply nets that match the specified criteria.",
            "get_supply_nets ?-quiet? ?-regexp? ?-nocase? ?-filter expression? ?-hierarchical? ?patterns?",
        ),
        # cat2/get_supply_ports.2
        _syn(            "get_supply_ports",
            "Creates a collection of supply ports that match the specified criteria.",
            "get_supply_ports ?-quiet? ?-regexp? ?-nocase? ?-filter expression? ?-hierarchical? ?patterns?",
        ),
        # cat2/get_supply_sets.2
        _syn(            "get_supply_sets",
            "Creates a collection of supply sets that match the specified criteria.",
            "get_supply_sets ?-hierarchical? ?-quiet? ?-regexp? ?-exact? ?-nocase? ?-filter expression? ?-of_objects objects? ?patterns?",
        ),
        # cat2/get_switching_activity.2
        _syn(            "get_switching_activity",
            "Gets switching activity information on nets, pins, ports and cells in the current design.",
            "get_switching_activity ?-state_condition state_condition? ?-path_sources path_sources? ?-rise? ?-fall? ?-related_clock? ?-scenarios scenario_list? ?-significant_digits digits? object_list",
        ),
        # cat2/get_terminals.2
        _syn(            "get_terminals",
            "Creates a collection of terminals that match the specified criteria.",
            "get_terminals ?-quiet? ?-regexp? ?-nocase? ?-filter expression? ?patterns | -of_objects port_list?",
        ),
        # cat2/get_timing_paths.2
        #   WARNING: unmatched closing bracket ']' at position 336
        _syn(            "get_timing_paths",
            "Creates a collection of timing paths for custom reporting and other processing.",
            "get_timing_paths ?-to to_list | -rise_to rise_to_list | -fall_to fall_to_list? ?-from from_list | -rise_from rise_from_list | -fall_from fall_from_list? ?-through through_list? ?-rise_through rise_through_list? ?-fall_through fall_through_list? ?-exclude exclude_list? | -rise_exclude rise_exclude_list | -fall_exclude fall_exclude_list? ?-delay_type delay_type? ?-nworst paths_per_endpoint? ?-max_paths max_path_count? ?-enable_preset_clear_arcs? ?-group group_name? ?-greater greater_limit? ?-lesser lesser_limit? ?-slack_greater_than greater_slack_limit? ?-slack_lesser_than lesser_slack_limit? ?-include_hierarchical_pins? ?-path_type full_clock_expanded | full? ?-unique_pins? ?-start_end_pair? ?-scenarios scenario_list?",
        ),
        # cat2/get_trace_option.2
        #   WARNING: unclosed bracket '[' at position 17
        _syn(            "get_trace_option",
            "Get the current option value controlling behavior of command tracing and output annotation..",
            "get_trace_option ?-command name | -profile | -memory_threshold | -cpu_threshold | ?-annotate | -is_traced? -time_threshold",
        ),
        # cat2/get_tracks.2
        _syn(            "get_tracks",
            "Creates a collection of track objects that match the specified criteria.",
            "get_tracks ?-quiet? ?-filter expression? ?-within rectangle | -touching rectangle | -intersect rectangle | -at at_point? ?patterns | -of_objects layers?",
        ),
        # cat2/get_upf_design_attribute.2
        _syn(            "get_upf_design_attribute",
            "Returns the value of a UPF attribute set on the specified objects.",
            "get_upf_design_attribute -objects object_list -attribute attribute_name",
        ),
        # cat2/get_upf_port_attribute.2
        _syn(            "get_upf_port_attribute",
            "Returns the value of a UPF attribute set on the specified objects.",
            "get_upf_port_attribute -objects object_list -attribute attribute_name",
        ),
        # cat2/get_via_rules.2
        _syn(            "get_via_rules",
            "Returns a collection of via_rules from current library.",
            "get_via_rules ?-filter expression? ?-quiet? ?-regexp? ?-nocase? ?-exact? ?-expect exact_count? ?-expect_at_least minimum_count? ?-expect_each_pattern_matches? ?patterns?",
        ),
        # cat2/get_zero_interconnect_delay_mode.2
        _syn(            "get_zero_interconnect_delay_mode",
            "Reports whether or not the timer is currently using zero interconnect delay mode.",
            "get_zero_interconnect_delay_mode",
        ),
        # cat2/getenv.2
        _syn(            "getenv",
            "Returns the value of a system environment variable.",
            "getenv variable_name",
        ),
        # cat2/group.2
        _syn(            "group",
            "Creates a new level of hierarchy.",
            "group ?cell_list | -logic | -pla | -fsm? ?-soft | -hdl_block block_name | -hdl_all_blocks | -hdl_bussed? ?-design_name design_name? ?-cell_name cell_name? ?-except exclude_list?",
        ),
        # cat2/group_variable.2
        _syn(            "group_variable",
            "Adds a variable to the specified variable group. This command is typically used only by the system administrator.",
            "group_variable group_name variable_name",
        ),
        # cat2/gui_add_annotation.2
        _syn(            "gui_add_annotation",
            "Adds an annotation to the layout window.",
            "gui_add_annotation ?-window window_name? ?-group group_type? ?-type shape_type? ?-symbol_type symbol_type? ?-symbol_size symbol_size? ?-text text? ?-color color? ?-pattern pattern? ?-width line_width? ?-line_style line_style? ?-visible visible? ?-info_tip info_tip? ?-query_text query_text? ?-query_command query_command? ?-radius radius? points",
        ),
        # cat2/gui_append_utable.2
        _syn(            "gui_append_utable",
            "Append data rows to an existing UserTable.",
            "gui_append_utable -name Name -rows TCL_Data_List -import File_Name ?-val_map ...? ?-col_map ...? ?-tsv_mode? ?-ssv_mode? -val_map Column_Value_Map -col_map Column_Value_Map ?-tsv_mode? ?-ssv_mode? -val_map Column_Value_Map -col_map Column_Value_Map ?-tsv_mode? ?-ssv_mode? -column Name ?-expr col_expr?",
        ),
        # cat2/gui_bin.2
        _syn(            "gui_bin",
            "Organizes a collection of objects into bins.",
            "gui_bin -clct Clct ?-attr Attribute | -cmd Command? ?-lower_bound Lower_Bound? ?-lower_bound_strict? ?-upper_bound Upper_Bound? ?-upper_bound_strict? ?-boundary Boundary? ?-num_bins Number_of_Bins | -bin_range Range_per_Bin? ?-underflow? ?-overflow? ?-nice_level Nice_Level? ?-small_is_good? ?-exact_binning? ?-ignore_values Ignore_List? ?-bar_brush Brush_Pattern? ?-create_slct_buses? ?-filter_cmd Filter_Command? ?-numBin numBins? ?-return_values? ?-slct_targets Selection_Targets? ?-slct_targets_operation Selection_Operation? ?-value_list Element_Value_List?",
        ),
        # cat2/gui_change_highlight.2
        _syn(            "gui_change_highlight",
            "Manipulate the set of globally highlighted objects.",
            "gui_change_highlight ?-add | -remove | -toggle? ?-color color_id | -all_colors? ?-collection clct?",
        ),
        # cat2/gui_close_utable.2
        _syn(            "gui_close_utable",
            "Close and free the given list of UserTables in memory.",
            "gui_close_utable -names Table_Names",
        ),
        # cat2/gui_close_window.2
        _syn(            "gui_close_window",
            "Close the specified window",
            "gui_close_window { -window window_id | -type window_type | -all } ?-exact_type_match?",
        ),
        # cat2/gui_create_attrgroup.2
        _syn(            "gui_create_attrgroup",
            "Creates a group of attributes for an object type.",
            "gui_create_attrgroup -class design_object -name name ?-attr_list {{attr_1}...{attr_n}}?",
        ),
        # cat2/gui_create_category_rule.2
        _syn(            "gui_create_category_rule",
            "Creates a category rule for automatic generation of one or more object categories.",
            "gui_create_category_rule ?-name rule_name? ?-filter filter_spec? -category category_spec ?-builtin?",
        ),
        # cat2/gui_create_menu.2
        _syn(            "gui_create_menu",
            "Create a menu item for the toplevel menubar or a context menu item. A menu hierarchy, based on the menu name, may be created as necessary to host the menu item.",
            "gui_create_menu -menu HierMenuName <-tcl_cmd TclCmd|-separator|-heading headingText> ?-enable_cmd EnableCmd? ?-get_state_cmd GetStateCmd? ?-icon IconFilePath? ?-hot_key HotKey? ?-tooltip ToolTip? ?-help_string HelpStr? ?-anchor_item AnchorItem? ?-anchor_offset AnchorOffset? ?-position MenuPos? ?-window_type WindowTypeName? ?-root ContextMenuRoot? ?-reference RefMenuItem?",
        ),
        # cat2/gui_create_pref_category.2
        _syn(            "gui_create_pref_category",
            "Create a preference category.",
            "gui_create_pref_category -category Category",
        ),
        # cat2/gui_create_pref_key.2
        _syn(            "gui_create_pref_key",
            "Create a preference key.",
            "gui_create_pref_key -key Key -value_type ValueType -value Value ?-category Category? ?-keep_value_if_exist? ?-read_only? ?-description Description? ?-min Minimum_Value? ?-max Maximum_Value? ?-legal_value_list Value_List? ?-string_to_int_map Value_Map? ?-save_on_exit Boolean_Value?",
        ),
        # cat2/gui_create_schematic.2
        _syn(            "gui_create_schematic",
            "Creates a schematic view.",
            "gui_create_schematic ?-clct objects? ?-size {w h}? ?-be_specific bool?",
        ),
        # cat2/gui_create_task.2
        _syn(            "gui_create_task",
            "Create a task.",
            "gui_create_task -task TaskName -item_root ItemRootName ?-default?",
        ),
        # cat2/gui_create_task_item.2
        _syn(            "gui_create_task_item",
            "Create an item in the task tree to access in the Task Assistant.",
            "gui_create_task_item -name ItemName -task TaskName | -item_root ItemRootName -page PageName ?-search_terms TermsList?",
        ),
        # cat2/gui_create_tk_palette_type.2
        _syn(            "gui_create_tk_palette_type",
            "Creates a user configurable main window palette type.",
            "gui_create_tk_palette_type {-type type_name} {-title palette_title} {-window_types window_type_list} {-create_command tcl_command} ?-dock_edge left | right | top | bottom? ?-icon string?",
        ),
        # cat2/gui_create_toolbar.2
        _syn(            "gui_create_toolbar",
            "Create a toolbar with the specified name.",
            "gui_create_toolbar -name ToolBarName ?-title Title? ?-dock_side DockSide? ?-hidden? ?-window_type WindowTypeName?",
        ),
        # cat2/gui_create_toolbar_item.2
        _syn(            "gui_create_toolbar_item",
            "Create a button in the specified toolbar.",
            "gui_create_toolbar_item -toolbar ToolBarName <-menu MenuName|-separator SeparatorName> ?-window_type WindowTypeName? ?-dropdown_menu MenuName? ?-dropdown_icon IconName?",
        ),
        # cat2/gui_create_utable.2
        _syn(            "gui_create_utable",
            "Create a new UserTable.",
            "gui_create_utable -name Table_Name -parent Table_Name -columns Column_List -timing_path Tim_Clct ?-expr_columns Column_Expr_List? ?-meta_obj MetaObj_Name? ?-replace? ?-fixed_name?",
        ),
        # cat2/gui_create_window.2
        _syn(            "gui_create_window",
            "Creates a window of the specified window type.",
            "gui_create_window -type window_type ?-parent parent_window_id? ?-show_state window_state? ?-title title? ?-rect rect | -size {width height}? ?-icon icon?",
        ),
        # cat2/gui_create_window_toolbar_type.2
        _syn(            "gui_create_window_toolbar_type",
            "Create new type for view toolbar",
            "gui_create_window_toolbar_type -type string ?-name string? ?-icon string? -view_types string_list -command string ?-apply?",
        ),
        # cat2/gui_delete_attrgroup.2
        _syn(            "gui_delete_attrgroup",
            "Removes a group of attributes or all attribute groups for an object type.",
            "gui_delete_attrgroup -class design_object -name name ?-all? ?-quiet?",
        ),
        # cat2/gui_delete_menu.2
        _syn(            "gui_delete_menu",
            "Delete a menu item for the toplevel menubar or a context menu",
            "gui_delete_menu ?-menu HierMenuName | -all? ?-window_type WindowTypeName | -root ContextMenuRoot?",
        ),
        # cat2/gui_delete_toolbar.2
        _syn(            "gui_delete_toolbar",
            "Delete a toolbar with the specified name.",
            "gui_delete_toolbar -name ToolBarName ?-window_type WindowTypeName?",
        ),
        # cat2/gui_delete_toolbar_item.2
        _syn(            "gui_delete_toolbar_item",
            "Remove a toolbar button specified by the menu name from the specified toolbar.",
            "gui_delete_toolbar_item -toolbar ToolBarName <-menu MenuName|-separator SeparatorName> ?-window_type WindowTypeName?",
        ),
        # cat2/gui_eval_command.2
        _syn(            "gui_eval_command",
            "Executes and optionally logs a tool command language (Tcl) command.",
            "gui_eval_command -command command ?-echo? ?-history? ?-honor_preview | -preview?",
        ),
        # cat2/gui_execute_menu_item.2
        _syn(            "gui_execute_menu_item",
            "Execute a menu item in the currently active window.",
            "gui_execute_menu_item { -menu menu_item_id }",
        ),
        # cat2/gui_exist_pref_category.2
        _syn(            "gui_exist_pref_category",
            "Check the existence of a preference category.",
            "gui_exist_pref_category -category Category",
        ),
        # cat2/gui_exist_pref_key.2
        _syn(            "gui_exist_pref_key",
            "Check the existence of a preference key.",
            "gui_exist_pref_key -key Key ?-category Category?",
        ),
        # cat2/gui_exist_window.2
        _syn(            "gui_exist_window",
            "Check for the existence of specified window or window type",
            "gui_exist_window { -window window_id | -type window_type } ?-parent window_id?",
        ),
        # cat2/gui_export_utable.2
        _syn(            "gui_export_utable",
            "Export the UserTable to a value file.",
            "gui_export_utable -name Table_Name ?-file File_Name ?-tsv_mode? ?-ssv_mode?? ?-tsv_mode? ?-ssv_mode? ?-filter Filter? ?-tsv_mode? ?-ssv_mode? ?-add_col_type? ?-add_metadata? ?-overwrite?",
        ),
        # cat2/gui_fill_utable.2
        _syn(            "gui_fill_utable",
            "Fill generated data rows to an existing UserTable.",
            "gui_fill_utable -name Name -file_column Name -file_suffix Suffix -file_dir Directory -label_column Name -label_value Value -date_column Name -tag_column Name -title_column Name",
        ),
        # cat2/gui_foreach_utable_row.2
        _syn(            "gui_foreach_utable_row",
            "Iterate/visit the given table row column values for the given filter and call a TCL proc.",
            "gui_foreach_utable_row -name Table_Name -action Action -columns Column_List ?-filter Filter_Expr? ?-data Data?",
        ),
        # cat2/gui_get_annotations.2
        _syn(            "gui_get_annotations",
            "Return a collection of layout annotations",
            "gui_get_annotations ?-window window_name? ?-group group_id? ?-within region? ?-intersect? ?-at location? ?-filter filter? ?-nocase? ?-regexp? string window_name string group_name string filter rectangle region location point",
        ),
        # cat2/gui_get_bucket_option.2
        _syn(            "gui_get_bucket_option",
            "Returns the value of an option for a bucket in the specified visual mode or map mode.",
            "gui_get_bucket_option -map map_name -bucket bucket_name -option option_name ?-default?",
        ),
        # cat2/gui_get_bucket_option_list.2
        _syn(            "gui_get_bucket_option_list",
            "Lists the available options for buckets in the specified visual mode or map mode.",
            "gui_get_bucket_option_list -map map_name",
        ),
        # cat2/gui_get_cell_block_marks.2
        _syn(            "gui_get_cell_block_marks",
            "Gets a list of the block mark string values on one or more cells.",
            "gui_get_cell_block_marks cells",
        ),
        # cat2/gui_get_current_task.2
        _syn(            "gui_get_current_task",
            "Get the name of the current task.",
            "gui_get_current_task",
        ),
        # cat2/gui_get_current_task_item.2
        _syn(            "gui_get_current_task_item",
            "Get the name of the current task item.",
            "gui_get_current_task_item",
        ),
        # cat2/gui_get_current_task_page.2
        _syn(            "gui_get_current_task_page",
            "Get the name of the current task page.",
            "gui_get_current_task page",
        ),
        # cat2/gui_get_current_window.2
        _syn(            "gui_get_current_window",
            "Retrieves the window ID of the active top-level or view window.",
            "gui_get_current_window ?-toplevel | -view | -parent parent_window_id? ?-hier_name? ?-types window_type_list? ?-mru?",
        ),
        # cat2/gui_get_highlight.2
        _syn(            "gui_get_highlight",
            "Get a collection of highlighted objects.",
            "gui_get_highlight ?-color color_id | -all_colors? ?-return_select_bus | -more_than?",
        ),
        # cat2/gui_get_highlight_options.2
        _syn(            "gui_get_highlight_options",
            "Query the options that control highlighting.",
            "gui_get_highlight_options ?-current_color | -all_colors | -auto_cycle_color?",
        ),
        # cat2/gui_get_map.2
        _syn(            "gui_get_map",
            "Retrieves attributes for a specified map mode.",
            "gui_get_map -name identifier ?-buckets? ?-title? ?-help_topic? ?-infotip? ?-discrete? ?-icon_file? ?-update_cmd? ?-float? ?-top_exaggeration? ?-mid_exaggeration? ?-bot_exaggeration?",
        ),
        # cat2/gui_get_map_list.2
        _syn(            "gui_get_map_list",
            "Lists the current visual and map modes.",
            "gui_get_map_list",
        ),
        # cat2/gui_get_map_option.2
        _syn(            "gui_get_map_option",
            "Returns the value of an option for the specified visual mode or map mode.",
            "gui_get_map_option -map map_name -option option_name ?-default?",
        ),
        # cat2/gui_get_map_option_list.2
        _syn(            "gui_get_map_option_list",
            "Lists the available options for the specified visual mode or map mode.",
            "gui_get_map_option_list -map map_name",
        ),
        # cat2/gui_get_mapbucket.2
        _syn(            "gui_get_mapbucket",
            "Gets attributes for Map Mode Bucket",
            "gui_get_mapbucket -map mode_identifier -name bucket_identifier ?-infotip? ?-color? ?-pattern? ?-exaggeration? ?-number? ?-maxval? ?-minval? ?-visible? ?-special? ?-title? ?-objcount?",
        ),
        # cat2/gui_get_mouse_tool_option.2
        _syn(            "gui_get_mouse_tool_option",
            "Get the value of a mouse tool option",
            "gui_get_mouse_tool_option -tool string -option string string string string string",
        ),
        # cat2/gui_get_pref_keys.2
        _syn(            "gui_get_pref_keys",
            "Return a list of preference keys under the specified category.",
            "gui_get_pref_keys -category Category",
        ),
        # cat2/gui_get_pref_value.2
        _syn(            "gui_get_pref_value",
            "Get the value of a preference key.",
            "gui_get_pref_value -key Key ?-category Category?",
        ),
        # cat2/gui_get_presets.2
        _syn(            "gui_get_presets",
            "Gets list of preset name for object specified by category",
            "gui_get_presets -category category ?-system? ?-shared?",
        ),
        # cat2/gui_get_region.2
        _syn(            "gui_get_region",
            "Returns the coordinates of the current region rectangle or rectilinear polygon.",
            "gui_get_region",
        ),
        # cat2/gui_get_setting.2
        _syn(            "gui_get_setting",
            "Gets a setting on the specified window.",
            "gui_get_setting -window WindowID {-setting Setting | -list}",
        ),
        # cat2/gui_get_task_list.2
        _syn(            "gui_get_task_list",
            "Lists all the available task names.",
            "gui_get_task_list",
        ),
        # cat2/gui_get_task_page.2
        _syn(            "gui_get_task_page",
            "Return the name of the task page for the given task item.",
            "gui_get_task_page",
        ),
        # cat2/gui_get_toolbar_names.2
        _syn(            "gui_get_toolbar_names",
            "Return a Tcl list of the names of all the toolbars that have been created with the gui_create_toolbar command.",
            "gui_get_toolbar_names ?-window WindowId?",
        ),
        # cat2/gui_get_utable.2
        _syn(            "gui_get_utable",
            "Get various state about User Table(s) [default: return list of all table names].",
            "gui_get_utable -name Table_Name -has_name -headers -tag -window Window_name -values Column_Name -bus_values Column_Name -rows -parent -filter -columns",
        ),
        # cat2/gui_get_window_ids.2
        _syn(            "gui_get_window_ids",
            "Get a list of window ids",
            "gui_get_window_ids ?-parent window_id? ?-type window_type?",
        ),
        # cat2/gui_get_window_pref_categories.2
        _syn(            "gui_get_window_pref_categories",
            "Get list of preference categories for object specified by window",
            "gui_get_window_pref_categories {-window window_id | -window_type window_type}",
        ),
        # cat2/gui_get_window_pref_keys.2
        _syn(            "gui_get_window_pref_keys",
            "Get list of preference categories for object specified by window",
            "gui_get_window_pref_keys {-window window_id | -window_type window_type} ?-category category?",
        ),
        # cat2/gui_get_window_pref_value.2
        _syn(            "gui_get_window_pref_value",
            "Get preference value for object specified by window or window type",
            "gui_get_window_pref_value {-window window_id | -window_type window_type} ?-category category? -key key",
        ),
        # cat2/gui_get_window_presets.2
        _syn(            "gui_get_window_presets",
            "Gets list of preset name for object specified by window_type",
            "gui_get_window_presets -window_type window_type ?-system? ?-shared?",
        ),
        # cat2/gui_get_window_types.2
        _syn(            "gui_get_window_types",
            "Get a list of window types",
            "gui_get_window_types ?-type token?",
        ),
        # cat2/gui_hide_palette.2
        _syn(            "gui_hide_palette",
            "Hides the specified palette.",
            "gui_hide_palette { -name palette_id | -type palette_type | -all } ?-parent window_id?",
        ),
        # cat2/gui_hide_toolbar.2
        _syn(            "gui_hide_toolbar",
            "Hides the specified toolbar or all the toolbars in the specified window or for a window type.",
            "gui_hide_toolbar -toolbar tool_bar_name | -all ?-window window_id? ?-window_type window_type?",
        ),
        # cat2/gui_import_utable.2
        _syn(            "gui_import_utable",
            "Create a UserTable and import records from a value file or a report.",
            "gui_import_utable -file File_Name ?-tsv_mode? ?-ssv_mode? ?-tsv_mode? ?-ssv_mode? ?-name Table_Name? ?-tsv_mode? ?-ssv_mode? ?-fold? ?-report_type Report_Type_Name? ?-meta_obj MetaObj_Name? ?-replace?",
        ),
        # cat2/gui_inspect_violations.2
        _syn(            "gui_inspect_violations",
            "Displays the specified DFT unified DRC violations in a new violation inspector window.",
            "gui_inspect_violations ?-type violation_type? violation_list",
        ),
        # cat2/gui_list_attrgroups.2
        _syn(            "gui_list_attrgroups",
            "Lists attribute group information for a specified object type or all object types.",
            "gui_list_attrgroups -class design_object -name name ?-all? ?-tcl? ?-full? ?-attr_list?",
        ),
        # cat2/gui_list_category_rules.2
        _syn(            "gui_list_category_rules",
            "Lists all category rules except built-in rules by default.",
            "gui_list_category_rules ?-all | -names rule_names_list? ?-format script | tcl_list?",
        ),
        # cat2/gui_list_cell_block_marks.2
        _syn(            "gui_list_cell_block_marks",
            "Lists the cell names and block mark values for cells that are marked in the design.",
            "gui_list_cell_block_marks",
        ),
        # cat2/gui_load_cell_density_mm.2
        _syn(            "gui_load_cell_density_mm",
            "Loads the data for cell density map mode.",
            "gui_load_cell_density_mm ?-area area?",
        ),
        # cat2/gui_load_hierarchy_vm.2
        _syn(            "gui_load_hierarchy_vm",
            "Loads the data for hierarchy visual mode.",
            "gui_load_hierarchy_vm -clear -level ncount -cells cell_list",
        ),
        # cat2/gui_load_pin_density_mm.2
        _syn(            "gui_load_pin_density_mm",
            "Loads the data for pin density map mode.",
            "gui_load_pin_density_mm ?-area area?",
        ),
        # cat2/gui_load_voltage_area_vm.2
        _syn(            "gui_load_voltage_area_vm",
            "Loads the data for voltage area visual mode.",
            "gui_load_voltage_area_vm",
        ),
        # cat2/gui_merge_utable.2
        _syn(            "gui_merge_utable",
            "Merge 2 (loaded) tables via the given join column(s).",
            "gui_merge_utable -name Table_Name -merge_table Table_Name -join_columns Column_Names ?-output_table Table_Name? ?-columns Column_Names?",
        ),
        # cat2/gui_mouse_tool.2
        _syn(            "gui_mouse_tool",
            "Operate mouse tools of a given view",
            "gui_mouse_tool -window window ?-start tool | -current | -list | -add_point {x y} | -drag {{x1 y1} {x2 y2}} | -delete_point | -apply | -reset | -cancel | -cycle | -cycle_back? window String tool String",
        ),
        # cat2/gui_open_utable.2
        _syn(            "gui_open_utable",
            "Open the given UserTable file.",
            "gui_open_utable -file File_Name ?-read_only?",
        ),
        # cat2/gui_overlay_layout.2
        _syn(            "gui_overlay_layout",
            "Add/Remove/Adjust a design overlay to a layout window",
            "gui_overlay_layout -window windowID -design design -add -remove -brightness value windowID String design String add Boolean flag remove Boolean flag brightness Integer",
        ),
        # cat2/gui_query_objects.2
        _syn(            "gui_query_objects",
            "Get the value of a query text for a collection of object.",
            "gui_query_objects object_collection",
        ),
        # cat2/gui_remove_all_annotations.2
        _syn(            "gui_remove_all_annotations",
            "Removes specified group of annotations or all annotations from the specified layout window or from all windows.",
            "gui_remove_all_annotations ?-window window_name? ?-group group_name?",
        ),
        # cat2/gui_remove_all_rulers.2
        _syn(            "gui_remove_all_rulers",
            "Removes rulers from the specified layout window or from all windows.",
            "gui_remove_all_rulers ?-window window_name?",
        ),
        # cat2/gui_remove_annotations.2
        _syn(            "gui_remove_annotations",
            "Removes specified group of annotations from the specified layout window.",
            "gui_remove_annotations ?-window window_name? ?-group group_name? ?anno?",
        ),
        # cat2/gui_remove_category_rules.2
        _syn(            "gui_remove_category_rules",
            "Removes all category rules except built-in rules by default.",
            "gui_remove_category_rules ?-all | -names rule_names_list?",
        ),
        # cat2/gui_remove_cell_block_marks.2
        _syn(            "gui_remove_cell_block_marks",
            "Removes the block mark string values from one or more cells.",
            "gui_remove_cell_block_marks -all | cells",
        ),
        # cat2/gui_remove_pref_key.2
        _syn(            "gui_remove_pref_key",
            "Remove a preference key.",
            "gui_remove_pref_key -key Key ?-category Category?",
        ),
        # cat2/gui_remove_ruler.2
        _syn(            "gui_remove_ruler",
            "Removes the specified rulers.",
            "gui_remove_ruler ?-window window_name? -point point | -all",
        ),
        # cat2/gui_report_hotkeys.2
        _syn(            "gui_report_hotkeys",
            "Report on the current hotkey bindings",
            "gui_report_hotkeys ?-window_type WindowTypeName?",
        ),
        # cat2/gui_report_task.2
        _syn(            "gui_report_task",
            "task.",
            "gui_report_task -task string | -item_root TaskName | ItemRootName ?-file string?",
        ),
        # cat2/gui_schematic_add_logic.2
        _syn(            "gui_schematic_add_logic",
            "Adds logic to a schematic",
            "gui_schematic_add_logic ?-window <win>? ?-new? ?-schematic <schem>? objs string <win> string <schem> string objs",
        ),
        # cat2/gui_schematic_remove_logic.2
        _syn(            "gui_schematic_remove_logic",
            "Removes logic from a schematic",
            "gui_schematic_remove_logic ?-schematic <schem>? objs string <schem> string objs",
        ),
        # cat2/gui_scroll.2
        _syn(            "gui_scroll",
            "Scroll a window's viewport.",
            "gui_scroll -window window ?-selection | -clct clct | ?-habs absX | -hrel relX? ?-vabs absY | -vrel relY?? window String absX Float relX Float absY Float relY Float",
        ),
        # cat2/gui_select_vmbucket.2
        _syn(            "gui_select_vmbucket",
            "Select the Contents of a Visual Mode Bucket",
            "gui_select_vmbucket -vmname mode_identifier -name bucket_identifier ?-replace | -add | -remove? string mode_identifier string bucket_identifier",
        ),
        # cat2/gui_selection_stack.2
        _syn(            "gui_selection_stack",
            "Command to manipulate selection stack",
            "gui_selection_stack {-push | -pop | -clear | -get n | -remove n | -list}",
        ),
        # cat2/gui_set_active_window.2
        _syn(            "gui_set_active_window",
            "Make the specified window the active window",
            "gui_set_active_window -window window_id",
        ),
        # cat2/gui_set_bucket_option.2
        _syn(            "gui_set_bucket_option",
            "Sets the value for an option on a bucket in the specified visual mode or map mode.",
            "gui_set_bucket_option -map map_name -bucket bucket_name -option option_name -value value | -default",
        ),
        # cat2/gui_set_cell_block_marks.2
        _syn(            "gui_set_cell_block_marks",
            "Sets a block mark on one or more cells.",
            "gui_set_cell_block_marks cells block_mark",
        ),
        # cat2/gui_set_current_task.2
        _syn(            "gui_set_current_task",
            "Set current task to the given task.",
            "gui_set_current_task -task task_name",
        ),
        # cat2/gui_set_highlight_options.2
        _syn(            "gui_set_highlight_options",
            "Change the options that control highlighting.",
            "gui_set_highlight_options ?-current_color color_id | -next_color | -auto_cycle_color enable?",
        ),
        # cat2/gui_set_hotkey.2
        _syn(            "gui_set_hotkey",
            "Sets a key binding to a Tcl command or a menu command in a GUI window.",
            "gui_set_hotkey -hot_key key_name -tcl_cmd command_name | -menu menu_name ?-replace? ?-delete? ?-replay_log_only? ?-window_type window_type_name | -all_window_types? key_name string command_name string menu_name string window_type_name string",
        ),
        # cat2/gui_set_layout_user_command.2
        _syn(            "gui_set_layout_user_command",
            "Set user defined command for layout input.",
            "gui_set_layout_user_command -apply_cmd TclCmd | -clear ?-input_type InputType? ?-snap_type SnapType? ?-status_text string? ?-cancel_cmd TclCmd?",
        ),
        # cat2/gui_set_map_option.2
        _syn(            "gui_set_map_option",
            "Sets the value for an option in the specified visual mode or map mode.",
            "gui_set_map_option -map map_name -option option_name -value value | -default",
        ),
        # cat2/gui_set_mouse_tool_option.2
        _syn(            "gui_set_mouse_tool_option",
            "Set an option on a mouse tool",
            "gui_set_mouse_tool_option -tool string -option string -value string string string string string string string",
        ),
        # cat2/gui_set_pref_value.2
        _syn(            "gui_set_pref_value",
            "Set the value of a preference key.",
            "gui_set_pref_value -key Key -value Value ?-category Category?",
        ),
        # cat2/gui_set_preset.2
        _syn(            "gui_set_preset",
            "Sets the specified preset for object specified by category",
            "gui_set_preset -category category ?-system? ?-shared? -default -name name",
        ),
        # cat2/gui_set_region.2
        _syn(            "gui_set_region",
            "Sets the coordinates of the current region rectangle or rectilinear polygon.",
            "gui_set_region shape",
        ),
        # cat2/gui_set_setting.2
        _syn(            "gui_set_setting",
            "Sets a setting on the specified window.",
            "gui_set_setting -window WindowID -setting Setting -value Value",
        ),
        # cat2/gui_set_task_list.2
        _syn(            "gui_set_task_list",
            "Set the list of tasks that are visible in the task assistant, and set their order.",
            "gui_set_task_list -tasks TaskList",
        ),
        # cat2/gui_set_timing_table_paths.2
        _syn(            "gui_set_timing_table_paths",
            "Set timing paths into a specified timing table.",
            "gui_set_timing_table_paths ?-command ACmd? ?-window AWindow? ?-new? ?-name ATable?",
        ),
        # cat2/gui_set_utable.2
        _syn(            "gui_set_utable",
            "Set various state about User Tables.",
            "gui_set_utable ?-name Table_Name? ?-parent Table_Name? ?-tag Report_Tag? ?-title Report_Title? ?-comment Report_Comment? ?-menu Root_Menu? ?-prefix Prefix_Char ?-column Column_Name?? ?-action TCL_Expr -column Column_Name -link Link_Text? ?-create_hook TCL_Proc? ?-close_hook TCL_Proc? ?-enter_hook TCL_Proc? ?-exit_hook TCL_Proc? ?-select_hook TCL_Proc? ?-sel_action TCL_Proc? ?-dsel_action TCL_Proc? ?-window Window_name? ?-filter Filter_Expr?",
        ),
        # cat2/gui_set_utable_meta.2
        _syn(            "gui_set_utable_meta",
            "Create a MetaData Object for use in creating a new UserTable.",
            "gui_set_utable_meta -name MetaDataObj_Name ?-remove? ?-title Report_Title? ?-comment Report_Comment? ?-tag Report_Tag? ?-menu Root_Menu? ?-col_name Column_Name? ?-col_type Column_Type? ?-read_only? ?-hidden? ?-user_enums Column_Type_Enums? ?-user_list Column_Type_List?",
        ),
        # cat2/gui_set_utable_values.2
        _syn(            "gui_set_utable_values",
            "Set the given UserTable values in the given column(s) and the filtered set of rows.",
            "gui_set_utable_values -name Table_Name -columns Column_List -values Value_List ?-filter Filter_Expr?",
        ),
        # cat2/gui_set_window_pref_key.2
        _syn(            "gui_set_window_pref_key",
            "Create a preference key owned by a particular window or window type",
            "gui_set_window_pref_key {-window window_id | -window_type window_type} ?-category category? -key key -value_type value_type -value value",
        ),
        # cat2/gui_set_window_preset.2
        _syn(            "gui_set_window_preset",
            "Sets the specified preset for object specified by window_type",
            "gui_set_window_preset -window_type window_type ?-system? ?-shared? -default -preset preset",
        ),
        # cat2/gui_show_file_in_editor.2
        _syn(            "gui_show_file_in_editor",
            "Show the contents of a file in an external text editor.",
            "gui_show_file_in_editor -filename filename ?-line linenum?",
        ),
        # cat2/gui_show_man_page.2
        _syn(            "gui_show_man_page",
            "Show a man page in the man browser",
            "gui_show_man_page ?-apropos? ?topic?",
        ),
        # cat2/gui_show_map.2
        _syn(            "gui_show_map",
            "Displays or hides the specified visual mode or map mode.",
            "gui_show_map -map map_name -show true | false ?-window window?",
        ),
        # cat2/gui_show_palette.2
        _syn(            "gui_show_palette",
            "Shows the palette in the specified window state.",
            "gui_show_palette { -name palette_id | -type palette_type } ?-parent parent_name? ?-show_state window_state? ?-dock_edge dock_edge? ?-size {width height}?",
        ),
        # cat2/gui_show_toolbar.2
        _syn(            "gui_show_toolbar",
            "Displays the specified toolbar or all the toolbars in the specified window or for a window type.",
            "gui_show_toolbar -toolbar tool_bar_name | -all ?-window window_id? ?-window_type window_type?",
        ),
        # cat2/gui_show_url_in_browser.2
        _syn(            "gui_show_url_in_browser",
            "Show the contents of a URL in an external web browser.",
            "gui_show_url_in_browser -url URL",
        ),
        # cat2/gui_show_window.2
        _syn(            "gui_show_window",
            "Show the window in the specified window state",
            "gui_show_window -window window_id ?-show_state window_state? ?{ -rect rect | -size isize }?",
        ),
        # cat2/gui_start.2
        _syn(            "gui_start",
            "Starts the application GUI.",
            "gui_start ?-file script? ?-no_windows? ?-offscreen 1 | 0?",
        ),
        # cat2/gui_stop.2
        _syn(            "gui_stop",
            "Stops the application GUI.",
            "gui_stop ?-close?",
        ),
        # cat2/gui_update_attrgroup.2
        _syn(            "gui_update_attrgroup",
            "Updates a group of attributes for an object type.",
            "gui_update_attrgroup -class design_object -name name ?-attr_list {{attr_1}...{attr_n}}? ?-add? ?-delete? ?-move up | down | top | bottom | after | before? ?-attr attribute? ?-anchor attribute?",
        ),
        # cat2/gui_update_pref_file.2
        _syn(            "gui_update_pref_file",
            "Save current application preferences to the user preference file.",
            "gui_update_pref_file ?-file FilePathName?",
        ),
        # cat2/gui_view_port_history.2
        _syn(            "gui_view_port_history",
            "Does the gui_view_port_history operations.",
            "gui_view_port_history ?-window window_name? ?-next? ?-previous? ?-add name? ?-to name? ?-list_names? ?-rect bounding box? ?-delete_name? ?-isprevious? ?-isnext? ?-dialog? ?-tcl_list? ?-help_cmd?",
        ),
        # cat2/gui_violation_schematic_add_objects.2
        _syn(            "gui_violation_schematic_add_objects",
            "Adds the specified objects to the violation schematic in a violation inspector window.",
            "gui_violation_schematic_add_objects ?-window window_name? ?-clct? object_list",
        ),
        # cat2/gui_wave_add_signal.2
        _syn(            "gui_wave_add_signal",
            "Adds the specified signals to the waveform view in a violation inspector window.",
            "gui_wave_add_signal ?-window window_name? ?-clct? object_list",
        ),
        # cat2/gui_write_layout_image.2
        _syn(            "gui_write_layout_image",
            "Save a layout image in a file",
            "gui_write_layout_image -output file_name ?-window window_title? ?-view_only?",
        ),
        # cat2/gui_write_utable.2
        _syn(            "gui_write_utable",
            "Write the UserTable to file in native UserTable format.",
            "gui_write_utable -name Table_Name ?-file File_Name? ?-filter Filter? ?-read_only? ?-overwrite?",
        ),
        # cat2/gui_write_window_image.2
        _syn(            "gui_write_window_image",
            "Saves an image of a view or toplevel window in the specified file",
            "gui_write_window_image ?-file filename? ?-format image_format? ?-window window_name? ?-palette palette_type? ?-size window_size? ?-clip?",
        ),
        # cat2/gui_zoom.2
        _syn(            "gui_zoom",
            "Change the viewport of a view",
            "gui_zoom -window window ?-fit | -exact? ?-full? ?-selection? ?-rect {{lx ly} {ux uy}}? ?-factor factor? ?-at_point {x y}? ?-clct clct? ?-zoom_in_mode? ?-zoom_out_mode? ?-select_mode? window String rect String factor Float",
        ),
        # cat2/gui_zoom_all_layouts_to_current_view.2
        _syn(            "gui_zoom_all_layouts_to_current_view",
            "Rescales all layout views to the current view.",
            "gui_zoom_all_layouts_to_current_view",
        ),
        # cat2/help.2
        _syn(            "help",
            "Displays quick help for one or more commands.",
            "help ?-verbose? ?-groups? ?pattern?",
        ),
        # cat2/history.2
        _syn(            "history",
            "Displays or modifies the commands recorded in the history list.",
            "history ?-h? ?-r? ?argument_list?",
        ),
        # cat2/identify_clock_gating.2
        _syn(            "identify_clock_gating",
            "Identifies Power Compiler-inserted clock-gating circuitry in a structural netlist.",
            "identify_clock_gating ?-gating_elements cell_collection?",
        ),
        # cat2/identify_register_banks.2
        _syn(            "identify_register_banks",
            "Identifies register banking opportunities and writes out a register banking script. This command is supported only in Design Compiler topographical mode.",
            "identify_register_banks -output_file file_name ?-input_map_file file_name? ?-register_group_file file_name? ?-exclude_instances exclude_cells? ?-wns_threshold percentage? ?-name_prefix prefix? ?-multibit_components_only?",
        ),
        # cat2/if.2
        _syn(            "if",
            "Conditional execution control structure.",
            "if",
        ),
        # cat2/import_ndm_block.2
        _syn(            "import_ndm_block",
            "Imports one or more IC Compiler II block abstracts as DCNXT block abstractions",
            "import_ndm_block -blocks block_names ?-output_dir ddc_cache_dir? ?-setup_script library_setup_script?",
        ),
        # cat2/index_collection.2
        _syn(            "index_collection",
            "Given a collection and an index into it, if the index is in range, create a new collection containing only the single object at the index in the base collection. The base collection remains unchanged. Optionally, a second index can be passed which creates a new collection with the objects between the two indices in the base collection. Makes an implicit assumption that index<=index2",
            "index_collection collection1 index index2 ?step?",
        ),
        # cat2/infer_switching_activity.2
        _syn(            "infer_switching_activity",
            "Infers and sets the switching activity annotation on drivers of special pins of the current design.",
            "infer_switching_activity ?-apply? ?-output file_name? ?-nosplit? ?-verbose? ?-scenarios scenario_list? ?-sci_based type?",
        ),
        # cat2/insert_buffer.2
        _syn(            "insert_buffer",
            "Inserts buffer cells on specified nets or nets connected to specified ports or pins.",
            "insert_buffer ?-new_net_names new_net_names? ?-new_cell_names new_cell_names? ?-no_of_cells number? ?-inverter_pair? object_list buffer_lib_cell",
        ),
        # cat2/insert_clock_gating.2
        _syn(            "insert_clock_gating",
            "Performs clock gating on an appropriately-prepared GTECH netlist.",
            "insert_clock_gating ?-regular_only? ?-global? ?-no_hier?",
        ),
        # cat2/insert_dft.2
        _syn(            "insert_dft",
            "Inserts DFT logic in the current design.",
            "insert_dft",
        ),
        # cat2/insert_isolation_cell.2
        _syn(            "insert_isolation_cell",
            "Inserts isolation cells on the specified nets, pins or ports. Isolation cell is a general term that applies to isolation cells and enabled level-shifter cells.",
            "insert_isolation_cell ?-force? ?-verbose? -enable enable_signal -object_list objects -reference lib_cell_name",
        ),
        # cat2/insert_mv_cells.2
        _syn(            "insert_mv_cells",
            "Inserts isolation and level-shifter cells to the design.",
            "insert_mv_cells ?-isolation? ?-level_shifter? ?-all? ?-retention_clamp? ?-verbose?",
        ),
        # cat2/is_false.2
        _syn(            "is_false",
            "Tests the value of a specified variable, and returns 1 if the value is 0 or the case-insensitive string false; returns 0 if the value is 1 or the case-insensitive string true.",
            "is_false value",
        ),
        # cat2/is_true.2
        _syn(            "is_true",
            "Tests the value of a specified variable, and returns 1 if the value is 1 or the case-insensitive string true; returns 0 if the value is 0 or the case-insensitive string false.",
            "is_true value",
        ),
        # cat2/lib2saif.2
        _syn(            "lib2saif",
            "Creates a forward-annotation SAIF file for a specified technology library.",
            "lib2saif ?-output file_name? library ?-lib_pathname lib_path_name?",
        ),
        # cat2/license_users.2
        _syn(            "license_users",
            "Lists the current users of the Synopsys licensed features.",
            "license_users ?feature_list?",
        ),
        # cat2/link.2
        _syn(            "link",
            "Resolves design references.",
            "link",
        ),
        # cat2/list.2
        _syn(            "list",
            "Creates a list.",
            "list arg1 arg2 ... argn",
        ),
        # cat2/list_attributes.2
        _syn(            "list_attributes",
            "Lists the currently-defined attributes.",
            "list_attributes ?-application? ?-class class_name? ?-nosplit?",
        ),
        # cat2/list_commands.2
        _syn(            "list_commands",
            "Displays quick help for one or more commands.",
            "list_commands ?-verbose? ?-groups? ?-bg? ?pattern?",
        ),
        # cat2/list_designs.2
        _syn(            "list_designs",
            "Lists the designs available in memory.",
            "list_designs ?design_list? ?-show_file?",
        ),
        # cat2/list_dont_touch_types.2
        _syn(            "list_dont_touch_types",
            "Lists the currently defined dont_touch types.",
            "list_dont_touch_types ?-class class_name?",
        ),
        # cat2/list_duplicate_designs.2
        _syn(            "list_duplicate_designs",
            "Lists designs that have the same design name in dc_shell.",
            "list_duplicate_designs",
        ),
        # cat2/list_files.2
        _syn(            "list_files",
            "Lists the files that are loaded into memory.",
            "list_files",
        ),
        # cat2/list_fusion_libs.2
        _syn(            "list_fusion_libs",
            "Lists available fusion libraries.",
            "list_fusion_libs",
        ),
        # cat2/list_hdl_blocks.2
        _syn(            "list_hdl_blocks",
            "Lists the HDL blocks available in memory.",
            "list_hdl_blocks ?-nosplit? ?-all_objects? ?instance_list?",
        ),
        # cat2/list_instances.2
        _syn(            "list_instances",
            "Lists the instances in the current design or current instance.",
            "list_instances ?instance_list? ?-hierarchy? ?-max_levels num_levels? ?-full? ?-config?",
        ),
        # cat2/list_libs.2
        _syn(            "list_libs",
            "Lists the libraries available in memory.",
            "list_libs ?lib_list?",
        ),
        # cat2/list_licenses.2
        _syn(            "list_licenses",
            "Displays a list of licenses currently checked out by the user.",
            "list_licenses",
        ),
        # cat2/list_size_only_types.2
        _syn(            "list_size_only_types",
            "Lists the currently defined size_only types.",
            "list_size_only_types",
        ),
        # cat2/list_test_models.2
        _syn(            "list_test_models",
            "Lists the designs in memory that have CTL test models attached to them.",
            "list_test_models ?-compressors?",
        ),
        # cat2/list_test_modes.2
        _syn(            "list_test_modes",
            "Displays all of the test modes that are defined for the current design.",
            "list_test_modes",
        ),
        # cat2/lminus.2
        _syn(            "lminus",
            "Removes one or more named elements from a list and returns a new list.",
            "lminus ?-exact? original_list elements",
        ),
        # cat2/load_of.2
        _syn(            "load_of",
            "Returns the capacitance of the specified library cell pin.",
            "load_of library_cell_pin",
        ),
        # cat2/load_upf.2
        _syn(            "load_upf",
            "Executes a script file containing UPF commands.",
            "load_upf ?gupf_file_name? ?-scope instance_name? ?-noecho? ?-simulation_only? ?-strict_check true | false? ?-supplemental supf_file_name?",
        ),
        # cat2/ls.2
        _syn(            "ls",
            "Lists the contents of a directory.",
            "ls",
        ),
        # cat2/magnet_placement.2
        _syn(            "magnet_placement",
            "Performs magnet placement.",
            "magnet_placement ?-move_fixed? ?-mark_fixed? ?-exclude_cells object_list? ?-avoid_soft_blockages? ?-stop_by_sequential_cells? ?-exclude_buffers? ?-logical_level level? ?-stop_points object_list? ?-cells object_list? ?-align? magnet_objects",
        ),
        # cat2/man.2
        _syn(            "man",
            "Displays reference manual pages.",
            "man topic",
        ),
        # cat2/map_isolation_cell.2
        _syn(            "map_isolation_cell",
            "Specifies how to map or remap the isolation and enable levelshifter cells belonging to the specified isolation strategy.",
            "map_isolation_cell isolation_strategy -domain power_domain -lib_cells lib_cells",
        ),
        # cat2/map_level_shifter_cell.2
        _syn(            "map_level_shifter_cell",
            "Specifies that the level-shifter cells belonging to the specified strategy can only be mapped to a subset of the library cells.",
            "map_level_shifter_cell level_shifter_strategy -domain power_domain -lib_cells lib_cells",
        ),
        # cat2/map_power_switch.2
        _syn(            "map_power_switch",
            "Defines which power switch library cells to use for the mapping of the given UPF power switch.",
            "map_power_switch switch_name -domain domain_name -lib_cells list",
        ),
        # cat2/map_retention_cell.2
        _syn(            "map_retention_cell",
            "Defines how to map the unmapped sequential cells to retention cells for the specified UPF retention strategy of the power domain.",
            "map_retention_cell retention_strategy -domain power_domain ?-lib_cells lib_cells? ?-lib_cell_type lib_cell_type? ?-elements objects? ?-lib_model_name name {-port port_name net_ref}*?",
        ),
        # cat2/map_retention_clamp_cell.2
        _syn(            "map_retention_clamp_cell",
            "Defines how to map the zeropin retention clamp cells for the specified UPF retention strategy of the power domain.",
            "map_retention_clamp_cell retention_strategies -domain power_domain -clock_clamp_lib_cells {lib_cells} -async_clamp_lib_cells {lib_cells}",
        ),
        # cat2/mem.2
        _syn(            "mem",
            "Reports memory usage information.",
            "mem ?-all? ?-verbose? ?-debug?",
        ),
        # cat2/merge_saif.2
        _syn(            "merge_saif",
            "Reads a list of SAIF files with their corresponding weights, computes the merged toggle rate and static probability, and annotates the switching activity for the nets, pins, and ports in the current design. The command then generates a merged output SAIF file.",
            "merge_saif -input_list saif_file_and_weight_list ?-instance_name inst_name? ?-output merged_saif_name? ?-simple_merge? ?-ignore ignore_name? ?-ignore_absolute ig_absolute_name? ?-exclude exclude_file_name? ?-exclude_absolute ex_absolute_file_name? ?-unit_base unit_value? ?-scale scale_value? ?-khrate khrate_value? ?-map_names?",
        ),
        # cat2/modify_die_area.2
        _syn(            "modify_die_area",
            "Modify the boundary of the current design to change the size of the area.",
            "modify_die_area -output output_def_name ?-area_scaling_factor scaling_factor? ?-height_scaling_factor scaling_factor? ?-width_scaling_factor scaling_factor? ?-fixed_edges list_of_sides? ?-core_utilization ratio? ?-sizing_type fixed_width | fixed_height | fixed_aspect_ratio? ?-compile? ?-run_track_creation_script script_file_name? ?-row_pattern row_pattern_name?",
        ),
        # cat2/move_lib.2
        _syn(            "move_lib",
            "Moves a library and its contents from one place to another.",
            "move_lib ?-force? ?-from_lib source_name? -to_lib destination_name",
        ),
        # cat2/name_format.2
        _syn(            "name_format",
            "Specifies the prefix and suffix used for naming isolation cells and level shifters created by the tool.",
            "name_format ?-isolation_prefix name? ?-isolation_suffix name? ?-level_shift_prefix name? ?-level_shift_suffix name?",
        ),
        # cat2/open_lib.2
        _syn(            "open_lib",
            "Open an already-existing library for edit or read access.",
            "open_lib ?-edit | -read? ?-ref_libs_for_edit? library_name",
        ),
        # cat2/open_mw_lib.2
        _syn(            "open_mw_lib",
            "Opens a Milkyway library.",
            "open_mw_lib ?-readonly | -write_ref? mw_lib",
        ),
        # cat2/optimize_netlist.2
        _syn(            "optimize_netlist",
            "Performs a high-effort optimization on the current design for better quality of results (QoR).",
            "optimize_netlist ?-area? ?-no_boundary_optimization? ?-no_seq_output_inversion? ?-force?",
        ),
        # cat2/optimize_registers.2
        _syn(            "optimize_registers",
            "Performs retiming of sequential cells (edge-triggered registers or level-sensitive latches) on a mapped gate-level netlist; determines the placement of sequential cells in a design to achieve a target clock period; and minimizes the number of sequential cells while maintaining that clock period.",
            "optimize_registers ?-minimum_period_only? ?-no_compile? ?-sync_transform multiclass | decompose | dont_retime? ?-async_transform multiclass | decompose | dont_retime? ?-check_design ?-verbose?? ?-print_critical_loop? ?-clock clock_name ?-edge rise | fall?? ?-latch? ?-justification_effort low | medium | high? ?-only_attributed_designs? ?-delay_threshold target_clock_period?",
        ),
        # cat2/parallel_execute.2
        _syn(            "parallel_execute",
            "Runs reporting or checking commands in parallel.",
            "parallel_execute ?-out file_name? ?-list_all? ?report_command_list?",
        ),
        # cat2/parse_proc_arguments.2
        _syn(            "parse_proc_arguments",
            "Parses the arguments passed into a Tcl procedure.",
            "parse_proc_arguments",
        ),
        # cat2/preview_dft.2
        _syn(            "preview_dft",
            "Previews, but does not implement, the test points, scan chains, and on-chip clocking control logic to be added to the current design.",
            "preview_dft ?-show object_types? ?-test_points all? ?-test_wrappers all? ?-bsd cells | data_registers | instructions | tap | all? ?-script? ?-verbose?",
        ),
        # cat2/print_message_info.2
        _syn(            "print_message_info",
            "Prints information about diagnostic messages that have occurred or have been limited.",
            "print_message_info ?-ids id_list? ?-summary?",
        ),
        # cat2/print_suppressed_messages.2
        _syn(            "print_suppressed_messages",
            "Displays an alphabetical list of message IDs that are currently suppressed.",
            "print_suppressed_messages",
        ),
        # cat2/print_variable_group.2
        _syn(            "print_variable_group",
            "Lists the variables defined in a specified variable group, along with their current values.",
            "print_variable_group group",
        ),
        # cat2/printenv.2
        _syn(            "printenv",
            "Prints the value of environment variables.",
            "printenv ?variable_name?",
        ),
        # cat2/printvar.2
        _syn(            "printvar",
            "Prints the values of one or more variables.",
            "printvar ?pattern? ?-user_defined | -application?",
        ),
        # cat2/proc_args.2
        _syn(            "proc_args",
            "Displays the formal parameters of a procedure.",
            "proc_args proc_name",
        ),
        # cat2/proc_body.2
        _syn(            "proc_body",
            "Displays the body of a procedure.",
            "proc_body proc_name",
        ),
        # cat2/propagate_constraints.2
        _syn(            "propagate_constraints",
            "Propagates timing constraints from lower levels of the design hierarchy to the current design.",
            "propagate_constraints ?-design design_list? ?-all? ?-clocks? ?-disable_timing? ?-dont_apply? ?-false_path? ?-gate_clock? ?-ideal_network? ?-ignore_from_or_to_port_exceptions? ?-ignore_through_port_exceptions? ?-max_delay? ?-min_delay? ?-multicycle_path? ?-operating_conditions? ?-power_supply_data? ?-output file_name? ?-port_isolation? ?-verbose? ?-case_analysis? ?-target_library_subset? ?-opcond_inference?",
        ),
        # cat2/propagate_switching_activity.2
        _syn(            "propagate_switching_activity",
            "Forces the propagation of power-switching activity information.",
            "propagate_switching_activity ?-verbose? ?-infer_related_clocks?",
        ),
        # cat2/propagate_user_attributes.2
        _syn(            "propagate_user_attributes",
            "Propagates user attributes from lower levels of the design hierarchy to the current design.",
            "propagate_user_attributes ?-design design_list? ?-verbose? attribute_list",
        ),
        # cat2/push_down_model.2
        _syn(            "push_down_model",
            "Creates a new hierarchy around the current design for use with wrapping models flow in SoCTest.",
            "push_down_model new_design_name",
        ),
        # cat2/pwd.2
        _syn(            "pwd",
            "Displays the path name of the present working directory (pwd), also called the current directory.",
            "pwd",
        ),
        # cat2/query_cell_instances.2
        _syn(            "query_cell_instances",
            "Finds all instances of a given library cell or module within the active scope. This is a UPF query command.",
            "query_cell_instances cell_name ?-domain domain_name?",
        ),
        # cat2/query_cell_mapped.2
        _syn(            "query_cell_mapped",
            "Identifies the library cell or module mapped to a given instance. This is a UPF query command.",
            "query_cell_mapped instance_name",
        ),
        # cat2/query_map_power_switch.2
        _syn(            "query_map_power_switch",
            "Returns information about the previous mapping of a library cell to a power switch in the active scope. This is a UPF query command.",
            "query_map_power_switch switch_name ?-detailed?",
        ),
        # cat2/query_net_ports.2
        _syn(            "query_net_ports",
            "Finds all the ports that are logically connected to a given net. This is a UPF query command.",
            "query_net_ports net_name ?-transitive true | false? ?-leaf?",
        ),
        # cat2/query_objects.2
        _syn(            "query_objects",
            "Searches for and displays objects in the database.",
            "query_objects ?-verbose? ?-truncate elem_count? ?-class class_name? object_spec",
        ),
        # cat2/query_port_net.2
        _syn(            "query_port_net",
            "Finds the net that is logically connected to a specified port. This is a UPF query command.",
            "query_port_net port_name ?-conn low | high?",
        ),
        # cat2/query_port_state.2
        _syn(            "query_port_state",
            "Returns information about the port states that have been previously defined for a specified supply port in the active scope. This is a UPF query command.",
            "query_port_state port_name ?-state state_name? ?-detailed?",
        ),
        # cat2/query_power_switch.2
        _syn(            "query_power_switch",
            "Returns information about a power switch that was previously created in the active scope. This is a UPF query command.",
            "query_power_switch switch_name ?-detailed?",
        ),
        # cat2/query_pst.2
        _syn(            "query_pst",
            "Returns information about the power state tables that have been previously created in the active scope. This is a UPF query command.",
            "query_pst table_name ?-detailed?",
        ),
        # cat2/query_pst_state.2
        _syn(            "query_pst_state",
            "Returns information about a state in a power state table that was previously created in the active scope. This is a UPF query command.",
            "query_pst_state state_name -pst table_name ?-detailed?",
        ),
        # cat2/query_qor_snapshot.2
        _syn(            "query_qor_snapshot",
            "Analyzes timing report files from existing QoR snapshots, applies any specified filters, and displays the results in an appropriate format. This command operates in two distinct modes: CTR (general timing) mode and CTS (clock tree synthesis) mode.",
            "query_qor_snapshot ?-name snapshot_name? ?-directory directory_name? ?-display? ?-type min | max? ?-incremental? ?-output_file file_name? ?-output_false_paths file_name? ?-sort_by column_list? ?-group_by column_list? ?-columns column_list? ?-and column_list? ?-filters filter_list? ?-hierarchy? ?-from module_list? ?-to module_list? ?-through module_list? ?-output_group_paths file_name? ?-group_path_prefix prefix? ?-group_path_append appendix? ?-case_sensitive? ?-subgroup {?subgroup_name? ?subgroup_options?}? ?-infeasible_paths?",
        ),
        # cat2/quit.2
        _syn(            "quit",
            "Exits the shell.",
            "quit",
        ),
        # cat2/read.2
        _syn(            "read",
            "Reads from a channel.",
            "read",
        ),
        # cat2/read_bsdl.2
        _syn(            "read_bsdl",
            "Reads the boundary-scan description language (BSDL) file for a boundary-scan design.",
            "read_bsdl ?-add_linkage_as_design_port true | false? file_name",
        ),
        # cat2/read_cell_expansion.2
        _syn(            "read_cell_expansion",
            "Reads the cell expansion data, including the area, width, and height of each cell that is expanded.",
            "read_cell_expansion input_file_name ?-reset?",
        ),
        # cat2/read_db.2
        _syn(            "read_db",
            "Reads in one or more design or library files in Synopsys database (.db) format.",
            "read_db file_names",
        ),
        # cat2/read_ddc.2
        _syn(            "read_ddc",
            "Reads in one or more design files in .ddc (Synopsys logical database) format.",
            "read_ddc file_names ?-scenarios scenario_list? ?-active_scenarios active_scenario_list?",
        ),
        # cat2/read_file.2
        _syn(            "read_file",
            "Reads designs or libraries into memory, or reads libraries into the shell.",
            "read_file file_list ?-define macro_names? ?-format format_name? ?-library library_name? ?-rtl? ?-single_file single_file_name? ?-work library_name? ?-scenarios scenario_list ?-active_scenarios active_scenario_list?? ?-autoread -top top_design_name ?-recursive? ?-exclude exclude_list? ?-param param_list? ?-output_script file_name? ?-verbose? ?-rebuild??",
        ),
        # cat2/read_floorplan.2
        _syn(            "read_floorplan",
            "Reads a script that describes a floorplan into the current design.",
            "read_floorplan file_name ?-echo? ?-verbose?",
        ),
        # cat2/read_lib.2
        _syn(            "read_lib",
            "Reads a technology library into the shell. Starting with the K-2015.06 release, the Library Compiler tool is a separate installation that is no longer part of the synthesis tools installation. Therefore, to run the Library Compiler read_lib command in the Design Compiler tool, the two tools must be linked during the tool installation process. For information about the installation process and how to link the Library Compiler tool to the Design Compiler tool, see the Synthesis Tools Installation Notes and the Library Compiler Installation Notes for the K-2015.06 release.",
            "read_lib file_name ?-test_model CTL_file_list? ?-html? ?-symbol slib_filename? ?-names_file file_list? ?-imported_jcr jcr_file? ?-format format? ?-lib_messages lib_msgs? ?-plibrary plibrary_file_name? ?-no_warnings? ?-pplibrary -pplibrary_filename?",
        ),
        # cat2/read_ocvm.2
        _syn(            "read_ocvm",
            "Reads a parametric on-chip variation (POCV) derating factor table.",
            "read_ocvm ?-min? ?-max? ?-distance_row row_number? ocvm_file",
        ),
        # cat2/read_parasitics.2
        _syn(            "read_parasitics",
            "Reads net parasitics information from an SPEF, DSPF, or RSPF file, and uses it to annotate the current design.",
            "read_parasitics ?-syntax_only? ?-elmore | -arnoldi? ?-increment? ?-pin_cap_included? ?-net_cap_only? ?-complete_with zero | wlm? ?-path path_name? ?-strip_path path_name? ?-quiet | -verbose? ?-dont_write_to_db? ?file_list?",
        ),
        # cat2/read_pin_map.2
        _syn(            "read_pin_map",
            "Reads in a port-to-pin mapping file, which defines the design port-to-package pin mapping for a boundary-scan design.",
            "read_pin_map path_name",
        ),
        # cat2/read_saif.2
        _syn(            "read_saif",
            "Reads a SAIF file and annotates switching activity information on nets, pins, ports, and cells in the current design.",
            "read_saif -input file_name ?-instance_name name? ?-target_instance instance? ?-ignore ignore_name? ?-ignore_absolute ig_absolute_name? ?-exclude exclude_file_name? ?-exclude_absolute ex_absolute_file_name? ?-names_file name_changes_log_file? ?-scale scale_value? ?-unit_base unit_value? ?-khrate khrate_value? ?-map_names? ?-auto_map_names? ?-verbose?",
        ),
        # cat2/read_scan_def.2
        _syn(            "read_scan_def",
            "Reads scan chain information from a SCANDEF file.",
            "read_scan_def file_name",
        ),
        # cat2/read_sdc.2
        _syn(            "read_sdc",
            "Reads in a script in Synopsys Design Constraints (SDC) format.",
            "read_sdc file_name ?-echo? ?-syntax_only? ?-version sdc_version?",
        ),
        # cat2/read_sdf.2
        _syn(            "read_sdf",
            "Reads leaf-cell and net-timing information from a file in Standard Delay Format (SDF) and uses that information to annotate the current design.",
            "read_sdf ?-load_delay net | cell? ?-path path_name? ?-min_type sdf_min | sdf_typ | sdf_max? ?-max_type sdf_min | sdf_typ | sdf_max? ?-worst? ?-min_file min_sdf_file_name? ?-max_file max_sdf_file_name? sdf_file_name",
        ),
        # cat2/read_sverilog.2
        _syn(            "read_sverilog",
            "Reads in one or more design or library files in SystemVerilog format.",
            "read_sverilog file_names ?-netlist? ?-rtl?",
        ),
        # cat2/read_tech_file.2
        _syn(            "read_tech_file",
            "Reads a technology section into the current library.",
            "read_tech_file ?-merge? ?-convert_sites site_name_pairs_list? tech_path",
        ),
        # cat2/read_test_model.2
        _syn(            "read_test_model",
            "Reads a test model file.",
            "read_test_model ?-format ddc | ctl? ?-design design_name? model_files",
        ),
        # cat2/read_test_protocol.2
        _syn(            "read_test_protocol",
            "Reads a STIL test protocol file into memory.",
            "read_test_protocol ?-verbose? ?-test_mode test_mode_name? ?-overwrite? ?-section section_name? input_file_name",
        ),
        # cat2/read_verilog.2
        _syn(            "read_verilog",
            "Reads in one or more design or library files in Verilog format.",
            "read_verilog ?-netlist | -rtl? verilog_files",
        ),
        # cat2/read_vhdl.2
        _syn(            "read_vhdl",
            "Reads in one or more designs or library files in VHDL format.",
            "read_vhdl ?-netlist? file_names",
        ),
        # cat2/rebuild_mw_lib.2
        _syn(            "rebuild_mw_lib",
            "Rebuilds the Milkyway library.",
            "rebuild_mw_lib libName",
        ),
        # cat2/redirect.2
        _syn(            "redirect",
            "Redirects the output of a command to a file.",
            "redirect ?-append? ?-tee? ?-file | -variable | -channel? ?-compress? ?-bg? ?-max_cores number_of_cores? target {command_string}",
        ),
        # cat2/remove_annotated_check.2
        _syn(            "remove_annotated_check",
            "Removes annotated timing-check information.",
            "remove_annotated_check -all | -from from_list | -to to_list ?-rise | -fall? ?-clock rise | fall? ?-setup? ?-hold? ?-recovery? ?-removal? ?-nochange_low? ?-nochange_high?",
        ),
        # cat2/remove_annotated_delay.2
        _syn(            "remove_annotated_delay",
            "Removes the annotated delay between two pins.",
            "remove_annotated_delay -all | -cell_all | -net_all | -non_clock_cell_all | -non_clock_net_all | -from from_list | -to to_list",
        ),
        # cat2/remove_annotated_transition.2
        _syn(            "remove_annotated_transition",
            "Removes the annotated transition at a pin.",
            "remove_annotated_transition -all",
        ),
        # cat2/remove_annotations.2
        _syn(            "remove_annotations",
            "Removes all annotated information on the design.",
            "remove_annotations",
        ),
        # cat2/remove_attribute.2
        _syn(            "remove_attribute",
            "Removes an attribute from the specified objects.",
            "remove_attribute ?-bus? ?-quiet? object_list attribute_name",
        ),
        # cat2/remove_auto_path_groups.2
        _syn(            "remove_auto_path_groups",
            "Removes path groups for the current design.",
            "remove_auto_path_groups ?-prefix prefix? ?-file file_name? ?-verbose? ?-user_path_groups_file user_file_name? ?-skip?",
        ),
        # cat2/remove_boundary_cell.2
        _syn(            "remove_boundary_cell",
            "Removes the boundary-cell configuration for the specified ports or core cells.",
            "remove_boundary_cell -class core_wrapper | shadow_wrapper | bsd -ports port_list | -core core_cell_list ?-function function_type?",
        ),
        # cat2/remove_boundary_cell_io.2
        _syn(            "remove_boundary_cell_io",
            "Removes the boundary-cell I/O specifications from the current boundary-scan design.",
            "remove_boundary_cell_io ?-all? ?-cell cell_list?",
        ),
        # cat2/remove_bounds.2
        _syn(            "remove_bounds",
            "Removes bounds from the current design.",
            "remove_bounds ?-verbose? ?-all? ?-name bound_name_list? objects",
        ),
        # cat2/remove_bsd_compliance.2
        _syn(            "remove_bsd_compliance",
            "Removes the compliance ports specifications from the current boundary-scan design.",
            "remove_bsd_compliance ?-all? ?-name pattern_name?",
        ),
        # cat2/remove_bsd_instruction.2
        _syn(            "remove_bsd_instruction",
            "Removes boundary-scan instructions from the instruction list to be used by insert_dft for the current design.",
            "remove_bsd_instruction instruction_list",
        ),
        # cat2/remove_bsd_linkage_port.2
        _syn(            "remove_bsd_linkage_port",
            "Removes the linkage-ports specifications from the current boundary-scan design.",
            "remove_bsd_linkage_port ?-all? ?-port_list port_list?",
        ),
        # cat2/remove_bsd_power_up_reset.2
        _syn(            "remove_bsd_power_up_reset",
            "Removes the power-up reset port specifications from the current boundary-scan design.",
            "remove_bsd_power_up_reset",
        ),
        # cat2/remove_buffer.2
        _syn(            "remove_buffer",
            "Removes the buffer cells at a specified driver pin or net on a mapped design.",
            "remove_buffer -from start_point -net net_list ?-to end_point_list? ?-level number_of_levels? cell_list",
        ),
        # cat2/remove_buffer_tree.2
        _syn(            "remove_buffer_tree",
            "Removes the buffer tree at a specified driver pin.",
            "remove_buffer_tree ?-from pin_list? ?-all? ?-source_of patterns?",
        ),
        # cat2/remove_bus.2
        _syn(            "remove_bus",
            "Removes a port bus or net bus.",
            "remove_bus object_list",
        ),
        # cat2/remove_case_analysis.2
        _syn(            "remove_case_analysis",
            "Removes the case-analysis value from the specified input ports or pins.",
            "remove_case_analysis port_or_pin_list | -all",
        ),
        # cat2/remove_cell.2
        _syn(            "remove_cell",
            "Removes cells from the current design.",
            "remove_cell cell_list | -all",
        ),
        # cat2/remove_cell_degradation.2
        _syn(            "remove_cell_degradation",
            "Removes the cell_degradation attribute on specified ports or designs.",
            "remove_cell_degradation object_list",
        ),
        # cat2/remove_clock.2
        _syn(            "remove_clock",
            "Removes clocks from the current design.",
            "remove_clock clock_list | -all",
        ),
        # cat2/remove_clock_exclusivity.2
        _syn(            "remove_clock_exclusivity",
            "Removes the clock exclusivity setting on cell previously set by the set_clock_exclusivity command.",
            "remove_clock_exclusivity ?-output output_pins? ?-all?",
        ),
        # cat2/remove_clock_gating.2
        _syn(            "remove_clock_gating",
            "Directs the compile -incremental and compile_ultra -incremental commands to remove clock gating from objects clock-gated by Power Compiler.",
            "remove_clock_gating ?-gated_registers gated_register_list? ?-min_bitwidth minsize_value? ?-gating_cells clock_gating_cells_list? ?-all? ?-no_hier? ?-verbose? ?-undo?",
        ),
        # cat2/remove_clock_gating_check.2
        _syn(            "remove_clock_gating_check",
            "Removes setup and hold checks from the specified clock-gating cells.",
            "remove_clock_gating_check ?-setup? ?-hold? ?-rise? ?-fall? object_list",
        ),
        # cat2/remove_clock_gating_style.2
        _syn(            "remove_clock_gating_style",
            "Removes the clock gating style applied on a given set of hierarchical cells or power domains.",
            "remove_clock_gating_style ?-instances {cell_list}? ?-power_domains {power_domain_list}? ?-designs designs?",
        ),
        # cat2/remove_clock_groups.2
        _syn(            "remove_clock_groups",
            "Removes specific exclusive or asynchronous clock groups from the current design.",
            "remove_clock_groups -logically_exclusive | -asynchronous | -physically_exclusive name_list | -all",
        ),
        # cat2/remove_clock_jitter.2
        _syn(            "remove_clock_jitter",
            "Removes clock jitter information previously set by the set_clock_jitter command.",
            "remove_clock_jitter -clocks clocks_list",
        ),
        # cat2/remove_clock_latency.2
        _syn(            "remove_clock_latency",
            "Removes clock latency information from the specified objects.",
            "remove_clock_latency ?-fall? ?-min? ?-max? ?-source? ?-early? ?-late? object_list ?-rise?",
        ),
        # cat2/remove_clock_sense.2
        _syn(            "remove_clock_sense",
            "Removes clock sense information from the specified pins.",
            "remove_clock_sense ?-all? ?-clocks clock_list? pins",
        ),
        # cat2/remove_clock_transition.2
        _syn(            "remove_clock_transition",
            "Removes clock-transition attributes on the specified clock objects.",
            "remove_clock_transition clock_list",
        ),
        # cat2/remove_clock_uncertainty.2
        _syn(            "remove_clock_uncertainty",
            "Removes clock-uncertainty information previously set by the set_clock_uncertainty command.",
            "remove_clock_uncertainty ?object_list | -from from_clock | -rise_from rise_from_clock | -fall_from fall_from_clock -to to_clock | -rise_to rise_to_clock | -fall_to fall_to_clock? ?-rise? ?-fall? ?-setup? ?-hold?",
        ),
        # cat2/remove_command_hook.2
        _syn(            "remove_command_hook",
            "Remove hook from command execution",
            "remove_command_hook -before name -after name -replace name commandName",
        ),
        # cat2/remove_congestion_options.2
        _syn(            "remove_congestion_options",
            "Removes congestion options from the current design.",
            "remove_congestion_options ?-all? id_list",
        ),
        # cat2/remove_constraint.2
        _syn(            "remove_constraint",
            "Removes all constraint attributes, clocks, and path delay information from the current design. Note that this command will be obsolete in the next release. It will be replaced by the remove_sdc command. Please adjust your scripts accordingly.",
            "remove_constraint ?-all? ?-all_sdc?",
        ),
        # cat2/remove_core_area.2
        _syn(            "remove_core_area",
            "Removes the core area of the design.",
            "remove_core_area",
        ),
        # cat2/remove_data_check.2
        _syn(            "remove_data_check",
            "Removes specified data-to-data checks previously set by the set_data_check command.",
            "remove_data_check -from from_object | -rise_from from_object | -fall_from from_object -to to_object | -rise_to to_object | -fall_to to_object ?-setup | -hold? ?-clock clock?",
        ),
        # cat2/remove_design.2
        _syn(            "remove_design",
            "Removes designs or libraries from memory.",
            "remove_design ?design_list | -designs | -all? ?-hierarchy? ?-quiet?",
        ),
        # cat2/remove_dft_clock_gating_pin.2
        _syn(            "remove_dft_clock_gating_pin",
            "Removes all DFT clock-gating pin specifications for the current design.",
            "remove_dft_clock_gating_pin",
        ),
        # cat2/remove_dft_connect.2
        _syn(            "remove_dft_connect",
            "Removes existing DFT connectivity specifications.",
            "remove_dft_connect ?-all? ?label_name?",
        ),
        # cat2/remove_dft_design.2
        _syn(            "remove_dft_design",
            "Removes the specified design so that it cannot be used for DFT insertion.",
            "remove_dft_design -design_name design_name | -type design_type | -all",
        ),
        # cat2/remove_dft_equivalent_signals.2
        _syn(            "remove_dft_equivalent_signals",
            "Removes all equivalent DFT signals specified with the set_dft_equivalent_signals command for the specified primary signal commands.",
            "remove_dft_equivalent_signals primary_signal",
        ),
        # cat2/remove_dft_location.2
        _syn(            "remove_dft_location",
            "Removes DFT hierarchy location specifications for the current design.",
            "remove_dft_location ?-type logic_type?",
        ),
        # cat2/remove_dft_partition.2
        _syn(            "remove_dft_partition",
            "Permanently removes a list of design DFT partitions associated with a design.",
            "remove_dft_partition ?list_of_partition_labels?",
        ),
        # cat2/remove_dft_power_control.2
        _syn(            "remove_dft_power_control",
            "Removes the power controller block specification from the current design.",
            "remove_dft_power_control",
        ),
        # cat2/remove_dft_signal.2
        _syn(            "remove_dft_signal",
            "Removes from specified ports the attributes that identify those ports as DFT signals in the current design.",
            "remove_dft_signal -view existing_dft | spec -port port_list -test_mode mode_name_list ?-hookup_pin pin_name? ?-usage use_type?",
        ),
        # cat2/remove_die_area.2
        _syn(            "remove_die_area",
            "Removes the die area from the current design.",
            "remove_die_area ?-verbose?",
        ),
        # cat2/remove_disable_clock_gating_check.2
        _syn(            "remove_disable_clock_gating_check",
            "Restores clock-gating checks that were previously disabled by the set_disable_clock_gating_check command for the specified cells and pins.",
            "remove_disable_clock_gating_check object_list",
        ),
        # cat2/remove_disable_timing.2
        _syn(            "remove_disable_timing",
            "Enables previously user-disabled timing arcs in the current design. It is equivalent to the set_disable_timing -restore command.",
            "remove_disable_timing object_list ?-from from_pin_name -to to_pin_name? ?-all_loop_breaking?",
        ),
        # cat2/remove_dp_int_round.2
        _syn(            "remove_dp_int_round",
            "Removes the rounding attribute from inferred multiplier and multiplier-based instantiated DesignWare cells.",
            "remove_dp_int_round ?cell_list | -all?",
        ),
        # cat2/remove_driving_cell.2
        _syn(            "remove_driving_cell",
            "Removes driving-cell attributes from the specified input or inout ports of the current design.",
            "remove_driving_cell ?ports?",
        ),
        # cat2/remove_early_data_check_records.2
        _syn(            "remove_early_data_check_records",
            "Removes the early data check records.",
            "remove_early_data_check_records ?records?",
        ),
        # cat2/remove_failsafe_fsm_groups.2
        _syn(            "remove_failsafe_fsm_groups",
            "Removes failsafe FSM groups from the current design.",
            "remove_failsafe_fsm_groups ?group_names? ?-all?",
        ),
        # cat2/remove_failsafe_fsm_rules.2
        _syn(            "remove_failsafe_fsm_rules",
            "Removes failsafe FSM rules from the current design.",
            "remove_failsafe_fsm_rules ?rule_names? ?-all?",
        ),
        # cat2/remove_from_rp_group.2
        _syn(            "remove_from_rp_group",
            "Removes a cell, relative placement group, or keepout from the specified relative placement groups.",
            "remove_from_rp_group rp_groups -leaf cell_name -hierarchy group_name ?-instance instance_name? -keepout keepout_name",
        ),
        # cat2/remove_generated_clock.2
        _syn(            "remove_generated_clock",
            "Removes a generated_clock object.",
            "remove_generated_clock -all | clock_list",
        ),
        # cat2/remove_host_options.2
        _syn(            "remove_host_options",
            "Removes all -max_cores specifications set by the set_host_options command.",
            "remove_host_options",
        ),
        # cat2/remove_ideal_latency.2
        _syn(            "remove_ideal_latency",
            "Removes ideal latency information from the specified objects.",
            "remove_ideal_latency ?-rise | -fall? ?-min | -max? object_list | -all",
        ),
        # cat2/remove_ideal_net.2
        _syn(            "remove_ideal_net",
            "Restores the ideal nets set by the set_ideal_net or set_ideal_network -no_propagate command to their initial nonideal state from the specified nets in the current design.",
            "remove_ideal_net net_list",
        ),
        # cat2/remove_ideal_network.2
        _syn(            "remove_ideal_network",
            "Removes a set of ports or pins in an ideal network in the current design. Cells and nets in the transitive fanout of the specified objects are no longer treated as ideal.",
            "remove_ideal_network object_list | -all",
        ),
        # cat2/remove_ideal_transition.2
        _syn(            "remove_ideal_transition",
            "Removes ideal transition information from the specified objects.",
            "remove_ideal_transition ?-rise | -fall? ?-min | -max? object_list | -all",
        ),
        # cat2/remove_ignored_layers.2
        _syn(            "remove_ignored_layers",
            "Removes ignored routing layers for congestion analysis and RC estimation. This command is supported only in Desgin Compiler topographical mode.",
            "remove_ignored_layers list_of_layers ?-all? ?-min_routing_layer? ?-max_routing_layer?",
        ),
        # cat2/remove_input_delay.2
        _syn(            "remove_input_delay",
            "Removes input delay on the specified pins or input ports.",
            "remove_input_delay ?-clock clock ?-clock_fall? ?-level_sensitive?? ?-rise? ?-fall? ?-max? ?-min? ports_pins",
        ),
        # cat2/remove_isolate_ports.2
        _syn(            "remove_isolate_ports",
            "Removes the specified ports from the list of ports that are isolated in the current design.",
            "remove_isolate_ports port_list",
        ),
        # cat2/remove_isolation_cell.2
        _syn(            "remove_isolation_cell",
            "Removes the specified isolation cells from the design.",
            "remove_isolation_cell ?-force? -object_list cells",
        ),
        # cat2/remove_keepout_margin.2
        _syn(            "remove_keepout_margin",
            "Removes keepout margin of specified type for the specified cells/lib cells in the design.",
            "remove_keepout_margin ?-type hard | soft? ?-derived? object_list",
        ),
        # cat2/remove_level_shifters.2
        _syn(            "remove_level_shifters",
            "Removes all of the level shifters from the design.",
            "remove_level_shifters ?-force?",
        ),
        # cat2/remove_libcell_subset.2
        _syn(            "remove_libcell_subset",
            "Removes target library family constraints from specified cells or removes a target library family defined by the define_libcell_subset command.",
            "remove_libcell_subset ?-object_list cells? ?-family_name name?",
        ),
        # cat2/remove_license.2
        _syn(            "remove_license",
            "Removes a licensed feature.",
            "remove_license feature_list ?-keep num_licenses?",
        ),
        # cat2/remove_link_library_subset.2
        _syn(            "remove_link_library_subset",
            "Removes the link library subset constraint from the top-level design or from the specified instances.",
            "remove_link_library_subset ?-object_list cells? ?-top?",
        ),
        # cat2/remove_min_pulse_width.2
        _syn(            "remove_min_pulse_width",
            "Removes a previously specified minimum pulse width constraint from specified clocks or clock pins.",
            "remove_min_pulse_width ?-low? ?-high? ?object_list?",
        ),
        # cat2/remove_multibit.2
        _syn(            "remove_multibit",
            "Removes the multibit components from the current design. Removes or detaches cells from the multibit components in a design.",
            "remove_multibit object_list",
        ),
        # cat2/remove_net.2
        _syn(            "remove_net",
            "Removes nets from the current design.",
            "remove_net net_list | -all ?-only_physical?",
        ),
        # cat2/remove_net_routing_layer_constraints.2
        _syn(            "remove_net_routing_layer_constraints",
            "Removes the routing layer constraints for the specified nets.",
            "remove_net_routing_layer_constraints list_of_nets",
        ),
        # cat2/remove_net_search_pattern.2
        _syn(            "remove_net_search_pattern",
            "Removes a net search pattern or all net search patterns.",
            "remove_net_search_pattern -pattern id | -all",
        ),
        # cat2/remove_net_shape.2
        _syn(            "remove_net_shape",
            "Removes all net shapes in the current design.",
            "remove_net_shape net_shapes ?-verbose?",
        ),
        # cat2/remove_ocvm.2
        _syn(            "remove_ocvm",
            "Removes parametric on-chip variation (POCV) derating previously set with the read_ocvm command.",
            "remove_ocvm ?-coefficient? ?-derate? ?object_list?",
        ),
        # cat2/remove_output_delay.2
        _syn(            "remove_output_delay",
            "Removes output delay on pins or output ports.",
            "remove_output_delay ?-clock clock ?-clock_fall? ?-level_sensitive?? ?-rise? ?-fall? ?-max? ?-min? port_pin_list",
        ),
        # cat2/remove_path_group.2
        _syn(            "remove_path_group",
            "Removes a list of path groups from the current design.",
            "remove_path_group group_list",
        ),
        # cat2/remove_pin_guides.2
        _syn(            "remove_pin_guides",
            "Removes all pin guides from the design.",
            "remove_pin_guides -all | patterns ?-verbose?",
        ),
        # cat2/remove_pin_map.2
        _syn(            "remove_pin_map",
            "Removes a design port-to-package pin mapping for a boundary-scan design.",
            "remove_pin_map package_name",
        ),
        # cat2/remove_pin_name_synonym.2
        _syn(            "remove_pin_name_synonym",
            "Removes pin name synonym definitions.",
            "remove_pin_name_synonym ?-all? ?synonym_list?",
        ),
        # cat2/remove_placement_blockage.2
        _syn(            "remove_placement_blockage",
            "Removes placement blockages.",
            "remove_placement_blockage patterns | -name name | -all ?-verbose?",
        ),
        # cat2/remove_port.2
        _syn(            "remove_port",
            "Removes ports from the current design or its subdesign.",
            "remove_port port_list",
        ),
        # cat2/remove_power_domain.2
        _syn(            "remove_power_domain",
            "Removes the specified power domains.",
            "remove_power_domain power_domains | -all",
        ),
        # cat2/remove_preferred_routing_direction.2
        _syn(            "remove_preferred_routing_direction",
            "Removes the preferred routing direction for the given routing layers.",
            "remove_preferred_routing_direction -layers list_of_layers",
        ),
        # cat2/remove_propagated_clock.2
        _syn(            "remove_propagated_clock",
            "Removes propagated clock latency previously set with the set_propagated_clock command, which restores ideal clock latency for the specified objects.",
            "remove_propagated_clock -all | object_list",
        ),
        # cat2/remove_route_guide.2
        _syn(            "remove_route_guide",
            "Removes the specified route guides.",
            "remove_route_guide ?-verbose? -name route_guide_name | -all | patterns",
        ),
        # cat2/remove_routing_rules.2
        _syn(            "remove_routing_rules",
            "Removes nondefault routing rules in a design defined by the define_routing_rule command.",
            "remove_routing_rules ?-all? rule_name_list",
        ),
        # cat2/remove_rp_group_options.2
        _syn(            "remove_rp_group_options",
            "Removes relative placement (RP) group attributes from the specified relative placement groups.",
            "remove_rp_group_options rp_groups ?-ignore? ?-x_offset? ?-y_offset? ?-cell_orient_opt? ?-auto_blockage? ?-disable_buffering? ?-allow_non_rp_cells? ?-ignore_rows? ?-max_rp_width? ?-max_rp_height?",
        ),
        # cat2/remove_rp_groups.2
        _syn(            "remove_rp_groups",
            "Removes a list of relative placement (RP) groups.",
            "remove_rp_groups rp_groups | -all ?-hierarchy? ?-quiet?",
        ),
        # cat2/remove_rtl_load.2
        _syn(            "remove_rtl_load",
            "Removes previously-set capacitance and resistance RTL load values from pins, ports, and nets.",
            "remove_rtl_load -all | pin_net_list",
        ),
        # cat2/remove_safety_core_groups.2
        _syn(            "remove_safety_core_groups",
            "Removes safety core groups from the current design.",
            "remove_safety_core_groups -all | group_names",
        ),
        # cat2/remove_safety_core_rules.2
        _syn(            "remove_safety_core_rules",
            "Removes safety core rules from the current design.",
            "remove_safety_core_rules ?-all? ?rule_names?",
        ),
        # cat2/remove_safety_error_code_groups.2
        _syn(            "remove_safety_error_code_groups",
            "Removes safety error code groups from the current design.",
            "remove_safety_error_code_groups ?names? ?-all?",
        ),
        # cat2/remove_safety_error_code_rules.2
        _syn(            "remove_safety_error_code_rules",
            "Removes safety error code rules from the design.",
            "remove_safety_error_code_rules ?names? ?-all?",
        ),
        # cat2/remove_safety_register_groups.2
        _syn(            "remove_safety_register_groups",
            "Removes safety register groups from the current design.",
            "remove_safety_register_groups ?group_names? ?-all?",
        ),
        # cat2/remove_safety_register_rules.2
        _syn(            "remove_safety_register_rules",
            "Removes safety register rules from the current design.",
            "remove_safety_register_rules ?rule_names? ?-all?",
        ),
        # cat2/remove_scaling_lib_group.2
        _syn(            "remove_scaling_lib_group",
            "Removes any previously specified scaling library group from the current design or from a subdesign.",
            "remove_scaling_lib_group ?-object_list objects?",
        ),
        # cat2/remove_scan_group.2
        _syn(            "remove_scan_group",
            "Removes an existing scan-group specification previously specified using the set_scan_group command.",
            "remove_scan_group scan_group_name",
        ),
        # cat2/remove_scan_link.2
        _syn(            "remove_scan_link",
            "Removes a scan-link specification for the current design.",
            "remove_scan_link scan_link_name Wire | Lockup ?-test_mode test_mode?",
        ),
        # cat2/remove_scan_path.2
        _syn(            "remove_scan_path",
            "Removes the scan-path specification for the current design in set_scan_path.",
            "remove_scan_path -chain scan_chain_name ?-view existing_dft | spec? ?-test_mode test_mode?",
        ),
        # cat2/remove_scan_register_type.2
        _syn(            "remove_scan_register_type",
            "Removes existing scan-register types, previously set by set_scan_register_type, from specified cells or from the current design.",
            "remove_scan_register_type ?cell_or_design_list?",
        ),
        # cat2/remove_scan_replacement.2
        _syn(            "remove_scan_replacement",
            "Removes the table entries specified through the set_scan_replacement command.",
            "remove_scan_replacement ?non_scan_seq_cell_list?",
        ),
        # cat2/remove_scan_skew_group.2
        _syn(            "remove_scan_skew_group",
            "Removes scan skew groups defined by the set_scan_skew_group command.",
            "remove_scan_skew_group scan_skew_group_list",
        ),
        # cat2/remove_scan_suppress_toggling.2
        _syn(            "remove_scan_suppress_toggling",
            "Removes the existing user specifications that were provided through the set_scan_suppress_toggling command in terms of a list of scan flip-flops to be gated by the insert_dft command.",
            "remove_scan_suppress_toggling",
        ),
        # cat2/remove_scenario.2
        _syn(            "remove_scenario",
            "Removes the specified scenarios from memory.",
            "remove_scenario scenario_name | -all",
        ),
        # cat2/remove_sdc.2
        _syn(            "remove_sdc",
            "Removes all Synopsys Design Constraints (SDC).",
            "remove_sdc ?-keep_parasitics?",
        ),
        # cat2/remove_sense.2
        _syn(            "remove_sense",
            "Removes sense information defined on pins or cell timing arcs.",
            "remove_sense ?-type clock? ?-clocks clock_list? ?-all? pins",
        ),
        # cat2/remove_target_library_subset.2
        _syn(            "remove_target_library_subset",
            "Removes target library subset constraints from the root design or from specified instances.",
            "remove_target_library_subset ?-object_list cells? ?-top?",
        ),
        # cat2/remove_terminal.2
        _syn(            "remove_terminal",
            "Removes terminals.",
            "remove_terminal terminals ?-verbose?",
        ),
        # cat2/remove_test_mode.2
        _syn(            "remove_test_mode",
            "Removes the mode declared by the define_test_mode command.",
            "remove_test_mode test_mode_label",
        ),
        # cat2/remove_test_model.2
        _syn(            "remove_test_model",
            "Permanently removes the test model associated with a design.",
            "remove_test_model ?-design design_name?",
        ),
        # cat2/remove_test_point_element.2
        _syn(            "remove_test_point_element",
            "Removes the test-point element specification for a particular test-point type and a list of pin objects for the current design.",
            "remove_test_point_element list_of_design_pin_objects ?-type test_point_type?",
        ),
        # cat2/remove_test_protocol.2
        _syn(            "remove_test_protocol",
            "Removes a test protocol from memory for the current design.",
            "remove_test_protocol ?-design design_name? ?-test_mode test_mode_name?",
        ),
        # cat2/remove_track.2
        _syn(            "remove_track",
            "Removes tracks from the current design.",
            "remove_track -all | patterns | -layer layer ?-dir X | Y? ?-verbose?",
        ),
        # cat2/remove_unconnected_ports.2
        _syn(            "remove_unconnected_ports",
            "Removes unconnected ports or pins from cells, references, and subdesigns.",
            "remove_unconnected_ports cell_list ?-blast_buses?",
        ),
        # cat2/remove_upf.2
        _syn(            "remove_upf",
            "Removes the UPF constraints from the design. This command is only supported in dc_shell.",
            "remove_upf",
        ),
        # cat2/remove_user_attribute.2
        _syn(            "remove_user_attribute",
            "Removes a user-specified attribute from a design or library object.",
            "remove_user_attribute object_list attribute_name ?-bus? ?-quiet?",
        ),
        # cat2/remove_user_shape.2
        _syn(            "remove_user_shape",
            "Removes objects that are user shapes.",
            "remove_user_shape ?-verbose? user_shapes",
        ),
        # cat2/remove_verification_priority.2
        _syn(            "remove_verification_priority",
            "Removes the verification_priority attribute from the specified objects.",
            "remove_verification_priority ?-all? object_list",
        ),
        # cat2/remove_via.2
        _syn(            "remove_via",
            "Removes vias from the current design.",
            "remove_via ?-verbose? ?vias?",
        ),
        # cat2/remove_via_ladder_constraints.2
        _syn(            "remove_via_ladder_constraints",
            "Removes the specified via ladder constraints.",
            "remove_via_ladder_constraints -pins collection_of_pins -all",
        ),
        # cat2/remove_via_ladder_rules.2
        _syn(            "remove_via_ladder_rules",
            "Removes via ladders rules for the block.",
            "remove_via_ladder_rules",
        ),
        # cat2/remove_via_rules.2
        _syn(            "remove_via_rules",
            "Removes via_rule objects from the current library.",
            "remove_via_rules ?-all? via_rule_list",
        ),
        # cat2/remove_voltage_area.2
        _syn(            "remove_voltage_area",
            "Removes voltage areas from the current design.",
            "remove_voltage_area ?-name list? -all | patterns",
        ),
        # cat2/remove_wire_load_min_block_size.2
        _syn(            "remove_wire_load_min_block_size",
            "Removes the wire_load_min_block_size attribute from the current design.",
            "remove_wire_load_min_block_size",
        ),
        # cat2/remove_wire_load_model.2
        _syn(            "remove_wire_load_model",
            "Removes wire-load model attributes from designs, ports, and hierarchical cells. This command is not supported in Design Compiler in topographical mode.",
            "remove_wire_load_model ?-min? ?-max? ?object_list?",
        ),
        # cat2/remove_wire_load_selection_group.2
        _syn(            "remove_wire_load_selection_group",
            "Removes the wire-load model selection group from designs and cells of the current design.",
            "remove_wire_load_selection_group ?-min? ?-max? ?object_list?",
        ),
        # cat2/rename.2
        _syn(            "rename",
            "Renames or deletes a command.",
            "rename old_name new_name",
        ),
        # cat2/rename_design.2
        _syn(            "rename_design",
            "Renames a design in memory, or moves a list of designs to a file.",
            "rename_design design_list ?target_name? ?-prefix prefix_name? ?-postfix postfix_name? ?-dont_link_with_original_name? ?-update_links?",
        ),
        # cat2/rename_mw_lib.2
        _syn(            "rename_mw_lib",
            "Renames a Milkyway library.",
            "rename_mw_lib -from lib_name -to lib_name",
        ),
        # cat2/replace_clock_gates.2
        _syn(            "replace_clock_gates",
            "Replaces manually-inserted clock gates with Power Compiler clock gates.",
            "replace_clock_gates ?-global? ?-no_hier?",
        ),
        # cat2/replace_synthetic.2
        _syn(            "replace_synthetic",
            "Implements all synthetic library parts of a design using generic logic.",
            "replace_synthetic ?-ungroup?",
        ),
        # cat2/report_access_control_configuration.2
        _syn(            "report_access_control_configuration",
            "Reports the access control specification for the current design.",
            "report_access_control_configuration",
        ),
        # cat2/report_activity.2
        _syn(            "report_activity",
            "Reports switching activity.",
            "report_activity ?-rtl? ?-driver? ?-show_zeros? ?-scenarios scenario_list?",
        ),
        # cat2/report_ahfs_options.2
        _syn(            "report_ahfs_options",
            "Generates a report about the automatic high-fanout synthesis options.",
            "report_ahfs_options",
        ),
        # cat2/report_annotated_check.2
        _syn(            "report_annotated_check",
            "Displays all annotated timing checks on the current design.",
            "report_annotated_check ?-nosplit?",
        ),
        # cat2/report_annotated_delay.2
        _syn(            "report_annotated_delay",
            "Displays delays annotated on cells and nets of the current design.",
            "report_annotated_delay ?-cell? ?-net? ?-nosplit? ?-summary? ?-min?",
        ),
        # cat2/report_annotated_transition.2
        _syn(            "report_annotated_transition",
            "Displays annotated transitions on all pins of the current design.",
            "report_annotated_transition -nosplit",
        ),
        # cat2/report_app_options.2
        _syn(            "report_app_options",
            "Generates a report of application options.",
            "report_app_options",
        ),
        # cat2/report_app_var.2
        _syn(            "report_app_var",
            "Shows the application variables.",
            "report_app_var ?-verbose? ?-only_changed_vars? ?pattern?",
        ),
        # cat2/report_attribute.2
        _syn(            "report_attribute",
            "Reports the attributes of a cell, net, pin, port, siterow, instance, or design.",
            "report_attribute ?-cell? ?-design? ?-hierarchy? ?-instance? ?-net? ?-port? ?-pin? ?-reference? ?-site? ?-nosplit? ?object_list?",
        ),
        # cat2/report_auto_floorplan_constraints.2
        _syn(            "report_auto_floorplan_constraints",
            "Reports constraints set for initializing floorplan.",
            "report_auto_floorplan_constraints ?-control_type? ?-shape? ?-side_length? ?-side_ratio? ?-core_utilization? ?-boundary? ?-orientation? ?-coincident_boundary? ?-core_offset? ?-row_core_ratio? ?-flip_first_row? ?-honor_pad_limit? ?-site_def? ?-origin_offset? ?-row_pattern? ?-track_script?",
        ),
        # cat2/report_auto_ungroup.2
        _syn(            "report_auto_ungroup",
            "Displays information about the cell hierarchies that have been ungrouped using the compile command with either the -auto_ungroup area or the -auto_ungroup delay option. Note: This command will be obsolete in a future release.",
            "report_auto_ungroup ?-nosplit? ?-full?",
        ),
        # cat2/report_autofix_configuration.2
        _syn(            "report_autofix_configuration",
            "Reports the global AutoFix specification applied to the current design.",
            "report_autofix_configuration ?-type fix_type?",
        ),
        # cat2/report_autofix_element.2
        _syn(            "report_autofix_element",
            "Reports all local AutoFix specifications applied to the current design.",
            "report_autofix_element ?-type fix_type? ?list_of_design_objects?",
        ),
        # cat2/report_autoungroup_options.2
        _syn(            "report_autoungroup_options",
            "Specifies the options to control autoungrouping.",
            "report_autoungroup_options",
        ),
        # cat2/report_background_jobs.2
        _syn(            "report_background_jobs",
            "Reports all the completed and running background jobs submitted to run by the redirect -bg command.",
            "report_background_jobs ?-reset?",
        ),
        # cat2/report_block_abstraction.2
        _syn(            "report_block_abstraction",
            "Reports information about the specified block abstraction instance.",
            "report_block_abstraction ?block_list?",
        ),
        # cat2/report_boundary_cell.2
        _syn(            "report_boundary_cell",
            "Reports the boundary-cell configuration specified for the current design.",
            "report_boundary_cell",
        ),
        # cat2/report_boundary_cell_io.2
        _syn(            "report_boundary_cell_io",
            "Displays options set by theset_boundary_cell_io command.",
            "report_boundary_cell_io",
        ),
        # cat2/report_bounds.2
        _syn(            "report_bounds",
            "Reports bounds in the design.",
            "report_bounds -all | bound_objects | -name name_list",
        ),
        # cat2/report_bsd_buffers.2
        _syn(            "report_bsd_buffers",
            "Displays information about BSR signal buffer chains.",
            "report_bsd_buffers",
        ),
        # cat2/report_bsd_compliance.2
        _syn(            "report_bsd_compliance",
            "Displays options set by the set_bsd_compliance command.",
            "report_bsd_compliance",
        ),
        # cat2/report_bsd_instruction.2
        _syn(            "report_bsd_instruction",
            "Displays options set by the set_bsd_instruction command.",
            "report_bsd_instruction ?-view spec | existing_dft? ?-instruction list_of_instruction_names?",
        ),
        # cat2/report_bsd_linkage_port.2
        _syn(            "report_bsd_linkage_port",
            "Displays options set by the set_bsd_linkage_port command.",
            "report_bsd_linkage_port",
        ),
        # cat2/report_bsd_power_up_reset.2
        _syn(            "report_bsd_power_up_reset",
            "Displays options set by the set_bsd_power_up_reset command.",
            "report_bsd_power_up_reset",
        ),
        # cat2/report_buffer_tree.2
        _syn(            "report_buffer_tree",
            "Reports the buffer tree and its level information at the given driver pin.",
            "report_buffer_tree ?-from start_point_list | -net net_list? ?-depth max_depth? ?-connections? ?-hierarchy? ?-physical? ?-nosplit?",
        ),
        # cat2/report_buffer_tree_qor.2
        _syn(            "report_buffer_tree_qor",
            "Displays quality-related properties of the buffer trees at the given driver pins.",
            "report_buffer_tree_qor ?-from list_of_driving_pins_or_nets?",
        ),
        # cat2/report_bus.2
        _syn(            "report_bus",
            "Lists the bused ports and nets in the current instance or in the current design.",
            "report_bus ?-nosplit?",
        ),
        # cat2/report_case_analysis.2
        _syn(            "report_case_analysis",
            "Reports case analysis on ports or pins.",
            "report_case_analysis ?-all? ?-nosplit?",
        ),
        # cat2/report_cell.2
        _syn(            "report_cell",
            "Displays information about cells in the current instance or current design.",
            "report_cell ?-nosplit? ?-connections? ?-verbose? ?-physical? ?-only_physical? ?-significant_digits digits? ?cells?",
        ),
        # cat2/report_cell_mode.2
        _syn(            "report_cell_mode",
            "Generates a report of the instance modes.",
            "report_cell_mode ?-nosplit? ?instance_list?",
        ),
        # cat2/report_check_library_options.2
        _syn(            "report_check_library_options",
            "Reports the values or the status of the options set by the set_check_library_options command.",
            "report_check_library_options ?-physical? ?-logic_vs_physical? ?-logic? ?-default?",
        ),
        # cat2/report_clock_gating.2
        _syn(            "report_clock_gating",
            "Reports the Power Compiler tool's clock-gating details.",
            "report_clock_gating ?-no_hier? ?-verbose? ?-gated? ?-ungated? ?-gating_elements? ?-only cell_list? ?-nosplit? ?-physical? ?-multi_stage? ?-style? ?-structure? ?-scenarios scenario_list? ?-enable_conditions?",
        ),
        # cat2/report_clock_gating_check.2
        _syn(            "report_clock_gating_check",
            "Prints a report of the clock-gating checks.",
            "report_clock_gating_check ?-nosplit? ?-significant_digits digits? ?instance_list?",
        ),
        # cat2/report_clock_jitter.2
        _syn(            "report_clock_jitter",
            "Reports clock jitter information previously set by the set_clock_jitter command.",
            "report_clock_jitter ?-clock clock_list?",
        ),
        # cat2/report_clock_tree.2
        _syn(            "report_clock_tree",
            "Reports the structural and timing characteristics of a compiled clock tree.",
            "report_clock_tree ?-clock_trees clock_tree_list? ?-summary? ?-structure? ?-drc_violators? ?-settings? ?-exceptions ?-show_all_sinks?? ?-from from_list | -to to_list? ?-operating_condition condition? ?-level_info? ?-high_fanout_net net_or_pin_list | -premesh | -postmesh? ?-nosplit? ?-all_drc_violators? ?-partial_structure_within_exceptions? ?-skew_group skew_groups_string? ?-histogram_transition file_name | -histogram_capacitance file_name | -histogram_rcdelay file_name | -histogram_fanout file_name | -histogram_rcdelay_to_sink file_name? ?-local_skew ?-histogram_local_skew file_name? ?-local_skew_skip_icg? ?-nworst number_of_pin_pairs? ?-launch_pins launch_pin_list? ?-capture_pins capture_pin_list?? ?-number_of_bins bin_number? ?-sink_group ?-sink_group_ignore_cts_exceptions | -sink_group_timing_relationship_limit limit | -sink_group_sort_by clock | sink_group | -sink_group_sort_order ascending | descending | -sink_group_timing_relationship_file file_name | -sink_group_detail_file file_name | -sink_group_ignore_buf_inv | -sink_group_ignore_icg?? ?-scenarios list_of_scenarios? ?-interclock_timing?",
        ),
        # cat2/report_collection.2
        _syn(            "report_collection",
            "Output a tabular report of attribute values for elements in a collection.",
            "report_collection collection ?-type report_type? ?-header header_type? ?-max_rows value_count? ?-columns column_specification? ?-nosplit?",
        ),
        # cat2/report_compile_options.2
        _syn(            "report_compile_options",
            "Displays information about the compile command options for the design of the current instance if set; or for the current design otherwise.",
            "report_compile_options ?-nosplit?",
        ),
        # cat2/report_compile_spg_mode.2
        _syn(            "report_compile_spg_mode",
            "Displays the tool settings updated by the set_compile_spg_mode command.",
            "report_compile_spg_mode",
        ),
        # cat2/report_congestion.2
        _syn(            "report_congestion",
            "Reports the congestion statistics.",
            "report_congestion ?-effort minimum | low | medium | high? ?-list_cells_over_grc_violation grc_violation_threshold?",
        ),
        # cat2/report_congestion_options.2
        _syn(            "report_congestion_options",
            "Reports congestion options in the design.",
            "report_congestion_options ?-all? id_list",
        ),
        # cat2/report_cross_probing.2
        _syn(            "report_cross_probing",
            "Reports cross-probing data for specified cells and ports.",
            "report_cross_probing ?-nosplit? ?-original_hierarchy? objects",
        ),
        # cat2/report_cross_probing_files.2
        _syn(            "report_cross_probing_files",
            "Shows a list of cross-probing files and their status.",
            "report_cross_probing_files ?-errors_only?",
        ),
        # cat2/report_crpr.2
        _syn(            "report_crpr",
            "Reports the clock reconvergence pessimism calculated between specified register clock pins or ports.",
            "report_crpr -from from_latch_clock_pin -to to_latch_clock_pin ?-from_clock from_clock? ?-to_clock to_clock? ?-setup | -hold? ?-significant_digits digits?",
        ),
        # cat2/report_datapath_gating.2
        _syn(            "report_datapath_gating",
            "Reports the status of datapath gating in the current design.",
            "report_datapath_gating ?-instances? ?-nosplit? ?-ungated? ?-gated?",
        ),
        # cat2/report_delay_calculation.2
        _syn(            "report_delay_calculation",
            "Displays the actual calculation of a timing arc delay value for a cell or net.",
            "report_delay_calculation -min -max -from from_pin -to to_pin ?-nosplit? ?-crosstalk? ?-from_rise_transition from_rise_value? ?-from_fall_transition from_fall_value? ?-derate? ?-significant_digits digits?",
        ),
        # cat2/report_delay_estimation_options.2
        _syn(            "report_delay_estimation_options",
            "Reports the parameters that influence delay estimation. This command is supported only in topographical mode.",
            "report_delay_estimation_options",
        ),
        # cat2/report_design.2
        _syn(            "report_design",
            "Displays attributes of the current design.",
            "report_design ?-nosplit? ?-physical?",
        ),
        # cat2/report_design_lib.2
        _syn(            "report_design_lib",
            "Lists the design units contained in the specified libraries.",
            "report_design_lib ?-libraries? ?-designs? ?-architectures? ?-packages? ?library_list?",
        ),
        # cat2/report_design_mismatch.2
        _syn(            "report_design_mismatch",
            "Reports design mismatches that were circumvented to allow linking the design.",
            "report_design_mismatch ?-summary? ?-class all | netlist | library?",
        ),
        # cat2/report_device_group.2
        _syn(            "report_device_group",
            "For DCNXT only, reports the number, area, and percentage of cells for each device group in the design. Also shows the number, area, and percentage of cells in user-specified narrow and/or wide device groups. Since the device group attribute is specified on the library cells, hierarchical cells do not have a device group. So, their usage is reported under the \"undefined\" device group category.",
            "report_device_group ?cell_list? ?-narrow_device_groups groups? ?-wide_device_groups groups? ?-nosplit? ?-verbose?",
        ),
        # cat2/report_dft_clock_controller.2
        _syn(            "report_dft_clock_controller",
            "Reports the on-chip clocking controller specification for the current design.",
            "report_dft_clock_controller ?-view existing_dft | spec?",
        ),
        # cat2/report_dft_clock_gating_configuration.2
        _syn(            "report_dft_clock_gating_configuration",
            "Displays the options specified by the set_dft_clock_gating_configuration command.",
            "report_dft_clock_gating_configuration",
        ),
        # cat2/report_dft_clock_gating_pin.2
        _syn(            "report_dft_clock_gating_pin",
            "Displays the specification specified by the set_dft_clock_gating_pin command.",
            "report_dft_clock_gating_pin",
        ),
        # cat2/report_dft_configuration.2
        _syn(            "report_dft_configuration",
            "Displays the options specified by the set_dft_configuration command.",
            "report_dft_configuration",
        ),
        # cat2/report_dft_connect.2
        _syn(            "report_dft_connect",
            "Reports the existing DFT connectivity specifications.",
            "report_dft_connect",
        ),
        # cat2/report_dft_design.2
        _syn(            "report_dft_design",
            "Reports all user-specified DFT designs.",
            "report_dft_design ?-all? ?-type design_type_name? ?-design_name design_name?",
        ),
        # cat2/report_dft_drc_rules.2
        _syn(            "report_dft_drc_rules",
            "Reports DFT DRC specifications that affect how certain DRC rule violations affect DFT insertion.",
            "report_dft_drc_rules ?-violation drc_list? ?-cell cell_list?",
        ),
        # cat2/report_dft_equivalent_signals.2
        _syn(            "report_dft_equivalent_signals",
            "Reports all of the equivalent DFT signals specified with set_dft_equivalent_signals command.",
            "report_dft_equivalent_signals",
        ),
        # cat2/report_dft_hierarchical_pins.2
        _syn(            "report_dft_hierarchical_pins",
            "Reports the ports and hierarchical pins created during DFT insertion.",
            "report_dft_hierarchical_pins ?-added_by_dft true | false? ?-ports_only false | true? ?-summary_only false | true?",
        ),
        # cat2/report_dft_insertion_configuration.2
        _syn(            "report_dft_insertion_configuration",
            "Displays options set by the set_dft_insertion_configuration command.",
            "report_dft_insertion_configuration",
        ),
        # cat2/report_dft_location.2
        _syn(            "report_dft_location",
            "Reports the DFT hierarchy location specifications for the current design.",
            "report_dft_location ?-all?",
        ),
        # cat2/report_dft_partition.2
        _syn(            "report_dft_partition",
            "Displays design partition information attached to a design.",
            "report_dft_partition",
        ),
        # cat2/report_dft_power_control.2
        _syn(            "report_dft_power_control",
            "Reports the power controller block specification for the current design.",
            "report_dft_power_control",
        ),
        # cat2/report_dft_signal.2
        _syn(            "report_dft_signal",
            "Displays options specified by the set_dft_signal command.",
            "report_dft_signal ?-view spec | existing_dft? ?-test_mode mode_name_list | all? ?-port list_of_port_names? ?-type signal_type?",
        ),
        # cat2/report_direct_power_rail_tie.2
        _syn(            "report_direct_power_rail_tie",
            "Reports all library pins on which the direct_power_rail_tie attribute is set to true.",
            "report_direct_power_rail_tie",
        ),
        # cat2/report_disable_timing.2
        _syn(            "report_disable_timing",
            "Reports disabled timing arcs in the current design.",
            "report_disable_timing ?-nosplit?",
        ),
        # cat2/report_dont_touch.2
        _syn(            "report_dont_touch",
            "Reports dont_touch cells or nets in the current design along with their dont_touch types.",
            "report_dont_touch ?objects | -class class_name? ?-nosplit?",
        ),
        # cat2/report_dp_smartgen_options.2
        _syn(            "report_dp_smartgen_options",
            "Displays datapath strategies available to the current design.",
            "report_dp_smartgen_options",
        ),
        # cat2/report_early_data_checks.2
        _syn(            "report_early_data_checks",
            "Reports details about early data checks.",
            "report_early_data_checks",
        ),
        # cat2/report_extraction_options.2
        _syn(            "report_extraction_options",
            "Reports the options that influence postroute extraction.",
            "report_extraction_options ?-scenarios scenario_list? ?-all?",
        ),
        # cat2/report_failsafe_fsm_groups.2
        _syn(            "report_failsafe_fsm_groups",
            "Reports failsafe fsm groups of the current design.",
            "report_failsafe_fsm_groups ?group_names?",
        ),
        # cat2/report_failsafe_fsm_rules.2
        _syn(            "report_failsafe_fsm_rules",
            "Reports failsafe fsm rules from the current design.",
            "report_failsafe_fsm_rules ?rule_names?",
        ),
        # cat2/report_fsm.2
        _syn(            "report_fsm",
            "Displays state-machine attributes and information for the design of the specified instance or all the instances",
            "report_fsm ?-nosplit? ?-design design_list? ?-verbose? ?-state_transition? ?-show_error_states? ?-all?",
        ),
        # cat2/report_fusion_lib.2
        _syn(            "report_fusion_lib",
            "Displays the contents of the specified fusion library.",
            "report_fusion_lib library_name",
        ),
        # cat2/report_gui_stroke_bindings.2
        _syn(            "report_gui_stroke_bindings",
            "Print a report on the dictionaries and the stroke-command bindings they contain..",
            "report_gui_stroke_bindings ?-dictionary dictionary_name?",
        ),
        # cat2/report_gui_stroke_builtins.2
        _syn(            "report_gui_stroke_builtins",
            "Print a report on the non-Tcl commands available for stroke bindings..",
            "?-dictionary dictionary_name?",
        ),
        # cat2/report_heterogeneous_fanout.2
        _syn(            "report_heterogeneous_fanout",
            "Displays supply net information for nets whose loads have different supplies.",
            "report_heterogeneous_fanout ?-nosplit? ?-nets net_list? ?-pins pin_list? ?-cells cell_list? ?-verbose?",
        ),
        # cat2/report_hierarchy.2
        _syn(            "report_hierarchy",
            "Displays the reference hierarchy of the current instance or the current design.",
            "report_hierarchy ?-nosplit? ?-full? ?-noleaf?",
        ),
        # cat2/report_host_options.2
        _syn(            "report_host_options",
            "Prints a report of multi-CPU processing options as defined by the set_host_options command.",
            "report_host_options",
        ),
        # cat2/report_icc2_options.2
        _syn(            "report_icc2_options",
            "Reports the options used to invoke the IC Compiler II session from within Design Compiler Graphical or DC Explorer physical mode.",
            "report_icc2_options ?-verbose? ?-check?",
        ),
        # cat2/report_icc_dp_options.2
        _syn(            "report_icc_dp_options",
            "Reports the options used to invoke the floorplan exploration session from Design Compiler Graphical. If you do not specify the options using the set_icc_dp_options command, report_icc_dp_options reports the default settings.",
            "report_icc_dp_options ?-check? ?-verbose?",
        ),
        # cat2/report_ideal_network.2
        _syn(            "report_ideal_network",
            "Displays information about ports, pins, nets, and cells on ideal networks in the current design.",
            "report_ideal_network ?-net? ?-cell? ?-load_pin? ?-timing? ?object_list?",
        ),
        # cat2/report_ieee_1500_configuration.2
        _syn(            "report_ieee_1500_configuration",
            "Displays the options specified by the set_ieee_1500_configuration command.",
            "report_ieee_1500_configuration",
        ),
        # cat2/report_ignored_layers.2
        _syn(            "report_ignored_layers",
            "Reports the routing layers that are ignored during congestion analysis and RC estimation. This command is supported only in topographical mode.",
            "report_ignored_layers",
        ),
        # cat2/report_inbound_cell.2
        _syn(            "report_inbound_cell",
            "Displays information about inbound cells in the current instance or current design.",
            "report_inbound_cell ?-summary? ?-hierarchical? ?cells?",
        ),
        # cat2/report_interclock_relation.2
        #   WARNING: unmatched closing bracket ']' at position 184
        _syn(            "report_interclock_relation",
            "Displays common multiple-clock periods between clocks of different periods or edge information for paths launched and captured by two different clocks. For multicorner-multimode designs, this command reports the interclock relations in the current design.",
            "report_interclock_relation ?-from from_clock_names | -rise_from from_clock_names | -fall_from from_clock_names? ?-to to_clock_names? | -rise_to to_clock_names | -fall_to to_clock_names? ?-nosplit? ?-significant_digits digits? ?-edge? ?-setup? ?-hold? ?-scenarios scenario_list?",
        ),
        # cat2/report_internal_loads.2
        _syn(            "report_internal_loads",
            "Displays internal loads on the nets in the current design.",
            "report_internal_loads ?-nosplit?",
        ),
        # cat2/report_isolate_ports.2
        _syn(            "report_isolate_ports",
            "Displays the status of port isolation on ports on which isolation was requested.",
            "report_isolate_ports ?-nosplit?",
        ),
        # cat2/report_isolation_cell.2
        _syn(            "report_isolation_cell",
            "Displays information about isolation cells in the current scope.",
            "report_isolation_cell ?isolation_cells? ?-domain power_domains? ?-isolation_strategy isolation_strategy_names? ?-ports pins_ports? ?-verbose? ?-nosplit?",
        ),
        # cat2/report_keepout_margin.2
        _syn(            "report_keepout_margin",
            "Reports keepout margins of a specified type for the specified cells in the design.",
            "report_keepout_margin ?-type hard | soft? ?-original? ?-parameters? ?-all_derivable? ?object_list?",
        ),
        # cat2/report_latch_loop_groups.2
        _syn(            "report_latch_loop_groups",
            "Reports the latch data pins involved in loops of transparent latches.",
            "report_latch_loop_groups ?-of_objects pin_list? ?-loop_breakers_only? ?-path_breakers_only? ?-nosplit?",
        ),
        # cat2/report_level_shifter.2
        _syn(            "report_level_shifter",
            "Displays information about level-shifter cells in the current scope.",
            "report_level_shifter ?level_shifter_cells? ?-domain power_domains? ?-verbose? ?-nosplit? ?-macro?",
        ),
        # cat2/report_lib.2
        _syn(            "report_lib",
            "Displays information about the specified logic library, physical library, or symbol library.",
            "report_lib ?-all? ?-ccs_recv? ?-em? ?-fpga? ?-k_factors? ?-power? ?-power_label? ?-table? ?-full_table? ?-timing? ?-timing_arcs? ?-timing_label? ?-noise? ?-vhdl_name? ?-yield? ?-switch? ?-pg_pin? ?-char? ?-operating_condition? ?-op_cond_name op_cond_name? ?-routing_rule? ?-rwm? ?-user_defined_data? library_name ?cell_list? ?-jcr? ?-pattern_must_join_pin? ?-pattern_must_join_pin_exclusion_list lib_cell_pin_list? ?-noise_arcs? ?-multibit?",
        ),
        # cat2/report_libcell_subset.2
        _syn(            "report_libcell_subset",
            "Reports the target library family specified on sequential and instantiated combinational cells.",
            "report_libcell_subset ?-object_list cells? ?-nosplit?",
        ),
        # cat2/report_link_library_subset.2
        _syn(            "report_link_library_subset",
            "Reports link library subsets on the design.",
            "report_link_library_subset ?-object_list cells? ?-top? ?-scenarios scenarios? ?-nosplit?",
        ),
        # cat2/report_logic_levels.2
        #   WARNING: unclosed bracket '[' at position 435
        _syn(            "report_logic_levels",
            "Displays logic levels information about a design. This command is not supported in Design Compiler or Design Compiler NXT",
            "report_logic_levels ?-to to_list? ?-from from_list? ?-through through_list? ?-exclude exclude_list? ?-nworst paths_per_endpoint? ?-max_paths max_path_count? ?-start_end_pair? ?-group group_name? ?-slack_greater_than greater_slack_limit? ?-slack_lesser_than lesser_slack_limit? ?-path_type path_type? ?-sort_paths_by sort_path_value? ?-num_bins number_of_bins? ?-bin_width bin_width_number? ?-max_paths_to_report max_path_report_count? ?-export_csv_file ?-summary_only? ?-nosplit?",
        ),
        # cat2/report_logic_lock_configuration.2
        _syn(            "report_logic_lock_configuration",
            "Reports the logic_lock configuration for the current design.",
            "report_logic_lock_configuration",
        ),
        # cat2/report_logicbist_configuration.2
        _syn(            "report_logicbist_configuration",
            "Displays options specified by the set_logicbist_configuration command.",
            "report_logicbist_configuration ?-test_mode mode_name_list | all?",
        ),
        # cat2/report_min_pulse_width.2
        _syn(            "report_min_pulse_width",
            "Displays minimum pulse width check information about specified sequential device clock pins.",
            "report_min_pulse_width ?-all_violators? ?-significant_digits digits? ?-nosplit? ?-scenarios scenario_list? ?pin_list?",
        ),
        # cat2/report_mis_violation_summary.2
        _syn(            "report_mis_violation_summary",
            "Displays information about multi-input switching cells tied to same net in current design.",
            "report_mis_violation_summary",
        ),
        # cat2/report_missing_constraints.2
        _syn(            "report_missing_constraints",
            "Reports missing constraints in current design.",
            "report_missing_constraints ?-class class_list? ?-clock_tracing_mode tracing_mode?",
        ),
        # cat2/report_mode.2
        _syn(            "report_mode",
            "Prints a report of the instance modes.",
            "report_mode ?-nosplit? ?instance_list?",
        ),
        # cat2/report_multibit.2
        _syn(            "report_multibit",
            "Displays information about multibit components in the current design or the subdesign.",
            "report_multibit ?-nosplit? ?-hierarchical? ?object_list?",
        ),
        # cat2/report_multibit_banking.2
        _syn(            "report_multibit_banking",
            "Reports all multibit registers in a design and the banking ratio.",
            "report_multibit_banking ?-hierarchical? ?-nosplit?",
        ),
        # cat2/report_mv_library_cells.2
        _syn(            "report_mv_library_cells",
            "Displays power management cells available in the target libraries.",
            "report_mv_library_cells ?-level_shifters? ?-isolation_cells? ?-retention_cells? ?-switch_cells? ?-always_on_cells? ?-cell_name master_cell_name? ?-verbose?",
        ),
        # cat2/report_mv_qor.2
        _syn(            "report_mv_qor",
            "Estimates and reports static power for the power domains of a design in UPF mode. This command is supported only in DC Explorer.",
            "report_mv_qor ?-verbose? ?-domains power_domain_list? ?-output output_file_name? ?-html?",
        ),
        # cat2/report_mw_lib.2
        _syn(            "report_mw_lib",
            "Displays information about the measurement units or reference libraries of a Milkyway library.",
            "report_mw_lib ?-unit_range? ?-mw_reference_library? ?mw_lib?",
        ),
        # cat2/report_name_rules.2
        _syn(            "report_name_rules",
            "Reports the values of name rules.",
            "report_name_rules ?name_rules?",
        ),
        # cat2/report_names.2
        _syn(            "report_names",
            "Reports potential name changes of ports, cells, and nets in a design.",
            "report_names ?-rules name_rules? ?-hierarchy? ?-dont_touch designs_list? ?-nosplit? ?-original? ?-dont_touch_collection object_list?",
        ),
        # cat2/report_net.2
        _syn(            "report_net",
            "Reports net information for the design of the current instance or for the current design.",
            "report_net ?-nosplit? ?-noflat? ?-transition_times? ?-only_physical? ?-verbose? ?-cell_degradation? ?-min? ?-connections? ?-physical? ?net_list? ?-significant_digits digits? ?-max_toggle_rate? ?-max_capacitance? ?-scenarios scenario_list?",
        ),
        # cat2/report_net_fanout.2
        _syn(            "report_net_fanout",
            "Displays net fanout or buffer-tree information for the current design.",
            "report_net_fanout ?-nosplit? ?-high_fanout? ?-threshold lower? ?-bound upper? ?-verbose? ?-connections? ?-physical? ?-min? ?-tree ?-depth level?? ?net_list?",
        ),
        # cat2/report_net_routing_layer_constraints.2
        _syn(            "report_net_routing_layer_constraints",
            "Reports the routing layer constraints for the specified nets.",
            "report_net_routing_layer_constraints nets ?-output file_name?",
        ),
        # cat2/report_net_routing_rules.2
        _syn(            "report_net_routing_rules",
            "Reports the nondefault routing rules for the specified nets.",
            "report_net_routing_rules nets ?-freeze? ?-minorchange? ?-normal? ?-output file_name?",
        ),
        # cat2/report_net_search_pattern.2
        _syn(            "report_net_search_pattern",
            "Reports the specified net search patterns.",
            "report_net_search_pattern -pattern id | -all",
        ),
        # cat2/report_net_search_pattern_delay_estimation_options.2
        _syn(            "report_net_search_pattern_delay_estimation_options",
            "Reports delay estimation options specified for a pattern or all net search patterns.",
            "report_net_search_pattern_delay_estimation_options -pattern id | -all",
        ),
        # cat2/report_net_search_pattern_priority.2
        _syn(            "report_net_search_pattern_priority",
            "Reports the pattern matching priority.",
            "report_net_search_pattern_priority",
        ),
        # cat2/report_obfuscation_configuration.2
        _syn(            "report_obfuscation_configuration",
            "Reports the obfuscation configuration for the current design.",
            "report_obfuscation_configuration",
        ),
        # cat2/report_ocvm.2
        _syn(            "report_ocvm",
            "Displays information about advanced on-chip variation (AOCV) and parametric on-chip variation (POCV) derating tables and coefficients, and reports derating calculation details.",
            "report_ocvm ?-min? ?-max? ?-early? ?-late? ?-rise? ?-fall? ?-clock? ?-data? ?-cell_delay? ?-net_delay? ?-list_annotated? ?-list_not_annotated? ?-nosplit? ?-arc_details? -type aocvm | pocvm ?object_list?",
        ),
        # cat2/report_opcond_inference.2
        _syn(            "report_opcond_inference",
            "Reports the strategy and settings for operating condition inference.",
            "report_opcond_inference ?-object_list cells?",
        ),
        # cat2/report_operating_conditions.2
        _syn(            "report_operating_conditions",
            "Displays a specific operating condition or all operating conditions in a library.",
            "report_operating_conditions -library library_name ?-name op_cond_name?",
        ),
        # cat2/report_optimize_dft_options.2
        _syn(            "report_optimize_dft_options",
            "Reports options for physical design-for-test (DFT) optimization.",
            "report_optimize_dft_options",
        ),
        # cat2/report_partitions.2
        _syn(            "report_partitions",
            "Lists the hierarchical designs and their associated attributes and relative size (estimated in RTL).",
            "report_partitions ?-nosplit?",
        ),
        # cat2/report_path_budget.2
        _syn(            "report_path_budget",
            "Displays budgeting information about a design.",
            "report_path_budget ?-to to_list? ?-from from_list? ?-through through_list? ?-nworst paths_per_endpoint? ?-max_paths max_path_count? ?-input_pins? ?-nets? ?-transition_time? ?-significant_digits digits? ?-nosplit? ?-all? ?-verbose?",
        ),
        # cat2/report_path_group.2
        _syn(            "report_path_group",
            "Reports information about path groups in the current design.",
            "report_path_group ?-nosplit? ?-expanded? ?-scenarios scenario_list?",
        ),
        # cat2/report_physical_constraints.2
        _syn(            "report_physical_constraints",
            "Reports the physical constraint settings for the current design. This command is supported only in topographical mode.",
            "report_physical_constraints ?-no_site_row? ?-pre_route?",
        ),
        # cat2/report_pin_map.2
        _syn(            "report_pin_map",
            "Displays package pin-map information set by the read_pin_map command.",
            "report_pin_map",
        ),
        # cat2/report_pin_name_synonym.2
        _syn(            "report_pin_name_synonym",
            "Reports pin-name synonym definitions.",
            "report_pin_name_synonym ?-nosplit?",
        ),
        # cat2/report_pipeline_scan_data_configuration.2
        _syn(            "report_pipeline_scan_data_configuration",
            "Displays options specified by the set_pipeline_scan_data_configuration command.",
            "report_pipeline_scan_data_configuration",
        ),
        # cat2/report_port.2
        _syn(            "report_port",
            "Displays information about ports of the current instance or the current design.",
            "report_port ?-drive? ?-verbose? ?-physical? ?-only_physical? ?-nosplit? ?-significant_digits digits? ?port_list?",
        ),
        # cat2/report_power_calculation.2
        _syn(            "report_power_calculation",
            "Displays the calculation of the internal power for a pin, the leakage power for a cell, or the switching power for a net.",
            "report_power_calculation pin_cell_or_net_list ?-state_condition boolean_eq_of_pins | default | all? ?-path_sources pin_name | default | all? ?-rise? ?-fall? ?-verbose? ?-nosplit?",
        ),
        # cat2/report_power_derate.2
        _syn(            "report_power_derate",
            "Reports the power derating factors for either the current design, a list of cells, or library cells in the current design.",
            "report_power_derate ?-scenarios scenario_list? ?-include_inherited? ?-significant_digits digits? ?-nosplit? ?object_list?",
        ),
        # cat2/report_power_domain.2
        _syn(            "report_power_domain",
            "Reports information about the specified power domain.",
            "report_power_domain ?power_domains? ?-hierarchy? ?-nosplit? ?-verbose? ?object_list?",
        ),
        # cat2/report_power_gating.2
        _syn(            "report_power_gating",
            "Reports the power-gating style of retention registers in the design.",
            "report_power_gating ?cell_or_design_list? ?-missing? ?-unconnected?",
        ),
        # cat2/report_power_model.2
        _syn(            "report_power_model",
            "Report information of power models in the design.",
            "report_power_model ?-verbose?",
        ),
        # cat2/report_power_pin_info.2
        _syn(            "report_power_pin_info",
            "Reports the power pin information for leaf cells in the current design.",
            "report_power_pin_info cell_instances ?-nosplit?",
        ),
        # cat2/report_power_switch.2
        _syn(            "report_power_switch",
            "Reports all of the specified power switches.",
            "report_power_switch ?power_switch_name? ?-verbose?",
        ),
        # cat2/report_preferred_routing_direction.2
        _syn(            "report_preferred_routing_direction",
            "Reports the preferred routing direction for all routing layers.",
            "report_preferred_routing_direction",
        ),
        # cat2/report_preserve_user_attribute.2
        _syn(            "report_preserve_user_attribute",
            "Reports the attribute preservation list.",
            "report_preserve_user_attribute",
        ),
        # cat2/report_pst.2
        _syn(            "report_pst",
            "Reports the power states in the current design previously created with the add_pst_state command.",
            "report_pst ?-supplies supply_list? ?-pst_state_limit number? ?-verbose? ?-scope instance_name? ?-derived? ?-voltage_type all | nominal? ?-reconcile?",
        ),
        # cat2/report_qor.2
        _syn(            "report_qor",
            "Displays QoR information and statistics for the current design.",
            "report_qor ?-significant_digits digits? ?-scenarios scenario_list? ?-summary? ?-ignore_infeasible_paths? ?-virtual_path_group?",
        ),
        # cat2/report_qtm_model.2
        _syn(            "report_qtm_model",
            "Reports Quick Timing Model (QTM) data.",
            "report_qtm_model ?-global_parameters? ?-ports? ?-arcs?",
        ),
        # cat2/report_reference.2
        _syn(            "report_reference",
            "Displays information about references in the current instance or in the current design.",
            "report_reference ?-nosplit? ?-hierarchy?",
        ),
        # cat2/report_register.2
        _syn(            "report_register",
            "Displays information about registers in the current instance, if set; or in the current design otherwise.",
            "report_register ?-nosplit? ?-no_hierarchy? ?-clock clock_name? ?-inverted_output? ?-level_sensitive | -edge_triggered? ?-master_slave? ?cell_list?",
        ),
        # cat2/report_resources.2
        _syn(            "report_resources",
            "Lists the resources and datapath blocks used in the design of the current instance, in the current design, or in a specific design or list of designs.",
            "report_resources ?-nosplit? ?-hierarchy? ?-context? ?-minpower? ?-html_file_name filename? ?design_list?",
        ),
        # cat2/report_retention_cell.2
        _syn(            "report_retention_cell",
            "Displays information about retention cells in the current scope.",
            "report_retention_cell ?retention_cells? ?-domain power_domains? ?-retention_strategy retention_strategy_names? ?-clamps? ?-verbose?",
        ),
        # cat2/report_retention_clamp_cell.2
        _syn(            "report_retention_clamp_cell",
            "Displays information about zero-pin retention clamp cells in the current scope.",
            "report_retention_clamp_cell ?retention_clamp_cells? ?-domain power_domains? ?-retention_strategy retention_strategy_names? ?-verbose?",
        ),
        # cat2/report_route_zrt_common_options.2
        _syn(            "report_route_zrt_common_options",
            "Reports the settings of route options that are common among the Zroute router commands.",
            "report_route_zrt_common_options",
        ),
        # cat2/report_route_zrt_global_options.2
        _syn(            "report_route_zrt_global_options",
            "Reports the settings of the global router options.",
            "report_route_zrt_global_options",
        ),
        # cat2/report_routing_rules.2
        _syn(            "report_routing_rules",
            "Reports on design-specific nondefault routing rules defined by the define_routing_rule command.",
            "report_routing_rules ?rule_name? ?-output file_name?",
        ),
        # cat2/report_rp_group_options.2
        _syn(            "report_rp_group_options",
            "Reports relative placement group attributes on the specified relative placement groups.",
            "report_rp_group_options rp_groups",
        ),
        # cat2/report_rtl_pg.2
        _syn(            "report_rtl_pg",
            "Used to report the RTL-derived PG connections in the design.",
            "report_rtl_pg ?-net rtlpg_net_name?",
        ),
        # cat2/report_safety_core_groups.2
        _syn(            "report_safety_core_groups",
            "Reports safety core groups of the current design.",
            "report_safety_core_groups ?group_names? ?-all?",
        ),
        # cat2/report_safety_core_rules.2
        _syn(            "report_safety_core_rules",
            "Reports safety core rules from the current design.",
            "report_safety_core_rules ?rule_names? ?-all?",
        ),
        # cat2/report_safety_error_code_groups.2
        _syn(            "report_safety_error_code_groups",
            "Reports safety error code groups of the design.",
            "report_safety_error_code_groups ?group_names?",
        ),
        # cat2/report_safety_error_code_rules.2
        _syn(            "report_safety_error_code_rules",
            "Reports safety error code rules from the design.",
            "report_safety_error_code_rules ?rule_names? ?-all?",
        ),
        # cat2/report_safety_logic_port_map.2
        _syn(            "report_safety_logic_port_map",
            "report the port map on safety logic module.",
            "report_safety_logic_port_map -module module to report the port map on",
        ),
        # cat2/report_safety_register_groups.2
        _syn(            "report_safety_register_groups",
            "Reports safety register groups of the current design.",
            "report_safety_register_groups ?group_names? ?-all?",
        ),
        # cat2/report_safety_register_rules.2
        _syn(            "report_safety_register_rules",
            "Reports safety register rules from the current design.",
            "report_safety_register_rules ?rule_names? ?-all?",
        ),
        # cat2/report_safety_status.2
        _syn(            "report_safety_status",
            "Perform and report checks related to safety_register_rules, safety_register_groups, fsm_register_rules and fsm_register_groups.",
            "report_safety_status ?-header string? ?-safety_register_rules safety_register_rules? ?-safety_register_groups safety_register_groups? ?-failsafe_fsm_rules failsafe_fsm_rules? ?-failsafe_fsm_groups failsafe_fsm_groups? ?-safety_error_code_groups group_name_list? ?-safety_error_code_rules rule_name_list? ?-repelling_group_bounds?",
        ),
        # cat2/report_saif.2
        _syn(            "report_saif",
            "Reports the statistics of switching activity annotation, on the current design or instance.",
            "report_saif ?-only cell_or_net_list? ?-hierarchy? ?-missing? ?-annotated_flag? ?-rtl_saif?",
        ),
        # cat2/report_scaling_lib_group.2
        _syn(            "report_scaling_lib_group",
            "Generates a report of scaling library groups previously created by the define_scaling_lib_group command.",
            "report_scaling_lib_group ?-all? ?-nosplit? ?-show_list show_list? ?-object_list object_list?",
        ),
        # cat2/report_scan_chain.2
        _syn(            "report_scan_chain",
            "Reports the SCANDEF scan chains defined on the current design.",
            "report_scan_chain",
        ),
        # cat2/report_scan_compression_configuration.2
        _syn(            "report_scan_compression_configuration",
            "Displays options specified by the set_scan_compression_configuration command.",
            "report_scan_compression_configuration ?-test_mode mode_name_list?",
        ),
        # cat2/report_scan_configuration.2
        _syn(            "report_scan_configuration",
            "Displays options specified by the set_scan_configuration command.",
            "report_scan_configuration ?-test_mode mode_name_list?",
        ),
        # cat2/report_scan_group.2
        _syn(            "report_scan_group",
            "Reports all scan groups that were specified using the set_scan_group command.",
            "report_scan_group scan_group_names",
        ),
        # cat2/report_scan_link.2
        _syn(            "report_scan_link",
            "Reports the scan links specified with the set_scan_link command.",
            "report_scan_link -test_mode mode_name ?link_type?",
        ),
        # cat2/report_scan_path.2
        _syn(            "report_scan_path",
            "Displays scan paths and scan cells specified by the set_scan_path command and displays scan paths inserted by the insert_dft command.",
            "report_scan_path ?-view spec | existing_dft? ?-chain chain_name | all? ?-cell chain_name | all? ?-test_mode mode_name_list | all?",
        ),
        # cat2/report_scan_register_type.2
        _syn(            "report_scan_register_type",
            "Displays test-related information about the current design.",
            "report_scan_register_type",
        ),
        # cat2/report_scan_replacement.2
        _syn(            "report_scan_replacement",
            "Displays the scan-replacement table specified by the set_scan_replacement command.",
            "report_scan_replacement",
        ),
        # cat2/report_scan_skew_group.2
        _syn(            "report_scan_skew_group",
            "Reports scan skew groups defined by the set_scan_skew_group command.",
            "report_scan_skew_group ?scan_skew_group_list?",
        ),
        # cat2/report_scan_state.2
        _syn(            "report_scan_state",
            "Displays the scan state of the current design.",
            "report_scan_state",
        ),
        # cat2/report_scan_suppress_toggling.2
        _syn(            "report_scan_suppress_toggling",
            "Reports on the user specifications that were provided through the set_scan_suppress_toggling command in terms of the list of scan flip-flops to be gated by the insert_dft command.",
            "report_scan_suppress_toggling",
        ),
        # cat2/report_scenario_options.2
        _syn(            "report_scenario_options",
            "Reports the scenario options set by the set_scenario_options command.",
            "report_scenario_options ?-scenarios scenario_list?",
        ),
        # cat2/report_scenarios.2
        _syn(            "report_scenarios",
            "Reports scenario setup information for a multi-scenario design.",
            "report_scenarios",
        ),
        # cat2/report_script_runtime.2
        _syn(            "report_script_runtime",
            "Reports the run time of the commands issued on the current session.",
            "report_script_runtime ?-simple? ?-reset? ?-legend? ?-cpu? ?-commands command_names? ?-sort digits?",
        ),
        # cat2/report_security_configuration.2
        _syn(            "report_security_configuration",
            "Reports the security configuration for the current design.",
            "report_security_configuration",
        ),
        # cat2/report_self_gating.2
        _syn(            "report_self_gating",
            "Reports information about Self-Gating performed by Power Compiler. This command is supported only in topographical mode.",
            "report_self_gating ?-gated? ?-ungated? ?-nosplit?",
        ),
        # cat2/report_separate_process_options.2
        _syn(            "report_separate_process_options",
            "Reports whether the tool uses separate UNIX processes for extraction, placement, and routing.",
            "report_separate_process_options",
        ),
        # cat2/report_serialize_configuration.2
        _syn(            "report_serialize_configuration",
            "Displays options specified by the set_serialize_configuration command or the reset_serialize_configuration command.",
            "report_serialize_configuration",
        ),
        # cat2/report_size_only.2
        _syn(            "report_size_only",
            "Reports size_only cells in the current design along with their size_only types.",
            "report_size_only ?-nosplit? ?-summary? ?cells?",
        ),
        # cat2/report_streaming_compression_configuration.2
        _syn(            "report_streaming_compression_configuration",
            "Displays options specified by the set_streaming_compression_configuration command.",
            "report_streaming_compression_configuration ?-test_mode mode_name_list?",
        ),
        # cat2/report_supply_net.2
        _syn(            "report_supply_net",
            "Reports all supply nets in the current scope.",
            "report_supply_net ?supply_net_name? ?-include_exception?",
        ),
        # cat2/report_supply_port.2
        _syn(            "report_supply_port",
            "Reports information about the supply ports in the current scope.",
            "report_supply_port ?supply_port_name?",
        ),
        # cat2/report_synlib.2
        _syn(            "report_synlib",
            "Displays information about synthetic libraries.",
            "report_synlib library ?module_list?",
        ),
        # cat2/report_synlib_history.2
        _syn(            "report_synlib_history",
            "Displays information about the updates on DesignWare Datapath and Building Block (DWBB) IPs. The command displays updates as early as P-2019.03 release. For release prior to P, user can refer to the text file located in $SYNOPSYS/dw/doc/manuals/dwbb_history.txt for details of updates.",
            "report_synlib_history ?-modules modules? ?-from from? ?-nosplit?",
        ),
        # cat2/report_target_library_subset.2
        _syn(            "report_target_library_subset",
            "Reports target library subsets on the design.",
            "report_target_library_subset ?-object_list cells? ?-top? ?-nosplit?",
        ),
        # cat2/report_test_assume.2
        _syn(            "report_test_assume",
            "Displays the value set on the pins by the set_test_assume command.",
            "report_test_assume",
        ),
        # cat2/report_test_model.2
        _syn(            "report_test_model",
            "Displays the test model information attached to a design.",
            "report_test_model ?-design design_name?",
        ),
        # cat2/report_test_point_configuration.2
        _syn(            "report_test_point_configuration",
            "Displays options specified by the set_test_point_configuration command.",
            "report_test_point_configuration",
        ),
        # cat2/report_test_point_element.2
        _syn(            "report_test_point_element",
            "Displays options specified by the set_test_point_element command.",
            "report_test_point_element ?list_of_design_pin_objects? ?-type test_point_type?",
        ),
        # cat2/report_testability_configuration.2
        _syn(            "report_testability_configuration",
            "Displays options specified by the set_testability_configuration command.",
            "report_testability_configuration ?-type valid_type?",
        ),
        # cat2/report_threshold_voltage_group.2
        _syn(            "report_threshold_voltage_group",
            "Reports the number, area, leakage, and percentage of cells for each threshold voltage group in the design. Also shows the number, area, leakage, and percentage of cells in user-specified low threshold voltage groups. Since the threshold voltage group attribute is specified on the library cells, hierarchical cells do not have a threshold voltage group. So, their usage is reported under the \"undefined\" threshold voltage group category. During parallel_execute, leakage reporting within this command is disabled.",
            "report_threshold_voltage_group ?cell_list? ?-lvth_groups groups? ?-nosplit? ?-verbose? ?-analysis_effort low | medium | high? ?-scenarios scenario_list?",
        ),
        # cat2/report_timing_derate.2
        _syn(            "report_timing_derate",
            "Reports timing derating factors previously set for the design or for specified objects using the set_timing_derate command.",
            "report_timing_derate ?-include_inherited? ?-pocvm_guardband? ?-pocvm_coefficient_scale_factor? object_list ?-nosplit? ?-scenarios scenario_list? ?-increment? ?-multiply?",
        ),
        # cat2/report_timing_requirements.2
        _syn(            "report_timing_requirements",
            "Reports timing path requirements (user attributes) and related information.",
            "report_timing_requirements ?-attributes? ?-ignored? ?-from from_list | -rise_from rise_from_list | -fall_from fall_from_list? ?-through through_list? ?-rise_through rise_through_list? ?-fall_through fall_through_list? ?-to to_list | -rise_to rise_to_list | -fall_to fall_to_list? ?-expanded? ?-nosplit?",
        ),
        # cat2/report_tlu_plus_files.2
        _syn(            "report_tlu_plus_files",
            "Reports the files used for TLUPlus extraction. This command is supported only in topographical mode.",
            "report_tlu_plus_files ?-scenarios scenario_list?",
        ),
        # cat2/report_top_implementation_options.2
        _syn(            "report_top_implementation_options",
            "Reports the top-level design options for the linking and optimization of a block's interface logic using transparent interface optimization.",
            "report_top_implementation_options",
        ),
        # cat2/report_trace.2
        _syn(            "report_trace",
            "Produce a report of performance profile metrics collected for traced commands.",
            "report_trace ?-start | -stop | resume? ?-profile profile_type? ?-command command_name? ?-cumulative count? ?-top count? ?-quiet? ?-resume?",
        ),
        # cat2/report_track.2
        _syn(            "report_track",
            "Reports the routing tracks for a specified layer or for all layers.",
            "report_track ?-layer layer? ?-dir X | Y?",
        ),
        # cat2/report_transformed_registers.2
        _syn(            "report_transformed_registers",
            "Reports register transformations during compile",
            "report_transformed_registers ?-summary? ?-constant? ?-unloaded? ?-merged? ?-replicated? ?-multibit? ?-inverted? ?-shiftReg?",
        ),
        # cat2/report_transitive_fanin.2
        _syn(            "report_transitive_fanin",
            "Reports logic in the transitive fanin of specified sinks.",
            "report_transitive_fanin -to sink_list ?-nosplit?",
        ),
        # cat2/report_transitive_fanout.2
        _syn(            "report_transitive_fanout",
            "Reports logic in the transitive fanout of specified sources.",
            "report_transitive_fanout -clock_tree | -from source_list ?-nosplit?",
        ),
        # cat2/report_ungroup.2
        _syn(            "report_ungroup",
            "Displays ungrouping statistics during compile",
            "report_ungroup ?-summary? ?-auto_ungroup? ?-user? ?-restrictions?",
        ),
        # cat2/report_units.2
        _syn(            "report_units",
            "Reports the units used for resistance, capacitance, timing, leakage power, current, and voltage in the flow. The units must be consistent with the main library units.",
            "report_units",
        ),
        # cat2/report_upf_cell_mismatch.2
        _syn(            "report_upf_cell_mismatch",
            "Reports PM cells which are dirtily mapped by violating TLS, PVT or UPF constraint by using set_upf_cell_mismatch command.",
            "report_upf_cell_mismatch -tls_violation -pvt_mismatch -no_unmapped ?-cells cells? ?-nosplit?",
        ),
        # cat2/report_use_test_model.2
        _syn(            "report_use_test_model",
            "Reports test model usage for each subdesign under the current design.",
            "report_use_test_model",
        ),
        # cat2/report_via_ladder_candidates.2
        _syn(            "report_via_ladder_candidates",
            "Reports via ladder candidates set by the set_via_ladder_candidate command.",
            "report_via_ladder_candidates lib_pin_list",
        ),
        # cat2/report_via_ladder_constraints.2
        _syn(            "report_via_ladder_constraints",
            "Reports via ladder constraints.",
            "report_via_ladder_constraints -pins pins -output file_name",
        ),
        # cat2/report_via_ladder_rules.2
        _syn(            "report_via_ladder_rules",
            "Reports via ladder rules set by the set_via_ladder_rules command.",
            "report_via_ladder_rules",
        ),
        # cat2/report_via_rules.2
        _syn(            "report_via_rules",
            "Displays via_rule's information from the current library.",
            "report_via_rules ?-verbose? ?-nosplit? -all via_rule_list",
        ),
        # cat2/report_voltage_area.2
        _syn(            "report_voltage_area",
            "Reports the voltage areas in the design. This command is supported only in topographical mode.",
            "report_voltage_area ?-name list? ?-nosplit? ?-verbose? -all | patterns",
        ),
        # cat2/report_watermark_configuration.2
        _syn(            "report_watermark_configuration",
            "Reports the watermark configuration for the current design.",
            "report_watermark_configuration",
        ),
        # cat2/report_wire_load.2
        _syn(            "report_wire_load",
            "Displays the characteristics of the wire-load models set on a design or in a library.",
            "report_wire_load ?-design design_name? ?-name model_name? ?-libraries? ?-nosplit?",
        ),
        # cat2/report_wrapper_configuration.2
        _syn(            "report_wrapper_configuration",
            "Reports the wrapper configuration of the current design.",
            "report_wrapper_configuration ?-test_mode mode_name_list?",
        ),
        # cat2/report_write_lib_mode.2
        _syn(            "report_write_lib_mode",
            "Reports the write_lib mode of the tool, either enabled or disabled.",
            "report_write_lib_mode",
        ),
        # cat2/reset_access_control_configuration.2
        _syn(            "reset_access_control_configuration",
            "Resets the access control specification for the current design.",
            "reset_access_control_configuration",
        ),
        # cat2/reset_app_options.2
        _syn(            "reset_app_options",
            "Resets previously set values of one or more application options to the unset status.",
            "reset_app_options names",
        ),
        # cat2/reset_autofix_configuration.2
        _syn(            "reset_autofix_configuration",
            "Resets the global AutoFix configuration applied to the design for the specified fixing type.",
            "reset_autofix_configuration -type fix_type",
        ),
        # cat2/reset_autofix_element.2
        _syn(            "reset_autofix_element",
            "Resets a local AutoFix configuration applied to design objects for the specified fixing type.",
            "reset_autofix_element list_of_design_objects -type fix_type",
        ),
        # cat2/reset_bsd_configuration.2
        _syn(            "reset_bsd_configuration",
            "Removes the IEEE 1149.1 or 1149.6 specifications from a boundary-scan design.",
            "reset_bsd_configuration",
        ),
        # cat2/reset_cell_mode.2
        _syn(            "reset_cell_mode",
            "Resets the modes of the specified instances.",
            "reset_cell_mode ?instance_list?",
        ),
        # cat2/reset_clock_gate_latency.2
        _syn(            "reset_clock_gate_latency",
            "Resets all clock-latency values previously specified for or applied to clock-gating cells.",
            "reset_clock_gate_latency ?-clock clock_list?",
        ),
        # cat2/reset_design.2
        _syn(            "reset_design",
            "Removes all user-specified objects and attributes from the current design, except those defined by using the set_attribute command and UPF commands.",
            "reset_design",
        ),
        # cat2/reset_dft_clock_controller.2
        _syn(            "reset_dft_clock_controller",
            "Resets the on-chip clocking controller specification for the current design.",
            "reset_dft_clock_controller ?-test_mode mode_name_list?",
        ),
        # cat2/reset_dft_clock_gating_configuration.2
        _syn(            "reset_dft_clock_gating_configuration",
            "Resets the DFT clock-gating configuration for the current design.",
            "reset_dft_clock_gating_configuration",
        ),
        # cat2/reset_dft_configuration.2
        _syn(            "reset_dft_configuration",
            "Resets the DFT configuration for the current design specified by the set_dft_configuration command.",
            "reset_dft_configuration",
        ),
        # cat2/reset_dft_drc_rules.2
        _syn(            "reset_dft_drc_rules",
            "Resets the DFT DRC rule specifications to their default behaviors.",
            "reset_dft_drc_rules ?-violation drc_list? ?-cell cell_list?",
        ),
        # cat2/reset_dft_insertion_configuration.2
        _syn(            "reset_dft_insertion_configuration",
            "Resets the DFT insertion configuration for the current design.",
            "reset_dft_insertion_configuration",
        ),
        # cat2/reset_ieee_1500_configuration.2
        _syn(            "reset_ieee_1500_configuration",
            "Resets the IEEE 1500 configuration for the current design.",
            "reset_ieee_1500_configuration",
        ),
        # cat2/reset_logic_lock_configuration.2
        _syn(            "reset_logic_lock_configuration",
            "Resets the logic_lock configuration for the current design.",
            "reset_logic_lock_configuration",
        ),
        # cat2/reset_logicbist_configuration.2
        _syn(            "reset_logicbist_configuration",
            "Resets the LogicBIST compression configuration to the default configuration values for the current design.",
            "reset_logicbist_configuration",
        ),
        # cat2/reset_mode.2
        _syn(            "reset_mode",
            "Resets the modes of the specified instances.",
            "reset_mode ?instance_list?",
        ),
        # cat2/reset_obfuscation_configuration.2
        _syn(            "reset_obfuscation_configuration",
            "Resets the obfuscation configuration for the current design.",
            "reset_obfuscation_configuration",
        ),
        # cat2/reset_path.2
        _syn(            "reset_path",
            "Resets the specified paths to single cycle timing.",
            "reset_path ?-setup | -hold? ?-rise | -fall? ?-from from_list | -rise_from rise_from_list | -fall_from fall_from_list? ?-through through_list? ?-rise_through rise_through_list? ?-fall_through fall_through_list? ?-to to_list | -rise_to rise_to_list | -fall_to fall_to_list?",
        ),
        # cat2/reset_physical_constraints.2
        _syn(            "reset_physical_constraints",
            "Resets all current physical constraints.",
            "reset_physical_constraints",
        ),
        # cat2/reset_pipeline_scan_data_configuration.2
        _syn(            "reset_pipeline_scan_data_configuration",
            "Resets the pipeline scan data configuration specified by the set_pipeline_scan_data_configuration command.",
            "reset_pipeline_scan_data_configuration",
        ),
        # cat2/reset_power_derate.2
        _syn(            "reset_power_derate",
            "Resets the power derating factors for either the current design, a list of cells, library cells or all cells in a power group in the current design.",
            "reset_power_derate ?-scenarios scenario_list? ?-groups group_names? ?object_list?",
        ),
        # cat2/reset_scan_compression_configuration.2
        _syn(            "reset_scan_compression_configuration",
            "Resets the scan compression configuration for the current design.",
            "reset_scan_compression_configuration",
        ),
        # cat2/reset_scan_configuration.2
        _syn(            "reset_scan_configuration",
            "Resets the scan configuration for the current design.",
            "reset_scan_configuration ?-test_mode mode_name_list?",
        ),
        # cat2/reset_security_configuration.2
        _syn(            "reset_security_configuration",
            "Resets the security configuration for the current design.",
            "reset_security_configuration",
        ),
        # cat2/reset_serialize_configuration.2
        _syn(            "reset_serialize_configuration",
            "Resets the serialize configuration to the default serialize configuration values for the current design.",
            "reset_serialize_configuration",
        ),
        # cat2/reset_streaming_compression_configuration.2
        _syn(            "reset_streaming_compression_configuration",
            "Resets the streaming scan compression configuration to the default configuration values for the current design.",
            "reset_streaming_compression_configuration",
        ),
        # cat2/reset_switching_activity.2
        _syn(            "reset_switching_activity",
            "Removes switching activity information from all objects in the current design.",
            "reset_switching_activity ?-verbose? ?cell_list?",
        ),
        # cat2/reset_test_mode.2
        _syn(            "reset_test_mode",
            "Resets the test mode for the current design.",
            "reset_test_mode",
        ),
        # cat2/reset_test_point_configuration.2
        _syn(            "reset_test_point_configuration",
            "Resets the automatic test point insertion configuration for the current design.",
            "reset_test_point_configuration",
        ),
        # cat2/reset_testability_configuration.2
        _syn(            "reset_testability_configuration",
            "Resets the testability configuration for the current design.",
            "reset_testability_configuration ?-type type?",
        ),
        # cat2/reset_timing_derate.2
        _syn(            "reset_timing_derate",
            "Removes all derating factors set on the current design and libraries.",
            "reset_timing_derate ?-pocvm_guardband? ?-pocvm_coefficient_scale_factor? ?-increment? ?-multiply?",
        ),
        # cat2/reset_watermark_configuration.2
        _syn(            "reset_watermark_configuration",
            "Resets the watermark configuration for the current design.",
            "reset_watermark_configuration",
        ),
        # cat2/reset_wrapper_configuration.2
        _syn(            "reset_wrapper_configuration",
            "Resets the wrapper configuration for the current design.",
            "reset_wrapper_configuration ?-test_mode mode_name?",
        ),
        # cat2/resize_polygon.2
        _syn(            "resize_polygon",
            "Pushes the edges of the specified polygon inward or outward by the specified direction and distance.",
            "resize_polygon polygons -size size -size_left size -size_right size -size_bottom size -size_top size",
        ),
        # cat2/rewire_clock_gating.2
        _syn(            "rewire_clock_gating",
            "Changes the clock-gating cell implemented by the tool for a particular gated cell.",
            "rewire_clock_gating ?-gating_cell new_clock_gating_cell? ?-gated_objects gated_objects_list? ?-balance_fanout? ?-undo? ?-verbose?",
        ),
        # cat2/rp_group_inclusions.2
        _syn(            "rp_group_inclusions",
            "Returns a collection of relative placement groups that are directly included in the specified relative placement groups.",
            "rp_group_inclusions ?rp_groups?",
        ),
        # cat2/rp_group_instantiations.2
        _syn(            "rp_group_instantiations",
            "Returns a collection of relative placement groups that are instantiated in any of the specified relative placement groups.",
            "rp_group_instantiations ?rp_groups?",
        ),
        # cat2/rp_group_references.2
        _syn(            "rp_group_references",
            "Returns a collection of cells that are directly included in the specified relative placement groups.",
            "rp_group_references ?rp_groups? ?-leaf | -instance | -all_leaf?",
        ),
        # cat2/run_test_point_analysis.2
        _syn(            "run_test_point_analysis",
            "Runs SpyGlass DFT testability analysis.",
            "run_test_point_analysis",
        ),
        # cat2/saif_map.2
        _syn(            "saif_map",
            "Manages the SAIF name-mapping mechanism for reading SAIF files.",
            "saif_map ?-start? ?-end? ?-reset? ?-report? ?-get_name? ?-set_name names? ?-add_name names? ?-remove_name names? ?-clear_name? ?-get_object_names name? ?-create_map? ?-write_map filename? ?-read_map filename? ?-type type? ?-inverted? ?-instances objects? ?-no_hierarchical? ?-columns columns? ?-sort columns? ?-rtl_summary? ?-missing_rtl? ?-input SAIF_file? ?-source_instance SAIF_instance_name? ?-target_instance target_instance_name? ?-review? ?-preview? ?-hsep character? ?object_list? ?-nosplit? ?-essential?",
        ),
        # cat2/save_lib.2
        _syn(            "save_lib",
            "Saves a library and its changed blocks to disk.",
            "save_lib ?-as library_name ?-version release_version?? ?-all? ?-compress? ?library?",
        ),
        # cat2/save_qtm_model.2
        _syn(            "save_qtm_model",
            "Saves the current quick timing model (QTM) description.",
            "save_qtm_model ?-format db | lib | script?",
        ),
        # cat2/save_ssf.2
        _syn(            "save_ssf",
            "Writes out the design's SSF commands into the specified file.",
            "save_ssf ?file_name?",
        ),
        # cat2/save_upf.2
        _syn(            "save_upf",
            "Writes out the design's UPF power intent as a UPF command script.",
            "save_upf ?upf_file_name? ?-supplemental supf_file_name? ?-include_supply_exceptions? ?-full_upf?",
        ),
        # cat2/scale_floorplan.2
        _syn(            "scale_floorplan",
            "Scales the given user floorplan.",
            "scale_floorplan -scale_ratio {scale_ratio | scale_ratio_x scale_ratio_y} -output output_def_name ?-script script_name? ?-apply?",
        ),
        # cat2/select_block_scenario.2
        _syn(            "select_block_scenario",
            "Performs scenario mapping between the top-level design and interface logic models (ILMs) or block abstractions.",
            "select_block_scenario ?-scenarios top_scenario_list? ?-block_references block_list? -block_scenario block_scenario | -reset",
        ),
        # cat2/set_access_control_configuration.2
        _syn(            "set_access_control_configuration",
            "Sets the default access control specification for the current design.",
            "set_access_control_configuration ?-test_mode_locks test_mode_list? ?-unlock_patterns test_mode_unlock_pattern_list?",
        ),
        # cat2/set_active_scenarios.2
        _syn(            "set_active_scenarios",
            "Specifies which scenarios are to be active.",
            "set_active_scenarios scenario_list | -all",
        ),
        # cat2/set_ahfs_options.2
        _syn(            "set_ahfs_options",
            "Specifies the options to use when running automatic high-fanout synthesis (AHFS).",
            "set_ahfs_options ?-enable_port_punching true | false? ?-no_port_punching cells? ?-default_reference references? ?-port_map_file file_name? ?-preserve_boundary_phase true | false? ?-constant_nets true | false? ?-global_route true | false? ?-default?",
        ),
        # cat2/set_always_on_cell.2
        _syn(            "set_always_on_cell",
            "Sets on-the-fly specification for an always-on library cell.",
            "set_always_on_cell cell_name",
        ),
        # cat2/set_always_on_strategy.2
        _syn(            "set_always_on_strategy",
            "Sets the always-on strategy for specified shutdown power domains.",
            "set_always_on_strategy -object_list list_of_domains -cell_type single_power | dual_power",
        ),
        # cat2/set_analyze_rtl_logic_level_threshold.2
        _syn(            "set_analyze_rtl_logic_level_threshold",
            "Specifies the logic level threshold value to be used by report_logic_levels command. Also used to remove the previously set value.",
            "set_analyze_rtl_logic_level_threshold ?-group group_name? ?-reset? ?threshold?",
        ),
        # cat2/set_annotated_check.2
        _syn(            "set_annotated_check",
            "Sets the setup, hold, recovery, or removal timing check value between two pins.",
            "set_annotated_check check_value -from from_pins -to to_pins -setup | -hold | -recovery | -removal | -nochange_high | -nochange_low ?-rise | -fall? ?-clock rise | fall? ?-worst? ?-increment?",
        ),
        # cat2/set_annotated_delay.2
        _syn(            "set_annotated_delay",
            "Sets the net or cell delay value between two pins.",
            "set_annotated_delay -net | -cell ?-dont_touch? ?-load_delay load_delay_type? ?-rise | -fall? ?-min? ?-max? delay_value ?-from from_pins? ?-to to_pins? ?-worst?",
        ),
        # cat2/set_annotated_transition.2
        _syn(            "set_annotated_transition",
            "Sets the transition time at a given pin.",
            "set_annotated_transition ?-rise | -fall? ?-min? ?-max? transition port_pin_list",
        ),
        # cat2/set_app_options.2
        _syn(            "set_app_options",
            "Sets application options to the specified value.",
            "set_app_options ?-block block? ?-category category? ?-name name? ?-value value? ?-list name_value_list?",
        ),
        # cat2/set_app_var.2
        _syn(            "set_app_var",
            "Sets the value of an application variable.",
            "set_app_var -default var value",
        ),
        # cat2/set_aspect_ratio.2
        _syn(            "set_aspect_ratio",
            "Specifies the placement aspect ratio for the core area. This command is supported only in topographical mode.",
            "set_aspect_ratio y_x_ratio",
        ),
        # cat2/set_attribute.2
        _syn(            "set_attribute",
            "Sets an attribute to a specified value on the specified list of objects.",
            "set_attribute objects attribute_name attribute_value ?-type boolean | integer | float | string? ?-bus? ?-quiet?",
        ),
        # cat2/set_auto_disable_drc_nets.2
        _syn(            "set_auto_disable_drc_nets",
            "Sets the auto_disable_drc_net attribute on the current design, causing the specified nets to have DRC disabled. This command was previously called by the set_auto_ideal_nets command.",
            "set_auto_disable_drc_nets ?-default? ?-none? ?-all? ?-clock true | false? ?-constant true | false? ?-scan true | false? ?-on_clock_network true | false?",
        ),
        # cat2/set_auto_floorplan_constraints.2
        _syn(            "set_auto_floorplan_constraints",
            "Sets constraints for implicit floorplan initialization.",
            "set_auto_floorplan_constraints ?-control_type core | die? ?-side_length {side_a side_b ?side_c side_d side_e side_f?}? ?-side_ratio {side_a side_b ?side_c side_d side_e side_f?}? ?-core_utilization utilization? ?-boundary {{x y} {x y} {x y} {x y} ...}? ?-orientation N | W | S | E? ?-coincident_boundary true | false? ?-core_offset {value | vertical_value horizontal_value | side_1 ... side_N}? ?-row_core_ratio row_core_ratio? ?-flip_first_row true | false? ?-honor_pad_limit? ?-site_def site_def_name? ?-origin_offset {x, y}? ?-row_pattern {row_pattern_name}? ?-track_script {track_creation_script_name}? ?-reset?",
        ),
        # cat2/set_autofix_configuration.2
        _syn(            "set_autofix_configuration",
            "Configures automatic fixing of violations (AutoFix), performed by DFT insertion, globally for the current design.",
            "set_autofix_configuration ?-type fix_type? ?-control_signal control_name? ?-test_data test_data_name? ?-method method? ?-fix_data enable | disable? ?-fix_latch enable | disable? ?-include_elements list_of_design_objects? ?-exclude_elements list_of_design_objects?",
        ),
        # cat2/set_autofix_element.2
        _syn(            "set_autofix_element",
            "Configures automatic fixing of violations (AutoFix), performed by DFT insertion, locally for a particular part of the design.",
            "set_autofix_element list_of_design_objects ?-type fix_type? ?-control_signal control_name? ?-test_data test_data_name? ?-method method? ?-fix_data enable | disable? ?-fix_latch enable | disable?",
        ),
        # cat2/set_autoungroup_options.2
        _syn(            "set_autoungroup_options",
            "Specifies the options to control autoungrouping.",
            "set_autoungroup_options ?-start_level level? ?-keep_parent_hierarchies constraints? ?-reset?",
        ),
        # cat2/set_balance_registers.2
        _syn(            "set_balance_registers",
            "Sets the balance_registers attribute on the specified designs or on the current design, so that the design is retimed during compile.",
            "set_balance_registers ?-design? ?true | false? ?design_list?",
        ),
        # cat2/set_boundary_cell.2
        _syn(            "set_boundary_cell",
            "Sets the boundary-cell configuration for the specified ports and core cells.",
            "set_boundary_cell -class core_wrapper | shadow_wrapper | bsd ?-function function? ?-ports port_list? ?-core_cells core_list? ?-type type? ?-design design_name? ?-register_io_implementation swap | in_place? ?-use_dedicated_wrapper_clock true | false? ?-safe_state 0 | 1 | none? ?-share true | false? ?-name bcell_name? ?-shift_clk bcell_shift_clk? ?-instance hier_cell_list? ?-include cell_list? ?-exclude cell_list? ?-reuse_threshold threshold_value? ?-hookup_pin hookup_pin_name? ?-add_toggle_logic true | false? ?-add_shared_wrapper_cell_only true | false? ?-pins list_of_pins? ?-internal_pin_type dir? ?-aon_enable aon_enable_port_or_hookup_pin? ?-add_loopback_logic true | false? ?-scan_en atpg_shift_port_or_hookup_pin? ?-internal_pins list_of_pins?",
        ),
        # cat2/set_boundary_cell_io.2
        _syn(            "set_boundary_cell_io",
            "Specifies the primary inputs (PIs) and primary outputs (POs) of a boundary cell in the current design.",
            "set_boundary_cell_io -access {pin_type pin_name} -type boundary | wrapper -cell shift_flop_name",
        ),
        # cat2/set_boundary_optimization.2
        _syn(            "set_boundary_optimization",
            "Sets the boundary_optimization attribute on specified cells, references, or designs, thus allowing for optimization across hierarchical boundaries.",
            "set_boundary_optimization object_list ?true | false?",
        ),
        # cat2/set_bsd_ac_port.2
        _syn(            "set_bsd_ac_port",
            "Identifies the AC ports in your design.",
            "set_bsd_ac_port -port_list list_of_ports",
        ),
        # cat2/set_bsd_compliance.2
        _syn(            "set_bsd_compliance",
            "Specifies an IEEE 1149.1 compliant pattern for a boundary-scan design.",
            "set_bsd_compliance -name pattern_name -pattern signal_port_bit_value_pairs",
        ),
        # cat2/set_bsd_configuration.2
        _syn(            "set_bsd_configuration",
            "Specifies the boundary-scan configuration for a design.",
            "set_bsd_configuration ?-asynchronous_reset true | false? ?-default_package package_name? ?-instruction_encoding binary | one_hot? ?-ir_width instruction_register_length? ?-style synchronous | asynchronous? ?-check_pad_designs none | all | pad_design_list? ?-control_cell_max_fanout max_fanout? ?-ieee1149.1_1993 enable | disable? ?-std std_version_name_list? ?-rtl enable | disable?",
        ),
        # cat2/set_bsd_instruction.2
        _syn(            "set_bsd_instruction",
            "Specifies boundary-scan instructions used by the insert_dft command for the current design or used by the check_bsd command in the verification flow.",
            "set_bsd_instruction ?-view existing_dft | spec? instruction_list ?-code inst_code_list? ?-register register_name? ?-input_clock_condition clock_conditioning? ?-output_condition BSR | HIGHZ | NONE? ?-internal_scan pin_name? ?-capture_value capture_value_list? ?-private? ?-clock_cycles clock_cycle_list? ?-signature pattern? ?-high pin_name_list? ?-low pin_name_list? ?-sequential_high pin_name_list? ?-sequential_low pin_name_list? ?-time real_time? ?-excluded_bsr_condition CLAMP | NONE? ?-bsd_init_data init_value? ?-length register_length?",
        ),
        # cat2/set_bsd_linkage_port.2
        _syn(            "set_bsd_linkage_port",
            "Identifies the linkage ports in your design.",
            "set_bsd_linkage_port -port_list list_of_ports",
        ),
        # cat2/set_bsd_power_up_reset.2
        _syn(            "set_bsd_power_up_reset",
            "Specifies and characterizes the power-up reset cell for the current design.",
            "set_bsd_power_up_reset -cell_name cell_name -reset_pin_name reset_pin_name -active high | low ?-delay power_up_reset_delay?",
        ),
        # cat2/set_cell_degradation.2
        _syn(            "set_cell_degradation",
            "Sets the cell_degradation attribute to a specified value on the specified ports or designs.",
            "set_cell_degradation cell_degradation_value object_list",
        ),
        # cat2/set_cell_internal_power.2
        _syn(            "set_cell_internal_power",
            "Sets or removes the power_value attribute on the specified pins. The value represents the power consumption for a single toggle of each pin.",
            "set_cell_internal_power pin_list ?power_value ?unit?? | -delete_all",
        ),
        # cat2/set_cell_location.2
        _syn(            "set_cell_location",
            "Specifies the physical location, orientation, and dont_touch status for leaf cells. This command is supported in Design Compiler topographical mode only.",
            "set_cell_location -coordinates {x y} ?-orientation target_orient? ?-fixed? object_list",
        ),
        # cat2/set_cell_mode.2
        _syn(            "set_cell_mode",
            "Selects the mode of a component.",
            "set_cell_mode ?mode_list? ?instance_list?",
        ),
        # cat2/set_check_library_options.2
        #   WARNING: unclosed bracket '[' at position 801
        _syn(            "set_check_library_options",
            "Sets options for the check_library command for various logic library and physical library checks.",
            "set_check_library_options ?-cell_area? ?-cell_footprint? ?-bus_delimiter? ?-tech_consistency? ?-view_comparison? ?-same_name_cell? ?-signal_em? ?-antenna? ?-rectilinear_cell? ?-physical_only_cell? ?-phys_property {property_list}? ?-rail view_data? ?-routeability? ?-routability? ?-min_pin_layer layer_name? ?-tech? ?-placement? ?-pattern_must_join_pin? ?-pattern_must_join_pin_exclusion_list lib_pin_list? ?-drc? ?-scaling {scaling_types}? ?-mcmm? ?-upf? ?-optimization {power}? ?-compare {construct | attribute | value}? ?-tolerance {type relative_tolerance absolute_tolerance}? ?-validate {timing noise ?value?}? ?-analyze {nominal_vs_sigma | table_trend | table_bound | table_slope | table_index | sensitivity | voltage_range}? ?-criteria {criteria_spec}? ?-group_attribute {groups_or_attributes}? ?-report_format {format_spec} ?-leq? ?-by_group_order? ?-char_integrity? ?-significant_digits digits? ?-physical? ?-logic_vs_physical? ?-logic? ?-reset? ?-all?",
        ),
        # cat2/set_cle_options.2
        _syn(            "set_cle_options",
            "Sets command line editor settings.",
            "set_cle_options ?-mode vi | emacs? ?-beep on | off? ?-defaults?",
        ),
        # cat2/set_clock_exclusivity.2
        _syn(            "set_clock_exclusivity",
            "Specifies a cell for which all the clocks that traverse from the input pins to the output pin will be mutually exclusive.",
            "set_clock_exclusivity -output output_pin ?-type mux | user_defined? ?-inputs input_pin_list?",
        ),
        # cat2/set_clock_gate_latency.2
        _syn(            "set_clock_gate_latency",
            "Specifies clock network latency values to be used for clock-gating cells, as a function of clock domain, clock-gating stage and fanout.",
            "set_clock_gate_latency ?-clock clock_list? ?-overwrite? -stage cg_stage -fanout_latency cg_fanout_list ?-transitive_fanout?",
        ),
        # cat2/set_clock_gating_check.2
        _syn(            "set_clock_gating_check",
            "Puts setup and hold checks on clock-gating cells.",
            "set_clock_gating_check ?-setup setup_margin? ?-hold hold_margin? ?-rise? ?-fall? ?-high | -low? ?object_list?",
        ),
        # cat2/set_clock_gating_enable.2
        _syn(            "set_clock_gating_enable",
            "Controls the signals to be used as the clock gating enable in the execution of the compile_ultra -gate_clock command.",
            "set_clock_gating_enable ?-exclude objects_to_exclude? ?-undo objects_to_remove_exclusion?",
        ),
        # cat2/set_clock_gating_objects.2
        _syn(            "set_clock_gating_objects",
            "Forces the enabling or disabling of clock gating for specified objects in the current design, overriding all conditions necessary for automatic RTL clock gating, by the compile_ultra -gate_clock command. Objects can be of type register, hierarchical cell, power domain, or design.",
            "set_clock_gating_objects ?-force_include object_list? ?-exclude object_list? ?-include object_list? ?-undo object_list?",
        ),
        # cat2/set_clock_gating_registers.2
        _syn(            "set_clock_gating_registers",
            "Forces the enabling or disabling of clock gating for the specified registers in the current design, overriding all conditions necessary for automatic RTL clock gating, performed by the compile_ultra -gate_clock command.",
            "set_clock_gating_registers ?-include_instances register_list? ?-exclude_instances register_list? ?-undo register_list?",
        ),
        # cat2/set_clock_gating_style.2
        _syn(            "set_clock_gating_style",
            "Sets the clock-gating style for clock-gate insertion and replacement.",
            "set_clock_gating_style ?-sequential_cell none | latch? ?-minimum_bitwidth minsize_value? ?-setup setup_value? ?-hold hold_value? ?-positive_edge_logic {cell_list | integrated ?active_low_enable? ?invert_gclk?}? ?-negative_edge_logic {cell_list | integrated ?active_low_enable? ?invert_gclk?}? ?-control_point none | before | after? ?-control_signal scan_enable | test_mode? ?-observation_point true | false? ?-observation_logic_depth depth_value? ?-max_fanout max_fanout_count? ?-num_stages num_stages_count? ?-no_sharing? ?-instances {instances_list}? ?-power_domains {power_domain_list}? ?-designs {designs_list}?",
        ),
        # cat2/set_clock_jitter.2
        _syn(            "set_clock_jitter",
            "Sets the duty-cycle jitter and/or the cycle clock jitter.",
            "set_clock_jitter ?-cycle cycle_to_cycle_jitter? ?-duty_cycle duty_cycle_jitter? -clocks clock_list",
        ),
        # cat2/set_clock_sense.2
        _syn(            "set_clock_sense",
            "Specifies the clock sense (with respect to the clock source) propagating forward from the specified pins.",
            "set_clock_sense -stop_propagation | -logical_stop_propagation | -positive | -negative | -pulse pulse_type ?-clocks clocks? pins",
        ),
        # cat2/set_combinational_type.2
        _syn(            "set_combinational_type",
            "Sets attributes on cell instances to specify which combinational cells from the target library are to be used by the compile command.",
            "set_combinational_type -replacement_gate replacement_gate ?cell_list?",
        ),
        # cat2/set_compile_directives.2
        _syn(            "set_compile_directives",
            "Controls the application of high-level optimization operations on cells, hierarchical pins, references, designs, and library cells.",
            "set_compile_directives object_list ?-delete_unloaded_gate true | false? ?-constant_propagation true | false? ?-phase_inversion true | false? ?-local_optimization true | false? ?-critical_path_resynthesis true | false?",
        ),
        # cat2/set_compile_partitions.2
        _syn(            "set_compile_partitions",
            "Specifies the compile partitions for the current design.",
            "set_compile_partitions -level level | -designs design_list | -all | -auto ?-force? ?-no_reset?",
        ),
        # cat2/set_compile_power_high_effort.2
        _syn(            "set_compile_power_high_effort",
            "Used to enable DCNXT high effort power options.",
            "set_compile_power_high_effort ?-leakage true | false? ?-total true | false?",
        ),
        # cat2/set_compile_spg_mode.2
        _syn(            "set_compile_spg_mode",
            "Sets tool settings to improve timing correlation with either the IC Compiler II or IC Compiler tool. The set_compile_spg_mode command settings take effect when you use the compile_ultra, compile_ultra -incremental, or optimize_netlist -area command.",
            "set_compile_spg_mode ?-reset?",
        ),
        # cat2/set_congestion_optimization.2
        _syn(            "set_congestion_optimization",
            "Sets the congestion_optimization attribute on the specified hierarchical cells or designs, allowing congestion optimization to be performed on the objects. This command is supported only in topographical mode.",
            "set_congestion_optimization obj_list ?true | false?",
        ),
        # cat2/set_congestion_options.2
        _syn(            "set_congestion_options",
            "Sets options for congestion optimization.",
            "set_congestion_options ?-max_util value? ?-layer name? ?-availability value? ?-coordinate {X1 Y1 X2 Y2}?",
        ),
        # cat2/set_connection_class.2
        _syn(            "set_connection_class",
            "Sets the connection class value on ports.",
            "set_connection_class connection_class_value object_list",
        ),
        # cat2/set_constant_register_removal.2
        _syn(            "set_constant_register_removal",
            "Sets an attribute to constant register(s) to selectively preserve or optimize it.",
            "set_constant_register_removal objects true | false object_list",
        ),
        # cat2/set_context_margin.2
        _syn(            "set_context_margin",
            "Specifies the margin by which to tighten or relax constraints.",
            "set_context_margin ?-percent? ?-relax? ?-min? ?-max? value ?object_list?",
        ),
        # cat2/set_cost_priority.2
        _syn(            "set_cost_priority",
            "Sets the cost_priority attribute to a specified value on the current design.",
            "set_cost_priority ?-default? ?-delay? cost_list ?-design_rules? ?-min_delay?",
        ),
        # cat2/set_critical_range.2
        _syn(            "set_critical_range",
            "Sets the critical_range attribute to a specified value on a list of designs.",
            "set_critical_range range_value designs",
        ),
        # cat2/set_current_command_mode.2
        _syn(            "set_current_command_mode",
            "",
            "set_current_command_mode -mode command_mode | -command command",
        ),
        # cat2/set_current_spfm.2
        _syn(            "set_current_spfm",
            "Set the current spfm value on the design.",
            "set_current_spfm urrent_spfm",
        ),
        # cat2/set_data_check.2
        _syn(            "set_data_check",
            "Sets data-to-data checks using the specified values of setup and hold time.",
            "set_data_check -from from_object | -rise_from from_object | -fall_from from_object -to to_object | -rise_to to_object | -fall_to to_object ?-setup | -hold? ?-clock clock_object? ?check_value?",
        ),
        # cat2/set_datapath_gating_options.2
        _syn(            "set_datapath_gating_options",
            "Specifies whether an instance should be included or excluded for datapath gating processing.",
            "set_datapath_gating_options ?-include instance_or_design? ?-exclude instance_or_design? ?-reset? ?-dp? ?-dw? ?-noungroup? ?-retime instance_or_design? ?-retime_clk_period period_value?",
        ),
        # cat2/set_datapath_optimization_effort.2
        _syn(            "set_datapath_optimization_effort",
            "Sets the datapath_optimization_effort attribute on specified designs, cells, or references, indicating the level of datapath optimization during compile_ultra command activity.",
            "set_datapath_optimization_effort object_list effort_level",
        ),
        # cat2/set_default_drive.2
        _syn(            "set_default_drive",
            "Sets the default driving strength for specified objects, to be used by Top-Down Environmental Propagation (TDEP).",
            "set_default_drive ?-min? ?-max? ?-rise? ?-fall? ?-none? ?resistance? ?cell_or_pin_list?",
        ),
        # cat2/set_default_driving_cell.2
        _syn(            "set_default_driving_cell",
            "Sets the default driving cell for specified objects, to be used by Top-Down Environmental Propagation (TDEP).",
            "set_default_driving_cell ?-lib_cell lib_cell_name? ?-library lib? ?-rise? ?-fall? ?-pin pin_name? ?-from_pin from_pin_name? ?-dont_scale? ?-no_design_rule? ?-multiply_by factor? ?-none? cell_or_pin_list",
        ),
        # cat2/set_default_fanout_load.2
        _syn(            "set_default_fanout_load",
            "Sets the default fanout load to be used by Top-Down Environmental Propagation (TDEP).",
            "set_default_fanout_load ?-none? ?fanout_load_value? ?cell_or_pin_list?",
        ),
        # cat2/set_default_input_delay.2
        _syn(            "set_default_input_delay",
            "Sets the value of the input delay as a percentage of the clock period to be assigned during environment propagation.",
            "set_default_input_delay ?-none? percent_delay ?cell_or_pin_list?",
        ),
        # cat2/set_default_load.2
        _syn(            "set_default_load",
            "Sets the default load to be used by Top-Down Environmental Propagation (TDEP).",
            "set_default_load ?-min? ?-max? ?-pin_load? ?-wire_load? ?-none? ?value? ?cell_or_pin_list?",
        ),
        # cat2/set_default_output_delay.2
        _syn(            "set_default_output_delay",
            "Sets the output delay as a percentage of the clock period to be assigned during environment propagation.",
            "set_default_output_delay ?-none? percent_delay ?cell_or_pin_list?",
        ),
        # cat2/set_delay_estimation_options.2
        _syn(            "set_delay_estimation_options",
            "Sets the parameters that influence preroute delay estimation. This command is supported only in topographical mode.",
            "set_delay_estimation_options ?-min_unit_horizontal_capacitance unit_capacitance? ?-min_unit_vertical_capacitance unit_capacitance? ?-min_unit_horizontal_resistance unit_resistance? ?-min_unit_vertical_resistance unit_resistance? ?-max_unit_horizontal_capacitance unit_capacitance? ?-max_unit_vertical_capacitance unit_capacitance? ?-max_unit_horizontal_resistance unit_resistance? ?-max_unit_vertical_resistance unit_resistance? ?-min_unit_horizontal_capacitance_scaling_factor scaling_factor? ?-min_unit_vertical_capacitance_scaling_factor scaling_factor? ?-min_unit_horizontal_resistance_scaling_factor scaling_factor? ?-min_unit_vertical_resistance_scaling_factor scaling_factor? ?-max_unit_horizontal_capacitance_scaling_factor scaling_factor? ?-max_unit_vertical_capacitance_scaling_factor scaling_factor? ?-max_unit_horizontal_resistance_scaling_factor scaling_factor? ?-max_unit_vertical_resistance_scaling_factor scaling_factor? ?-min_via_resistance via_resistance? ?-max_via_resistance via_resistance? ?-min_via_resistance_scaling_factor scaling_factor? ?-max_via_resistance_scaling_factor scaling_factor? ?-density_outside_block density? ?-default?",
        ),
        # cat2/set_design_attributes.2
        _syn(            "set_design_attributes",
            "Sets the specified UPF attribute and value on the listed cells.",
            "set_design_attributes ?-elements list? ?-models list? -attribute name_value_pair",
        ),
        # cat2/set_design_license.2
        _syn(            "set_design_license",
            "Adds license information to the current design and can be used to require a license before a design can be read in.",
            "set_design_license ?-dont_show references? ?-quiet? ?-limited limited_keys? regular_keys",
        ),
        # cat2/set_design_top.2
        _syn(            "set_design_top",
            "Specifies the top-level design instance.",
            "set_design_top instance_name",
        ),
        # cat2/set_device_constraint.2
        _syn(            "set_device_constraint",
            "For DCNXT, limits the usage of narrow and/or wide device library cells to a specified percentage of all cells.",
            "set_device_constraint ?-narrow_percentage percent_value? ?-wide_percentage percent_value? ?-cost cell_count? ?-include_blackboxes? ?-reset?",
        ),
        # cat2/set_device_group_type.2
        _syn(            "set_device_group_type",
            "For DCNXT, assign device_group labels to narrow or wide device group type.",
            "set_device_group_type ?-type narrow | wide? ?device_groups? ?-reset?",
        ),
        # cat2/set_dft_clock_controller.2
        _syn(            "set_dft_clock_controller",
            "Specifies the parameters for DFT-inserted clock controllers.",
            "set_dft_clock_controller ?-cell_name controller_cell_name? -design_name controller_design_name ?-ateclocks port_list? ?-pllclocks pin_list? ?-1x_clocks pin_list? ?-2x_clocks pin_list? ?-4x_clocks pin_list? ?-chain_count number_chains? ?-cycles_per_clock number_cycles? ?-test_mode_port port_name?",
        ),
        # cat2/set_dft_clock_gating_configuration.2
        _syn(            "set_dft_clock_gating_configuration",
            "Specifies the clock-gating configuration for a design.",
            "set_dft_clock_gating_configuration ?-exclude_elements object_list? ?-dont_connect_cgs_of cell_list?",
        ),
        # cat2/set_dft_clock_gating_pin.2
        _syn(            "set_dft_clock_gating_pin",
            "Specifies the test pin of a clock-gating cell in a design. The main purpose of this command is to identify the unconnected test pins of the clock-gating cells that were not inserted by Power Compiler. These pins are connected to test ports when you run the insert_dft command.",
            "set_dft_clock_gating_pin object_list -pin_name instance_pin_name ?-control_signal ScanEnable | TestMode | scan_enable | test_mode? ?-active_state 1 | 0?",
        ),
        # cat2/set_dft_configuration.2
        _syn(            "set_dft_configuration",
            "Sets the DFT configuration for the current design.",
            "set_dft_configuration ?-scan enable | disable? ?-fix_clock enable | disable? ?-fix_set enable | disable? ?-fix_reset enable | disable? ?-fix_xpropagation enable | disable? ?-fix_bus enable | disable? ?-fix_bidirectional enable | disable? ?-testability enable | disable? ?-test_points enable | disable? ?-wrapper enable | disable? ?-boundary enable | disable? ?-bsd enable | disable? ?-clock_controller enable | disable? ?-mode_decoding_style binary | one_hot? ?-scan_compression enable | disable? ?-streaming_compression enable | disable? ?-pipeline_scan_data enable | disable? ?-connect_clock_gating enable | disable? ?-integration enable | disable? ?-power_control enable | disable? ?-ieee_1500 enable | disable? ?-control_points enable | disable? ?-observe_points enable | disable?",
        ),
        # cat2/set_dft_connect.2
        _syn(            "set_dft_connect",
            "Specifies a list of DFT connectivity associations. The specified source is connected to objects specified in the target list.",
            "set_dft_connect string_label -type clock_gating_control | scan_enable -source port_or_pin ?-target object_list? ?-rise_target rise_clock_list? ?-fall_target fall_clock_list? ?-exclude cell_list?",
        ),
        # cat2/set_dft_drc_configuration.2
        _syn(            "set_dft_drc_configuration",
            "Sets the DFT DRC configuration for the current design.",
            "set_dft_drc_configuration ?-internal_pins enable | disable? ?-pll_bypass enable | disable? ?-assume_pi_scan enable | disable? ?-assume_po_scan enable | disable? ?-static_x_analysis enable | disable? ?-use_test_model true | false? ?-clock_gating_init_cycles integer? ?-allow_se_set_reset_fix true | false? ?-analyze_multi_clock_activation enable | disable?",
        ),
        # cat2/set_dft_drc_rules.2
        _syn(            "set_dft_drc_rules",
            "Alters how certain DRC rule violations affect DFT insertion for the specified cells.",
            "set_dft_drc_rules ?-allow drc_list? ?-ignore drc_list? ?-cell cell_list?",
        ),
        # cat2/set_dft_equivalent_signals.2
        _syn(            "set_dft_equivalent_signals",
            "Sets a given list of DFT signals as equivalents.",
            "set_dft_equivalent_signals signal_list",
        ),
        # cat2/set_dft_insertion_configuration.2
        _syn(            "set_dft_insertion_configuration",
            "Sets the DFT insertion configuration for the current design.",
            "set_dft_insertion_configuration ?-map_effort low | medium | high? ?-synthesis_optimization none | all? ?-route_scan_enable true | false? ?-route_scan_clock true | false? ?-route_scan_serial true | false? ?-preserve_design_name true | false? ?-unscan true | false?",
        ),
        # cat2/set_dft_location.2
        _syn(            "set_dft_location",
            "Specifies the DFT hierarchy location for DFT insertion.",
            "set_dft_location dft_hier_name ?-exclude CODEC | TCM | LOCKUP_LATCH | PIPELINE_SI_LOGIC | PIPELINE_SE_LOGIC | WRAPPER | BSR | TAP | REC_MUX | PLL | SERIAL_CNTRL | SERIAL_REG | XOR_SELECT | RETIMING_FLOP | IEEE_1500? ?-include CODEC | TCM | LOCKUP_LATCH | PIPELINE_SI_LOGIC | PIPELINE_SE_LOGIC | WRAPPER | BSR | TAP | REC_MUX | PLL | SERIAL_CNTRL | SERIAL_REG | XOR_SELECT | RETIMING_FLOP | IEEE_1500?",
        ),
        # cat2/set_dft_power_control.2
        _syn(            "set_dft_power_control",
            "Specifies the power controller block instance for the current design.",
            "set_dft_power_control power_controller_hierarchical_instance_name",
        ),
        # cat2/set_dft_signal.2
        #   WARNING: unclosed bracket '[' at position 107
        _syn(            "set_dft_signal",
            "Specifies the DFT signal types for DRC and DFT insertion.",
            "set_dft_signal ?-view existing_dft | spec? ?-test_mode mode_name_list? -type signal_type ?-port port_list? ?-active_state 0 | 1 ?-timing timing? ?-period period? ?-hookup_pin hookup_pin? ?-hookup_sense hookup_sense? ?-internal_clocks none | single | multi? ?-ctrl_bits ctrl_bits_list? ?-pll_clock clock_name? ?-ate_clock clock_name? ?-differential_clock clock_port? ?-connect_to object_list? ?-connect_to_domain_rise clock_list? ?-connect_to_domain_fall clock_list? ?-usage use_type? ?-associated_internal_clocks clock_pins_list? ?-associated_clock associated_clock? ?-exclude cell_list? ?-codec decompressor_name?",
        ),
        # cat2/set_direct_power_rail_tie.2
        _syn(            "set_direct_power_rail_tie",
            "Sets the direct_power_rail_tie attribute on library pins.",
            "set_direct_power_rail_tie lib_pin_list ?true | false?",
        ),
        # cat2/set_disable_auto_mux_clock_exclusivity.2
        _syn(            "set_disable_auto_mux_clock_exclusivity",
            "Disables automatic inference of MUXed clock exclusivity at specified cell output pins.",
            "set_disable_auto_mux_clock_exclusivity ?object_list?",
        ),
        # cat2/set_disable_clock_gating_check.2
        _syn(            "set_disable_clock_gating_check",
            "Disables the clock-gating check for the specified objects in the current design.",
            "set_disable_clock_gating_check object_list",
        ),
        # cat2/set_domain_supply_net.2
        _syn(            "set_domain_supply_net",
            "Sets the primary power net and primary ground net of an already existing power domain.",
            "set_domain_supply_net domain_name -primary_power_net supply_net_name -primary_ground_net supply_net_name",
        ),
        # cat2/set_dont_retime.2
        _syn(            "set_dont_retime",
            "Sets the dont_retime attribute on cells and designs in the current design to prevent sequential cells from being moved by retiming optimizations.",
            "set_dont_retime object_list ?true | false?",
        ),
        # cat2/set_dont_touch_network.2
        _syn(            "set_dont_touch_network",
            "Sets the dont_touch_network attribute on clocks, pins, or ports in the current design to prevent cells and nets in the transitive fanout of the set_dont_touch_network objects from being modified or replaced during optimization.",
            "set_dont_touch_network objects ?-no_propagate?",
        ),
        # cat2/set_dp_int_round.2
        _syn(            "set_dp_int_round",
            "Sets the rounding positions on the inferred multiplier and the multiplier-based instantiated DesignWare cells.",
            "set_dp_int_round cell_list external_rounding_position ?internal_rounding_position?",
        ),
        # cat2/set_dp_smartgen_options.2
        _syn(            "set_dp_smartgen_options",
            "Controls the strategies used when generating the datapath cell for arithmetic and shift operators.",
            "set_dp_smartgen_options ?-all_options auto | true | false | default? ?-booth_encoding auto | true | false? ?-booth_radix8 auto | true | false? ?-booth_mux_based auto | true | false? ?-booth_cell auto | true | false? ?-mult_radix4 auto | true | false? ?-mult_nand_based auto | true | false? ?-inv_out_adder_cell auto | true | false? ?-inv_sum_adder_cell auto | true | false? ?-4to2_compressor_cell auto | true | false? ?-ling_adder auto | true | false? ?-hybrid_adder auto | true | false? ?-carry_select_adder_cell auto | true | false? ?-cond_sum_adder auto | true | false? ?-sklansky_adder auto | true | false? ?-brent_kung_adder auto | true | false? ?-bounded_fanout_adder auto | true | false? ?-mux_based auto | true | false? ?-inv_adder_cell auto | true | false? ?-sop2pos_transformation auto | true | false? ?-tp_opt_tree auto | true | false? ?-tp_oper_sel auto | true | false? ?-smart_compare auto | true | false? ?-optimize_for default | area | speed | area,speed? ?-power_effort off | auto | medium | high? ?-mult_arch auto | and | nand | and_radix4 | nand_radix4 | benc_radix4 | benc_radix8 | benc_radix4_mux | benc_radix8_mux? ?-hierarchy? ?design or cell list?",
        ),
        # cat2/set_drive.2
        _syn(            "set_drive",
            "Sets the rise_drive or fall_drive attributes to the specified resistance values on the specified input and inout ports.",
            "set_drive resistance ?-rise? ?-fall? ?-min? ?-max? port_list",
        ),
        # cat2/set_dynamic_optimization.2
        _syn(            "set_dynamic_optimization",
            "Enables or disables dynamic-power optimization on the current design.",
            "set_dynamic_optimization true | false",
        ),
        # cat2/set_early_data_check_policy.2
        _syn(            "set_early_data_check_policy",
            "Sets the policy for all the checks, or modifies the policy settings for the list of checks.",
            "set_early_data_check_policy ?-checks checks? ?-policy policy?",
        ),
        # cat2/set_equal.2
        _syn(            "set_equal",
            "Defines two input ports as logically equivalent.",
            "set_equal port1 port2",
        ),
        # cat2/set_equivalent.2
        _syn(            "set_equivalent",
            "Declares that supply nets or supply sets are electrically or functionally equivalent.",
            "set_equivalent ?-nets supply_net_name_list? ?-sets supply_set_name_list? ?-function_only?",
        ),
        # cat2/set_etm_link_mode.2
        _syn(            "set_etm_link_mode",
            "Enables or Disables ETM linking mode",
            "set_etm_link_mode ?-start? ?-modules module_names? ?-end?",
        ),
        # cat2/set_extraction_options.2
        _syn(            "set_extraction_options",
            "Sets the parameters that influence parasitic data extraction.",
            "set_extraction_options ?-max_process_scale max_process_scaling? ?-min_process_scale min_process_scaling? ?-reference_direction vertical | horizontal | use_from_tluplus? ?-default?",
        ),
        # cat2/set_failsafe_fsm_rule.2
        _syn(            "set_failsafe_fsm_rule",
            "Associates the registers with the rule.",
            "set_failsafe_fsm_rule -rule failsafe_fsm_rule_name -registers registers -error_signal error_signal_pin ?-correction_signal pin_or_port?",
        ),
        # cat2/set_fanout_load.2
        _syn(            "set_fanout_load",
            "Sets the fanout_load attribute on the specified output ports of the current design.",
            "set_fanout_load value ports",
        ),
        # cat2/set_fix_hold.2
        _syn(            "set_fix_hold",
            "Sets the fix_hold attribute on clocks in the current design.",
            "set_fix_hold clocks",
        ),
        # cat2/set_fix_multiple_port_nets.2
        _syn(            "set_fix_multiple_port_nets",
            "Sets the fix_multiple_port_nets attribute to a specified value on the current design or a list of designs.",
            "set_fix_multiple_port_nets -default | -all ?-feedthroughs? ?-outputs? ?-constants? ?-buffer_constants? ?-no_rewire? ?-ignore_dont_touch? ?-exclude_clock_network? ?design_list?",
        ),
        # cat2/set_flatten.2
        _syn(            "set_flatten",
            "Sets or removes the flatten attribute on specified designs or on the current design, to enable or disable the flattening optimization step during compile.",
            "set_flatten ?true | false? ?-effort low | medium | high? ?-minimize single_output | multiple_output | none? ?-phase true | false? ?-design design_list? ?-quiet?",
        ),
        # cat2/set_floorplan_width_rules.2
        _syn(            "set_floorplan_width_rules",
            "Defines a width floorplan rule.",
            "set_floorplan_width_rules -name rule_name -direction vertical | horizontal | any -object_types block_boundary | core_area | hard_macro | soft_macro | unplaceable_area | boundary_cell_region | std_cell_area -type concave | continuous | incorner | jog | simple ?-step distance? ?-offset distance?",
        ),
        # cat2/set_fm_eco_mode.2
        _syn(            "set_fm_eco_mode",
            "Enables Formality Auto ECO Mode in Design Compiler.",
            "set_fm_eco_mode -region frd_file_name ?-netlist onet_file_name? ?-compile_options compile_options? ?-output enet_name? ?-pre_compile_script file_name? ?-post_compile_script file_name?",
        ),
        # cat2/set_fp_base_gate.2
        _syn(            "set_fp_base_gate",
            "Sets either a library leaf cell area or a user-specified cell area as the base unit area to use for gate equivalence calculations related to estimating the size of black boxes.",
            "set_fp_base_gate {-cell master_name | -area cell_area}",
        ),
        # cat2/set_fsm_encoding.2
        _syn(            "set_fsm_encoding",
            "Specifies the bit encodings for states in the current design.",
            "set_fsm_encoding encoding_list",
        ),
        # cat2/set_fsm_encoding_style.2
        _syn(            "set_fsm_encoding_style",
            "Defines the encoding style for assigning unencoded states.",
            "set_fsm_encoding_style {one_hot | zero_one_hot | binary | gray | auto | neutral}",
        ),
        # cat2/set_fsm_minimize.2
        _syn(            "set_fsm_minimize",
            "Determines whether or not state minimization is to be performed on the state machine design during compile.",
            "set_fsm_minimize true | false",
        ),
        # cat2/set_fsm_order.2
        _syn(            "set_fsm_order",
            "Sets the ordering of states in a state machine design.",
            "set_fsm_order state_list",
        ),
        # cat2/set_fsm_preserve_state.2
        _syn(            "set_fsm_preserve_state",
            "Specifies states to be preserved during state minimization.",
            "set_fsm_preserve_state state_list",
        ),
        # cat2/set_fsm_state_vector.2
        _syn(            "set_fsm_state_vector",
            "Specifies the instance names for flip-flops used to implement the state vector.",
            "set_fsm_state_vector vector_list",
        ),
        # cat2/set_gui_stroke_binding.2
        _syn(            "set_gui_stroke_binding",
            "Set the command binding for a stroke.",
            "set_gui_stroke_binding dictionary_name stroke_sequence ?-builtin builtin_cmd_name? ?-clear? ?-tcl_cmd tcl_command? ?-label tcl_command_label?",
        ),
        # cat2/set_gui_stroke_preferences.2
        _syn(            "set_gui_stroke_preferences",
            "Set preferences controlling stroke command entry.",
            "set_gui_stroke_preferences ?-type stroke_entry_type? ?-shift? ?-ctrl? ?-alt? ?-extended_help_delay ms_delay?",
        ),
        # cat2/set_host_options.2
        _syn(            "set_host_options",
            "Controls the maximum number of CPU cores that can be used for parallel execution.",
            "set_host_options -max_cores number_of_cores",
        ),
        # cat2/set_hpc_options.2
        _syn(            "set_hpc_options",
            "Applies high performance core settings to the current design",
            "set_hpc_options ?-list? ?-core core_name? ?-stage stage_name? ?-report_only?",
        ),
        # cat2/set_icc2_options.2
        _syn(            "set_icc2_options",
            "Specifies the options used to launch the IC Compiler II tool from within Design Compiler Graphical or DC Explorer physical mode.",
            "set_icc2_options -icc2_executable executable -ref_libs library ?-check? ?-work_dir directory? ?-golden_upf upf_file? ?-technology technology_file | -use_technology_lib tech_lib_name? ?-keep_files? ?-reset? ?-convert_sites convert_sites? ?-scale_factor scale_factor? ?-congestion_use_global_route {true | false}? ?-silent?",
        ),
        # cat2/set_icc_dp_options.2
        _syn(            "set_icc_dp_options",
            "Specifies the options used to invoke floorplan exploration from Design Compiler Graphical.",
            "set_icc_dp_options -work_dir directory -icc_executable executable -check flag -file_name_prefix prefix -keep_files flag",
        ),
        # cat2/set_ideal_net.2
        _syn(            "set_ideal_net",
            "Sets the specified nets as ideal. Note that this command has been deprecated; you should use the set_ideal_network -no_propagate command instead.",
            "set_ideal_net nets",
        ),
        # cat2/set_ideal_transition.2
        _syn(            "set_ideal_transition",
            "Specifies ideal transition for the ideal network and ideal nets.",
            "set_ideal_transition ?-rise | -fall? ?-min | -max? transition_time object_list",
        ),
        # cat2/set_ieee_1500_configuration.2
        _syn(            "set_ieee_1500_configuration",
            "Sets the IEEE 1500 insertion configuration for the current design.",
            "set_ieee_1500_configuration ?-wir_width integer?",
        ),
        # cat2/set_ignored_layers.2
        _syn(            "set_ignored_layers",
            "Specifies the routing layers that are ignored for RC estimation and congestion analysis. This command is supported only in topographical mode.",
            "set_ignored_layers ?-rc_congestion_ignored_layers layer_names? ?-min_routing_layer min_name? ?-max_routing_layer max_name?",
        ),
        # cat2/set_impl_priority.2
        _syn(            "set_impl_priority",
            "Sets the formula attribute of the priority parameter and/or the set_id attribute for implementations in synthetic libraries.",
            "set_impl_priority ?-priority formula? ?-set_id id? implementation_list",
        ),
        # cat2/set_implementation.2
        _syn(            "set_implementation",
            "Specifies the implementation to use for synthetic library cell instances in a design.",
            "set_implementation implementation_name cell_list ?-check_impl?",
        ),
        # cat2/set_input_parasitics.2
        #   WARNING: unclosed bracket '(' at position 74
        _syn(            "set_input_parasitics",
            "Sets additional parasitic information on nets connected to ports.",
            "set_input_parasitics -resistance rvalue ?-min? ?-max? input_ports ?value?_(resistance_value",
        ),
        # cat2/set_isolate_ports.2
        _syn(            "set_isolate_ports",
            "Specifies the ports to be isolated from the internal fanouts of the driver nets.",
            "set_isolate_ports ?-type inverter | buffer? ?-driver cell_name? ?-force? port_list",
        ),
        # cat2/set_isolation.2
        _syn(            "set_isolation",
            "Sets the UPF strategy for inserting isolation cells between a specified power domain and other power domains.",
            "set_isolation isolation_strategy_name -domain power_domain ?-isolation_power_net isolation_power_net? ?-isolation_ground_net isolation_ground_net? ?-isolation_supply isolation_supply_set? ?-clamp_value 0 | 1 | latch? ?-applies_to inputs | outputs | both? ?-applies_to_boundary upper | lower | both? ?-source source_supply_set_name? ?-sink sink_supply_set_name? ?-diff_supply_only true | false? ?-elements objects? ?-exclude_elements objects? ?-no_isolation? ?-force_isolation? ?-name_prefix prefix_string? ?-name_suffix suffix_string? ?-isolation_signal isolation_signal? ?-isolation_sense low | high? ?-location self | parent | fanout? ?-async_set_reset async_set_reset_signal high | low? ?-update? ?-async_clamp_value boolean?",
        ),
        # cat2/set_isolation_cell.2
        _syn(            "set_isolation_cell",
            "Sets the specified library cells as isolation cells.",
            "set_isolation_cell cell_name ?-data_pin data_pin_name? ?-enable_pin enable_pin_name?",
        ),
        # cat2/set_isolation_control.2
        _syn(            "set_isolation_control",
            "Specifies the isolation control signal and the side of the domain boundary on which to insert isolation cells.",
            "set_isolation_control isolation_strategy -domain power_domain -isolation_signal isolation_signal ?-isolation_sense low | high? ?-location self | parent | fanout?",
        ),
        # cat2/set_keepout_margin.2
        _syn(            "set_keepout_margin",
            "Creates a keepout margin of the specified type for the specified cell or library cell.",
            "set_keepout_margin ?-type hard | soft? ?-outer {lx by rx ty}? ?-tracks_per_macro_pin value? ?-min_padding_per_macro value? ?-max_padding_per_macro value? ?-all_macros? ?-macro_masters? ?-macro_instances? ?-north? ?object_list?",
        ),
        # cat2/set_latch_loop_breakers.2
        _syn(            "set_latch_loop_breakers",
            "Specifies transparent latch data pins to be used as loop-breaker latch data pins when the variable timing_enable_through_paths is set to true.",
            "set_latch_loop_breakers -pin pin_list ?-remove? ?-avoid?",
        ),
        # cat2/set_leakage_optimization.2
        _syn(            "set_leakage_optimization",
            "Enables or disables leakage-power optimization on the current design. Note: This command is no longer needed for the compile_ultra command because leakage-power optimization is enabled by default and cannot be disabled within the compile_ultra command. This man page describes the previous usage for this command.",
            "set_leakage_optimization true | false",
        ),
        # cat2/set_leakage_power_model.2
        _syn(            "set_leakage_power_model",
            "Specifies the model that will be optimized by leakage optimizations.",
            "set_leakage_power_model ?-type model_name? ?-mvth_weights weights? ?-reset?",
        ),
        # cat2/set_level_shifter.2
        _syn(            "set_level_shifter",
            "Sets a strategy for level shifting during implementation.",
            "set_level_shifter level_shifter_name -domain domain_name ?-elements list? ?-exclude_elements list? ?-applies_to inputs | outputs | both? ?-applies_to_boundary upper | lower | both? ?-threshold value? ?-rule low_to_high | high_to_low | both? ?-location self | parent | other | automatic? ?-no_shift? ?-force_shift? ?-source source_supply_set_name? ?-sink sink_supply_set_name? ?-input_supply input_supply_set_name? ?-output_supply output_supply_set_name? ?-name_prefix prefix? ?-name_suffix suffix? ?-update?",
        ),
        # cat2/set_level_shifter_cell.2
        _syn(            "set_level_shifter_cell",
            "Sets on-the-fly specification of a library level-shifter cell.",
            "set_level_shifter_cell cell_name ?-cell_type cell_type? ?-cell_input_voltage_range {lower_range upper_range}? ?-cell_output_voltage_range {lower_range upper_range}? ?-std_cell_main_rail_pg_pin pg_pin_name? ?-data_pin data_pin_name? ?-input_voltage_range {lower_range upper_range}? ?-output_voltage_range {lower_range upper_range}? ?-input_signal_level signal_level? ?-enable_pin enable_pin_name? ?-enable_signal_level signal_level? ?-output_signal_level signal_level?",
        ),
        # cat2/set_lib_attribute.2
        _syn(            "set_lib_attribute",
            "Sets the value of an attribute on a library object.",
            "set_lib_attribute object_list attribute_name attribute_value",
        ),
        # cat2/set_libcell_dimensions.2
        _syn(            "set_libcell_dimensions",
            "Sets the width and height of a library cell.",
            "set_libcell_dimensions -cell cell_name -width width -height height",
        ),
        # cat2/set_libcell_subset.2
        _syn(            "set_libcell_subset",
            "Restricts the optimization of sequential cells and instantiated combinational cells to a family of target libraries.",
            "set_libcell_subset -object_list cells -family_name name",
        ),
        # cat2/set_libpin_location.2
        _syn(            "set_libpin_location",
            "Sets the location of a pin of a library cell relative to the origin of the library cell.",
            "set_libpin_location -cell library_cell_name -pin pin_name_of_the_library_cell -coordinate {x_coordinate y_coordinate}",
        ),
        # cat2/set_link_library_subset.2
        _syn(            "set_link_library_subset",
            "Restricts the selection of library cells so they are chosen from a subset of the libraries specified by the link_library variable. This command can resolve ambiguity among libraries with the same voltage, temperature, and process.",
            "set_link_library_subset ?-object_list cells? ?-top? ?library_list?",
        ),
        # cat2/set_local_link_library.2
        _syn(            "set_local_link_library",
            "Sets the local_link_library attribute to specified files and libraries on the current design.",
            "set_local_link_library local_link_library",
        ),
        # cat2/set_logic_dc.2
        _syn(            "set_logic_dc",
            "Specifies one or more input ports in the current design that are to be driven by don't care. The set_logic_one and set_logic_zero commands are used the same way as this command.",
            "set_logic_dc port_list",
        ),
        # cat2/set_logic_lock_configuration.2
        _syn(            "set_logic_lock_configuration",
            "Sets the default logic lock configuration for the current design.",
            "set_logic_lock_configuration ?-parameters parameter_list? ?-exec_name executable_name? ?-map_parameters list_of_reserved_parameter_name:tool_parameter_name?",
        ),
        # cat2/set_logic_one.2
        _syn(            "set_logic_one",
            "Specifies one or more input ports in the current design that are to be driven by logic one. The set_logic_zero and set_logic_dc commands are used the same way as this command.",
            "set_logic_one port_list",
        ),
        # cat2/set_logic_zero.2
        _syn(            "set_logic_zero",
            "Specifies one or more input ports in the current design that are to be driven by logic zero. The set_logic_one and set_logic_dc commands are used the same way as this command.",
            "set_logic_zero port_list",
        ),
        # cat2/set_logicbist_configuration.2
        _syn(            "set_logicbist_configuration",
            "Specifies the LogicBIST compression configuration for the design.",
            "set_logicbist_configuration ?-chain_count chain_count | -max_length max_chain_length? ?-clock clock_name? ?-pattern_counter_width register_width? ?-shift_counter_width register_width? ?-prpg_width register_width? ?-misr_width register_width? ?-burn_in disable | enable? ?-occ_clock_weights weight_list? ?-reset_weights weight_list? ?-power_ramp_up disable | enable? ?-power_ramp_down disable | enable? ?-base_mode base_mode_name? ?-test_mode logicbist_mode_name? ?-self_test_mode autonomous_mode_name?",
        ),
        # cat2/set_map_only.2
        _syn(            "set_map_only",
            "Sets the map_only attribute on specified objects so that they can be excluded from logic-level optimization during compile.",
            "set_map_only object_list ?flag?",
        ),
        # cat2/set_max_net_length.2
        _syn(            "set_max_net_length",
            "Sets the max_net_length attribute to a specified value on specified input ports and designs.",
            "set_max_net_length net_length_value object_list",
        ),
        # cat2/set_max_time_borrow.2
        _syn(            "set_max_time_borrow",
            "Sets the max_time_borrow attribute to a specified value on clocks, latch cells, data pins, or clock (enable) pins, to constrain the amount of time borrowing possible for level-sensitive latches.",
            "set_max_time_borrow delay_value object_list",
        ),
        # cat2/set_message_info.2
        #   WARNING: unclosed bracket '[' at position 32
        _syn(            "set_message_info",
            "Set some information about diagnostic messages.",
            "set_message_info -id message_id ?-limit max_limit | -stop_on ?-stop_off?",
        ),
        # cat2/set_message_severity.2
        _syn(            "set_message_severity",
            "Sets the severity level of violation messages for boundary-scan compliance checking.",
            "set_message_severity -names message_tags severity",
        ),
        # cat2/set_min_capacitance.2
        _syn(            "set_min_capacitance",
            "Sets the min_capacitance attribute to a specified value on specified input ports in the current design.",
            "set_min_capacitance capacitance_value object_list",
        ),
        # cat2/set_min_library.2
        _syn(            "set_min_library",
            "Sets an alternate library to use for minimum delay analysis.",
            "set_min_library max_library -min_version min_library | -none",
        ),
        # cat2/set_min_pulse_width.2
        _syn(            "set_min_pulse_width",
            "Sets a minimum pulse width constraint for clocks or clock pins.",
            "set_min_pulse_width ?-low? ?-high? value object_list",
        ),
        # cat2/set_minimize_tree_delay.2
        _syn(            "set_minimize_tree_delay",
            "Sets the minimize_tree_delay attribute on a design or designs.",
            "set_minimize_tree_delay ?true | false? ?-design design_list? ?design_list?",
        ),
        # cat2/set_mode.2
        _syn(            "set_mode",
            "Selects the mode of a component.",
            "set_mode ?mode_list? ?instance_list?",
        ),
        # cat2/set_model_drive.2
        _syn(            "set_model_drive",
            "Sets the model_drive attribute to a specified value on specified input or inout ports to set their drive values during synthetic library modeling.",
            "set_model_drive drive_value port_list",
        ),
        # cat2/set_model_load.2
        _syn(            "set_model_load",
            "Sets the model_load attribute to a specified value on specified ports to set their load values during synthetic library modeling.",
            "set_model_load load_value port_list",
        ),
        # cat2/set_model_map_effort.2
        _syn(            "set_model_map_effort",
            "Sets the model_map_effort attribute to a specified value on the current design, to specify the relative amount of CPU time to use during synthetic library modeling.",
            "set_model_map_effort low | medium | high",
        ),
        # cat2/set_multi_vth_constraint.2
        _syn(            "set_multi_vth_constraint",
            "Limits the usage of low-threshold-voltage cells to a specified percentage of all cells.",
            "set_multi_vth_constraint ?-lvth_groups groups? ?-lvth_percentage percent_value? ?-cost cell_count | area? ?-type hard | soft? ?-include_blackboxes? ?-reset?",
        ),
        # cat2/set_multibit_options.2
        #   WARNING: unclosed bracket '[' at position 161
        _syn(            "set_multibit_options",
            "Allows the user to customize and setup the multi-bit optimization flow.",
            "set_multibit_options ?-default? ?-stage stage_name? ?-mode multibit_mode? ?-critical_range range? ?-slack_threshold percentage? ?-path_groups list_of_pathgoups? ?-exclude_registers_with_timing_exceptions true | ?-exclude cells_to_exclude? ?-name_prefix prefix_for_created_mb_cells? ?-multibit_components_only? ?-ignore_timing_exception list_of_timing_exceptions_to_not_exclude?",
        ),
        # cat2/set_mw_lib_reference.2
        _syn(            "set_mw_lib_reference",
            "Sets the reference library for the Milkyway library.",
            "set_mw_lib_reference ?-mw_reference_library lib_list? ?-reference_control_file file_name? libName",
        ),
        # cat2/set_mw_technology_file.2
        _syn(            "set_mw_technology_file",
            "Sets the technology file of the Milkyway library.",
            "set_mw_technology_file ?-technology tech_file? ?-alf alf_file? libName",
        ),
        # cat2/set_net_routing_layer_constraints.2
        _syn(            "set_net_routing_layer_constraints",
            "Assigns routing layer constraints to the specified nets.",
            "set_net_routing_layer_constraints list_of_nets -min_layer_name minimum_routing_layer_name -max_layer_name maximum_routing_layer_name",
        ),
        # cat2/set_net_routing_rule.2
        _syn(            "set_net_routing_rule",
            "Assigns a nondefault or default routing rule to specific nets.",
            "set_net_routing_rule -rule rule_name list_of_nets ?-reroute normal | minorchange | freeze? ?-timing_driven_spacing? ?-top_layer_probe AnyPort | OutPort | AllPort? ?-rule_is_user one-of-string?",
        ),
        # cat2/set_net_search_pattern_delay_estimation_options.2
        _syn(            "set_net_search_pattern_delay_estimation_options",
            "Sets delay estimation options for a pattern.",
            "set_net_search_pattern_delay_estimation_options -pattern id ?-default? ?-rule rule_name? ?-min_layer_name layer_name? ?-max_layer_name layer_name?",
        ),
        # cat2/set_net_search_pattern_priority.2
        _syn(            "set_net_search_pattern_priority",
            "Sets the net search pattern matching priority.",
            "set_net_search_pattern_priority string | -default",
        ),
        # cat2/set_non_bias_approved_list.2
        _syn(            "set_non_bias_approved_list",
            "Specifies cells/lib-cells that have to be waived from the nonbias cell in bias domain check in check_mv_design.",
            "set_non_bias_approved_list ?-lib_cells lib_cells_list? ?-cells cells_list?",
        ),
        # cat2/set_obfuscation_configuration.2
        _syn(            "set_obfuscation_configuration",
            "Sets the default obfuscation configuration for the current design.",
            "set_obfuscation_configuration ?-parameters parameter_list? ?-exec_name executable_name? ?-location instance_path_name? ?-exclude_cells cell_list? ?-map_parameters list_of_reserved_parameter_name:tool_parameter_name? ?-exclude list_of_cells?",
        ),
        # cat2/set_opcond_inference.2
        _syn(            "set_opcond_inference",
            "Specifies the strategy for operating condition inference.",
            "set_opcond_inference ?-level level_value? ?-match_process_temperature true | false? ?-object_list cells? ?-applies_to macro_cells pad_cells switch_cells?",
        ),
        # cat2/set_operating_conditions.2
        _syn(            "set_operating_conditions",
            "Defines the operating conditions for the current design.",
            "set_operating_conditions ?-analysis_type bc_wc | on_chip_variation? ?-min min_condition? ?-max max_condition? ?-min_library min_lib? ?-max_library max_lib? ?-min_phys min_proc? ?-max_phys max_proc? ?-library lib? ?-object_list objects? ?condition?",
        ),
        # cat2/set_opposite.2
        _syn(            "set_opposite",
            "Defines two input ports as logically opposite.",
            "set_opposite port1 port2",
        ),
        # cat2/set_optimize_dft_options.2
        _syn(            "set_optimize_dft_options",
            "Defines options for physical design-for-test (DFT) optimization.",
            "set_optimize_dft_options ?-repartitioning_method none | single_directional | multi_directional | adaptive? ?-single_dir_option horizontal | vertical?",
        ),
        # cat2/set_optimize_registers.2
        _syn(            "set_optimize_registers",
            "Sets the optimize_registers attribute on the specified designs or on the current design, so that compile automatically invokes the DC Ultra optimize_registers command to retime the design during optimization.",
            "set_optimize_registers ?true | false? ?-designs design_list? ?-minimum_period_only? ?-sync_transform multiclass | decompose | dont_retime? ?-async_transform multiclass | decompose | dont_retime? ?-check_design ?-verbose?? ?-print_critical_loop? ?-clock clock_name ?-edge rise | fall?? ?-latch? ?-justification_effort low | medium | high? ?-delay_threshold target_clock_period?",
        ),
        # cat2/set_output_clock_port_type.2
        _syn(            "set_output_clock_port_type",
            "Specifies the output clock port as a data port or a clock port.",
            "set_output_clock_port_type -data | -clock port_list",
        ),
        # cat2/set_partial_on_translation.2
        _syn(            "set_partial_on_translation",
            "Defines the translation of PARTIAL_ON to FULL_ON or OFF for purposes of evaluating the power state of supply sets and power domains.",
            "set_partial_on_translation ?default_translation? ?-full_on_tools {tools}? ?-off_tools {tools}?",
        ),
        # cat2/set_path_margin.2
        _syn(            "set_path_margin",
            "Specifies a margin to adjust required times for specified paths in the current design.",
            "set_path_margin margin_value ?-rise | -fall? ?-setup | -hold? ?-from from_list | -rise_from rise_from_list | -fall_from fall_from_list? ?-through through_list? ?-rise_through rise_through_list? ?-fall_through fall_through_list? ?-to to_list | -rise_to rise_to_list | -fall_to fall_to_list? ?-reset_path?",
        ),
        # cat2/set_pg_pin_model.2
        _syn(            "set_pg_pin_model",
            "Defines the power and ground pins for a library cell.",
            "set_pg_pin_model cell_name ?-pg_pin_name pin_names? ?-pg_voltage_name voltage_names? ?-pg_pin_type pin_types? ?-pg_pin_direction pin_directions? ?-pg_physical_connection physical_connections? ?-pg_related_bias_pin related_bias_pins?",
        ),
        # cat2/set_physical_hierarchy.2
        _syn(            "set_physical_hierarchy",
            "Sets a list of cells to be physical hierarchies. This command is supported only in Design Compiler topographical mode.",
            "set_physical_hierarchy object_list",
        ),
        # cat2/set_pin_access_optimization_options.2
        _syn(            "set_pin_access_optimization_options",
            "Sets the library cells with easy pin access and difficult pin access for pin access optimization. This command is supported only in topographical mode.",
            "set_pin_access_optimization_options ?-easy_pin_access_libcells library_cells? ?-hard_pin_access_libcells library_cells? ?-default?",
        ),
        # cat2/set_pin_model.2
        _syn(            "set_pin_model",
            "Specifies the related power and ground pins for a library cell.",
            "set_pin_model cell_name ?-pins pin_names? ?-related_power_pin pin_names? ?-related_ground_pin pin_names? ?-related_bias_pin pin_names? ?-power_down_function functions?",
        ),
        # cat2/set_pin_name_synonym.2
        _syn(            "set_pin_name_synonym",
            "Defines synonyms for pin names.",
            "set_pin_name_synonym ?-full_name? ?-force? pin_name_synonym pin_name",
        ),
        # cat2/set_pin_physical_constraints.2
        _syn(            "set_pin_physical_constraints",
            "Sets physical constraints for pin instances.",
            "set_pin_physical_constraints objects | -pin_name pin_name ?-cell cell_name? | -nets nets ?-cell cell_name? ?-layers layers? ?-width pin_width? ?-depth pin_depth? ?-side side_number? ?-offset offset_distance? ?-order order_number? ?-pin_spacing spacing? ?-exclude_sides exclude_side_numbers? ?-off_edge center | location | auto? ?-location point?",
        ),
        # cat2/set_pipeline_scan_data_configuration.2
        _syn(            "set_pipeline_scan_data_configuration",
            "Specifies the pipelined scan data configuration for the design.",
            "set_pipeline_scan_data_configuration ?-head_pipeline_clock clock_name? ?-tail_pipeline_clock clock_name? ?-head_pipeline_stages total_depth? ?-tail_pipeline_stages total_depth? ?-head_shared_pipeline_stages shared_top_level_depth? ?-tail_shared_pipeline_stages shared_top_level_depth? ?-head_scan_flop true | false?",
        ),
        # cat2/set_pipeline_scan_enable_configuration.2
        _syn(            "set_pipeline_scan_enable_configuration",
            "Specifies the configuration used for inserting DFT pipeline scan enable logic in the design.",
            "set_pipeline_scan_enable_configuration ?-exclude_elements object_list? ?-pipeline_fanout_limit integer?",
        ),
        # cat2/set_placement_area.2
        _syn(            "set_placement_area",
            "Creates the core placement area. This command is supported only in topographical mode.",
            "set_placement_area -coordinate {X1 Y1 X2 Y2} ?-fixed | -unfixed?",
        ),
        # cat2/set_placement_spacing_rule.2
        _syn(            "set_placement_spacing_rule",
            "Specifies the placement spacing rule between library cells that have been assigned labels with set_placement_spacing_label command.",
            "set_placement_spacing_rule -labels {label_names} ?-unit unit? ?-adjacent_rows? ?-halo? {min max}",
        ),
        # cat2/set_port_attributes.2
        _syn(            "set_port_attributes",
            "Sets the specified attributes and their value on the ports.",
            "set_port_attributes ?-ports port_list? ?-elements element_list? ?-exclude_ports port_list? ?-exclude_elements element_list? ?-applies_to inputs | outputs | both? ?-attribute at_name at_value? ?-receiver_supply supply_set_ref? ?-driver_supply supply_set_ref? ?-repeater_supply supply_set_ref? ?-model model_name? ?-feedthrough? ?-unconnected? ?-is_analog? ?-clamp_value clamp_value?",
        ),
        # cat2/set_port_fanout_number.2
        _syn(            "set_port_fanout_number",
            "Sets the number of external fanout points driven by specified ports in the current design.",
            "set_port_fanout_number fanout_number port_list",
        ),
        # cat2/set_port_location.2
        _syn(            "set_port_location",
            "Annotates the specified top-level port with x- and y-coordinates and layer geometry, which the tool uses when running the reoptimize_design command.",
            "set_port_location ?-coordinate {x y}? ?-layer_name layer_name? ?-layer_area {lx ly ux uy}? ?-append? port_name",
        ),
        # cat2/set_port_side.2
        _syn(            "set_port_side",
            "Specifies the port side constraints for core generation. This command is supported only in topographical mode.",
            "set_port_side port_list -side {l | r | b | t | number}",
        ),
        # cat2/set_power_clock_scaling.2
        _syn(            "set_power_clock_scaling",
            "Specify clock scaling for power analysis.",
            "set_power_clock_scaling ?-period period_value? ?-ratio ratio_value? ?clock_objects?",
        ),
        # cat2/set_power_derate.2
        _syn(            "set_power_derate",
            "Sets power derating factors on different power components for either the current design, a list of cells, library cells or all cells in a power group in the current design.",
            "set_power_derate ?-scenarios scenario_list? ?-leakage? ?-switching? ?-internal? ?-groups group_names? derate_value ?object_list?",
        ),
        # cat2/set_power_guide.2
        _syn(            "set_power_guide",
            "Sets an existing exclusive move bound as a power guide or power well. This power guide is used as an always-on power guide.",
            "set_power_guide -name exclusive_movebound_name ?-guard_band_x horizontal_guard_band_width? ?-guard_band_y vertical_guard_band_width?",
        ),
        # cat2/set_power_prediction.2
        _syn(            "set_power_prediction",
            "Sets the power prediction mode for compile_ultra or compile_ultra -incremental. This command is supported only in topographical mode.",
            "set_power_prediction ?true | false? ?-ct_references lib_cell_list?",
        ),
        # cat2/set_power_switch_cell.2
        _syn(            "set_power_switch_cell",
            "Defines the specified library cells as power-switch cells.",
            "set_power_switch_cell cell_name ?-cell_type coarse_grain | fine_grain? ?-is_macro? ?-switch_pin pin_name? ?-pg_pin {pin_name switch_function pg_function}?",
        ),
        # cat2/set_prefer.2
        _syn(            "set_prefer",
            "Sets the preferred attribute on the specified library cells.",
            "set_prefer ?-min? cell_list",
        ),
        # cat2/set_preferred_routing_direction.2
        _syn(            "set_preferred_routing_direction",
            "Sets the preferred routing direction for the specified routing layers.",
            "set_preferred_routing_direction -layers list_of_layers -direction horizontal | vertical",
        ),
        # cat2/set_preferred_scenario.2
        _syn(            "set_preferred_scenario",
            "Sets the preferred scenario.",
            "set_preferred_scenario ?scenario_name?",
        ),
        # cat2/set_preserve_clock_gate.2
        _syn(            "set_preserve_clock_gate",
            "Sets the pwr_cg_preservation_type attribute on clock-gating objects.",
            "set_preserve_clock_gate cell_collection ?-dont_modify_fanout? ?-dont_modify_enable?",
        ),
        # cat2/set_qor_data_metric_properties.2
        _syn(            "set_qor_data_metric_properties",
            "Customize metric properties in QORsum table panels",
            "set_qor_data_metric_properties -panel panel_name -metric metric_name ?-group group_name? ?-tooltip tooltip_text? ?-color color_style? ?-light_percent percent_value? ?-medium_percent percent_value? ?-dark_percent percent_value? ?-absolute_threshold abs_value? ?-improves improve_style? ?-visibility visibility? ?-output output_dir? ?-use_default_panel?",
        ),
        # cat2/set_qor_data_options.2
        _syn(            "set_qor_data_options",
            "Configures QoR data captured by the write_qor_data command.",
            "set_qor_data_options ?-output output_dir? ?-label_order list_of_labels? ?-run_name name? ?-dynamic_scenario scenario_name_or_object? ?-leakage_scenario scenario_name_or_object? ?-clock_name clock_or_skew_group_name? ?-clock_scenario scenario_name_or_object? ?-color_hierarchies hierarchy_list? ?-adjust_power power_list? ?-primetime_scenario scenario_name?",
        ),
        # cat2/set_qor_strategy.2
        _syn(            "set_qor_strategy",
            "Applies or reports optimization metrics and application settings for the current design.",
            "set_qor_strategy ?-output file_name? ?-report_only? ?-diff_only? ?-reduced_effort? -stage {synthesis} -metric {timing total_power} ?-mode mode?",
        ),
        # cat2/set_qtm_global_parameter.2
        _syn(            "set_qtm_global_parameter",
            "Sets a global parameter for quick timing models (QTMs).",
            "set_qtm_global_parameter ?-param parameter? ?-lib_cell lib_cell? ?-pin pin_name? ?-clock pin_name? ?-value parameter_value?",
        ),
        # cat2/set_qtm_port_drive.2
        _syn(            "set_qtm_port_drive",
            "Sets the drive on quick timing model (QTM) ports.",
            "set_qtm_port_drive ?-type drive_type? ?-value drive_value? ?-input_transition_rise rtrans? ?-input_transition_fall ftrans? port_list",
        ),
        # cat2/set_qtm_port_load.2
        _syn(            "set_qtm_port_load",
            "Sets the load on quick timing model (QTM) ports.",
            "set_qtm_port_load ?-type load_type? ?-factor multiplication_factor? ?-value load_value? port_list",
        ),
        # cat2/set_qtm_technology.2
        _syn(            "set_qtm_technology",
            "Sets quick timing model technology variables.",
            "set_qtm_technology ?-library name? ?-max_transition max_trans_value? ?-min_transition min_trans_value? ?-max_capacitance max_cap_value? ?-min_capacitance min_cap_value? ?-wire_load_model wlm_name? ?-operating_condition opcond_name? ?-process process_value? ?-voltage voltage_value? ?-temperature temperature_value?",
        ),
        # cat2/set_query_rules.2
        _syn(            "set_query_rules",
            "Defines rules for rule-based query.",
            "set_query_rules ?-hierarchical_separators separator_list? ?-bus_name_notations bus_name_list? ?-class class_list? ?-regsub regsub? ?-regsub_cumulative? ?-wildcard? ?-suffix suffix_list? ?-verbose? ?-nocase? ?-reset? ?-show?",
        ),
        # cat2/set_ref_libs.2
        _syn(            "set_ref_libs",
            "Sets the reference library list on a library.",
            "set_ref_libs ?-library name? ?-ref_libs {paths}? ?-use_technology_lib tech_lib_name? ?-add path? ?-before path? ?-remove path? ?-clear? ?-rebind?",
        ),
        # cat2/set_register_merging.2
        _syn(            "set_register_merging",
            "Sets the register_merging attribute on the specified cells or designs, allowing register merging optimization on the objects.",
            "set_register_merging obj_list ?true | false?",
        ),
        # cat2/set_register_replication.2
        _syn(            "set_register_replication",
            "Sets the register_replication attribute on the specified sequential cells, thus allowing register replication on the objects.",
            "set_register_replication ?-max_fanout max_fanout_value? ?-num_copies copy_value? ?-replicate replicate_switch? ?-include_fanin_logic cell? ?-include_fanout_logic cell? ?-driven_by_original_register end_points_list? object_list",
        ),
        # cat2/set_register_type.2
        _syn(            "set_register_type",
            "Sets the latch_type or flip_flop_type attributes on designs or cell instances, to specify which sequential cells from the target library are to be used by the compile command.",
            "set_register_type -latch example_latch -exact | -flip_flop example_flip_flop ?-exact? ?cell_or_design_list?",
        ),
        # cat2/set_related_supply_net.2
        _syn(            "set_related_supply_net",
            "Associates a supply net to the port of the design or the pin of a cell.",
            "set_related_supply_net ?supply_net_name? ?-object_list objects? ?-reset? ?-ground ground_net_name? ?-power power_net_name?",
        ),
        # cat2/set_repeater.2
        _syn(            "set_repeater",
            "Defines the UPF repeater strategy for the power domains in the design.",
            "set_repeater repeater_strategy_name -domain power_domain ?-repeater_supply repeater_supply_set? ?-applies_to inputs | outputs | both? ?-applies_to_boundary upper | lower | both? ?-elements objects? ?-exclude_elements exclude_objects? ?-name_prefix prefix? ?-name_suffix suffix? ?-update?",
        ),
        # cat2/set_replace_clock_gates.2
        _syn(            "set_replace_clock_gates",
            "Set directives for clock gate replacement. Forces the enabling or disabling of clock gate replacement for specified combinational cells in the current design. Also sets the edge type for modules or black-box cells that otherwise could not be replaced. The cells are replaced by executing the replace_clock_gates command.",
            "set_replace_clock_gates ?-include_cells cell_list? ?-exclude_cells cell_list? ?-rising_edge_clock pin_list? ?-falling_edge_clock pin_list? ?-undo object_list?",
        ),
        # cat2/set_resistance.2
        _syn(            "set_resistance",
            "Sets the resistance value on nets.",
            "set_resistance value ?-min? ?-max? net_list",
        ),
        # cat2/set_resource_allocation.2
        _syn(            "set_resource_allocation",
            "Sets the resource_allocation attribute on the current design, specifying the type of resource allocation to be used by compile.",
            "set_resource_allocation none | area_only | area_no_tree_balancing | constraint_driven",
        ),
        # cat2/set_retention.2
        _syn(            "set_retention",
            "Defines the UPF retention strategy for the power domains in the design.",
            "set_retention retention_strategy -domain power_domain ?-retention_power_net retention_power_net? ?-retention_ground_net retention_ground_net? ?-retention_supply retention_supply_set? ?-no_retention? ?-elements objects? ?-save_condition {boolean_function}? ?-restore_condition {boolean_function}? ?-retention_condition {boolean_function}? ?-exclude_elements objects? ?-save_signal {save_signal save_sense}? ?-restore_signal {restore_signal restore_sense}? ?-update? ?-use_retention_as_primary? ?-applies_to flop | latch | any?",
        ),
        # cat2/set_retention_cell.2
        _syn(            "set_retention_cell",
            "Sets the specified library cells as retention cells.",
            "set_retention_cell cell_name ?-cell_type retention_type? ?-retention_pin {pin_name pin_type disable_value}?",
        ),
        # cat2/set_retention_control.2
        _syn(            "set_retention_control",
            "Defines the UPF retention control signals for a retention strategy.",
            "set_retention_control retention_strategy -domain power_domain -save_signal {save_signal save_sense} -restore_signal {restore_signal restore_sense} ?-assert_r_mutex {net_name sense}? ?-assert_s_mutex {net_name sense}? ?-assert_rs_mutex {net_name sense}?",
        ),
        # cat2/set_retention_control_pins.2
        _syn(            "set_retention_control_pins",
            "Converts the retention register library cell attributes in the old library format to the ones that can be used in $retain flow. The $retain flow requires retention register library cells to have new retention cell attributes, which is different from the original power gating flow.",
            "set_retention_control_pins ?-type style? ?-power_pin_index power_pin | -library_pin library_pin_name? ?-is_save_pin | -is_restore_pin | -is_save_restore_pin? lib_or_lib_cell_list",
        ),
        # cat2/set_retention_elements.2
        _syn(            "set_retention_elements",
            "Creates a named list of elements that can be used in the set_retention command.",
            "set_retention_elements retention_list_name -elements objects",
        ),
        # cat2/set_route_zrt_common_options.2
        _syn(            "set_route_zrt_common_options",
            "Sets the options common to all phases of Zroute routing. Options set are saved with the design.",
            "set_route_zrt_common_options ?-reroute_clock_shapes true | false? ?-reroute_user_shapes true | false? ?-plan_group_aware off | all_routing | top_level_routing_only? ?-reshield_modified_nets off | reshield | unshield? ?-child_process_net_threshold int? ?-verbose_level int? ?-clock_topology normal | comb? ?-comb_distance int? ?-pg_shield_distance_threshold distance? ?-connect_floating_shapes true | false? ?-allow_pg_as_shield true | false? ?-rc_driven_setup_effort_level off | low | medium | high? ?-read_user_metal_blockage_layer true | false? ?-wide_macro_pin_as_fat_wire true | false? ?-route_top_boundary_mode stay_half_min_space_inside | stay_inside | ignore? ?-standard_cell_blockage_as_thin true | false? ?-freeze_layer_by_layer_name {{layer true | false}...}? ?-freeze_via_to_frozen_layer_by_layer_name {{layer true | false}...}? ?-forbid_new_metal_by_layer_name {{layer true | false}...}? ?-global_max_layer_mode soft | allow_pin_connection | hard? ?-global_min_layer_mode soft | allow_pin_connection | hard? ?-ignore_var_spacing_to_blockage true | false? ?-ignore_var_spacing_to_pg true | false? ?-ignore_var_spacing_to_shield true | false? ?-min_edge_offset_for_macro_pin_connection_by_layer_name {{layer offset}...}? ?-net_max_layer_mode soft | allow_pin_connection | hard? ?-net_min_layer_mode soft | allow_pin_connection | hard? ?-net_max_layer_mode_soft_cost low | medium | high? ?-net_min_layer_mode_soft_cost low | medium | high? ?-extra_preferred_direction_wire_cost_multiplier_by_layer_name {{layer multiplier}...}? ?-extra_nonpreferred_direction_wire_cost_multiplier_by_layer_name {{layer multiplier}...}? ?-extra_via_cost_multiplier_by_layer_name {{layer multiplier}...}? ?-extra_via_off_grid_cost_multiplier_by_layer_name {{layer multiplier}...}? ?-number_of_vias_over_global_max_layer int? ?-number_of_vias_under_global_min_layer int? ?-number_of_vias_over_net_max_layer int? ?-number_of_vias_under_net_min_layer int? ?-via_array_mode off | swap | rotate | all? ?-post_detail_route_redundant_via_insertion off | low | medium | high? ?-post_incremental_detail_route_fix_soft_violations true | false? ?-concurrent_redundant_via_mode off | reserve_space | insert_at_high_cost ?-concurrent_redundant_via_effort_level low | medium | high?? ?-eco_route_concurrent_redundant_via_mode off | reserve_space ?-eco_route_concurrent_redundant_via_effort_level low | medium | high?? ?-rotate_default_vias true | false? ?-route_soft_rule_effort_level off | min | low | medium | high? ?-post_detail_route_fix_soft_violations true | false? ?-post_eco_route_fix_soft_violations true | false? ?-post_group_route_fix_soft_violations true | false? ?-routing_rule_effort_level {{rule {layer {effort_list}}...}...}? ?-soft_rule_weight_to_effort_level_map {{weight_level effort_level}...}? ?-enforce_voltage_areas off | strict | relaxed? ?-voltage_area_weight {{voltage_area_name weight}...}? ?-single_connection_to_pins connection_mode? ?-mark_clock_nets_minor_change true | false? ?-track_auto_fill true | false? ?-tie_off_mode all | rail_only? ?-connect_within_pins_by_layer_name {{layer mode}...}? ?-number_of_secondary_pg_pin_connections int? ?-separate_tie_off_from_secondary_pg true | false? ?-default true | false? ?-shielding_nets pg_net_names? ?-report_local_double_pattern_odd_cycles true | false? ?-wire_on_grid_by_layer_name {{layer true | false}...}? ?-via_on_grid_by_layer_name {{layer true | false}...}? ?-min_shield_length_by_layer_name {{layer length}...}?",
        ),
        # cat2/set_route_zrt_global_options.2
        _syn(            "set_route_zrt_global_options",
            "Sets the options for Zroute global routing.",
            "set_route_zrt_global_options ?-exclude_blocked_gcells_from_congestion_report true | false? ?-layer_based_congestion_map true | false? ?-timing_driven true | false? ?-timing_driven_effort_level low | medium | high? ?-crosstalk_driven true | false? ?-double_pattern_utilization_by_layer_name {{layer int}...}? ?-effort minimum | low | medium | high | ultra? ?-force_full_effort true | false? ?-extra_blocked_layer_utilization_reduction int? ?-macro_boundary_track_utilization int? ?-macro_boundary_width int? ?-macro_corner_track_utilization int? ?-voltage_area_corner_track_utilization int? ?-default true | false? ?-auto_gcell true | false?",
        ),
        # cat2/set_rp_group_options.2
        _syn(            "set_rp_group_options",
            "Sets relative placement group attributes on the specified relative placement groups.",
            "set_rp_group_options rp_groups ?-alignment bottom-left | bottom-pin | bottom-right? ?-pin_align_name pin_name? ?-utilization percentage? ?-ignore? ?-x_offset float? ?-y_offset float? ?-group_orient default | N | FN | S | FS? ?-cell_orient_opt? ?-auto_blockage? ?-disable_buffering? ?-cts_option fixed_placement | size_only? ?-route_opt_option fixed_placement | in_place_size_only? ?-psynopt_option fixed_placement | size_only | all_optimization? ?-move_effort low | medium | high? ?-allow_keepout_over_tapcell false | true? ?-allow_non_rp_cells? ?-place_around_fixed_cells standard | physical_only | all | none? ?-anchor_corner bottom-left | bottom-right | top-left | top-right | rp-location ?-anchor_row integer? ?-anchor_column integer?? ?-placement_type bit_slice | compression | vertical_compression? ?-ignore_rows ignore_row_names_list? ?-max_rp_width float? ?-max_rp_height float?",
        ),
        # cat2/set_rtl_load.2
        _syn(            "set_rtl_load",
            "Sets an RTL load value for capacitance and resistance on pins, ports, and nets.",
            "set_rtl_load ?-min? ?-max? pin_net_list ?-capacitance cvalue? ?-resistance rvalue?",
        ),
        # cat2/set_safety_core_rule.2
        _syn(            "set_safety_core_rule",
            "Associates the cores with the rule.",
            "set_safety_core_rule -rule rule_name -error_signal pin_or_port ?-split_pins pin_names? -cores core_list",
        ),
        # cat2/set_safety_error_code_rule.2
        _syn(            "set_safety_error_code_rule",
            "Associates the rule with one set of data bits.",
            "set_safety_error_code_rule -rule safety_error_code_rule -data pins_or_ports ?-error_signal pin_or_port? ?-correction_signal correction_pin? ?-clock pin_or_port? ?-requirement_id requirement_id_string? ?-checkbits cell_or_port_list? ?-enable pin_or_port?",
        ),
        # cat2/set_safety_logic_port_map.2
        _syn(            "set_safety_logic_port_map",
            "Set the port map on safety logic module.",
            "set_safety_logic_port_map -module module to set the port map on -voting voting pin -error error pin -input string_list ?-correction string? ?-checkbits string_list? -type voting | encoder | decoder",
        ),
        # cat2/set_safety_register_rule.2
        _syn(            "set_safety_register_rule",
            "Associates the registers with the rules.",
            "set_safety_register_rule -rule safety_register_rule_name -registers registers ?-error_signal error_signal_pin? ?-correction_signal correction_pin? ?-target?",
        ),
        # cat2/set_scaling_lib_group.2
        _syn(            "set_scaling_lib_group",
            "Specifies the scaling library group (previously defined by the define_scaling_lib_group command) to use for the current design or a subdesign.",
            "set_scaling_lib_group ?-min min_group? ?-max max_group? ?-object_list objects? ?group?",
        ),
        # cat2/set_scan_compression_configuration.2
        #   WARNING: unmatched closing bracket ']' at position 914
        _syn(            "set_scan_compression_configuration",
            "Specifies the scan compression configuration for the design.",
            "set_scan_compression_configuration ?-chain_count chain_count | -max_length max_chain_length | -minimum_compression compression_factor? ?-xtolerance high | default? ?-synchronize_chains none | all | tail | head? ?-compressor_pipeline false | true? ?-serialize chip_level | core_level | none? ?-integration_only true | false? ?-hybrid true | false? ?-force_diagnosis true | false? ?-static_x_chain_isolation true | false? ?-inputs number_of_inputs? ?-outputs number_of_outputs? ?-base_mode base_mode_name? ?-test_mode scan_compression_mode_name? ?-min_power false | true? ?-shared_inputs number_of_shared_inputs? ?-shared_outputs number_of_shared_outputs? ?-identical_cores core_list? ?-scramble_identical_outputs true | false? ?-shared_block_select false | true? ?-shared_codec_controls false | true? ?-shift_power_groups false | true? ?-shift_power_chain_length chain_length? | -shift_power_chain_ratio chain_ratio? ?-shift_power_clock clock_name? ?-shift_power_disable test_control_name? ?-location compressor_decompressor_location?",
        ),
        # cat2/set_scan_configuration.2
        _syn(            "set_scan_configuration",
            "Specifies the scan chain design.",
            "set_scan_configuration ?-max_length max_chain_length | -exact_length chain_length | -chain_count chain_count | -count_per_domain chain_count? ?-add_lockup true | false? ?-clock_mixing no_mix | mix_edges | mix_clocks | mix_clocks_not_edges? ?-add_test_retiming_flops begin_and_end | begin_only | end_only | none? ?-create_dedicated_scan_out_ports true | false? ?-internal_clocks none | single | multi? ?-insert_terminal_lockup true | false? ?-lockup_type latch | flip_flop? ?-mix_internal_clock_driver true | false? ?-preserve_multibit_segment false | true? ?-style multiplexed_flip_flop | clocked_scan | lssd | combinational | scan_enabled_lssd | none? ?-shared_scan_in pin_count? ?-exclude_elements exclude_list? ?-voltage_mixing true | false? ?-power_domain_mixing true | false? ?-test_mode mode_name? ?-domain_based_scan_enable true | false? ?-reuse_mv_cells true | false? ?-pipeline_scan_enable true | false? ?-pipeline_fanout_limit max_scan_cells? ?-create_test_clocks_by_system_clock_domain true | false? ?-replace true | false? ?-hierarchical_isolation true | false? ?-static_x_chain_isolation X_chains_isolation?",
        ),
        # cat2/set_scan_element.2
        _syn(            "set_scan_element",
            "Sets the scan_element attribute on specified design objects, to determine whether scan replacement replaces them with scan cells.",
            "set_scan_element true | false cell_design_ref_list",
        ),
        # cat2/set_scan_group.2
        _syn(            "set_scan_group",
            "Specifies an unordered group of cells that are not yet connected, but should be kept together within a scan chain. Also identifies existing logic in the current design that is to be designated as a scan segment.",
            "set_scan_group scan_group_name ?-access signal_type_pin_pairs? ?-include_elements object_list? ?-serial_routed false | true? ?-lockup_exists false | true? ?-segment_length length_of_virtual_segment? ?-clock top_level_clock_port? ?-edge rising | falling? ?-class occ | wrapper | input_wrapper | output_wrapper | bypass? ?-exclude_elements Valid_Scan_group_elements?",
        ),
        # cat2/set_scan_link.2
        _syn(            "set_scan_link",
            "Declares a scan link for the current design.",
            "set_scan_link scan_link_name Wire | Lockup ?-test_mode mode_name?",
        ),
        # cat2/set_scan_path.2
        _syn(            "set_scan_path",
            "Specifies a scan chain for the current design.",
            "set_scan_path scan_chain_name ?-ordered_elements ordered_list? ?-head_elements head_list? ?-tail_elements tail_list? ?-include_elements include_list? ?-infer_dft_signals? ?-dedicated_scan_out true | false? ?-complete true | false? ?-exact_length length? ?-bsd_style global | synchronous | asynchronous? ?-insert_terminal_lockup true | false? ?-scan_master_clock clock_name? ?-edge rising | falling? ?-scan_slave_clock clock_name? ?-scan_enable port_name? ?-scan_data_in port_name? ?-scan_data_out port_name? ?-test_mode mode_name? ?-view view_name? ?-class scan | wrapper | bsd | occ | spc | ieee_1500 | ieee_1500_ring | pco_wrapper? ?-opcode opcode_value? ?-init_data init_value? ?-hookup hookup_pin_list? ?-input_wrapper_cells_only enable | disable? ?-output_wrapper_cells_only enable | disable? ?-pipeline_head_registers scan_chain_element_names? ?-pipeline_tail_registers scan_chain_element_names? ?-sel_wir_position SelectWIR_position_in_ring_data_register_:_closest_to_WSI/TDI_or_WSO/TDO?",
        ),
        # cat2/set_scan_register_type.2
        _syn(            "set_scan_register_type",
            "Specifies a list of scan sequential cells from the target library that are to be used by insert_dft or compile -scan when scan replacing designs or cell instances.",
            "set_scan_register_type ?-exact? ?-type example_scan_seq_cell_list? ?cell_or_design_list?",
        ),
        # cat2/set_scan_replacement.2
        _syn(            "set_scan_replacement",
            "Specifies a table of one-to-one mappings of flip-flops to their equivalent scan flip-flops from the target library that are to be used by insert_dft when scan replacing cell instances. Note that as of 2006.06-SP1, compile -scan and compile_ultra -scan map to scan cells directly, rather than doing scan replacement. So, this command has no effect on compile -scan and compile_ultra -scan.",
            "set_scan_replacement ?-nonscan non_scan_seq_cell_list? ?-lssd lssd_rep_cell? ?-multiplexed_flip_flop muxed_scan_cell? ?-clocked_scan clocked_scan_cell? ?-combinational combinational_scan_cell? ?-scan_enabled_lssd scan_enabled_lssd_cell?",
        ),
        # cat2/set_scan_skew_group.2
        _syn(            "set_scan_skew_group",
            "Defines a scan skew group of scan cells, which might have a different clock latency characteristic than other parts of the design.",
            "set_scan_skew_group scan_skew_group_name -include_elements object_list",
        ),
        # cat2/set_scan_state.2
        _syn(            "set_scan_state",
            "Sets the scan state status for the current db design.",
            "set_scan_state unknown | test_ready | scan_existing",
        ),
        # cat2/set_scan_suppress_toggling.2
        _syn(            "set_scan_suppress_toggling",
            "Specifies how the insert_dft command should insert gating at scan flip-flop functional outputs to suppress downstream toggling activity during scan shift.",
            "set_scan_suppress_toggling ?-selection_method manual | auto | mixed? ?-include_elements cell_design_ref_list? ?-exclude_elements cell_design_ref_list? ?-min_slack minimum_timing_slack_after_gating? ?-ignore_timing_impact true | false? ?-total_percentage_gating percentage_value?",
        ),
        # cat2/set_scenario_options.2
        _syn(            "set_scenario_options",
            "Sets the scenario options for one or more scenarios.",
            "set_scenario_options ?-scenarios scenario_list? ?-setup true | false? ?-hold true | false? ?-leakage_power true | false? ?-dynamic_power true | false? ?-cts_mode true | false? ?-cts_corner min | max | min_max | none? ?-reset_all true | false?",
        ),
        # cat2/set_scope.2
        _syn(            "set_scope",
            "Specifies the current scope.",
            "set_scope ?instance?",
        ),
        # cat2/set_script_runtime_report_mode.2
        _syn(            "set_script_runtime_report_mode",
            "Sets or queries the report mode of script runtime.",
            "set_script_runtime_report_mode ?mode_name?",
        ),
        # cat2/set_security_configuration.2
        _syn(            "set_security_configuration",
            "Sets the default security configuration for the current design.",
            "set_security_configuration ?-logic_lock enable | disable? ?-obfuscation enable | disable? ?-watermark enable | disable? ?-soc_id uid_name? ?-id uid_name? ?-access_control enable | disable?",
        ),
        # cat2/set_self_gating_objects.2
        _syn(            "set_self_gating_objects",
            "Forces the enabling or disabling of self-gating for specified objects in the current design, overriding all conditions necessary for automatic self-gating, by the compile_ultra -self_gating command. Objects can be of type register, hierarchical cell, power domain or design.",
            "set_self_gating_objects ?-force_include object_list? ?-exclude object_list? ?-include object_list? ?-undo object_list? ?-type cell_type?",
        ),
        # cat2/set_self_gating_options.2
        _syn(            "set_self_gating_options",
            "Sets the self-gating options for the self-gate insertion. This command is supported only in topographical mode.",
            "set_self_gating_options ?-min_fanout min_fanout_count? ?-max_fanout max_fanout_count? ?-min_bitwidth min_bitwidth_count? ?-max_bitwidth max_bitwidth_count? ?-interaction_with_clock_gating none | insert | merge?",
        ),
        # cat2/set_sense.2
        _syn(            "set_sense",
            "Specifies unateness propagating forward for pins with respect to clock source.",
            "set_sense ?-type clock? ?-positive? ?-negative? ?-stop_propagation? ?-pulse pulse_type? ?-clocks clock_list? ?-clock_leaf? pins",
        ),
        # cat2/set_separate_process_options.2
        _syn(            "set_separate_process_options",
            "Sets options that control whether the tool uses separate UNIX processes for extraction, placement, and routing.",
            "set_separate_process_options ?-placement true | false?",
        ),
        # cat2/set_serialize_configuration.2
        _syn(            "set_serialize_configuration",
            "Specifies the serializer configuration for the design.",
            "set_serialize_configuration ?-inputs number_of_deserializer_inputs? ?-outputs number_of_serializer_outputs? ?-ip_inputs list_core_instance_and_number_of_deserializer_ip_inputs? ?-ip_outputs list_core_instance_and_number_of_serializer_ip_outputs? ?-update_stage true | false? ?-exclude_clocks list_of_clock_names_to_exclude? ?-serializer_clock clock_for_serializer_controller? ?-update_clock clock_for_update_stage_in_load_deserializer? ?-strobe user_defined_signal_for_strobe_in_unload_serializer? ?-wide_duty_cycle true | false? ?-parallel_mode parallel_scan_compression_mode_name? ?-test_mode serial_scan_compression_mode_name?",
        ),
        # cat2/set_spfm_loss.2
        _syn(            "set_spfm_loss",
            "Set the spfm loss on the design.",
            "set_spfm_loss pfm_loss -registers cell_or_pin_name_list",
        ),
        # cat2/set_spfm_target.2
        _syn(            "set_spfm_target",
            "Set the spfm target on the design.",
            "set_spfm_target pfm_target",
        ),
        # cat2/set_streaming_compression_configuration.2
        _syn(            "set_streaming_compression_configuration",
            "Specifies the streaming compression configuration for the design.",
            "set_streaming_compression_configuration ?-compressed_max_length max_chain_length | -max_length max_chain_length | -chain_count chain_count? ?-inputs number_of_inputs? ?-outputs number_of_outputs? ?-external_clock_chain true | false? ?-test_mode compression_mode_name? ?-base_mode base_mode_name? ?-clock clock_name? ?-decompressor_clock clock_name? ?-compressor_clock clock_name? ?-exclude_clocks clock_name_list? ?-min_power false | true? ?-shift_power_groups false | true? ?-shift_power_chain_length chain_length? ?-shift_power_chain_ratio chain_ratio? ?-shift_power_clock clock_name? ?-shift_power_disable test_control_name? ?-configuration_ports Specify_ports_for_multiple_configuration_IP?",
        ),
        # cat2/set_structure.2
        _syn(            "set_structure",
            "Sets structure attributes on a design or on a list of designs, to determine how the designs are structured during compile.",
            "set_structure ?true | false? ?-design design_list? ?-boolean true | false? ?-boolean_effort low | medium | high? ?-timing true | false?",
        ),
        # cat2/set_svf.2
        _syn(            "set_svf",
            "Generates a Formality setup information file for efficient compare point matching in Formality.",
            "set_svf filename ?-append? ?-off?",
        ),
        # cat2/set_switching_activity.2
        _syn(            "set_switching_activity",
            "Sets the switching activity annotation on nets, pins, ports and cells of the current design.",
            "set_switching_activity ?-static_probability static_probability? ?-toggle_rate toggle_rate? ?-state_condition state_condition? ?-path_sources path_sources? ?-rise_ratio rise_ratio? ?-period period_value | -base_clock clock? ?-type object_type_list? ?-hierarchy? ?object_list? ?-verbose? ?-scenarios {scenario_name1 scenario_name2 ... }?",
        ),
        # cat2/set_switching_activity_profile.2
        _syn(            "set_switching_activity_profile",
            "Generates switching activity profiles and sets the profiles on input-bused ports of the current design.",
            "set_switching_activity_profile ?-uniform {static_probability toggle_rate}? ?-linear {{breakpoint_0 static_probability_0 toggle_rate_0} {breakpoint_1 static_probability_1 toggle_rate_1}}? ?-normal_dist {std_dev temp_corr sample_rate is_signed}? ?-period period_value | -base_clock clock? ?object_list? ?-all_buses? ?-verbose?",
        ),
        # cat2/set_synlib_dont_get_license.2
        _syn(            "set_synlib_dont_get_license",
            "Specifies a list of synthetic library part licenses that are not automatically checked out.",
            "set_synlib_dont_get_license license_list",
        ),
        # cat2/set_tap_elements.2
        _syn(            "set_tap_elements",
            "Specifies the set of TAP state elements for the boundary-scan TAP controller.",
            "set_tap_elements -state_cells cell_names",
        ),
        # cat2/set_target_library_subset.2
        _syn(            "set_target_library_subset",
            "Restricts the optimization of a block to a subset of the target libraries.",
            "set_target_library_subset ?-top | -object_list cells? ?-dont_use lib_cells? ?-use lib_cells? ?-clock_path? ?-only_here lib_cells? ?-milkyway_reflibs milkyway_reflib_paths? ?library_file_name_list?",
        ),
        # cat2/set_technology.2
        _syn(            "set_technology",
            "Applies technology-node settings to the current design",
            "set_technology -node node_number ?-report_only?",
        ),
        # cat2/set_test_assume.2
        _syn(            "set_test_assume",
            "Sets the test_assume attribute to a logic value to be assumed on specified cell output pins throughout test design rule checking.",
            "set_test_assume zero_or_one_value pin_list",
        ),
        # cat2/set_test_point_configuration.2
        _syn(            "set_test_point_configuration",
            "Specifies the automatic test point insertion configuration options (deprecated).",
            "set_test_point_configuration -target pattern_reduction | testability ?-control_signal control_name? ?-clock_signal clock_name? ?-clock_type dominant | dedicated? ?-max_control_points n? ?-max_observe_points n? ?-test_points_per_scan_cell n? ?-power_saving enable | disable? ?-max_additional_logic_area n?",
        ),
        # cat2/set_test_point_element.2
        _syn(            "set_test_point_element",
            "Configures the insertion of force, control, and observe userdefined test points.",
            "set_test_point_element list_of_design_pin_objects ?-type control_0 | control_z0 | control_1 | control_z1 | control_01 | control_z01 | force_0 | force_z0 | force_1 | force_z1 | force_01 | force_z01 | observe? ?-control_signal control_name? ?-clock_signal clock_name? ?-test_points_per_source_or_sink n? ?-clock_local_hookup_pin hookup_pin_full_name?",
        ),
        # cat2/set_testability_configuration.2
        #   WARNING: unmatched closing bracket ')' at position 1069
        #   WARNING: unmatched closing bracket ')' at position 1185
        _syn(            "set_testability_configuration",
            "Configures automatic test-point insertion and global test-point insertion parameters.",
            "set_testability_configuration ?-target random_resistant | untestable_logic | x_blocking | multicycle_paths | shadow_wrapper | core_wrapper | atpg_conflict | user? ?-test_point_file file_name? ?-only_from_file false | true? ?-clock_signal clock_name? ?-allowed_clock_signals clock_list? ?-disallowed_clock_signals clock_list? ?-control_signal control_name? ?-test_points_per_scan_cell n? ?-include_elements object_list? ?-include_fanin_cone object_list? ?-include_fanout_cone object_list? ?-exclude_elements object_list? ?-exclude_fanin_cone object_list? ?-exclude_fanout_cone object_list? ?-effort low | medium | high? ?-isolate_elements cell_list? ?-max_test_points n? ?-max_test_point_register_percent test_point_register_percent_value? ?-random_pattern_count n? ?-target_test_coverage coverage_value? ?-reuse_threshold threshold_value? ?-depth_threshold threshold_value? ?-sg_command_file file_name? ?-test_point_without_control_signal control | observe | force? ?-dedicated_chains observe_only | control_only | observe_and_control? Values: control | force | observe) Values: random_resistant | untestable_logic | x_blocking | multicycle_paths | core_wrapper | shadow_wrapper | user)",
        ),
        # cat2/set_timing_derate.2
        _syn(            "set_timing_derate",
            "Sets a derating factor on the current design or specified objects. Derating factors adjust the worst-case calculated delays for a particular operating condition.",
            "set_timing_derate ?-rise? ?-fall? ?-min? ?-max? ?-early? ?-late? ?-clock? ?-data? ?-net_delay? ?-cell_delay? ?-cell_check? ?-pocvm_guardband? ?-pocvm_coefficient_scale_factor? ?-min_period? ?-min_pulse_width? value object_list",
        ),
        # cat2/set_timing_ranges.2
        _syn(            "set_timing_ranges",
            "Sets timing ranges for the current design.",
            "set_timing_ranges ?timing_ranges? ?-library library_name?",
        ),
        # cat2/set_tlu_plus_files.2
        _syn(            "set_tlu_plus_files",
            "Sets the files used for TLUPlus extraction. This command is supported only in topographical mode.",
            "set_tlu_plus_files ?-max_tluplus max_tluplus_file? ?-min_tluplus min_tluplus_file? ?-max_emulation_tluplus max_emul_file? ?-min_emulation_tluplus min_emul_file? ?-tech2itf_map mapping_file?",
        ),
        # cat2/set_top_implementation_options.2
        _syn(            "set_top_implementation_options",
            "Sets the top-level design options for the linking and optimization of the block's interface logic using transparent interface optimization.",
            "set_top_implementation_options -block_references reference_names ?-load_logic full_interface | compact_interface? ?-optimize_block_interface true | false? ?-optimize_shared_logic true | false? ?-size_only_mode off | auto | in_place | footprint? ?-block_update_setup_script file_name? ?-block_update_cmd_script file_name? ?-reset?",
        ),
        # cat2/set_trace_option.2
        #   WARNING: unclosed bracket '[' at position 17
        _syn(            "set_trace_option",
            "Set an option value controlling behavior of command tracing and output annotation..",
            "set_trace_option ?-command name | -profile profile_metric_types | -memory_threshold threshold | -cpu_threshold ?-annotate annnotate_type? ?-time_threshold Unsigned_threshold_in_seconds:_-1_means_unset_threshold?",
        ),
        # cat2/set_transform_for_retiming.2
        _syn(            "set_transform_for_retiming",
            "Sets the transform_for_retiming attribute on cells in the current design. This can effect both hierarchical cells and sequential leaf cells.",
            "set_transform_for_retiming cell_list multiclass | decompose | dont_retime",
        ),
        # cat2/set_unconnected.2
        _syn(            "set_unconnected",
            "Lists output ports to be unconnected.",
            "set_unconnected port_list",
        ),
        # cat2/set_ungroup.2
        _syn(            "set_ungroup",
            "Sets the ungroup attribute on specified designs, cells, or references, indicating that they are to be ungrouped during compile.",
            "set_ungroup object_list true | false",
        ),
        # cat2/set_uninitialized_register_value.2
        _syn(            "set_uninitialized_register_value",
            "Specifies the initial state to be set on uninitialized registers by constant removal engines. Uninitialized registers are registers for which the constant engines could not compute an initial state.",
            "set_uninitialized_register_value ?-value init_value? object_list",
        ),
        # cat2/set_unloaded_register_removal.2
        _syn(            "set_unloaded_register_removal",
            "Sets an attribute to unlaoded register(s) to selectively preserve or optimize it.",
            "set_unloaded_register_removal objects true | false ?flag?",
        ),
        # cat2/set_upf_cell_mismatch.2
        _syn(            "set_upf_cell_mismatch",
            "Used to specify relaxations that tool can apply to get a final mapped netlist.",
            "set_upf_cell_mismatch -allow_tls_violation -allow_pvt_mismatch -no_unmapped retention | isolation | both -reset",
        ),
        # cat2/set_upf_query_options.2
        _syn(            "set_upf_query_options",
            "Sets the options for specifying design elements in UPF commands.",
            "set_upf_query_options -bus_struct_mode true | false",
        ),
        # cat2/set_user_attribute.2
        _syn(            "set_user_attribute",
            "Sets the value of an attribute on a design or library object.",
            "set_user_attribute object_list attribute_name attribute_value ?-bus? ?-quiet?",
        ),
        # cat2/set_user_budget.2
        _syn(            "set_user_budget",
            "Sets user budgets or budget ratios.",
            "set_user_budget -from object_list -to object_list ?-percent? value",
        ),
        # cat2/set_utilization.2
        _syn(            "set_utilization",
            "Specifies placement utilization constraint for core area. This command is supported only in topographical mode.",
            "set_utilization util_float",
        ),
        # cat2/set_variation.2
        _syn(            "set_variation",
            "Used to define tolerance levels of supplies in the design that is enabled for voltage reconciliation.",
            "set_variation ?-supply supply_net? ?-tolerance {vboth | vlow vhigh}?",
        ),
        # cat2/set_verification_priority.2
        _syn(            "set_verification_priority",
            "Sets the verification_priority attribute on specified designs, cells, or references, indicating the level of optimization during compile_ultra.",
            "set_verification_priority -all ?-high? ?-low? object_list",
        ),
        # cat2/set_verification_top.2
        _syn(            "set_verification_top",
            "",
            "set_verification_top",
        ),
        # cat2/set_via_ladder_candidate.2
        _syn(            "set_via_ladder_candidate",
            "Specify via ladder candidates for optimization.",
            "set_via_ladder_candidate library_pin -ladder_name ladder_name",
        ),
        # cat2/set_via_ladder_constraints.2
        _syn(            "set_via_ladder_constraints",
            "Attaches ordered via ladder lists to specified instances of logical pins.",
            "set_via_ladder_constraints -pins pin_names via_ladder_list",
        ),
        # cat2/set_via_ladder_rules.2
        _syn(            "set_via_ladder_rules",
            "Sets via ladder rules for the design.",
            "set_via_ladder_rules -master_pin_map masterpin_ladders_list -master_pin_map_file file -default_ladders via_ladders_list -all_instances_of cell_master_pin_list -all_clock_outputs true | false -all_clock_inputs true | false -all_pins_driving port_list -remove_all_rules",
        ),
        # cat2/set_voltage.2
        _syn(            "set_voltage",
            "Applies an operating voltage to a list of supply net or internal supply port objects.",
            "set_voltage max_voltage ?-min min_voltage? -object_list supply_objects",
        ),
        # cat2/set_voltage_area.2
        _syn(            "set_voltage_area",
            "Updates a voltage_area in the current design.",
            "set_voltage_area ?-add_power_domains domain_list? voltage_area_object ?-name new_name?",
        ),
        # cat2/set_voltage_model.2
        _syn(            "set_voltage_model",
            "Sets the voltage model for the specified library.",
            "set_voltage_model library_name ?-voltage {voltage_name voltage_value}?",
        ),
        # cat2/set_vsdc.2
        _syn(            "set_vsdc",
            "Generates a setup information file in V-SDC format for efficient compare point matching in formal verification tools.",
            "set_vsdc filename ?-append? ?-off?",
        ),
        # cat2/set_watermark_configuration.2
        _syn(            "set_watermark_configuration",
            "Sets the default watermark configuration for the current design.",
            "set_watermark_configuration ?-parameters parameter_list? ?-exec_name executable_name? ?-map_parameters list_of_reserved_parameter_name:tool_parameter_name?",
        ),
        # cat2/set_wire_load.2
        #   WARNING: unmatched closing bracket ']' at position 123
        _syn(            "set_wire_load",
            "Sets the wire loading model for the current design or for the specified cluster or ports.",
            "set_wire_load ?-mode mode_name? ?-size value? ?-library library_name? ?-cluster cluster_name? ?-selection_group group_name?? ?-min? ?-max? ?-name model_name? ?object_list?",
        ),
        # cat2/set_wire_load_min_block_size.2
        _syn(            "set_wire_load_min_block_size",
            "Sets the wire load min_block_size attribute on the current design.",
            "set_wire_load_min_block_size size",
        ),
        # cat2/set_wire_load_selection_group.2
        _syn(            "set_wire_load_selection_group",
            "Specify a selection group to use for determining a wire load model to be assigned to designs and cells or to a specified cluster.",
            "set_wire_load_selection_group ?-library lib? ?-min? ?-max? group_name ?object_list?",
        ),
        # cat2/set_wrapper_configuration.2
        _syn(            "set_wrapper_configuration",
            "Sets the default wrapper configuration for the current design.",
            "set_wrapper_configuration -class core_wrapper | shadow_wrapper ?-style dedicated | shared? ?-core core_list? ?-dedicated_cell_type WC_D1 | WC_D1_S | none? ?-shared_cell_type WC_S1 | WC_S1_S | none? ?-dedicated_design_name design_name? ?-shared_design_name design_name? ?-register_io_implementation swap | in_place? ?-use_dedicated_wrapper_clock true | false? ?-safe_state 0 | 1 | none? ?-delay_test true | false? ?-max_length integer? ?-chain_count integer? ?-mix_cells true | false? ?-input_shift_enable port_name? ?-output_shift_enable port_name? ?-maximize_reuse enable | disable? ?-reuse_threshold threshold_value? ?-depth_threshold threshold_value? ?-use_system_clock_for_dedicated_wrp_cells enable | disable? ?-end_of_chain_logic enable | disable? ?-input_mask_bound mask_bound? ?-output_mask_bound mask_bound? ?-hier_wrapping enable | disable? ?-use_separate_wrapper_chain_controls enable | disable? ?-shift_enable port_name? ?-test_mode mode_name? ?-create_only_wrapper_modes mode_list? ?-add_wrapper_cells_to_power_domains enable | disable? ?-gate_dedicated_wrapper_cell_clk enable | disable? ?-gate_cells none | existing_cg | all? ?-hold_mux_for_shared_wrapper_cells enable | disable? ?-no_dedicated_wrapper_cells enable | disable? ?-feedthrough_chains enable | disable? ?-input_wrapper_cells cell_list? ?-output_wrapper_cells cell_list? ?-exclude_gate_cells list_of_clock_gating_or_registers? ?-force_clock_enable all?",
        ),
        # cat2/set_zero_interconnect_delay_mode.2
        _syn(            "set_zero_interconnect_delay_mode",
            "Forces the timer to ignore the contribution on a timing path from any wire capacitance in the design.",
            "set_zero_interconnect_delay_mode ?true | false?",
        ),
        # cat2/setenv.2
        _syn(            "setenv",
            "Sets the value of a system environment variable.",
            "setenv variable_name new_value",
        ),
        # cat2/sh.2
        _syn(            "sh",
            "Executes a command in a child process.",
            "sh",
        ),
        # cat2/sh_list_key_bindings.2
        _syn(            "sh_list_key_bindings",
            "Displays all the key bindings and edit mode of current shell session. This variable is for use in Tcl mode only.",
            "sh_list_key_bindings ?-nosplit?",
        ),
        # cat2/shell_is_dcnxt_shell.2
        _syn(            "shell_is_dcnxt_shell",
            "Determines if the shell was invoked in DCNXT mode.",
            "shell_is_dcnxt_shell",
        ),
        # cat2/shell_is_in_exploration_mode.2
        _syn(            "shell_is_in_exploration_mode",
            "Determines if the shell was invoked in DC Explorer.",
            "shell_is_in_exploration_mode",
        ),
        # cat2/shell_is_in_ndm_mode.2
        _syn(            "shell_is_in_ndm_mode",
            "Determines if the Design Compiler shell is in NDM mode.",
            "shell_is_in_ndm_mode",
        ),
        # cat2/shell_is_in_topographical_mode.2
        _syn(            "shell_is_in_topographical_mode",
            "Determines if the Design Compiler shell was invoked in topographical mode.",
            "shell_is_in_topographical_mode",
        ),
        # cat2/shell_is_in_xg_mode.2
        _syn(            "shell_is_in_xg_mode",
            "Determines if the shell is in XG mode.",
            "shell_is_in_xg_mode",
        ),
        # cat2/sim_assertion_control.2
        _syn(            "sim_assertion_control",
            "This is a simulation command.",
            "sim_assertion_control ?-elements element_list? ?-exclude_elements exclude_list? ?-domain domain_name? ?-model model_name? ?-controlling_domain controlling_domain_name? ?-control_expr boolean_expression? ?-type type? ?-transitive transitive?",
        ),
        # cat2/sim_corruption_control.2
        _syn(            "sim_corruption_control",
            "This is a simulation command.",
            "sim_corruption_control ?-type type? ?-elements element_list? ?-exclude_elements exclude_list? ?-model model_name? ?-domain domain_name? ?-transitive transitivefP?",
        ),
        # cat2/sim_replay_control.2
        _syn(            "sim_replay_control",
            "This is a simulation command.",
            "sim_replay_control ?-elements element_list? ?-exclude_elements exclude_list? ?-model model_name? ?-domain domain_name? ?-controlling_domain controlling_domain_name? ?-transitive transitive?",
        ),
        # cat2/simplify_constants.2
        _syn(            "simplify_constants",
            "Propagates constants and other information in the current design.",
            "simplify_constants ?-boundary_optimization?",
        ),
        # cat2/size_cell.2
        _syn(            "size_cell",
            "Relinks leaf cells to a new library cell that has the required drive strength (or other properties).",
            "size_cell cell_object lib_cell_object",
        ),
        # cat2/sort_collection.2
        _syn(            "sort_collection",
            "Sorts a collection based on one or more attributes, resulting in a new, sorted collection. The sort is ascending by default.",
            "sort_collection ?-descending? ?-dictionary? ?-limit value_count? collection criteria",
        ),
        # cat2/source.2
        _syn(            "source",
            "Read a file and evaluate it as a Tcl script.",
            "source ?-echo? ?-verbose? ?-continue_on_error? file",
        ),
        # cat2/split_register_bank.2
        _syn(            "split_register_bank",
            "Splits a multibit register bank into smaller multibit registers or single-bit registers.",
            "split_register_bank bank_name -lib_cells list_of_lib_cells",
        ),
        # cat2/ssf_version.2
        _syn(            "ssf_version",
            "Check the SSF version.",
            "ssf_version ?version?",
        ),
        # cat2/start_gui.2
        _syn(            "start_gui",
            "Starts the application GUI.",
            "start_gui",
        ),
        # cat2/start_icc2.2
        _syn(            "start_icc2",
            "Launches an IC Compiler II floorplanning session from within Design Compiler Graphical or DC Explorer physical mode.",
            "start_icc2 -f file_name ?-check_only? ?-verbose?",
        ),
        # cat2/start_icc2_dp.2
        _syn(            "start_icc2_dp",
            "Launches an IC Compiler II floorplanning session from within Design Compiler Graphical.",
            "start_icc2_dp -f file_name ?-check_only? ?-verbose?",
        ),
        # cat2/start_icc_dp.2
        _syn(            "start_icc_dp",
            "Launches the floorplan exploration session from Design Compiler Graphical.",
            "start_icc_dp -f file_name -check_only flag -verbose flag",
        ),
        # cat2/stop_gui.2
        _syn(            "stop_gui",
            "Stops the application GUI.",
            "stop_gui",
        ),
        # cat2/streaming_dft_planner.2
        _syn(            "streaming_dft_planner",
            "Provides visualization of the current DFTMAX Ultra architecture.",
            "streaming_dft_planner ?-show flow | elements | all? ?-preview_output file_name?",
        ),
        # cat2/sub_designs_of.2
        _syn(            "sub_designs_of",
            "Gets the subdesigns according to the options.",
            "sub_designs_of ?-hierarchy? ?-in_partition | -partition_only? ?-dt_only | -ndt_only? ?-multiple_instances | -single_instances? ?-names_only? design",
        ),
        # cat2/sub_instances_of.2
        _syn(            "sub_instances_of",
            "Gets the subinstances according to the options.",
            "sub_instances_of ?-hierarchy? ?-in_partition? ?-partition_only? ?-dt_only? ?-ndt_only? ?-of_references reference_list? ?-master_instance? ?-names_only? design",
        ),
        # cat2/suppress_icc2_message.2
        _syn(            "suppress_icc2_message",
            "Disables printing of one or more IC Compiler II informational or warning messages during ICC2Link.",
            "suppress_icc2_message ?message_list?",
        ),
        # cat2/suppress_message.2
        _syn(            "suppress_message",
            "Disables printing of one or more informational or warning messages.",
            "suppress_message ?message_list?",
        ),
        # cat2/translate.2
        _syn(            "translate",
            "Translates a design from one technology to another.",
            "translate ?-preserve_structure?",
        ),
        # cat2/unalias.2
        _syn(            "unalias",
            "Removes one or more aliases.",
            "unalias patterns",
        ),
        # cat2/ungroup.2
        _syn(            "ungroup",
            "Removes a level of hierarchy.",
            "ungroup cell_list | -all ?-prefix prefix_name? ?-flatten? ?-simple_names? ?-soft? ?-small n? ?-force? ?-start_level n? ?-all_instances?",
        ),
        # cat2/uniquify.2
        _syn(            "uniquify",
            "Removes the multiply instantiated hierarchy in the current design by creating a unique design for each cell instance.",
            "uniquify ?-force? ?-base_name base_name? ?-cell cell_list? ?-reference design_name? ?-new_name new_design_name? ?-dont_skip_empty_designs?",
        ),
        # cat2/unset_power_guide.2
        _syn(            "unset_power_guide",
            "Unsets an existing power guide to be just like an exclusive movebound.",
            "unset_power_guide ?power_guide_list?",
        ),
        # cat2/unsetenv.2
        _syn(            "unsetenv",
            "Removes a system environment variable.",
            "unsetenv variable_name",
        ),
        # cat2/unsuppress_message.2
        _syn(            "unsuppress_message",
            "Enables printing of one or more suppressed informational or suppressed warning messages.",
            "unsuppress_message ?messages?",
        ),
        # cat2/update_bounds.2
        _syn(            "update_bounds",
            "Updates an existing bound by adding or removing objects.",
            "update_bounds ?-name bound_name? ?-bound bound_object? ?-add? ?-remove? cell_list",
        ),
        # cat2/update_cross_probing_files.2
        _syn(            "update_cross_probing_files",
            "Updates the paths of the cross-probed files.",
            "update_cross_probing_files ?-search_path paths? ?-original_file file1? ?-new_file file2? ?-write_script_only output_file? ?-force? ?-verbose?",
        ),
        # cat2/update_floorplan.2
        _syn(            "update_floorplan",
            "Updates the floorplan when reading a floorplan script file generated by the write_floorplan command.",
            "update_floorplan",
        ),
        # cat2/update_lib.2
        _syn(            "update_lib",
            "Reads in a specified library file and uses it to update an existing technology, synthetic, or symbol library.",
            "update_lib ?-overwrite? ?-permanent? library_name file_name ?-no_warnings?",
        ),
        # cat2/update_lib_model.2
        _syn(            "update_lib_model",
            "Updates the library to conform to the PG pin library syntax. This command gets the PG information either from reference library FRAM view or from specific Tcl commands. The library voltage, PG pin of the cell, and related PG pin of the cell pin are updated.",
            "update_lib_model -reference_mode FRAM | TCL ?library_name?",
        ),
        # cat2/update_lib_pg_pin_model.2
        _syn(            "update_lib_pg_pin_model",
            "Defines the power and ground pin model for a library cell.",
            "update_lib_pg_pin_model cell_name -pg_pin_name pin_names ?-pg_voltage_name voltage_names? ?-pg_pin_type pin_types? ?-pg_pin_direction pin_directions? ?-pg_physical_connection physical_connections? ?-pg_related_bias_pin related_bias_pin?",
        ),
        # cat2/update_lib_pin_model.2
        _syn(            "update_lib_pin_model",
            "Sets the pin map for the specified library cell.",
            "update_lib_pin_model cell_name -pins list_of_pins ?-related_power_pin list_of_pins? ?-related_ground_pin list_of_pins? ?-related_bias_pin list_of_pins? ?-power_down_function power_down_func?",
        ),
        # cat2/update_lib_voltage_model.2
        _syn(            "update_lib_voltage_model",
            "Sets the voltage model for the specified library.",
            "update_lib_voltage_model library_name ?-voltage {voltage_name voltage_value}?",
        ),
        # cat2/update_timing.2
        _syn(            "update_timing",
            "Updates timing information on the current design.",
            "update_timing",
        ),
        # cat2/upf_version.2
        _syn(            "upf_version",
            "Accepts and preserves a UPF version string.",
            "upf_version ?version?",
        ),
        # cat2/use_interface_cell.2
        _syn(            "use_interface_cell",
            "Specifies how to map the isolation, level-shifter, and enable level-shifter cells belonging to the specified isolation and/or level-shifter strategy.",
            "use_interface_cell interface_implementation_name -strategy list_of_isolation_level_shifter_strategies -domain power_domain -lib_cells lib_cells ?-force_function? ?-port_map port_map_list?",
        ),
        # cat2/use_test_model.2
        _syn(            "use_test_model",
            "Specifies the subdesigns that will use test model information during DRC and DFT insertion.",
            "use_test_model ?-true design_list? ?-false design_list?",
        ),
        # cat2/view_qor_data.2
        _syn(            "view_qor_data",
            "Launches a localhost web server and Firefox window to view the QoRsum report.",
            "view_qor_data ?-location location? ?-no_web_server? ?-port port_number? ?-browser firefox | chrome?",
        ),
        # cat2/which.2
        _syn(            "which",
            "Locates a file and displays its pathname.",
            "which filename_list",
        ),
        # cat2/while.2
        _syn(            "while",
            "Loop execution control structure.",
            "while",
        ),
        # cat2/win_select_objects.2
        _syn(            "win_select_objects",
            "Creates a collection of objects equivalent to a graphical selection operation.",
            "win_select_objects ?-slct_targets slct_bus? ?-slct_targets_operation operation? ?-create_slct_buses? ?-root instance? ?-within rectangle | -line line | -at point | -radius r | -again_at? ?-intersect? ?-index i? ?-visible?",
        ),
        # cat2/win_set_filter.2
        _syn(            "win_set_filter",
            "Sets a filter to apply to objects selected by the win_select_objects command.",
            "win_set_filter -class class_name ?-stop_level level? ?-start_level level? ?-z_level level? ?-filter expression? ?-layer list? ?-user_filter true | false? ?-user_filter_cmd tcl_cmd? ?-highlighted_only true | false? ?-expand_cell_types list? ?-part list? ?-visible?",
        ),
        # cat2/win_set_select_class.2
        _syn(            "win_set_select_class",
            "Sets the design objects to be collected by the win_select_objects command.",
            "win_set_select_class {-all | class_names} ?-visible?",
        ),
        # cat2/write_app_var.2
        _syn(            "write_app_var",
            "Writes a script to set the current variable values.",
            "write_app_var -output file ?-all | -only_changed_vars? ?pattern?",
        ),
        # cat2/write_bsd_rtl.2
        _syn(            "write_bsd_rtl",
            "Writes the RTL for the configured boundary-scan design into an output file.",
            "write_bsd_rtl ?-output output_file_name? ?-format verilog? ?-all? ?-tap? ?-bsr?",
        ),
        # cat2/write_bsdl.2
        _syn(            "write_bsdl",
            "Generates the boundary-scan description language (BSDL) file for a boundary-scan design.",
            "write_bsdl ?-naming_check VHDL | BSDL | none? ?-output file_name? ?-effort low | medium | high?",
        ),
        # cat2/write_cell_expansion.2
        _syn(            "write_cell_expansion",
            "Writes the cell expansion data, including the area, width, and height of each cell that is expanded.",
            "write_cell_expansion output_file_name",
        ),
        # cat2/write_collection.2
        #   WARNING: unmatched closing bracket ']' at position 42
        _syn(            "write_collection",
            "Output a machine readable report of attribute values for elements in a collection.",
            "write_collection collection -file filename? ?-format format? ?-max_rows value_count? ?-columns attribute_list? ?-metadata?",
        ),
        # cat2/write_def.2
        _syn(            "write_def",
            "Writes the physical data of the specified design to a file in DEF format. To ensure that the names match in the DEF and Verilog files, run the change_names -rules verilog command before saving the design.",
            "write_def -output output_file_name ?-version def_version? ?-unit conversion_factor? ?-compressed? ?-rows_tracks_gcells? ?-vias? ?-all_vias? ?-nondefault_rule? ?-lef lef_file_name? ?-regions_groups? ?-components? ?-macro? ?-fixed? ?-placed? ?-pins? ?-blockages? ?-specialnets? ?-notch_gap? ?-pg_metal_fill? ?-nets? ?-routed_nets? ?-diode_pins? ?-floating_metal_fill? ?-scanchain? ?-no_legalize? ?-verbose?",
        ),
        # cat2/write_design_lib_paths.2
        _syn(            "write_design_lib_paths",
            "Writes into a file the paths to which design libraries are mapped.",
            "write_design_lib_paths ?-filename file_name? ?-dc_setup?",
        ),
        # cat2/write_environment.2
        _syn(            "write_environment",
            "Writes the variable settings and constraints for the specified cells or designs.",
            "write_environment ?-cells cell_list | -designs design_list? ?-format dcsh | dctcl? ?-output file_name? ?-suffix suffix? ?-environment_only? ?-constraints_only? ?-no_lib_info? ?-compress? ?-consistency? ?-script? ?-capture_setup?",
        ),
        # cat2/write_file.2
        _syn(            "write_file",
            "Writes a design netlist or schematic from memory to a file.",
            "write_file ?-format output_format? ?-hierarchy? ?-no_implicit? ?-output output_file_name? ?-scenarios scenario_list? ?-library library_name? ?-include_anchor_cells? ?-exclude_references reference_names? ?-pg? ?design_list? ?-key_file key_file_path? ?-encrypt?",
        ),
        # cat2/write_floorplan.2
        _syn(            "write_floorplan",
            "Writes a Tcl script that contains detailed floorplanning information for the specified design. This file can be used to recreate elements of the floorplan.",
            "write_floorplan ?-all? ?-create_bound? ?-no_bound? ?-no_create_boundary? ?-no_placement_blockage? ?-no_route_guide? ?-no_voltage_area? ?-placement {placement_info_types} ?-create_terminal?? ?-preroute? ?-user_shape? ?-net_shape? ?-row? ?-pin_guide? ?-track? ?-def_version def_version? ?-def_units conversion_factor? file_name ?-format format?",
        ),
        # cat2/write_icc2_files.2
        _syn(            "write_icc2_files",
            "Writes the files needed to load the design in IC Compiler II.",
            "write_icc2_files -output dir_name ?-force? ?-golden_upf upf_files? ?-pg? ?-environment_only? ?-scenarios scenario_list? ?-golden_floorplan golden_floorplan_file? ?-def_version def_version? ?-def_units conversion_factor?",
        ),
        # cat2/write_lib.2
        _syn(            "write_lib",
            "Writes a compiled library to disk as a Synopsys .db file.",
            "write_lib library_name ?-format db? ?-output file_name? ?-names_file file_list?",
        ),
        # cat2/write_lib_specification_model.2
        _syn(            "write_lib_specification_model",
            "Writes the PG pin library conversion-specification commands in the output file.",
            "write_lib_specification_model output_file_name",
        ),
        # cat2/write_link_library.2
        _syn(            "write_link_library",
            "Writes shell commands to save the current link library settings for design instances.",
            "write_link_library ?-full_path_lib_names? ?-nosplit? ?-full_path_lib_names? ?-nosplit? ?-output file_name? ?-target target?",
        ),
        # cat2/write_milkyway.2
        _syn(            "write_milkyway",
            "Writes out the design to Milkyway database format.",
            "write_milkyway -output filename ?-overwrite? ?-scenario scenario_list?",
        ),
        # cat2/write_multibit_components.2
        _syn(            "write_multibit_components",
            "Writes out a set of create_multibit command statements that if executed will allow the user to re-create the current set of multibit components of the design.",
            "write_multibit_components ?-output output_file_name?",
        ),
        # cat2/write_multibit_guidance_files.2
        _syn(            "write_multibit_guidance_files",
            "Writes out the mapping guidance files for the input map file and the register group file that can be used for placement-based multibit mapping in Design Compiler Graphical and IC Compiler.",
            "write_multibit_guidance_files ?-prefix prefix_of_output_file_names?",
        ),
        # cat2/write_mw_lib_files.2
        _syn(            "write_mw_lib_files",
            "Writes the technology, or plib, or reference control file of the Milkyway library.",
            "write_mw_lib_files ?-technology? ?-reference_control_file? ?-stream_layer_map_file file_format? -output file_name ?libName?",
        ),
        # cat2/write_parasitics.2
        _syn(            "write_parasitics",
            "Writes parasitics for all scenarios in SPEF format or as a Tcl script that contains set_load and set_resistance commands.",
            "write_parasitics ?-output file_name? ?-format reduced? ?-scenario scenario_name? ?-min? ?-ratio ratio_number? ?-script?",
        ),
        # cat2/write_physical_constraints.2
        _syn(            "write_physical_constraints",
            "Writes the script of Tcl commands to export the current physical constraint settings. This command is supported only in topographical mode. Note: The write_physical_constraints command is now aliased to the write_floorplan command. You should use the write_floorplan command instead.",
            "write_physical_constraints -output tcl_file ?-no_site_row? ?-pre_route?",
        ),
        # cat2/write_qor_data.2
        _syn(            "write_qor_data",
            "Captures QoR results to disk for viewing and comparing with the QORsum web application and report.",
            "write_qor_data ?-label label_name? ?-output output_dir? ?-report_list list_of_reports? ?-report_group group_name? ?-exclude_list list_of_reports? ?-mark_start_time?",
        ),
        # cat2/write_qtm_model.2
        _syn(            "write_qtm_model",
            "Writes the Quick Timing Model (QTM) file.",
            "write_qtm_model -out_dir output_qtm_directory ?-text?",
        ),
        # cat2/write_rp_groups.2
        _syn(            "write_rp_groups",
            "Writes out the relative placement constraints for the specified relative placement groups.",
            "write_rp_groups rp_groups | -all ?-hierarchy? ?-quiet? ?-nosplit? ?-output filename? ?-create? ?-leaf? ?-keepout? ?-instance? ?-include?",
        ),
        # cat2/write_rtl_load.2
        _syn(            "write_rtl_load",
            "Writes a script of RTL load commands for the current design.",
            "write_rtl_load ?-format dctcl | dcsh? ?-output file_name?",
        ),
        # cat2/write_safety_register_data.2
        _syn(            "write_safety_register_data",
            "Writes a script file for creating safety register rules and groups.",
            "write_safety_register_data -output filename",
        ),
        # cat2/write_saif.2
        _syn(            "write_saif",
            "Writes a backward Switching Activity Interchange Format (SAIF) file.",
            "write_saif -output file_name ?-instances instances? ?-no_hierarchy? ?-rtl? ?-propagated? ?-exclude_sdpd?",
        ),
        # cat2/write_scan_def.2
        _syn(            "write_scan_def",
            "Generates SCANDEF scan chain information for performing scan chain reordering in the physical implementation flow.",
            "write_scan_def ?-output def_file? ?-expand_elements list_of_cells?",
        ),
        # cat2/write_script.2
        _syn(            "write_script",
            "Writes shell commands to save the current settings.",
            "write_script ?-hierarchy? ?-no_annotated_check? ?-no_annotated_delay? ?-no_cg? ?-full_path_lib_names? ?-nosplit? ?-format dctcl | dcsh? ?-include loop_breaking? ?-output file_name?",
        ),
        # cat2/write_sdc.2
        _syn(            "write_sdc",
            "Writes out a script in Synopsys Design Constraints (SDC) format.",
            "write_sdc file_name ?-nosplit? ?-version sdc_version?",
        ),
        # cat2/write_sdf.2
        _syn(            "write_sdf",
            "Writes a Standard Delay Format (SDF) back-annotation file.",
            "write_sdf ?-version sdf_version? ?-significant_digits digits? ?-instance inst_name? file_name",
        ),
        # cat2/write_tech_file.2
        _syn(            "write_tech_file",
            "Write a technology file from the current library.",
            "write_tech_file ?-library lib_name? file_name",
        ),
        # cat2/write_test.2
        #   WARNING: unclosed bracket '[' at position 45
        _syn(            "write_test",
            "Formats the test patterns for the current design into one or more test vector files.",
            "write_test ?-output output_vector_file_name? ?-capture_cycle -format stil | wgl_serial | verilog ?-multiple_pattern_counter list? ?-multiple_signature list? ?-multiple_seed list? ?-multiple_occ list?",
        ),
        # cat2/write_test_model.2
        _syn(            "write_test_model",
            "Writes a test model file.",
            "write_test_model ?-format ctl | ddc? ?-names verilog | verilog_single_bit? ?-output model_file? ?-inclusive? ?-design design_name?",
        ),
        # cat2/write_test_protocol.2
        _syn(            "write_test_protocol",
            "Writes a STIL test protocol file.",
            "write_test_protocol ?-design design_name? ?-output file_name? ?-test_mode mode_name? ?-instruction instruction_name? ?-names format_name? ?-disable_codecs decompressor_list?",
        ),
        # cat2/write_timing_context.2
        _syn(            "write_timing_context",
            "Writes Scenarios constraints and configuration for the current design",
            "write_timing_context -output directory ?-scenarios scenario_list? ?-format icc2? ?-nosplit?",
        ),
    )
