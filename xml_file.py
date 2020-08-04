xml_files = []
VM_IP_addresses = ["192.168.122.37","192.168.122.221","192.168.122.193"]
VM_names = ["m1","m2","m3"]

m1_xml = "<!--WARNING: THIS IS AN AUTO-GENERATED FILE. CHANGES TO IT ARE LIKELY TO BEOVERWRITTEN AND LOST. Changes to this xml configuration should be made using:  virsh edit m1or other application using the libvirt API.--><domain type='kvm'>  <name>m1</name>  <uuid>034873f9-1e43-451d-a65d-b4df3238d2f9</uuid>  <memory unit='KiB'>614400</memory>  <currentMemory unit='KiB'>614400</currentMemory>  <vcpu placement='static'>1</vcpu>  <os>    <type arch='x86_64' machine='pc-i440fx-bionic'>hvm</type>    <boot dev='hd'/>  </os>  <features>    <acpi/>    <apic/>    <vmport state='off'/>  </features>  <cpu mode='custom' match='exact' check='partial'>    <model fallback='allow'>Broadwell-noTSX-IBRS</model>  </cpu>  <clock offset='utc'>    <timer name='rtc' tickpolicy='catchup'/>    <timer name='pit' tickpolicy='delay'/>    <timer name='hpet' present='no'/>  </clock>  <on_poweroff>destroy</on_poweroff>  <on_reboot>restart</on_reboot>  <on_crash>destroy</on_crash>  <pm>    <suspend-to-mem enabled='no'/>    <suspend-to-disk enabled='no'/>  </pm>  <devices>    <emulator>/usr/bin/qemu-kvm</emulator>    <disk type='file' device='disk'>      <driver name='qemu' type='qcow2'/>      <source file='/var/lib/libvirt/images/m1.qcow2'/>      <target dev='vda' bus='virtio'/>      <address type='pci' domain='0x0000' bus='0x00' slot='0x07' function='0x0'/>    </disk>    <disk type='file' device='cdrom'>      <driver name='qemu' type='raw'/>      <target dev='hda' bus='ide'/>      <readonly/>      <address type='drive' controller='0' bus='0' target='0' unit='0'/>    </disk>    <controller type='usb' index='0' model='ich9-ehci1'>      <address type='pci' domain='0x0000' bus='0x00' slot='0x05' function='0x7'/>    </controller>    <controller type='usb' index='0' model='ich9-uhci1'>      <master startport='0'/>      <address type='pci' domain='0x0000' bus='0x00' slot='0x05' function='0x0' multifunction='on'/>    </controller>    <controller type='usb' index='0' model='ich9-uhci2'>      <master startport='2'/>      <address type='pci' domain='0x0000' bus='0x00' slot='0x05' function='0x1'/>    </controller>    <controller type='usb' index='0' model='ich9-uhci3'>      <master startport='4'/>      <address type='pci' domain='0x0000' bus='0x00' slot='0x05' function='0x2'/>    </controller>    <controller type='pci' index='0' model='pci-root'/>    <controller type='ide' index='0'>      <address type='pci' domain='0x0000' bus='0x00' slot='0x01' function='0x1'/>    </controller>    <controller type='virtio-serial' index='0'>      <address type='pci' domain='0x0000' bus='0x00' slot='0x06' function='0x0'/>    </controller>    <interface type='network'>      <mac address='52:54:00:30:89:e3'/>      <source network='default'/>      <model type='virtio'/>      <address type='pci' domain='0x0000' bus='0x00' slot='0x03' function='0x0'/>    </interface>    <serial type='pty'>      <target type='isa-serial' port='0'>        <model name='isa-serial'/>      </target>    </serial>    <console type='pty'>      <target type='serial' port='0'/>    </console>    <channel type='spicevmc'>      <target type='virtio' name='com.redhat.spice.0'/>      <address type='virtio-serial' controller='0' bus='0' port='1'/>    </channel>    <input type='tablet' bus='usb'>      <address type='usb' bus='0' port='1'/>    </input>    <input type='mouse' bus='ps2'/>    <input type='keyboard' bus='ps2'/>    <graphics type='spice' autoport='yes'>      <listen type='address'/>      <image compression='off'/>    </graphics>    <sound model='ich6'>      <address type='pci' domain='0x0000' bus='0x00' slot='0x04' function='0x0'/>    </sound>    <video>      <model type='qxl' ram='65536' vram='65536' vgamem='16384' heads='1' primary='yes'/>      <address type='pci' domain='0x0000' bus='0x00' slot='0x02' function='0x0'/>    </video>    <redirdev bus='usb' type='spicevmc'>      <address type='usb' bus='0' port='2'/>    </redirdev>    <redirdev bus='usb' type='spicevmc'>      <address type='usb' bus='0' port='3'/>    </redirdev>    <memballoon model='virtio'>      <address type='pci' domain='0x0000' bus='0x00' slot='0x08' function='0x0'/>    </memballoon>  </devices></domain>"

m2_xml = "<!--WARNING: THIS IS AN AUTO-GENERATED FILE. CHANGES TO IT ARE LIKELY TO BEOVERWRITTEN AND LOST. Changes to this xml configuration should be made using:  virsh edit m2or other application using the libvirt API.--><domain type='kvm'>  <name>m2</name>  <uuid>83679f59-c668-4ed8-9b05-23e61ec6f007</uuid>  <memory unit='KiB'>614400</memory>  <currentMemory unit='KiB'>614400</currentMemory>  <vcpu placement='static'>1</vcpu>  <os>    <type arch='x86_64' machine='pc-i440fx-bionic'>hvm</type>    <boot dev='hd'/>  </os>  <features>    <acpi/>    <apic/>    <vmport state='off'/>  </features>  <cpu mode='custom' match='exact' check='partial'>    <model fallback='allow'>Broadwell-noTSX-IBRS</model>  </cpu>  <clock offset='utc'>    <timer name='rtc' tickpolicy='catchup'/>    <timer name='pit' tickpolicy='delay'/>    <timer name='hpet' present='no'/>  </clock>  <on_poweroff>destroy</on_poweroff>  <on_reboot>restart</on_reboot>  <on_crash>destroy</on_crash>  <pm>    <suspend-to-mem enabled='no'/>    <suspend-to-disk enabled='no'/>  </pm>  <devices>    <emulator>/usr/bin/qemu-kvm</emulator>    <disk type='file' device='disk'>      <driver name='qemu' type='qcow2'/>      <source file='/var/lib/libvirt/images/m2.qcow2'/>      <target dev='vda' bus='virtio'/>      <address type='pci' domain='0x0000' bus='0x00' slot='0x07' function='0x0'/>    </disk>    <disk type='file' device='cdrom'>      <driver name='qemu' type='raw'/>      <target dev='hda' bus='ide'/>      <readonly/>      <address type='drive' controller='0' bus='0' target='0' unit='0'/>    </disk>    <controller type='usb' index='0' model='ich9-ehci1'>      <address type='pci' domain='0x0000' bus='0x00' slot='0x05' function='0x7'/>    </controller>    <controller type='usb' index='0' model='ich9-uhci1'>      <master startport='0'/>      <address type='pci' domain='0x0000' bus='0x00' slot='0x05' function='0x0' multifunction='on'/>    </controller>    <controller type='usb' index='0' model='ich9-uhci2'>      <master startport='2'/>      <address type='pci' domain='0x0000' bus='0x00' slot='0x05' function='0x1'/>    </controller>    <controller type='usb' index='0' model='ich9-uhci3'>      <master startport='4'/>      <address type='pci' domain='0x0000' bus='0x00' slot='0x05' function='0x2'/>    </controller>    <controller type='pci' index='0' model='pci-root'/>    <controller type='ide' index='0'>      <address type='pci' domain='0x0000' bus='0x00' slot='0x01' function='0x1'/>    </controller>    <controller type='virtio-serial' index='0'>      <address type='pci' domain='0x0000' bus='0x00' slot='0x06' function='0x0'/>    </controller>    <interface type='network'>      <mac address='52:54:00:29:ee:12'/>      <source network='default'/>      <model type='virtio'/>      <address type='pci' domain='0x0000' bus='0x00' slot='0x03' function='0x0'/>    </interface>    <serial type='pty'>      <target type='isa-serial' port='0'>        <model name='isa-serial'/>      </target>    </serial>    <console type='pty'>      <target type='serial' port='0'/>    </console>    <channel type='spicevmc'>      <target type='virtio' name='com.redhat.spice.0'/>      <address type='virtio-serial' controller='0' bus='0' port='1'/>    </channel>    <input type='tablet' bus='usb'>      <address type='usb' bus='0' port='1'/>    </input>    <input type='mouse' bus='ps2'/>    <input type='keyboard' bus='ps2'/>    <graphics type='spice' autoport='yes'>      <listen type='address'/>      <image compression='off'/>    </graphics>    <sound model='ich6'>      <address type='pci' domain='0x0000' bus='0x00' slot='0x04' function='0x0'/>    </sound>    <video>      <model type='qxl' ram='65536' vram='65536' vgamem='16384' heads='1' primary='yes'/>      <address type='pci' domain='0x0000' bus='0x00' slot='0x02' function='0x0'/>    </video>    <redirdev bus='usb' type='spicevmc'>      <address type='usb' bus='0' port='2'/>    </redirdev>    <redirdev bus='usb' type='spicevmc'>      <address type='usb' bus='0' port='3'/>    </redirdev>    <memballoon model='virtio'>      <address type='pci' domain='0x0000' bus='0x00' slot='0x08' function='0x0'/>    </memballoon>  </devices></domain>"

m3_xml = "<!--WARNING: THIS IS AN AUTO-GENERATED FILE. CHANGES TO IT ARE LIKELY TO BEOVERWRITTEN AND LOST. Changes to this xml configuration should be made using:  virsh edit m3or other application using the libvirt API.--><domain type='kvm'>  <name>m3</name>  <uuid>f53e2bc8-7689-4ba5-bca8-7b21a2ece592</uuid>  <memory unit='KiB'>614400</memory>  <currentMemory unit='KiB'>614400</currentMemory>  <vcpu placement='static'>1</vcpu>  <os>    <type arch='x86_64' machine='pc-i440fx-bionic'>hvm</type>    <boot dev='hd'/>  </os>  <features>    <acpi/>    <apic/>    <vmport state='off'/>  </features>  <cpu mode='custom' match='exact' check='partial'>    <model fallback='allow'>Broadwell-noTSX-IBRS</model>  </cpu>  <clock offset='utc'>    <timer name='rtc' tickpolicy='catchup'/>    <timer name='pit' tickpolicy='delay'/>    <timer name='hpet' present='no'/>  </clock>  <on_poweroff>destroy</on_poweroff>  <on_reboot>restart</on_reboot>  <on_crash>destroy</on_crash>  <pm>    <suspend-to-mem enabled='no'/>    <suspend-to-disk enabled='no'/>  </pm>  <devices>    <emulator>/usr/bin/qemu-kvm</emulator>    <disk type='file' device='disk'>      <driver name='qemu' type='qcow2'/>      <source file='/var/lib/libvirt/images/m3.qcow2'/>      <target dev='vda' bus='virtio'/>      <address type='pci' domain='0x0000' bus='0x00' slot='0x07' function='0x0'/>    </disk>    <disk type='file' device='cdrom'>      <driver name='qemu' type='raw'/>      <target dev='hda' bus='ide'/>      <readonly/>      <address type='drive' controller='0' bus='0' target='0' unit='0'/>    </disk>    <controller type='usb' index='0' model='ich9-ehci1'>      <address type='pci' domain='0x0000' bus='0x00' slot='0x05' function='0x7'/>    </controller>    <controller type='usb' index='0' model='ich9-uhci1'>      <master startport='0'/>      <address type='pci' domain='0x0000' bus='0x00' slot='0x05' function='0x0' multifunction='on'/>    </controller>    <controller type='usb' index='0' model='ich9-uhci2'>      <master startport='2'/>      <address type='pci' domain='0x0000' bus='0x00' slot='0x05' function='0x1'/>    </controller>    <controller type='usb' index='0' model='ich9-uhci3'>      <master startport='4'/>      <address type='pci' domain='0x0000' bus='0x00' slot='0x05' function='0x2'/>    </controller>    <controller type='pci' index='0' model='pci-root'/>    <controller type='ide' index='0'>      <address type='pci' domain='0x0000' bus='0x00' slot='0x01' function='0x1'/>    </controller>    <controller type='virtio-serial' index='0'>      <address type='pci' domain='0x0000' bus='0x00' slot='0x06' function='0x0'/>    </controller>    <interface type='network'>      <mac address='52:54:00:52:fe:6f'/>      <source network='default'/>      <model type='virtio'/>      <address type='pci' domain='0x0000' bus='0x00' slot='0x03' function='0x0'/>    </interface>    <serial type='pty'>      <target type='isa-serial' port='0'>        <model name='isa-serial'/>      </target>    </serial>    <console type='pty'>      <target type='serial' port='0'/>    </console>    <channel type='spicevmc'>      <target type='virtio' name='com.redhat.spice.0'/>      <address type='virtio-serial' controller='0' bus='0' port='1'/>    </channel>    <input type='tablet' bus='usb'>      <address type='usb' bus='0' port='1'/>    </input>    <input type='mouse' bus='ps2'/>    <input type='keyboard' bus='ps2'/>    <graphics type='spice' autoport='yes'>      <listen type='address'/>      <image compression='off'/>    </graphics>    <sound model='ich6'>      <address type='pci' domain='0x0000' bus='0x00' slot='0x04' function='0x0'/>    </sound>    <video>      <model type='qxl' ram='65536' vram='65536' vgamem='16384' heads='1' primary='yes'/>      <address type='pci' domain='0x0000' bus='0x00' slot='0x02' function='0x0'/>    </video>    <redirdev bus='usb' type='spicevmc'>      <address type='usb' bus='0' port='2'/>    </redirdev>    <redirdev bus='usb' type='spicevmc'>      <address type='usb' bus='0' port='3'/>    </redirdev>    <memballoon model='virtio'>      <address type='pci' domain='0x0000' bus='0x00' slot='0x08' function='0x0'/>    </memballoon>  </devices></domain>"

xml_files.append(m1_xml)
xml_files.append(m2_xml)
xml_files.append(m3_xml)