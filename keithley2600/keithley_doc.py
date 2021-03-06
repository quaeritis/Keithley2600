# -*- coding: utf-8 -*-
#
# Copyright © keithley2600 Project Contributors
# Licensed under the terms of the MIT License
# (see keithley2600/__init__.py for details)


# Warning: PROPERTIES, CONSTANTS, FUNCTIONS and CLASSES must be mutually
# exclusive. A string used for a PROPERTY cannot be used to create a class
# later, when the property already exists (and vice versa).

"""
Submodule listing accepted keithley TSP commands.

"""

WARNING = """Warning: PROPERTIES, CONSATNTS, FUNCTIONS must
not contain elements from and CLASSES. E.g., once a property is created,
it cannot be used as a class anymore"""

CONSTANTS = [
            'CAPACITY',
            'ARMED_EVENT_ID',
            'MEASURE_COMPLETE_EVENT_ID',
            'PULSE_COMPLETE_EVENT_ID',
            'SOURCE_COMPLETE_EVENT_ID',
            'SWEEP_COMPLETE_EVENT_ID',
            'SWEEPING_EVENT_ID',
            'IDLE_EVENT_ID',
            'EVENT_ID',
            'OUTPUT_OFF',
            'OUTPUT_ON',
            'OUTPUT_HIGH_Z',
            'OUTPUT_DCAMPS',
            'OUTPUT_DCVOLTS',
            'MEASURE_DCAMPS',
            'MEASURE_DCVOLTS',
            'MEASURE_OHMS',
            'MEASURE_WATTS',
            'DISABLE',
            'ENABLE',
            'SENSE_LOCAL',
            'SENSE_REMOTE',
            'SENSE_CALA',
            'SOURCE_IDLE',
            'SOURCE_HOLD',
            'AUTORANGE_OFF',
            'AUTORANGE_ON',
            'AUTORANGE_FOLLOW_LIMIT',
            'ON',
            'OFF',
            ]

FUNCTIONS = [
            'beep',
            'bitand',
            'bitor',
            'bitxor',
            'clear',
            'get',
            'getfield',
            'set',
            'setfield',
            'test',
            'toggle',
            'clear',
            'clearcache',
            'add',
            'clear',
            'next',
            'delay',
            'readbit',
            'readport',
            'assert',
            'clear',
            'release',
            'reset',
            'wait',
            'writebit',
            'writeport',
            'clear',
            'getannunciators',
            'getcursor',
            'getlastkey',
            'gettext',
            'inputvalue',
            'add',
            'catalog',
            'delete',
            'menu',
            'prompt',
            'sendkey',
            'setcursor',
            'settext',
            'clear',
            'wait',
            'waitkey',
            'clear',
            'next',
            'all',
            'clear',
            'next',
            'exit',
            'chdir',
            'cwd',
            'is_dir',
            'is_file',
            'mkdir',
            'readdir',
            'rmdir',
            'gettimezone',
            'gm_isweep',
            'gm_vsweep',
            'i_leakage_measure',
            'i_leakage_threshold',
            'InitiatePulseTest',
            'InitiatePulseTestDual',
            'close',
            'flush',
            'input',
            'open',
            # 'output',  # XXX: not supported because of conflict with smuX.source.output
            'read',
            'type',
            'write',
            'applysettings',
            'reset',
            'restoredefaults',
            'assert',
            'clear',
            'connect',
            'disconnect',
            'wait',
            'reset',
            'makegetter',
            'makesetter',
            'meminfo',
            'execute',
            'getglobal',
            'setglobal',
            'opc',
            'remove',
            'rename',
            'print',
            'printbuffer',
            'printnumber',
            'QueryPulseConfig',
            'reset',
            'savebuffer',
            'delete',
            'catalog',
            'load',
            'new',
            'newautorun',
            'restore',
            'run',
            'catalog',
            'list',
            'run',
            'save',
            'read',
            'write',
            'settime',
            'settimezone',
            'recall',
            'save',
            'abort',
            'getstats',
            'recalculatestats',
            'lock',
            'restore',
            'save',
            'unlock',
            'calibratehi',
            'calibratelo',
            'check',
            'makebuffer',
            'calibratev',
            'calibratei',
            'overlappedv',
            'overlappedi',
            'overlappedr',
            'overlappedp',
            'measurevandstep',
            'measureiandstep',
            'measurerandstep',
            'measurepandstep',
            'reset',
            'savebuffer',
            'calibratev',
            'calibratei',
            'set',
            'set',
            'initiate',
            'set',
            'linearv',
            'lineari',
            'listv',
            'listi',
            'logv',
            'logi',
            'set',
            'reset',
            't',
            'reset',
            'clear',
            'reset',
            'wait',
            'clear',
            'clear',
            'reset',
            'wait',
            'wait',
            'readbit',
            'readport',
            'reset',
            'assert',
            'clear',
            'release',
            'reset',
            'wait',
            'writebit',
            'writeport',
            'clear',
            'connect',
            'disconnect',
            'execute',
            'idn',
            'read',
            'readavailable',
            'reset',
            'termination',
            'abort',
            'rbtablecopy',
            'runscript',
            'write',
            'add',
            'catalog',
            'delete',
            'get',
            'waitcomplete',
            'delete',
            'get',
            'waitcomplete',
            'v',
            'i',
            'iv',
            'r',
            'p',
            ]

PROPERTIES = [
            'enable',
            'appendmode',
            'basetimestamp',
            'cachemode',
            'capacity',
            'collectsourcevalues',
            'collecttimestamps',
            'fillcount',
            'fillmode',
            'measurefunctions',
            'measureranges',
            'n',
            'readings',
            'sourcefunctions',
            'sourceoutputstates',
            'sourceranges',
            'sourcevalues',
            'statuses',
            'timestampresolution',
            'timestamps',
            'count',
            'mode',
            'overrun',
            'pulsewidth',
            'stimulus',
            'writeprotect',
            'locallockout',
            'numpad',
            'screen',
            'digits',
            'func',
            'func',
            'overrun',
            'count',
            'count',
            'enable',
            'overwritemethod',
            'asciiprecision',
            'byteorder',
            'data',
            'address',
            'autoconnect',
            'address[N]',
            'domain',
            'dynamic',
            'hostname',
            'verify',
            'duplex',
            'gateway',
            'ipaddress',
            'method',
            'speed',
            'subnetmask',
            'linktimeout',
            'lxidomain',
            'nagle',
            'address[N]',
            'name',
            'duplex',
            'gateway',
            'ipaddress',
            'macaddress',
            'dst',
            'rawsocket',
            'telnet',
            'vxi11',
            'speed',
            'subnetmask',
            'timedwait',
            # 'connected', # XXX: conflicts with connected attribute of Keithley2600Base
            'ipaddress',
            'mode',
            'overrun',
            'protocol',
            'pseudostate',
            'stimulus',
            'autolinefreq',
            'description',
            'linefreq',
            'model',
            'password',
            'passwordmode',
            'prompts',
            'prompts4882',
            'revision',
            'serialno',
            'showerrors',
            'anonymous',
            'autorun',
            'name',
            'baud',
            'databits',
            'flowcontrol',
            'parity',
            'poweron',
            'adjustdate',
            'date',
            'due',
            'password',
            'polarity',
            'state',
            'speed',
            'threshold',
            'analogfilter',
            'autorangev',
            'autorangei',
            'autozero',
            'count',
            'delay',
            'delayfactor',
            'count',
            'enable',
            'type',
            'highcrangedelayfactor',
            'interval',
            'lowrangev',
            'lowrangei',
            'nplc',
            'rangev',
            'rangei',
            'enablev',
            'enablei',
            'enabler',
            'enablep',
            'levelv',
            'leveli',
            'levelr',
            'levelp',
            'sense',
            'autorangev',
            'autorangei',
            'compliance',
            'delay',
            'func',
            'highc',
            'limitv',
            'limiti',
            'lowrangev',
            'lowrangei',
            'offfunc',
            'offlimitv',
            'offlimiti',
            'offmode',
            'output',
            'outputenableaction',
            'settling',
            'sink',
            'count',
            'stimulus',
            'autoclear',
            'count',
            'action',
            'stimulus',
            'action',
            'action',
            'stimulus',
            'action',
            'stimulus',
            'condition',
            'node_enable',
            'node_event',
            'request_enable',
            'request_event',
            'orenable',
            'overrun',
            'stimulus',
            'count',
            'delay',
            'delaylist',
            'overrun',
            'passthrough',
            'stimulus',
            'group',
            'master',
            'state',
            'mode',
            'overrun',
            'pulsewidth',
            'stimulus',
            'writeprotect',
            'timeout',
            'abortonconnect',
            'condition',
            'enable',
            'event',
            'ntr',
            'ptr',
            ]

CLASSES = [
            'arm',
            'beeper',
            'bit',
            'blender',
            'buffer',
            'bufferVar',
            'buffer_available',
            'cal',
            'calibrating',
            'calibration',
            'config',
            'contact',
            'current_limit',
            'dataqueue',
            'digio',
            'display',
            'dns',
            'endpulse',
            'endsweep',
            'errorqueue',
            'eventlog',
            'factory',
            'filter',
            'format',
            'fs',
            'gpib',
            'instrument',
            'io',
            'lan',
            'limit',
            'loadmenu',
            'localnode',
            'measure',
            'measurement',
            'measuring',
            'node',
            'nvbuffer1',
            'nvbuffer2',
            'operation',
            'os',
            'over_temperature',
            'port',
            'questionable',
            'reading_overflow',
            'rel',
            'remote',
            'script',
            'serial',
            'setup',
            'smua',
            'smub',
            'source',
            'standard',
            'status',
            'sweeping',
            'system',
            'system2',
            'system3',
            'system4',
            'system5',
            'timer',
            'trigger',
            'trigger_blender',
            'trigger_overrrun',
            'trigger_overrun',
            'trigger_timer',
            'tsp',
            'tsplink',
            'tspnet',
            'unstable_output',
            'user',
            'userstring',
            'voltage_limit',
            ]

ALL = [
 'InitiatePulseTest',
 'InitiatePulseTestDual',
 'QueryPulseConfig',
 'beeper.beep',
 'beeper.enable',
 'bit.bitand',
 'bit.bitor',
 'bit.bitxor',
 'bit.clear',
 'bit.get',
 'bit.getfield',
 'bit.set',
 'bit.setfield',
 'bit.test',
 'bit.toggle',
 'bufferVar.appendmode',
 'bufferVar.basetimestamp',
 'bufferVar.cachemode',
 'bufferVar.capacity',
 'bufferVar.clear',
 'bufferVar.clearcache',
 'bufferVar.collectsourcevalues',
 'bufferVar.collecttimestamps',
 'bufferVar.fillcount',
 'bufferVar.fillmode',
 'bufferVar.measurefunctions',
 'bufferVar.measureranges',
 'bufferVar.n',
 'bufferVar.readings',
 'bufferVar.sourcefunctions',
 'bufferVar.sourceoutputstates',
 'bufferVar.sourceranges',
 'bufferVar.sourcevalues',
 'bufferVar.statuses',
 'bufferVar.timestampresolution',
 'bufferVar.timestamps',
 'dataqueue.CAPACITY',
 'dataqueue.add',
 'dataqueue.clear',
 'dataqueue.count',
 'dataqueue.next',
 'delay',
 'digio.readbit',
 'digio.readport',
 'digio.trigger.assert',
 'digio.trigger.clear',
 'digio.trigger.release',
 'digio.trigger.reset',
 'digio.trigger.wait',
 'digio.trigger[N].EVENT_ID',
 'digio.trigger[N].mode',
 'digio.trigger[N].overrun',
 'digio.trigger[N].pulsewidth',
 'digio.trigger[N].stimulus',
 'digio.writebit',
 'digio.writeport',
 'digio.writeprotect',
 'display.clear',
 'display.getannunciators',
 'display.getcursor',
 'display.getlastkey',
 'display.gettext',
 'display.inputvalue',
 'display.loadmenu.add',
 'display.loadmenu.catalog',
 'display.loadmenu.delete',
 'display.locallockout',
 'display.menu',
 'display.numpad',
 'display.prompt',
 'display.screen',
 'display.sendkey',
 'display.setcursor',
 'display.settext',
 'display.smua.digits',
 'display.smua.limit.func',
 'display.smua.measure.func',
 'display.smub.digits',
 'display.smub.limit.func',
 'display.smub.measure.func',
 'display.trigger.EVENT_ID',
 'display.trigger.clear',
 'display.trigger.overrun',
 'display.trigger.wait',
 'display.waitkey',
 'errorqueue.clear',
 'errorqueue.count',
 'errorqueue.next',
 'eventlog.all',
 'eventlog.clear',
 'eventlog.count',
 'eventlog.enable',
 'eventlog.next',
 'eventlog.overwritemethod',
 'exit',
 'format.asciiprecision',
 'format.byteorder',
 'format.data',
 'fs.chdir',
 'fs.cwd',
 'fs.is_dir',
 'fs.is_file',
 'fs.mkdir',
 'fs.readdir',
 'fs.rmdir',
 'gettimezone',
 'gm_isweep',
 'gm_vsweep',
 'gpib.address',
 'i_leakage_measure',
 'i_leakage_threshold',
 'io.close',
 'io.flush',
 'io.input',
 'io.open',
 #  'io.output', # XXX: not supported because of conflict with smuX.source.output
 'io.read',
 'io.type',
 'io.write',
 'kei.*',
 'lan.applysettings',
 'lan.autoconnect',
 'lan.config.dns.address[N]',
 'lan.config.dns.domain',
 'lan.config.dns.dynamic',
 'lan.config.dns.hostname',
 'lan.config.dns.verify',
 'lan.config.duplex',
 'lan.config.gateway',
 'lan.config.ipaddress',
 'lan.config.method',
 'lan.config.speed',
 'lan.config.subnetmask',
 'lan.linktimeout',
 'lan.lxidomain',
 'lan.nagle',
 'lan.reset',
 'lan.restoredefaults',
 'lan.status.dns.address[N]',
 'lan.status.dns.name',
 'lan.status.duplex',
 'lan.status.gateway',
 'lan.status.ipaddress',
 'lan.status.macaddress',
 'lan.status.port.dst',
 'lan.status.port.rawsocket',
 'lan.status.port.telnet',
 'lan.status.port.vxi11',
 'lan.status.speed',
 'lan.status.subnetmask',
 'lan.timedwait',
 'lan.trigger.assert',
 'lan.trigger.clear',
 'lan.trigger.connect',
 'lan.trigger.disconnect',
 'lan.trigger.wait',
 'lan.trigger[N].EVENT_ID',
 # 'lan.trigger[N].connected',  # XXX: conflicts with connected attribute of Keithley2600Base
 'lan.trigger[N].ipaddress',
 'lan.trigger[N].mode',
 'lan.trigger[N].overrun',
 'lan.trigger[N].protocol',
 'lan.trigger[N].pseudostate',
 'lan.trigger[N].stimulus',
 'localnode.autolinefreq',
 'localnode.description',
 'localnode.linefreq',
 'localnode.model',
 'localnode.password',
 'localnode.passwordmode',
 'localnode.prompts',
 'localnode.prompts4882',
 'localnode.reset',
 'localnode.revision',
 'localnode.serialno',
 'localnode.showerrors',
 'makegetter',
 'makesetter',
 'meminfo',
 'node.execute',
 'node.getglobal',
 'node.setglobal',
 'opc',
 'os.remove',
 'os.rename',
 'print',
 'printbuffer',
 'printnumber',
 'reset',
 'savebuffer',
 'script.anonymous',
 'script.delete',
 'script.factory.catalog',
 'script.load',
 'script.new',
 'script.newautorun',
 'script.restore',
 'script.run',
 'script.user.catalog',
 'serial.baud',
 'serial.databits',
 'serial.flowcontrol',
 'serial.parity',
 'serial.read',
 'serial.write',
 'settime',
 'settimezone',
 'setup.poweron',
 'setup.recall',
 'setup.save',
 'smua.abort',
 'smua.buffer.getstats',
 'smua.buffer.recalculatestats',
 'smua.cal.adjustdate',
 'smua.cal.date',
 'smua.cal.due',
 'smua.cal.lock',
 'smua.cal.password',
 'smua.cal.polarity',
 'smua.cal.restore',
 'smua.cal.save',
 'smua.cal.state',
 'smua.cal.unlock',
 'smua.contact.calibratehi',
 'smua.contact.calibratelo',
 'smua.contact.check',
 'smua.contact.r',
 'smua.contact.speed',
 'smua.contact.threshold',
 'smua.makebuffer',
 'smua.measure.v',
 'smua.measure.i',
 'smua.measure.analogfilter',
 'smua.measure.autorangev',
 'smua.measure.autorangei',
 'smua.measure.autozero',
 'smua.measure.calibratev',
 'smua.measure.calibratei',
 'smua.measure.count',
 'smua.measure.delay',
 'smua.measure.delayfactor',
 'smua.measure.filter.count',
 'smua.measure.filter.enable',
 'smua.measure.filter.type',
 'smua.measure.highcrangedelayfactor',
 'smua.measure.interval',
 'smua.measure.lowrangev',
 'smua.measure.lowrangei',
 'smua.measure.nplc',
 'smua.measure.overlappedv',
 'smua.measure.overlappedi',
 'smua.measure.overlappedr',
 'smua.measure.overlappedp',
 'smua.measure.rangev',
 'smua.measure.rangei',
 'smua.measure.rel.enablev',
 'smua.measure.rel.enablei',
 'smua.measure.rel.enabler',
 'smua.measure.rel.enablep',
 'smua.measure.rel.levelv',
 'smua.measure.rel.leveli',
 'smua.measure.rel.levelr',
 'smua.measure.rel.levelp',
 'smua.measurevandstep',
 'smua.measureiandstep',
 'smua.measurerandstep',
 'smua.measurepandstep',
 'smua.nvbufferY',
 'smua.nvbufferY.readings[N]',
 'smua.reset',
 'smua.savebuffer',
 'smua.sense',
 'smua.source.autorangei',
 'smua.source.autorangev',
 'smua.source.calibratei',
 'smua.source.calibratev',
 'smua.source.compliance',
 'smua.source.delay',
 'smua.source.func',
 'smua.source.highc',
 'smua.source.leveli',
 'smua.source.levelv',
 'smua.source.limiti',
 'smua.source.limitv',
 'smua.source.lowrangei',
 'smua.source.lowrangev',
 'smua.source.offfunc',
 'smua.source.offlimiti',
 'smua.source.offlimitv',
 'smua.source.offmode',
 'smua.source.output',
 'smua.source.outputenableaction',
 'smua.source.rangev',
 'smua.source.rangei',
 'smua.source.settling',
 'smua.source.sink',
 'smua.trigger.ARMED_EVENT_ID',
 'smua.trigger.IDLE_EVENT_ID',
 'smua.trigger.MEASURE_COMPLETE_EVENT_ID',
 'smua.trigger.PULSE_COMPLETE_EVENT_ID',
 'smua.trigger.SOURCE_COMPLETE_EVENT_ID',
 'smua.trigger.SWEEPING_EVENT_ID',
 'smua.trigger.SWEEP_COMPLETE_EVENT_ID',
 'smua.trigger.arm.count',
 'smua.trigger.arm.set',
 'smua.trigger.arm.stimulus',
 'smua.trigger.autoclear',
 'smua.trigger.count',
 'smua.trigger.endpulse.action',
 'smua.trigger.endpulse.set',
 'smua.trigger.endpulse.stimulus',
 'smua.trigger.endsweep.action',
 'smua.trigger.initiate',
 'smua.trigger.measure.i',
 'smua.trigger.measure.v',
 'smua.trigger.measure.r',
 'smua.trigger.measure.p',
 'smua.trigger.measure.action',
 'smua.trigger.measure.set',
 'smua.trigger.measure.stimulus',
 'smua.trigger.source.action',
 'smua.trigger.source.limiti',
 'smua.trigger.source.limitv',
 'smua.trigger.source.lineari',
 'smua.trigger.source.linearv',
 'smua.trigger.source.listi',
 'smua.trigger.source.listv',
 'smua.trigger.source.logY',
 'smua.trigger.source.logi',
 'smua.trigger.source.logv',
 'smua.trigger.source.set',
 'smua.trigger.source.stimulus',
 'smub.abort',
 'smub.buffer.getstats',
 'smub.buffer.recalculatestats',
 'smub.cal.adjustdate',
 'smub.cal.date',
 'smub.cal.due',
 'smub.cal.lock',
 'smub.cal.password',
 'smub.cal.polarity',
 'smub.cal.restore',
 'smub.cal.save',
 'smub.cal.state',
 'smub.cal.unlock',
 'smub.contact.calibratehi',
 'smub.contact.calibratelo',
 'smub.contact.check',
 'smub.contact.r',
 'smub.contact.speed',
 'smub.contact.threshold',
 'smub.makebuffer',
 'smub.measure.Y',
 'smub.measure.analogfilter',
 'smub.measure.autorangeY',
 'smub.measure.autozero',
 'smub.measure.calibrateY',
 'smub.measure.count',
 'smub.measure.delay',
 'smub.measure.delayfactor',
 'smub.measure.filter.count',
 'smub.measure.filter.enable',
 'smub.measure.filter.type',
 'smub.measure.highcrangedelayfactor',
 'smub.measure.interval',
 'smub.measure.lowrangeY',
 'smub.measure.nplc',
 'smub.measure.overlappedY',
 'smub.measure.rangeY',
 'smub.measure.rel.enableY',
 'smub.measure.rel.levelY',
 'smub.measureYandstep',
 'smub.nvbufferY',
 'smub.nvbufferY.readings[N]',
 'smub.reset',
 'smub.savebuffer',
 'smub.sense',
 'smub.source.autorangeY',
 'smub.source.calibrateY',
 'smub.source.compliance',
 'smub.source.delay',
 'smub.source.func',
 'smub.source.highc',
 'smub.source.levelY',
 'smub.source.limitY',
 'smub.source.lowrangeY',
 'smub.source.offfunc',
 'smub.source.offlimitY',
 'smub.source.offmode',
 'smub.source.output',
 'smub.source.outputenableaction',
 'smub.source.rangeY',
 'smub.source.settling',
 'smub.source.sink',
 'smub.trigger.ARMED_EVENT_ID',
 'smub.trigger.IDLE_EVENT_ID',
 'smub.trigger.MEASURE_COMPLETE_EVENT_ID',
 'smub.trigger.PULSE_COMPLETE_EVENT_ID',
 'smub.trigger.SOURCE_COMPLETE_EVENT_ID',
 'smub.trigger.SWEEPING_EVENT_ID',
 'smub.trigger.SWEEP_COMPLETE_EVENT_ID',
 'smub.trigger.arm.count',
 'smub.trigger.arm.set',
 'smub.trigger.arm.stimulus',
 'smub.trigger.autoclear',
 'smub.trigger.count',
 'smub.trigger.endpulse.action',
 'smub.trigger.endpulse.set',
 'smub.trigger.endpulse.stimulus',
 'smub.trigger.endsweep.action',
 'smub.trigger.initiate',
 'smub.trigger.measure.Y',
 'smub.trigger.measure.action',
 'smub.trigger.measure.set',
 'smub.trigger.measure.stimulus',
 'smub.trigger.source.action',
 'smub.trigger.source.limitY',
 'smub.trigger.source.linearY',
 'smub.trigger.source.listY',
 'smub.trigger.source.logY',
 'smub.trigger.source.set',
 'smub.trigger.source.stimulus',
 'status.condition',
 'status.measurement.*',
 'status.measurement.buffer_available.*',
 'status.measurement.current_limit.*',
 'status.measurement.instrument.*',
 'status.measurement.instrument.smua.*',
 'status.measurement.instrument.smub.*',
 'status.measurement.reading_overflow.*',
 'status.measurement.voltage_limit.*',
 'status.node_enable',
 'status.node_event',
 'status.operation.*',
 'status.operation.calibrating.*',
 'status.operation.instrument.digio.*',
 'status.operation.instrument.digio.trigger_overrun.*',
 'status.operation.instrument.lan.*',
 'status.operation.instrument.lan.trigger_overrun.*',
 'status.operation.instrument.smua.*',
 'status.operation.instrument.smua.trigger_overrrun.*',
 'status.operation.instrument.smub.*',
 'status.operation.instrument.smub.trigger_overrrun.*',
 'status.operation.instrument.trigger_blender.*',
 'status.operation.instrument.trigger_blender.trigger_overrun.*',
 'status.operation.instrument.trigger_timer.*',
 'status.operation.instrument.trigger_timer.trigger_overrun.*',
 'status.operation.instrument.tsplink.*',
 'status.operation.instrument.tsplink.trigger_overrun.*',
 'status.operation.measuring.*',
 'status.operation.remote.*',
 'status.operation.sweeping.*',
 'status.operation.trigger_overrun.*',
 'status.operation.user.*',
 'status.questionable.*',
 'status.questionable.calibration.*',
 'status.questionable.instrument.*',
 'status.questionable.instrument.smua.*',
 'status.questionable.instrument.smub.*',
 'status.questionable.over_temperature.*',
 'status.questionable.unstable_output.*',
 'status.request_enable',
 'status.request_event',
 'status.reset',
 'status.standard.*',
 'status.system.*',
 'status.system2.*',
 'status.system3.*',
 'status.system4.*',
 'status.system5.*',
 'timer.measure.t',
 'timer.reset',
 'trigger.EVENT_ID',
 'trigger.blender.clear',
 'trigger.blender.reset',
 'trigger.blender.wait',
 'trigger.blender[N].EVENT_ID',
 'trigger.blender[N].orenable',
 'trigger.blender[N].overrun',
 'trigger.blender[N].stimulus[M]',
 'trigger.clear',
 'trigger.timer.clear',
 'trigger.timer.reset',
 'trigger.timer.wait',
 'trigger.timer[N].EVENT_ID',
 'trigger.timer[N].count',
 'trigger.timer[N].delay',
 'trigger.timer[N].delaylist',
 'trigger.timer[N].overrun',
 'trigger.timer[N].passthrough',
 'trigger.timer[N].stimulus',
 'trigger.wait',
 'tsplink.group',
 'tsplink.master',
 'tsplink.readbit',
 'tsplink.readport',
 'tsplink.reset',
 'tsplink.state',
 'tsplink.trigger.assert',
 'tsplink.trigger.clear',
 'tsplink.trigger.release',
 'tsplink.trigger.reset',
 'tsplink.trigger.wait',
 'tsplink.trigger[N].EVENT_ID',
 'tsplink.trigger[N].mode',
 'tsplink.trigger[N].overrun',
 'tsplink.trigger[N].pulsewidth',
 'tsplink.trigger[N].stimulus',
 'tsplink.writebit',
 'tsplink.writeport',
 'tsplink.writeprotect',
 'tspnet.clear',
 'tspnet.connect',
 'tspnet.disconnect',
 'tspnet.execute',
 'tspnet.idn',
 'tspnet.read',
 'tspnet.readavailable',
 'tspnet.reset',
 'tspnet.termination',
 'tspnet.timeout',
 'tspnet.tsp.abort',
 'tspnet.tsp.abortonconnect',
 'tspnet.tsp.rbtablecopy',
 'tspnet.tsp.runscript',
 'tspnet.write',
 'userstring.add',
 'userstring.catalog',
 'userstring.delete',
 'userstring.get',
 'waitcomplete',
 ]

PROPERTY_LISTS = [
        'trigger.blender[1].stimulus',
        'trigger.blender[2].stimulus',
        'smua.nvbuffer1.readings',
        'smua.nvbuffer2.readings',
        'smub.nvbuffer1.readings',
        'smub.nvbuffer2.readings',
        'readings',
        ]

properties = set(PROPERTIES)
functions = set(FUNCTIONS)
constants = set(CONSTANTS)
classes = set(CLASSES)

check0 = bool(properties & classes)
check1 = bool(functions & classes)
check2 = bool(constants & classes)

if check0 or check1 or check2:
    raise RuntimeError(WARNING)
