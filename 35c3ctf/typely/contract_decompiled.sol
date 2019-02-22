contract Contract {
    function main() {
        memory[0x40:0x60] = 0x80;
    
        if(msg.data.length < 0x04) { revert(memory[0x00:0x00]); }
    
        var var0 = msg.data[0x00:0x20] / 0x0100000000000000000000000000000000000000000000000000000000;
    
        if(var0 == 0x2f54bf6e) {
            var var1 = msg.value;
        
            if(var1) { revert(memory[0x00:0x00]); }
        
            var1 = 0x00b0;
            var var2 = 0x04;
            var var3 = msg.data.length - var2;
        
            if(var3 < 0x20) { revert(memory[0x00:0x00]); }
        
            var2 = isOwner(var2, var3);
            var temp0 = memory[0x40:0x60];
            memory[temp0:temp0 + 0x20] = !!var2;
            var temp1 = memory[0x40:0x60];
            return memory[temp1:temp1 + (temp0 + 0x20) - temp1];
        } else if(var0 == 0x4b8fcc14) {
            var1 = msg.value;
        
            if(var1) { revert(memory[0x00:0x00]); }
        
            var1 = 0x0119;
            var2 = 0x04;
            var3 = msg.data.length - var2;
        
            if(var3 < 0x20) { revert(memory[0x00:0x00]); }
        
            func_00ED(var2, var3);
            stop();
        } else if(var0 == 0x61f1d889) {
            var1 = msg.value;
        
            if(var1) { revert(memory[0x00:0x00]); }
        
            var1 = 0x015e;
            var2 = 0x04;
            var3 = msg.data.length - var2;
        
            if(var3 < 0x40) { revert(memory[0x00:0x00]); }
        
            setFlag(var2, var3);
            stop();
        } else if(var0 == 0x839a19d9) {
            var1 = msg.value;
        
            if(var1) { revert(memory[0x00:0x00]); }
        
            var1 = 0x0199;
            var2 = 0x04;
            var3 = msg.data.length - var2;
        
            if(var3 < 0x20) { revert(memory[0x00:0x00]); }
        
            var1 = func_0183(var2, var3);
            var temp2 = memory[0x40:0x60];
            memory[temp2:temp2 + 0x20] = var1;
            var temp3 = memory[0x40:0x60];
            return memory[temp3:temp3 + (temp2 + 0x20) - temp3];
        } else { revert(memory[0x00:0x00]); }
    }
    
    function isOwner(var arg0, var arg1) returns(var arg0) {
        arg0 = msg.data[arg0:arg0 + 0x20] & 0xffffffffffffffffffffffffffffffffffffffff;
        memory[0x20:0x40] = 0x00;
        memory[0x00:0x20] = arg0;
        return storage[keccak256(memory[0x00:0x40])] & 0xff;
    }
    
    function func_00ED(var arg0, var arg1) {
        arg0 = msg.data[arg0:arg0 + 0x20] & 0xffffffffffffffffffffffffffffffffffffffff;
        memory[0x00:0x20] = msg.sender;
        memory[0x20:0x40] = 0x00;
    
        if(!(storage[keccak256(memory[0x00:0x40])] & 0xff)) { revert(memory[0x00:0x00]); }
    
        arg1 = 0x00;
        var temp0 = memory[0x40:0x60];
        var temp1;
        temp1, memory[temp0:temp0 + 0x00] = address(arg0 & 0xffffffffffffffffffffffffffffffffffffffff).delegatecall.gas(msg.gas)(memory[temp0:temp0 + memory[0x40:0x60] - temp0]);
        var var1 = returndata.length;
        var var2 = var1;
    
        if(var2 == 0x00) {
            // Error: StackRead before write???
            var var0;
            arg1 = var0;
        
            if(!arg1) { revert(memory[0x00:0x00]); }
        
        label_0298:
            return;
        } else {
            var temp2 = memory[0x40:0x60];
            var1 = temp2;
            memory[0x40:0x60] = var1 + (returndata.length + 0x3f & ~0x1f);
            memory[var1:var1 + 0x20] = returndata.length;
            var temp3 = returndata.length;
            memory[var1 + 0x20:var1 + 0x20 + temp3] = returndata[0x00:0x00 + temp3];
            arg1 = var0;
        
            if(arg1) { goto label_0298; }
            else { revert(memory[0x00:0x00]); }
        }
    }
    
    function setFlag(var arg0, var arg1) {
        var temp0 = arg0;
        arg0 = msg.data[temp0:temp0 + 0x20];
        arg1 = msg.data[temp0 + 0x20:temp0 + 0x20 + 0x20];
        storage[0x64] = arg0;
        storage[0x65] = arg1;
    }
    
    function func_0183(var arg0, var arg1) returns(var r0) {
        arg0 = msg.data[arg0:arg0 + 0x20];
        arg1 = 0x00;
        var var0 = arg0 >= 0x64; // first arg must have value >= 0x64
    
        if(!var0) {
            if(!var0) { revert(memory[0x00:0x00]); }
        
        label_02C7:
            return storage[arg0];  // get storage at index
        } else if(arg0 <= 0x68) { goto label_02C7; }
        else { revert(memory[0x00:0x00]); }
    }
}

